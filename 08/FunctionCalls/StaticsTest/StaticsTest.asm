@256
D=A
@SP
M=D
@Sys.init$RETURN0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$RETURN0)
(Class1.set)
@0
D=A
@R13
M=D
(Class1.set$REPEATLOOP)
@R13
D=M
@Class1.set$REPEATEND
D;JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class1.set$REPEATLOOP
0;JMP
(Class1.set$REPEATEND)
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@Class1.0
M=D
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@Class1.1
M=D
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@R14
M=D
@5
D=A
@R14
A=M-D
D=M
@R13
M=D
@ARG
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@R14
A=M-D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
(Class1.get)
@0
D=A
@R13
M=D
(Class1.get$REPEATLOOP)
@R13
D=M
@Class1.get$REPEATEND
D;JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class1.get$REPEATLOOP
0;JMP
(Class1.get$REPEATEND)
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M-D
@LCL
D=M
@R14
M=D
@5
D=A
@R14
A=M-D
D=M
@R13
M=D
@ARG
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@R14
A=M-D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
(Sys.init)
@0
D=A
@R13
M=D
(Sys.init$REPEATLOOP)
@R13
D=M
@Sys.init$REPEATEND
D;JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Sys.init$REPEATLOOP
0;JMP
(Sys.init$REPEATEND)
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init$RETURN1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Sys.init$RETURN1)
@SP
AM=M-1
D=M
@R5
M=D
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init$RETURN2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Sys.init$RETURN2)
@SP
AM=M-1
D=M
@R5
M=D
@Sys.init$RETURN3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(Sys.init$RETURN3)
@Sys.init$RETURN4
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(Sys.init$RETURN4)
(Sys.init$WHILE)
@Sys.init$WHILE
0;JMP
(Class2.set)
@0
D=A
@R13
M=D
(Class2.set$REPEATLOOP)
@R13
D=M
@Class2.set$REPEATEND
D;JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class2.set$REPEATLOOP
0;JMP
(Class2.set$REPEATEND)
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@Class2.0
M=D
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@Class2.1
M=D
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@R14
M=D
@5
D=A
@R14
A=M-D
D=M
@R13
M=D
@ARG
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@R14
A=M-D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP
(Class2.get)
@0
D=A
@R13
M=D
(Class2.get$REPEATLOOP)
@R13
D=M
@Class2.get$REPEATEND
D;JEQ
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
@Class2.get$REPEATLOOP
0;JMP
(Class2.get$REPEATEND)
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
A=A-1
M=M-D
@LCL
D=M
@R14
M=D
@5
D=A
@R14
A=M-D
D=M
@R13
M=D
@ARG
D=M
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@R14
A=M-D
D=M
@THAT
M=D
@2
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13
A=M
0;JMP