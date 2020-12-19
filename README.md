This repository contains the gem5 implementation of Selective Delay, a novel method against cache side-channel attacks of time measurements. This method restricts
the execution time of load instructions after RDTSC or RDTSCP instructions to a fixed time.

Modify Ranges
----
We mainly modify the "O3" pipeline to realize our design.

Run
----
Same as the original Gem5 simulator.


More detials will be updated after Our paper is completed. <br>
Selective Delay: Modifying the Execution Logic of Sensitive Instructions to Defeat Cache Side-Channel Attacks.
