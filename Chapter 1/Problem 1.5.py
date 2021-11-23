f = "need code here or pycharm puts all my text in italics"

"""
We will assume the needle is dropped at a random position with a random angle.
the probability density function of the angle is as given in problem 1.4

We will say the point of the needle is equally likely to land at any distance between 2 lines.  We're going to consider
the top edge of the paper to be lines so that if the needle lands anywhere on the paper, irrespective of
its angle, it has a chance to cross a line

Given this assumption, the point of the needle will always land between two lines and we can say that the position
will have a probability distribution of 1/l.  Normalizing l to length 1, we can say 

p(x) = 1/1
p(x) = 1
P(x) = ∫ p(x) * dx | from x to x + dx   <<I really don't like this notation because we're saying x=x to x=x+dx
P(x) = x | from x to x + dx             <<confusing but whatever
P(x) = x + dx - x
P(x) = dx
P(x1 to x2) = ∫ P(x) | x1 to x2
P(x1 to x2) = x2 - x1
P(0 to 1) = 1                           <<sanity checking; probability does sum to 1

We will consider the position where the needle lands to be the point closest to the bottom of the paper
(so the needle always has an angle between 0 and 180)

In order not to double-count our probabilities, we will only consider angles between 0 and 90
This is because the span of the needle is the same when flipped along an axis perpendicular to the lines
Therefore we will only consider needle spans between 0 and 1

We will say that if the top point of the needle rests exactly on the upper parallel line it "crosses" the line
but we will not say this for the bottom point resting on the bottom line
(the needle can still "cross" the line if the bottom point lands on the bottom line, but it must be exactly
perpendicular)
Therefore, the needle will span the parallel lines if the span + the position is greater than or equal to 1

For any needle span, the likelihood of the needle crossing the line is exactly equal to the likelihood of
it being found between the span of values whose length is the span of the needle itself

This is not obvious, but let us say that the needle spans a length of 0.25
The needle will crosses the line if its bottom point is located between 0.75-1
Since the probability distribution of the needle location is uniform, we can ignore the position and say that the
likelihood of it crossing is the likelihood of it being located within a range of length 0.25

Further, because we've normalized the line to length 1, this value is also equal to the probability that the
needle will span the line.

Therefore, the probability that the needle crosses the line is equal to the magnitude of the span of the needle!
    (This makes intuitive sense - the longer the span of the needle, the higher the likelihood it spans a line)

The probability that the needle spans a length s (constrained by symmetry to be between 0 and 1 as described earlier)
is given by
Psp(x) = -dx / [pi*sqrt(1-x^2)]  <<note that we cannot ignore the -dx, given the sqrt(1-x^2) term in the bottom

If the needle spans length s, it crosses the line with probability s
Therefore, the probability that the needle crosses the line is given by Pcr(x) = x * Psp(x)
    here, x is the span of the needle, not the position between the lines - we are evaluating this probability over a 
    range of needle spans

As stated earlier, we will only evaluate this integral between needle spans of 0 and 1, as needles flipped in a 
direction perpendicular to the lines span the same distance - we don't want to count them twice
Note that we actually have to go from 1 to 0 with a negative differential due to the 1/sqrt(1-x^2) term

Pcr(1 to 0) = ∫ x * Px=s(x) | x=1 to x=0
Pcr(1 to 0) = ∫ {-x / [pi*sqrt(1-x^2)]} * dx | x=1 to x=0
    h = 1-x^2
    dh/dx = -2x
    dx = dh/-2x
Pcr(1 to 0) = ∫ {-x / [pi*sqrt(h)]} * dh/-2x | x=1 to x=0
Pcr(1 to 0) = ∫ {1 / [2*pi*sqrt(h)]} * dh | x=1 to x=0
Pcr(1 to 0) = sqrt(h) / pi | x=1 to x=0

Pcr(1 to 0) = sqrt(1-x^2)/pi | x=1 to x=0
Pcr(1 to 0) = sqrt(1-0)/pi - sqrt(1-1)/pi
Pcr(1 to 0) = 1/pi

Therefore, the probability that the needle crosses the line is equal to 1/pi

Note that when given limits of integration, Wolfram-Alpha evaluates this integral to 1.1 which is impossible because, 
ya know, you only got 100% probability to throw around.  I hope that's because Wolfram sucks and I'm awesome, and not
because I screwed up somewhere.  When Wolfram-Alpha evaluates this integral without limits, it agrees with what I've 
derived so...I think I'm right?
"""
