f = "need code here or pycharm puts all my text in italics"

"""
a)
To find A, we set ∫ p(x) from x=-∞ to x =∞ equal to 1
∫ p(x) = 1 = ∫ A * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞

The closest integral I could find was the cumulative distribution function
    https://mathworld.wolfram.com/NormalDistribution.html

D(x) = 1/[σ*sqrt(2*pi)] * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x
D(x) = (1/2)*{1 + erf[(x - a)/(σ * sqrt(2)]}

The reason I like this is that it has suitable boundaries of integration and our original function can be transformed
using simple substitutions 
As far as I can tell the erf function does not work here because the limits of integration are from x to 0, and it's
not obvious how to interpret our integral at its negative limit in terms of the erf function

We can transform our Gaussian probability to an appropriate form by using the following definitions:

λ = 1/(2σ^2)
σ = sqrt(1/[2*λ])
[σ*sqrt(2*pi)] * {1/[σ*sqrt(2*pi)]} = 1
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
From a graph, I can tell that A is the magnitude of the maximum value of the distribution.
    Since we are treating this as a probability distribution A will always be normalized
a is the offset from center (this will not affect the average values)
λ is the width of the base.  at x=a+/-λ/2, the probability density drops sharply


<x> =  ∫ x * p(x) = ∫ A * x * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                             <<definition of <x>
<x> =  A * ∫ x * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                                          <<pull out A
    v = x + a                                                                                               <<let's make this tractable
    dv = dx
<x> =  A * ∫ (v + a) * e^(-λv^2) * dv | v=-∞ to v=∞                                                         <<subtsitute v
<x> =  A * ∫ v * e^(-λv^2) * dv + a * e^(-λv^2) * dv | v=-∞ to v=∞                                          <<expand the integral
<x> =  A * ∫ v * e^(-λv^2) * dv | v=-∞ to v=∞ + A * ∫ a * e^(-λv^2) * dv | v=-∞ to v=∞                      <<separate into 2 integrals
<x> =  A * ∫ v * e^(-λv^2) * dv | v=-∞ to v=∞ + a * A * ∫ e^(-λv^2) * dv | v=-∞ to v=∞                      <<pull out a
    Note here that the right hand side of this function is simply a * 1, since we know that the integral
    of the probability density function is 1 and A * ∫ e^(-λv^2) * dv | v=-∞ to v=∞
    is just a disguised version of the probability density function
<x> =  A * ∫ v * e^(-λv^2) * dv | v=-∞ to v=∞ + a                                                           <<A * ∫ e^(-λv^2) * dv | v=-∞ to v=∞ = 1
    w = v / sqrt(λ)                                                                                         <<more substitutions to make the integral tractable
    v = w * sqrt(λ)
    dv = dw * sqrt(λ)
<x> = A * ∫ w * sqrt(λ) * e^(-w^2) * dw * sqrt(λ) | w=-∞ to w=∞ + a                                         <<substitute all v's for w's 
<x> = A * ∫ w * λ * e^(-w^2) * dw | w=-∞ to w=∞ + a                                                         <<sqrt(λ) * sqrt(λ) = λ
<x> = λ * A * ∫ w * e^(-w^2) * dw | w=-∞ to w=∞ + a                                                         <<pull out the λ
    u = -w^2                                                                                                <<EVEN MORE SUBSTITUTIONS OH MY GOD AND JESUS
    du = -2w * dw
    dw = -du/2w
<x> = λ * A * ∫ w * e^(u) * -du/2w | w=-∞ to w=∞ + a                                                        <<substitute all w's for u's (except where they'll cancel)
<x> = -λ * A/2 * ∫ e^(u) * du | w=-∞ to w=∞ + a                                                             <<cancel out the w's, pull out the 1/2
<x> = -λ * A/2 * e^(u) | w=-∞ to w=∞ + a                                                                    <<am I dead yet
<x> = -λ * A/2 * e^(-w^2) | w=-∞ to w=∞ + a                                                                 <<re-substitute w's for us
<x> = a                                                                                                     << e^(-∞^2) = 0; 0-0 = 0
    Note - we did know this would be the answer when we originally messed around with the variables.  However, it's
    good to learn how to work with gaussian integrals, and I hope to god to never have to do this again

    Oh, wait.  Nope, gotta do it again.  But harder this time.
<x^2> =  ∫ x^2 * p(x) = ∫ A * x^2 * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                       <<Why. Whyyyy.  WHYYYYYYYYYY
<x^2> =  A * ∫ x^2 * e^(-λ[x-a]^2) * dx | x=-∞ to x =∞                                                      <<I feel bad for myself.  I really do.
    v = x - a                                                                                               <<there's gotta be an easier way, right?  no...?  ok...
    x = v + a                                                                                               <<would you believe I got this backwards at first and had to redo it all?
    dv = dx                                                                                                 <<luckily I went back and found out I did the first part wrong too
<x^2> =  A * ∫ (v + a)^2 * e^(-λ*v^2) * dv | v=-∞ to v =∞                                                   <<so, I've gotten quite a bit of practice at this now
<x^2> =  A * ∫ (v^2 + 2*v*a + a^2) * e^(-λ*v^2) * dv | v=-∞ to v =∞                                         <<no one is making me do this but I'll be goddamned if I'm not gonna complain about it anyway
    We already know that the a^2 portion of this integral will evaluate to a^2 and the 2*v*a portion
    of the integral will evaluate to 0.  Take that, Gauss with your stupid integrals.  I'm onto you now.
<x^2> =  A * ∫ v^2 * e^(-λ*v^2) * dv | v=-∞ to v =∞ + a^2                                                   <<can I even evaluate this at all?
    v = u / sqrt(λ)                                                                                         <<let's simplify again...sigh
    dv = du / sqrt(λ)
<x^2> =  A * ∫ (u^2 / λ) * e^(-u^2) * du / sqrt(λ) | u=-∞ to u =∞ + a^2                                     <<get the lambda out of the exponential term
<x^2> =  ∫ (u^2 / λ) * A * e^(-u^2) * du / sqrt(λ) | u=-∞ to u =∞ + a^2                                     <<I've got an idea...integration by parts looks promising
<x^2> =  (1 / λ^1.5) * ∫ u^2 * A * e^(-u^2) * du | u=-∞ to u =∞ + a^2                                       <<I hate that (1 / λ^1.5) term
    ∫R * dT = R * T - ∫T dR                                                                                 <<I do not understand definite integration by parts well enough
                                                                                                            to know if what I'm doing is valid
                                                                                                            
    R = u^2                                                                                                 <<This will differentiate into terms I know what to do with
    dT = A * e^(-u^2) * du = sqrt(λ/pi) * e^(-λ[x-a]^2) * dx                                                <<and this looks like our old friend D(x)  λ = 1/(2σ^2)
    dT = sqrt(λ/pi) * e^(-[x-a]^2/(2σ^2)) * dx                                                              <<Yep, it's him alright.  straight from hell.
    
    dR = 2u * du
    T = ∫ dT = ∫sqrt(λ/pi) * e^(-λ[x-a]^2) * dx = sqrt(λ/pi) * ∫ e^(-λ[x-a]^2) * dx                                        
        So my plan here is to integrate dT using the definition of the cumulative distribution function from earlier
        I'm trying to evaluate this as an indefinite integral but D(x) is a definite integral
        but it also feels somewhat like an indefinite integral, as its limits are a variable x and -∞.  
        can we just pretend this is OK?  I'll be our secret.  I won't tell anyone in the whole world.
    
    D(x) = sqrt(λ/pi) * ∫ e^[-(x'-a)^2/(2σ^2)] dx' | from x'=-∞ to x'=x                                     <<this our simplified version of D(x)
    D(x) = (1/2)*{1 + erf[(x - a)/(σ * sqrt(2)]}                                                            <<this is the solution to the integral
    T = D(x)
        It feels like I should be able to substitute x=∞ here and use the fact that D(x) was already integrated from
        -∞ to x
        However, to finish this problem I to multiply T by R, and you need to evaluate the product of T*R at x=-∞ and 
        then at x=∞.
        T(∞) * R(∞) - T(-∞) * R(-∞) = Q
        The problem is that I don't know what R(∞) or R(-∞) are.  I only know D(∞) 
        D(∞) = R∞ - R-∞ 
        However, I can get D(0) which would be R(0) - R(-∞)
        And if I then get D(∞) that is R(∞) - R(-∞)
        And I can subtract the two to get R(∞) - R(0)
        Fuck this I'm going to bed
    
    R
<x^2> =  (A / λ^1.5) * ∫ u^2 * e^(-u^2) * du | u=-∞ to u =∞ + a^2
"""