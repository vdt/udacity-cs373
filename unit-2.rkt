#! /usr/bin/env racket

#lang racket

(require rackunit)

(define (divisible-by-5 x)
  (integer? (/ x 5)))
(check-equal?  (divisible-by-5 5) #t)
(check-equal? (divisible-by-5 4) #f)

(define (amount-after-selfish-move x)
  (/ (* 4 (- x 1)) 5))
(check-equal? (amount-after-selfish-move 6) 4)
(check-equal? (amount-after-selfish-move 1) 0)

(define (amount-after-n-selfish-moves x n)
  (if (<= n 0)
      x
      (amount-after-n-selfish-moves (amount-after-selfish-move x)
                                    (- n 1))))
(check-equal? (amount-after-n-selfish-moves 1 0) 1)
(check-equal? (amount-after-n-selfish-moves 1 1) 0)
(check-equal? (amount-after-n-selfish-moves 6 1) 4)

(define (amount-after-1-night-of-selfish-moves x)
  (amount-after-n-selfish-moves x 5))

(define (start-coconut-count)
  (define (start-with-n-coconuts? n)
    (divisible-by-5 (- (amount-after-1-night-of-selfish-moves n) 1)))
  (for/first ([n (in-naturals)]
               #:when (start-with-n-coconuts? n))
       n))

(printf "start cocunut count = ~v\n" (start-coconut-count))
