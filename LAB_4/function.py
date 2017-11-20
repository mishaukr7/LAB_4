import sys


def rosenbrock(x):
    '''
        ## Rosenbrocks classic parabolic valley ("banana") function
    '''
    a = x[0]
    b = x[1]
    return ((1.0 - a) ** 2) + (100.0 * (b - (a ** 2)) ** 2)


def _hooke_best_nearby(f, delta, point, prevbest, bounds=None, args=[]):

    z = [x for x in point]
    minf = prevbest
    ftmp = 0.0

    fev = 0

    for i in range(len(point)):
        # see if moving point in the positive delta direction decreases the
        z[i] = _value_in_bounds(point[i] + delta[i], bounds[i][0], bounds[i][1])

        ftmp = f(z, *args)
        fev += 1
        if ftmp < minf:
            minf = ftmp
        else:
            # if not, try moving it in the other direction
            delta[i] = -delta[i]
            z[i] = _value_in_bounds(point[i] + delta[i], bounds[i][0], bounds[i][1])

            ftmp = f(z, *args)
            fev += 1
            if ftmp < minf:
                minf = ftmp
            else:
                # if moving the point in both delta directions result in no improvement, then just keep the point where it is
                z[i] = point[i]

    for i in range(len(z)):
        point[i] = z[i]
    return (minf, fev)


def _point_in_bounds(point, bounds):
    '''
        shifts the point so it is within the given bounds
    '''
    for i in range(len(point)):
        if point[i] < bounds[i][0]:
            point[i] = bounds[i][0]
        elif point[i] > bounds[i][1]:
            point[i] = bounds[i][1]


def _is_point_in_bounds(point, bounds):
    '''
        true if the point is in the bounds, else false
    '''
    out = True
    for i in range(len(point)):
        if point[i] < bounds[i][0]:
            out = False
        elif point[i] > bounds[i][1]:
            out = False
    return out


def _value_in_bounds(val, low, high):
    if val < low:
        return low
    elif val > high:
        return high
    else:
        return val


def hooke(f, startpt, bounds=None, rho=0.5, epsilon=1E-6, itermax=5000, args=[]):
    '''
        In this version of the Hooke and Jeeves algorithm, we coerce the function into staying within the given bounds.
        basically, any time the function tries to pick a point outside the bounds we shift the point to the boundary
        on whatever dimension it is out of bounds in. Implementing bounds this way may be questionable from a theory standpoint,
        but that's how COPASI does it, that's how I'll do it too.

    '''

    result = dict()
    result['success'] = True
    result['message'] = 'success'

    delta = [0.0] * len(startpt)
    endpt = [0.0] * len(startpt)
    if bounds is None:
        # if bounds is none, make it none for all (it will be converted to below)
        bounds = [[None, None] for x in startpt]
    else:
        bounds = [[x[0], x[1]] for x in bounds]  # make it so it wont update the original
    startpt = [x for x in startpt]  # make it so it wont update the original

    fmin = None
    nfev = 0
    iters = 0

    for bound in bounds:
        if bound[0] is None:
            bound[0] = float('-inf')
        else:
            bound[0] = float(bound[0])
        if bound[1] is None:
            bound[1] = float('inf')
        else:
            bound[1] = float(bound[1])
    try:
        # shift
        _point_in_bounds(startpt, bounds)  # shift startpt so it is within the bounds

        xbefore = [x for x in startpt]
        newx = [x for x in startpt]
        for i in range(len(startpt)):
            delta[i] = abs(startpt[i] * rho)
            if (delta[i] == 0.0):
                # we always want a non-zero delta because otherwise we'd just be checking the same point over and over
                # and wouldn't find a minimum
                delta[i] = rho

        steplength = rho

        fbefore = f(newx, *args)
        nfev += 1

        newf = fbefore
        fmin = newf
        while ((iters < itermax) and (steplength > epsilon)):
            iters += 1
            # print "after %5d , f(x) = %.4le at" % (funevals, fbefore)

            #        for j in range(len(startpt)):
            # print "   x[%2d] = %4le" % (j, xbefore[j])
            #            pass

            ##/* find best new point, one coord at a time */
            newx = [x for x in xbefore]
            (newf, evals) = _hooke_best_nearby(f, delta, newx, fbefore, bounds, args)

            nfev += evals
            ##/* if we made some improvements, pursue that direction */
            keep = 1
            while ((newf < fbefore) and (keep == 1)):
                fmin = newf
                for i in range(len(startpt)):
                    ##/* firstly, arrange the sign of delta[] */
                    if newx[i] <= xbefore[i]:
                        delta[i] = -abs(delta[i])
                    else:
                        delta[i] = abs(delta[i])
                    ## /* now, move further in this direction */
                    tmp = xbefore[i]
                    xbefore[i] = newx[i]
                    newx[i] = _value_in_bounds(newx[i] + newx[i] - tmp, bounds[i][0], bounds[i][1])
                fbefore = newf
                (newf, evals) = _hooke_best_nearby(f, delta, newx, fbefore, bounds, args)
                nfev += evals
                ##/* if the further (optimistic) move was bad.... */
                if (newf >= fbefore):
                    break

                ## /* make sure that the differences between the new */
                ## /* and the old points are due to actual */
                ## /* displacements; beware of roundoff errors that */
                ## /* might cause newf < fbefore */
                keep = 0
                for i in range(len(startpt)):
                    keep = 1
                    if (abs(newx[i] - xbefore[i]) > (0.5 * abs(delta[i]))):
                        break
                    else:
                        keep = 0
            if ((steplength >= epsilon) and (newf >= fbefore)):
                steplength = steplength * rho
                delta = [x * rho for x in delta]
        for x in range(len(xbefore)):
            endpt[x] = xbefore[x]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        result['success'] = False
        result['message'] = str(e) + ". line number: " + str(exc_tb.tb_lineno)
    finally:
        result['nit'] = iters
        result['fevals'] = nfev
        result['fun'] = fmin
        result['x'] = endpt

    return result


def main():
    start = [-1.2, 1.0]
    res = hooke(rosenbrock, start, bounds=((0, 3), (0, 10)), rho=0.5)
    # res = hooke(rosenbrock, start, rho=0.5)
    print(res)

main()