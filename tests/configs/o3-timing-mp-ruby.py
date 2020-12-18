# Copyright (c) 2006-2007 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import m5
from m5.objects import *

nb_cores = 4
cpus = [ DerivO3CPU(cpu_id=i) for i in range(nb_cores) ]

import ruby_config
ruby_memory = ruby_config.generate("TwoLevel_SplitL1UnifiedL2.rb", nb_cores)

# system simulated
system = System(cpu = cpus, physmem = ruby_memory, membus = SystemXBar(),
                mem_mode = "timing",
                clk_domain = SrcClockDomain(clock = '1GHz'))

# Create a seperate clock domain for components that should run at
# CPUs frequency
system.cpu_clk_domain = SrcClockDomain(clock = '2GHz')

for cpu in cpus:
    # create the interrupt controller
    cpu.createInterruptController()
    cpu.connectAllPorts(system.membus)
    # All cpus are associated with cpu_clk_domain
    cpu.clk_domain = system.cpu_clk_domain

# connect memory to membus
system.physmem.port = system.membus.master

# Connect the system port for loading of binaries etc
system.system_port = system.membus.slave

# -----------------------
# run simulation
# -----------------------

root = Root(full_system = False, system = system)
root.system.mem_mode = 'timing'
