This repository contains the gem5 implementation of Constant-Time Loading, a novel method against cache side-channel attacks of time measurements. This method restricts
the execution time of load instructions after RDTSC or RDTSCP instructions to a fixed time.

Modify Ranges
----
We mainly modified the "O3" pipeline to realize our design.

Run
----
Same as the original Gem5 simulator.

Notes
----
More details will be updated after Our paper is published. <br>
Constant-Time Loading: Modifying CPU Pipeline to Defeat Cache Side-Channel Attacks.
