print_str:
    prc #33
    prc #10

    prn r12
    prc #10

    mov r7 #14
    prn r7
    prc #10

    prn #10
    prc #10
    prn #3
    prc #10

    add r2 #10 #3
    prn r2
    prc #10

    mul r10 #6 #3
    prn r10 
    prc #10

    min r3 #11 #9
    prn r3
    prc #10

    max r4 #11 #9
    prn r4
    prc #10

    prc #72
    prc #101
    prc  #108
    prc #108
    prc #111
    prc #32
    prc #119
    prc #111
    prc #114
    prc #108
    prc #100
    prc #33
    prc #10
    ret 

main:
    add r30 r30 #-1
    mov !r30 r31
    cal print_str
    mov r31 !r30
    add r30 r30 #-1
    ret 
