# ELK
Internship at SOLEIL project ELK 
POC ELK (Proof of Concept):

Objective: Solution to use application logs from the main machine and beamline control systems.
Analysis of application logs:
Collection of available logs: C++ tango devices, java devices, java applications, coox tools, archiving system, flyscan continuous scan service, and spyc
Collection of dumps: monitoring the dumps and extracting the call stack (backtrace) so that the devs could perform analysis as soon as possible
Estimation of data volumes by frequency, type, application, and level for all lines and for the RCM
Exploitation of logs: concrete case study and creation of visualizations and dashboards
Study of the interactions with other systems: PANIC, PLUSS
Study of constraints for a deployment: installation, start, stop, purge, backup, managing updates , authentication, security, and availability
Study of target architecture
Study of centralization process from RCL to RES and RCM to RES
Sizing in terms of volume and performance to define the infrastructure
Investment
Industrialization
 
General Knowledge: 
 
Raid 0/1/5/10: a data storage visualization consisting of using multiple disk drives in order to prevent data loss  (data redundancy ) or improve performance .
Threads: a program under execution is known as a process and thread is a basic unit of execution. It comprises a thread ID, a program counter, a register set, and a stack. 
Multithreading: when Ido multiple threads simultaneously.
http: hypertext transfer protocol which allows us to manage my files, it is a request-response system (client-server) with multiple commands (puts/post/get/delete).    
Docker: Software development platform and kind of virtualization technology, which makes it eases developing and playing applications inside of neatly packaged virtual containerized environments. Consumes less space than a virtual machine, with a short boot up time and better performance, and is easy to set up, etc...
Why SQL:  we can access and modify data easily. The maximum data is much greater than 64000 boxes. Easy transactions (state A to state B, otherwise state A only)
NOSQL: Not Only structured query language. NOSQL can scale vertically and horizontally, where every item stands on its own (key-value stores). The workload can be separated into 2 or more servers, each server will be responsible for part of my database. Ican consult any information in my database using a hash function (each key value has a hash number corresponding to it).
CAP Triangle: Consistency, Availability, Partition Tolerance
Configuration Of Virtual Machine: Vagrant permits building and managing my virtual machine environments in a single workflow. 
First ELK application using a test sample database: My tutor taught me how to receive, transfer and structure data in the Elastic Stack using an example database that consists of movies, actors, years, and directors etc. We did the following:
SSH: Secure shell is a network protocol for operating network services securely over an unsecured network, it uses client server architecture while providing secure channel encrypting used to make data transferred confidential and unsusceptible to interception using packet analysis.
NAT: Network address translation; in order to avoid the need to assign a new address to every host in the same house for example (TV, phone, laptop, computer etc.). Upon connection to the internet, the NAT in the router maps the private ip addresses into a public address and vice versa when sending and receiving data from the internet.
