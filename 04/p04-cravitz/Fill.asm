// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(LOOP) // Infinite loop to check for input

    // Start loop counter at 8192 (512*256)/16
    @8192
    D=A
    @count
    M=D

    // Check for keyboard input
    @KBD
    D=M
    @IF_KEY
    D;JNE

// Loop through all screen registers
(IF_NO_KEY)
    // While loop (while count >= 0)
    @count
    D=M
    @END
    D;JLT

    // Set screen through screen + 8192 = 0 (to make everything white)
    @SCREEN
    D=A+D
    @R0
    M=D
    @0
    D=A
    @R0
    A=M
    M=0

    @count
    M=M-1

    @IF_NO_KEY
    0;JMP

(IF_KEY)
    @count
    D=M
    @END
    D;JLT

    // Set screen through screen + 8192 = -1 (to make everything black)
    @SCREEN
    D=A+D
    @R0
    M=D
    @0
    D=A-1
    @R0
    A=M
    M=D

    @count
    M=M-1

    @IF_KEY
    0;JMP

(END)
    @LOOP
    0;JMP