f = "need code here or pycharm puts all my text in italics"

"""
a)
To find A, we set ∫ p(x) from x=-∞ to x =∞ equal to 1
∫ p(x) = 1 = ∫ A * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞

The closest integral I could find was the cumulative distribution function      https://mathworld.wolfram.com/NormalDistribution.html
Note that the website uses the variable μ where our homework uses the variable a.  I will use the variable a instead. 

D(x) = 1/[σ*sqrt(2*pi)] * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x
D(x) = (1/2)*{1 + erf[(x - a)/(σ * sqrt(2)]}

The reason I like this is that it has suitable boundaries of integration - its boundaries are x'=-∞ to x'=x, so if
you evaluate it at x=∞, it is equivalent to integrating the original function from x=-∞ to x=∞
Also, our original function can be transformed to an equivalent form using simple substitutions.    
As far as I can tell the erf function does not work here because the limits of integration are from x to 0, and it's
not obvious how to interpret our integral in terms of the erf function (although we could transform our system into
a form suitable for use with the erf function)

We can transform our Gaussian probability to an appropriate form by using the following definitions:

λ = 1/(2σ^2)
σ = sqrt(1/[2*λ])
sqrt(pi/λ) = [σ*sqrt(2*pi)]
sqrt(pi/λ) * sqrt(λ/pi) = 1

We're going to redefine the term preceding the integral in terms of λ rather than σ

D(x) = 1/[σ*sqrt(2*pi)] * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x                           <<original equation
D(x) = 1/[sqrt(1/[2*λ])*sqrt(2*pi)] * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x               <<σ = sqrt(1/[2*λ])
D(x) = 1/sqrt(pi/λ) * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x                               <<simplified

D(x) = sqrt(λ/pi) * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x                                 <<this is the version we will use
D(x) = (1/2)*{1 + erf[(x - a)/(σ * sqrt(2)]}                                                        <<this is the solution to the integral


∫ p(x) = 1 = ∫ A * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                                <<original integral definition
∫ p(x) = 1 = A * ∫ e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                                <<pull out A
∫ p(x) = 1 = A * sqrt(pi/λ) * sqrt(λ/pi) * ∫ e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                      <<multiply by sqrt(pi/λ) * sqrt(λ/pi) which is 1
∫ p(x) = 1 = A * sqrt(pi/λ) * sqrt(λ/pi) * ∫ e^(-[x-a]^2/(2σ^2)) * dx | x=-∞ to x =∞                <<λ = 1/(2σ^2)
∫ p(x) = 1 = A * sqrt(pi/λ) * D(x) | x =∞                                                           <<definition of the cumulative distribution function 
∫ p(x) = 1 = A * sqrt(pi/λ) * (1/2) * {1 + erf[(x - a)/(σ * sqrt(2)]} | x =∞                        <<alternative definition of the cumulative distribution function
∫ p(x) = 1 = A * sqrt(pi/λ) * (1/2) * {1 + erf[(∞ - a)/(σ * sqrt(2)]}                               <<x=∞ 
∫ p(x) = 1 = A * sqrt(pi/λ) * (1/2) * {1 + 1}                                                       <<erf(∞) = 1
∫ p(x) = 1 = A * sqrt(pi/λ)                                                                         <<simplified
         A = sqrt(λ/pi)                                                                             <<solve for A

b)
By graphing this function online with random values for A, λ, and a, I can get a preliminary understanding of how
this function behaves.  This is a bell-curve, with a symmetric gradient, offset from the origin along the x-axis,
and with a certain height
A is the magnitude of the maximum value of the curve at its peak.
    Since we are treating this as a probability distribution A will always be normalized per part a)
a is the offset from the origin along the x axis to the center of the bell curve
λ is the width of the base.  at x=a+/-λ/2, the probability density drops sharply


<x> =  ∫ x * p(x) = ∫ A * x * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                             <<definition of <x>
<x> =  A * ∫ x * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                                          <<pull out A
    v = x + a                                                                                               <<replace x-a in the exponent with a single variable
    dv = dx
<x> =  A * ∫ (v + a) * e^(-λv^2) * dv | v=-∞ to v=∞                                                         <<subtsitute v and dv in the original equation
<x> =  A * ∫ v * e^(-λv^2) * dv + a * e^(-λv^2) * dv | v=-∞ to v=∞                                          <<expand the (v + a) term
<x> =  A * ∫ v * e^(-λv^2) * dv | v=-∞ to v=∞ + A * ∫ a * e^(-λv^2) * dv | v=-∞ to v=∞                      <<separate into 2 integrals
<x> =  A * ∫ v * e^(-λv^2) * dv | v=-∞ to v=∞ + a * A * ∫ e^(-λv^2) * dv | v=-∞ to v=∞                      <<pull out a
    Note here that the right hand side of this equation is equal to a, since we know that the integral
    of the probability density function is 1 and A * ∫ e^(-λv^2) * dv | v=-∞ to v=∞
    is just a disguised version of the probability density function
<x> =  A * ∫ v * e^(-λv^2) * dv | v=-∞ to v=∞ + a                                                           <<A * ∫ e^(-λv^2) * dv | v=-∞ to v=∞ = 1
    v = w / sqrt(λ)                                                                                         <<we will now remove the λ term from the exponent
    w = v * sqrt(λ)
    dv = dw / sqrt(λ)
<x> = A * ∫ w / sqrt(λ) * e^(-w^2) * dw / sqrt(λ) | w=-∞ to w=∞ + a                                         <<substitute all v's and dv's for w's and dw's 
<x> = A * ∫ w * e^(-w^2) * dw / λ | w=-∞ to w=∞ + a                                                         <<sqrt(λ) * sqrt(λ) = λ
<x> = (A / λ) * ∫ w * e^(-w^2) * dw | w=-∞ to w=∞ + a                                                       <<pull out the 1/λ term
    u = -w^2                                                                                                <<we can now do another substitution to evaluate this integral directly
    du = -2w * dw
    dw = -du/2w
<x> = (A / λ) * ∫ w * e^(u) * -du/2w | w=-∞ to w=∞ + a                                                      <<substitute all w's and dw's for u's and du's (except where they'll cancel)
<x> = -(A / [2*λ]) * ∫ e^(u) * du | w=-∞ to w=∞ + a                                                         <<cancel out the w's, pull out the 1/2
<x> = -(A / [2*λ]) * e^(u) | w=-∞ to w=∞ + a                                                                <<integral of e^u * du = e^u
<x> = -(A / [2*λ]) * e^(-w^2) | w=-∞ to w=∞ + a                                                             <<re-substitute w's for us
<x> = a                                                                                                     << e^(-∞^2) = 0; 0-0 = 0
    Note - we did know this would be the answer when we originally messed around with the variables.  However, it's
    good to learn how to work with gaussian integrals, and I hope to god to never have to do this again

    Oh, wait.  Nope, gotta do it again.  But harder this time.
<x^2> =  ∫ x^2 * p(x) = ∫ A * x^2 * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                       <<This will be harder - the trick we used earlier will not work.
<x^2> =  A * ∫ x^2 * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                                      <<Pull out the A term, let's get to work
    v = x - a                                                                                               <<Once again, we're going to get rid of the x-a term in the exponent
    x = v + a                                                                                               
    dv = dx                                                                                                 
<x^2> =  A * ∫ (v + a)^2 * e^(-λ*v^2) * dv | v=-∞ to v =∞                                                   <<substitute all x's and dx's with v's and dv's
<x^2> =  A * ∫ (v^2 + 2*v*a + a^2) * e^(-λ*v^2) * dv | v=-∞ to v =∞                                         <<expand the (v+a)^2 term
    We already know that the a^2 portion of this integral will evaluate to a^2 and the 2*v*a portion
    of the integral will evaluate to 0.  We now need to figure out how to integrate the v^2 term
<x^2> =  A * ∫ v^2 * e^(-λ*v^2) * dv | v=-∞ to v =∞ + a^2                                                   <<replacing the 2*v*a and a^2 portions of the integral
    v = u / sqrt(λ)                                                                                         <<let's the the lambda out of the exponential
    dv = du / sqrt(λ)
<x^2> =  A * ∫ (u^2 / λ) * e^(-u^2) * du / sqrt(λ) | u=-∞ to u =∞ + a^2                                     <<replace all v's and dv's with u's and du's
<x^2> =  (A / λ^1.5) * ∫ u^2 * e^(-u^2) * du | u=-∞ to u =∞ + a^2                                           <<pull out the lamda denominator term
<x^2> =  (1 / λ^1.5) * ∫ u^2 * A * e^(-u^2) * du | u=-∞ to u =∞ + a^2                                       <<I've got an idea...integration by parts looks promising
    ∫R * dT = R * T - ∫T dR                                                                                 <<I do not understand definite integration by parts well enough
                                                                                                            to know if what I'm doing is valid
                                                                                                            
    R = u^2                                                                                                 <<This will differentiate into a term I know how to integrate (it will go to 0)
    dT = A * e^(-u^2) * du                                                                                  <<this looks like our old friend D(x)
    dT = sqrt(λ/pi) * e^(-λ[x-a]^2) * dx                                                                    <<A = sqrt(λ/pi)
    dT = sqrt(λ/pi) * e^(-[x-a]^2/(2σ^2)) * dx                                                              <<λ = 1/(2σ^2)
        This is our original form of the cumulative distribution function.
        when integrated from x'=-∞ to x'=x, this is equal to D(x).
    
    dR = 2u * du
    T = ∫ dT 
      = ∫sqrt(λ/pi) * e^(-[x-a]^2/(2σ^2)) * dx    
      = sqrt(λ/pi) * ∫ e^(-[x-a]^2/(2σ^2)) * dx                                         
        So my plan here is to integrate dT using the definition of the cumulative distribution function from earlier
        I'm trying to evaluate this as an indefinite integral but D(x) is a definite integral, and I don't think
        that what I'm trying to do is valid
        I've copied the definitions of D(x) from earlier for reference
 
    D(x) = sqrt(λ/pi) * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x                                     <<this our simplified version of D(x)
    D(x) = (1/2)*{1 + erf[(x - a)/(σ * sqrt(2)]}                                                            <<this is the solution to the integral

        It feels like I should be able to substitute x=∞ here and use the fact that D(x) was already integrated from
        -∞ to x
        However, when you integrate by parts using a definite integral, you evaluate the product of T*R at x=-∞ and 
        then at x=∞.
        T(∞) * R(∞) - T(-∞) * R(-∞) = Q                                                                     <<I'm just using Q as a temporary output variable here
        The problem is that I don't know what R(∞) or R(-∞) are.  I only know D(x) and D(∞)
        D(∞) = T(∞) - T(-∞)
        D(x) = T(x) - T(-∞)
             
        
c) Did this online, see intro to part b)
"""