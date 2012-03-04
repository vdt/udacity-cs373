#! /usr/bin/env racket
#lang racket

(require rackunit)

(define (mu-prime mu sigma-square nu r-square)
  (/ (+ (* r-square mu)
        (* sigma-square nu))
     (+ sigma-square r-square)))
(check-equal? (mu-prime 1 1 1 1) 1)
(check-equal? (mu-prime 10 4 12 4) 11)

(define (sigma-square-prime sigma-square r-square)
  (/ 1 (+ (/ 1 sigma-square)
          (/ 1 r-square))))
(check-equal? (sigma-square-prime 1 1) 1/2)
(check-equal? (sigma-square-prime 4 4) 2)

(define mu 10)
(define nu 13)
(define sigma-square 8)
(define r-square 2)
(printf (string-append "suppose we have: mu = ~v, nu = ~v\n"
                       "\tsigma-square = ~v, r-square = ~v\n")
        mu nu sigma-square r-square)
(printf "mu-prime = ~v\n" (mu-prime mu sigma-square nu r-square))
(printf "sigma-sqaure-prime = ~v\n" (sigma-square-prime sigma-square r-square))
