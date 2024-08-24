// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// while (R1 > 0):
//    total+=R0
//    R1--
// R2 = total

// Set R2 to 0
@0 
D=A
@R2 
M=D

// Start count at R0
@R0
D=M
@count
M=D

// While loop (while count > 0)
(LOOP)
    @count
    D=M
    @END
    D;JEQ

    // Add R1 to what's stored in R2
    @R1
    D=M
    @R2
    M=M+D

    @count
    M=M-1

    @LOOP
    0;JMP

(END)
    @END
    0;JMP