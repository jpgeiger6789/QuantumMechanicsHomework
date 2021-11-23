f = "need code here or pycharm puts all my text in italics"

"""
a)
It really feels like p(x) should be a constant 1/xmax since there is a 1-to-1 mapping between the angle and the
position and p(θ) is a constant = 1/pi
However we do need to prove this somehow (it turns out not to be true) 
p(θ) = 1 / pi      <<the probability density function is uniform from 0 to pi (and sums to 100%, or 1)
x(θ) = cos(θ)      <<the value of x goes from -1 to 1 and is given as the cosine of the angle
θ = acos(x)        <<take the acos of both sides (this is valid, as the acos is defined and continuous from -1 to 1)
P(θ) = ∫ p(θ) dθ | evaluated from θ to θ + dθ       <<the probability of the needle being found inside a certain interval
P(θ) = ∫ dθ / pi | evaluated from θ to θ + dθ       <<substitution
P(θ) = θ / pi | evaluated from θ to θ + dθ          <<evaluate the integral
P(θ) = (θ + dθ) / pi - θ / pi                       <<enter the limits of integration
P(θ) = dθ / pi                                      <<ok here we get funky. 
                                        
    dx/dθ = -sin(θ)                                 <<take the derviative of x(θ) = cos(θ)
    dθ = - dx / sin(θ)                              <<solve for d(θ)
    dθ = - dx / sin(acos(x))                        <<substitute to a form we can integrate
        sin(acos(x)) = sqrt(1-x^2)                  <<been a second had to look this one up
        this is derived from sin(θ)^2+cos(θ)^2=1
        sin(acos(x))^2 + cos(acos(x))^2 = 1
        sin(acos(x))^2 = 1 - x^2
    dθ = - dx / sqrt(1-x^2)                         <<this looks way better than before but still shitty
P(x) =  -dx / [pi*sqrt(1-x^2)]                      <<We have completely removed all of the references to θ from P(θ)
                                                    so the probability is now a function of x
                                                    This is the probability that the needle will be found at some
                                                    infinitesimal gap around x (really between x and x - dx)
                                                    If this is the probability of an infinitesimally small interval,
                                                    the probability of a non-infinitesimally small interval must be 
                                                    the integral of this value for the ranges given
                                                    Note that the negative value is due to the fact that a positive
                                                    rotation of the angle results in a decreasing value of x

P(x1 to x2) = ∫ -dx / [pi * sqrt(1-x^2)] | x = x1 to x = x2        
P(x1 to x2) = - asin(x)/pi | x = x1 to x = x2       <<thank god for wolfram-alpha
                                                    <<note that this is real-valued only between -1 and 1
                                                    but that's fine for us
                                                    Also, note that when this integral is evaluated, x1 must be greater
                                                    than x2.  This is because we are evaluating in the direction of
                                                    positive rotation, which is the direction of decreasing x
                                                    We will now multiply this by -1 to evaluate this in a normal way

P(x1 to x2) = asin(x)/pi | x = x1 to x = x2         <<this form of the probability equation correctly moves in the 
                                                    direction of increasing x and x1 can now be less than x2, as is
                                                    normally done
                                                    Note that you cannot do this for the original probability function
                                                    (I didn't figure this out until problem 1.5) because 
                                                    P(x) is proportional to 1/sqrt(1-x^2) and cannot be evaluated
                                                    at x = 1
                                                    the negative infinitesimal prevents you from going from 0 to 1:
                                                    you actually go from 1-dx to 0-dx
                                      
asin(1)/pi - asin(-1)/pi                            <<if we evaluate this for the total range of possible x values, this
                                                    does sum to 1! 
                                                    So what happens if you want to find the probability of the needle
                                                    falling between x=-.5 to x=-.25?
                                                    
asin(-.25)/pi - asin(-.5)/pi  = .08                 <<this is a positive number.  This works!
                                                    <<so...how do we go from this absolute probability function to a 
                                                    probability density function?
                                                    The answer is that if you know the probability for an infinitesimally
                                                    small range, you can divide by that range to find the density at a
                                                    single point
                                                    Here, we have to remember that our infinitesimal range was in the
                                                    negative direction, so to get the probability density function
                                                    we need to divide by -dx
p(x) = P(x) / -dx
p(x) =  1 / [pi*sqrt(1-x^2)]                        This is the answer to part a)          

b)

<x> = ∫ x*p(x) | -1 to 1
    ∫ x / [pi * sqrt(1-x^2)] * dx
    h = (1-x^2)
    dh = -2x * dx
    dx = dh / -2x
    ∫ -dh / [2 * pi * sqrt(h)]
    = -sqrt(h) / pi
    = -sqrt(1-x^2) / pi | -1 to 1
    = 0                                             <<average value of x is 0 - this makes sense
    Doing this in Wolfram-Alpha gives the same answer (0)
<x^2> = ∫ x^2 * p(x) | -1 to 1
    = .5                                            <<average value of x^2 is .5 - plugged this into wolfram-alpha
variance = <x^2> - <x> ^ 2 = .5
std dev = sqrt(variance) = sqrt(.5)                 <<standard deviation of x is sqrt(.5)
                                                    
                                                    Since x=cos(θ), <x> = <cos(θ)> and <x^2> = <cos^2(θ)>
"""
