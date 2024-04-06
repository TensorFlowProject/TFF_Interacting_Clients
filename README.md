# TFF_Interacting_Clients

What I have done this time is that I try to connect the interactions of two client to each other which this give us the hope of connecting server and client together too in a similar way.
Anyway, I explain the part of my code.
First of all, I should say here we consider two clients which are trust together completely. Second of all, here we share weights and biases between two clients which is what we send in TFF.
1. greet.proto :
   This is obvious file that which is the one of the needs for send and recieve the needed data. One important thing that should I say because of we can't send 2D arrays  , I turned the weights to 1D array and then send it. And also my code involves a simple saying hello for both clients.
2. New_Thing :
   This is mainly our previous code but this time we try to change the initiliaze weights and biases from zero to the given weights from server side(Of course except that the first time).
3. greet_client :
   This has two duties :
    1. Recieve the weights and biases from the side of "Client 2" and give it to code of New_Thing which is our "Client 1" either.
    2. Send the weights and biases from "Client 1" to "Client 2"
4. greet_server :
   This has two duties :
    1. Recieve the send and biases from the side of "Client 1" and give it to code of New_Thing_Server which is our "Client 2" either.
    2. Send the weights and biases from "Client 2" to "Client 1"
5. New_Thing_Server :
   This is the code of "Client 2" which is like the code of "New_Thing".
   
I hope I clarify good. I say some issues that I have with this to think more for those problems together.

Thank you:)
