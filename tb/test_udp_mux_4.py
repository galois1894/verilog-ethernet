#!/usr/bin/env python
"""

Copyright (c) 2014-2016 Alex Forencich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from myhdl import *
import os

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

import udp_ep

module = 'udp_mux_4'

srcs = []

srcs.append("../rtl/%s.v" % module)
srcs.append("test_%s.v" % module)

src = ' '.join(srcs)

build_cmd = "iverilog -o test_%s.vvp %s" % (module, src)

def dut_udp_mux_4(clk,
                 rst,
                 current_test,

                 input_0_udp_hdr_valid,
                 input_0_udp_hdr_ready,
                 input_0_eth_dest_mac,
                 input_0_eth_src_mac,
                 input_0_eth_type,
                 input_0_ip_version,
                 input_0_ip_ihl,
                 input_0_ip_dscp,
                 input_0_ip_ecn,
                 input_0_ip_length,
                 input_0_ip_identification,
                 input_0_ip_flags,
                 input_0_ip_fragment_offset,
                 input_0_ip_ttl,
                 input_0_ip_protocol,
                 input_0_ip_header_checksum,
                 input_0_ip_source_ip,
                 input_0_ip_dest_ip,
                 input_0_udp_source_port,
                 input_0_udp_dest_port,
                 input_0_udp_length,
                 input_0_udp_checksum,
                 input_0_udp_payload_tdata,
                 input_0_udp_payload_tvalid,
                 input_0_udp_payload_tready,
                 input_0_udp_payload_tlast,
                 input_0_udp_payload_tuser,
                 input_1_udp_hdr_valid,
                 input_1_udp_hdr_ready,
                 input_1_eth_dest_mac,
                 input_1_eth_src_mac,
                 input_1_eth_type,
                 input_1_ip_version,
                 input_1_ip_ihl,
                 input_1_ip_dscp,
                 input_1_ip_ecn,
                 input_1_ip_length,
                 input_1_ip_identification,
                 input_1_ip_flags,
                 input_1_ip_fragment_offset,
                 input_1_ip_ttl,
                 input_1_ip_protocol,
                 input_1_ip_header_checksum,
                 input_1_ip_source_ip,
                 input_1_ip_dest_ip,
                 input_1_udp_source_port,
                 input_1_udp_dest_port,
                 input_1_udp_length,
                 input_1_udp_checksum,
                 input_1_udp_payload_tdata,
                 input_1_udp_payload_tvalid,
                 input_1_udp_payload_tready,
                 input_1_udp_payload_tlast,
                 input_1_udp_payload_tuser,
                 input_2_udp_hdr_valid,
                 input_2_udp_hdr_ready,
                 input_2_eth_dest_mac,
                 input_2_eth_src_mac,
                 input_2_eth_type,
                 input_2_ip_version,
                 input_2_ip_ihl,
                 input_2_ip_dscp,
                 input_2_ip_ecn,
                 input_2_ip_length,
                 input_2_ip_identification,
                 input_2_ip_flags,
                 input_2_ip_fragment_offset,
                 input_2_ip_ttl,
                 input_2_ip_protocol,
                 input_2_ip_header_checksum,
                 input_2_ip_source_ip,
                 input_2_ip_dest_ip,
                 input_2_udp_source_port,
                 input_2_udp_dest_port,
                 input_2_udp_length,
                 input_2_udp_checksum,
                 input_2_udp_payload_tdata,
                 input_2_udp_payload_tvalid,
                 input_2_udp_payload_tready,
                 input_2_udp_payload_tlast,
                 input_2_udp_payload_tuser,
                 input_3_udp_hdr_valid,
                 input_3_udp_hdr_ready,
                 input_3_eth_dest_mac,
                 input_3_eth_src_mac,
                 input_3_eth_type,
                 input_3_ip_version,
                 input_3_ip_ihl,
                 input_3_ip_dscp,
                 input_3_ip_ecn,
                 input_3_ip_length,
                 input_3_ip_identification,
                 input_3_ip_flags,
                 input_3_ip_fragment_offset,
                 input_3_ip_ttl,
                 input_3_ip_protocol,
                 input_3_ip_header_checksum,
                 input_3_ip_source_ip,
                 input_3_ip_dest_ip,
                 input_3_udp_source_port,
                 input_3_udp_dest_port,
                 input_3_udp_length,
                 input_3_udp_checksum,
                 input_3_udp_payload_tdata,
                 input_3_udp_payload_tvalid,
                 input_3_udp_payload_tready,
                 input_3_udp_payload_tlast,
                 input_3_udp_payload_tuser,

                 output_udp_hdr_valid,
                 output_udp_hdr_ready,
                 output_eth_dest_mac,
                 output_eth_src_mac,
                 output_eth_type,
                 output_ip_version,
                 output_ip_ihl,
                 output_ip_dscp,
                 output_ip_ecn,
                 output_ip_length,
                 output_ip_identification,
                 output_ip_flags,
                 output_ip_fragment_offset,
                 output_ip_ttl,
                 output_ip_protocol,
                 output_ip_header_checksum,
                 output_ip_source_ip,
                 output_ip_dest_ip,
                 output_udp_source_port,
                 output_udp_dest_port,
                 output_udp_length,
                 output_udp_checksum,
                 output_udp_payload_tdata,
                 output_udp_payload_tvalid,
                 output_udp_payload_tready,
                 output_udp_payload_tlast,
                 output_udp_payload_tuser,

                 enable,
                 select):

    if os.system(build_cmd):
        raise Exception("Error running build command")
    return Cosimulation("vvp -m myhdl test_%s.vvp -lxt2" % module,
                clk=clk,
                rst=rst,
                current_test=current_test,

                input_0_udp_hdr_valid=input_0_udp_hdr_valid,
                input_0_udp_hdr_ready=input_0_udp_hdr_ready,
                input_0_eth_dest_mac=input_0_eth_dest_mac,
                input_0_eth_src_mac=input_0_eth_src_mac,
                input_0_eth_type=input_0_eth_type,
                input_0_ip_version=input_0_ip_version,
                input_0_ip_ihl=input_0_ip_ihl,
                input_0_ip_dscp=input_0_ip_dscp,
                input_0_ip_ecn=input_0_ip_ecn,
                input_0_ip_length=input_0_ip_length,
                input_0_ip_identification=input_0_ip_identification,
                input_0_ip_flags=input_0_ip_flags,
                input_0_ip_fragment_offset=input_0_ip_fragment_offset,
                input_0_ip_ttl=input_0_ip_ttl,
                input_0_ip_protocol=input_0_ip_protocol,
                input_0_ip_header_checksum=input_0_ip_header_checksum,
                input_0_ip_source_ip=input_0_ip_source_ip,
                input_0_ip_dest_ip=input_0_ip_dest_ip,
                input_0_udp_source_port=input_0_udp_source_port,
                input_0_udp_dest_port=input_0_udp_dest_port,
                input_0_udp_length=input_0_udp_length,
                input_0_udp_checksum=input_0_udp_checksum,
                input_0_udp_payload_tdata=input_0_udp_payload_tdata,
                input_0_udp_payload_tvalid=input_0_udp_payload_tvalid,
                input_0_udp_payload_tready=input_0_udp_payload_tready,
                input_0_udp_payload_tlast=input_0_udp_payload_tlast,
                input_0_udp_payload_tuser=input_0_udp_payload_tuser,
                input_1_udp_hdr_valid=input_1_udp_hdr_valid,
                input_1_udp_hdr_ready=input_1_udp_hdr_ready,
                input_1_eth_dest_mac=input_1_eth_dest_mac,
                input_1_eth_src_mac=input_1_eth_src_mac,
                input_1_eth_type=input_1_eth_type,
                input_1_ip_version=input_1_ip_version,
                input_1_ip_ihl=input_1_ip_ihl,
                input_1_ip_dscp=input_1_ip_dscp,
                input_1_ip_ecn=input_1_ip_ecn,
                input_1_ip_length=input_1_ip_length,
                input_1_ip_identification=input_1_ip_identification,
                input_1_ip_flags=input_1_ip_flags,
                input_1_ip_fragment_offset=input_1_ip_fragment_offset,
                input_1_ip_ttl=input_1_ip_ttl,
                input_1_ip_protocol=input_1_ip_protocol,
                input_1_ip_header_checksum=input_1_ip_header_checksum,
                input_1_ip_source_ip=input_1_ip_source_ip,
                input_1_ip_dest_ip=input_1_ip_dest_ip,
                input_1_udp_source_port=input_1_udp_source_port,
                input_1_udp_dest_port=input_1_udp_dest_port,
                input_1_udp_length=input_1_udp_length,
                input_1_udp_checksum=input_1_udp_checksum,
                input_1_udp_payload_tdata=input_1_udp_payload_tdata,
                input_1_udp_payload_tvalid=input_1_udp_payload_tvalid,
                input_1_udp_payload_tready=input_1_udp_payload_tready,
                input_1_udp_payload_tlast=input_1_udp_payload_tlast,
                input_1_udp_payload_tuser=input_1_udp_payload_tuser,
                input_2_udp_hdr_valid=input_2_udp_hdr_valid,
                input_2_udp_hdr_ready=input_2_udp_hdr_ready,
                input_2_eth_dest_mac=input_2_eth_dest_mac,
                input_2_eth_src_mac=input_2_eth_src_mac,
                input_2_eth_type=input_2_eth_type,
                input_2_ip_version=input_2_ip_version,
                input_2_ip_ihl=input_2_ip_ihl,
                input_2_ip_dscp=input_2_ip_dscp,
                input_2_ip_ecn=input_2_ip_ecn,
                input_2_ip_length=input_2_ip_length,
                input_2_ip_identification=input_2_ip_identification,
                input_2_ip_flags=input_2_ip_flags,
                input_2_ip_fragment_offset=input_2_ip_fragment_offset,
                input_2_ip_ttl=input_2_ip_ttl,
                input_2_ip_protocol=input_2_ip_protocol,
                input_2_ip_header_checksum=input_2_ip_header_checksum,
                input_2_ip_source_ip=input_2_ip_source_ip,
                input_2_ip_dest_ip=input_2_ip_dest_ip,
                input_2_udp_source_port=input_2_udp_source_port,
                input_2_udp_dest_port=input_2_udp_dest_port,
                input_2_udp_length=input_2_udp_length,
                input_2_udp_checksum=input_2_udp_checksum,
                input_2_udp_payload_tdata=input_2_udp_payload_tdata,
                input_2_udp_payload_tvalid=input_2_udp_payload_tvalid,
                input_2_udp_payload_tready=input_2_udp_payload_tready,
                input_2_udp_payload_tlast=input_2_udp_payload_tlast,
                input_2_udp_payload_tuser=input_2_udp_payload_tuser,
                input_3_udp_hdr_valid=input_3_udp_hdr_valid,
                input_3_udp_hdr_ready=input_3_udp_hdr_ready,
                input_3_eth_dest_mac=input_3_eth_dest_mac,
                input_3_eth_src_mac=input_3_eth_src_mac,
                input_3_eth_type=input_3_eth_type,
                input_3_ip_version=input_3_ip_version,
                input_3_ip_ihl=input_3_ip_ihl,
                input_3_ip_dscp=input_3_ip_dscp,
                input_3_ip_ecn=input_3_ip_ecn,
                input_3_ip_length=input_3_ip_length,
                input_3_ip_identification=input_3_ip_identification,
                input_3_ip_flags=input_3_ip_flags,
                input_3_ip_fragment_offset=input_3_ip_fragment_offset,
                input_3_ip_ttl=input_3_ip_ttl,
                input_3_ip_protocol=input_3_ip_protocol,
                input_3_ip_header_checksum=input_3_ip_header_checksum,
                input_3_ip_source_ip=input_3_ip_source_ip,
                input_3_ip_dest_ip=input_3_ip_dest_ip,
                input_3_udp_source_port=input_3_udp_source_port,
                input_3_udp_dest_port=input_3_udp_dest_port,
                input_3_udp_length=input_3_udp_length,
                input_3_udp_checksum=input_3_udp_checksum,
                input_3_udp_payload_tdata=input_3_udp_payload_tdata,
                input_3_udp_payload_tvalid=input_3_udp_payload_tvalid,
                input_3_udp_payload_tready=input_3_udp_payload_tready,
                input_3_udp_payload_tlast=input_3_udp_payload_tlast,
                input_3_udp_payload_tuser=input_3_udp_payload_tuser,

                output_udp_hdr_valid=output_udp_hdr_valid,
                output_udp_hdr_ready=output_udp_hdr_ready,
                output_eth_dest_mac=output_eth_dest_mac,
                output_eth_src_mac=output_eth_src_mac,
                output_eth_type=output_eth_type,
                output_ip_version=output_ip_version,
                output_ip_ihl=output_ip_ihl,
                output_ip_dscp=output_ip_dscp,
                output_ip_ecn=output_ip_ecn,
                output_ip_length=output_ip_length,
                output_ip_identification=output_ip_identification,
                output_ip_flags=output_ip_flags,
                output_ip_fragment_offset=output_ip_fragment_offset,
                output_ip_ttl=output_ip_ttl,
                output_ip_protocol=output_ip_protocol,
                output_ip_header_checksum=output_ip_header_checksum,
                output_ip_source_ip=output_ip_source_ip,
                output_ip_dest_ip=output_ip_dest_ip,
                output_udp_source_port=output_udp_source_port,
                output_udp_dest_port=output_udp_dest_port,
                output_udp_length=output_udp_length,
                output_udp_checksum=output_udp_checksum,
                output_udp_payload_tdata=output_udp_payload_tdata,
                output_udp_payload_tvalid=output_udp_payload_tvalid,
                output_udp_payload_tready=output_udp_payload_tready,
                output_udp_payload_tlast=output_udp_payload_tlast,
                output_udp_payload_tuser=output_udp_payload_tuser,

                enable=enable,
                select=select)

def bench():

    # Inputs
    clk = Signal(bool(0))
    rst = Signal(bool(0))
    current_test = Signal(intbv(0)[8:])

    input_0_udp_hdr_valid = Signal(bool(0))
    input_0_eth_dest_mac = Signal(intbv(0)[48:])
    input_0_eth_src_mac = Signal(intbv(0)[48:])
    input_0_eth_type = Signal(intbv(0)[16:])
    input_0_ip_version = Signal(intbv(0)[4:])
    input_0_ip_ihl = Signal(intbv(0)[4:])
    input_0_ip_dscp = Signal(intbv(0)[6:])
    input_0_ip_ecn = Signal(intbv(0)[2:])
    input_0_ip_length = Signal(intbv(0)[16:])
    input_0_ip_identification = Signal(intbv(0)[16:])
    input_0_ip_flags = Signal(intbv(0)[3:])
    input_0_ip_fragment_offset = Signal(intbv(0)[13:])
    input_0_ip_ttl = Signal(intbv(0)[8:])
    input_0_ip_protocol = Signal(intbv(0)[8:])
    input_0_ip_header_checksum = Signal(intbv(0)[16:])
    input_0_ip_source_ip = Signal(intbv(0)[32:])
    input_0_ip_dest_ip = Signal(intbv(0)[32:])
    input_0_udp_source_port = Signal(intbv(0)[16:])
    input_0_udp_dest_port = Signal(intbv(0)[16:])
    input_0_udp_length = Signal(intbv(0)[16:])
    input_0_udp_checksum = Signal(intbv(0)[16:])
    input_0_udp_payload_tdata = Signal(intbv(0)[8:])
    input_0_udp_payload_tvalid = Signal(bool(0))
    input_0_udp_payload_tlast = Signal(bool(0))
    input_0_udp_payload_tuser = Signal(bool(0))
    input_1_udp_hdr_valid = Signal(bool(0))
    input_1_eth_dest_mac = Signal(intbv(0)[48:])
    input_1_eth_src_mac = Signal(intbv(0)[48:])
    input_1_eth_type = Signal(intbv(0)[16:])
    input_1_ip_version = Signal(intbv(0)[4:])
    input_1_ip_ihl = Signal(intbv(0)[4:])
    input_1_ip_dscp = Signal(intbv(0)[6:])
    input_1_ip_ecn = Signal(intbv(0)[2:])
    input_1_ip_length = Signal(intbv(0)[16:])
    input_1_ip_identification = Signal(intbv(0)[16:])
    input_1_ip_flags = Signal(intbv(0)[3:])
    input_1_ip_fragment_offset = Signal(intbv(0)[13:])
    input_1_ip_ttl = Signal(intbv(0)[8:])
    input_1_ip_protocol = Signal(intbv(0)[8:])
    input_1_ip_header_checksum = Signal(intbv(0)[16:])
    input_1_ip_source_ip = Signal(intbv(0)[32:])
    input_1_ip_dest_ip = Signal(intbv(0)[32:])
    input_1_udp_source_port = Signal(intbv(0)[16:])
    input_1_udp_dest_port = Signal(intbv(0)[16:])
    input_1_udp_length = Signal(intbv(0)[16:])
    input_1_udp_checksum = Signal(intbv(0)[16:])
    input_1_udp_payload_tdata = Signal(intbv(0)[8:])
    input_1_udp_payload_tvalid = Signal(bool(0))
    input_1_udp_payload_tlast = Signal(bool(0))
    input_1_udp_payload_tuser = Signal(bool(0))
    input_2_udp_hdr_valid = Signal(bool(0))
    input_2_eth_dest_mac = Signal(intbv(0)[48:])
    input_2_eth_src_mac = Signal(intbv(0)[48:])
    input_2_eth_type = Signal(intbv(0)[16:])
    input_2_ip_version = Signal(intbv(0)[4:])
    input_2_ip_ihl = Signal(intbv(0)[4:])
    input_2_ip_dscp = Signal(intbv(0)[6:])
    input_2_ip_ecn = Signal(intbv(0)[2:])
    input_2_ip_length = Signal(intbv(0)[16:])
    input_2_ip_identification = Signal(intbv(0)[16:])
    input_2_ip_flags = Signal(intbv(0)[3:])
    input_2_ip_fragment_offset = Signal(intbv(0)[13:])
    input_2_ip_ttl = Signal(intbv(0)[8:])
    input_2_ip_protocol = Signal(intbv(0)[8:])
    input_2_ip_header_checksum = Signal(intbv(0)[16:])
    input_2_ip_source_ip = Signal(intbv(0)[32:])
    input_2_ip_dest_ip = Signal(intbv(0)[32:])
    input_2_udp_source_port = Signal(intbv(0)[16:])
    input_2_udp_dest_port = Signal(intbv(0)[16:])
    input_2_udp_length = Signal(intbv(0)[16:])
    input_2_udp_checksum = Signal(intbv(0)[16:])
    input_2_udp_payload_tdata = Signal(intbv(0)[8:])
    input_2_udp_payload_tvalid = Signal(bool(0))
    input_2_udp_payload_tlast = Signal(bool(0))
    input_2_udp_payload_tuser = Signal(bool(0))
    input_3_udp_hdr_valid = Signal(bool(0))
    input_3_eth_dest_mac = Signal(intbv(0)[48:])
    input_3_eth_src_mac = Signal(intbv(0)[48:])
    input_3_eth_type = Signal(intbv(0)[16:])
    input_3_ip_version = Signal(intbv(0)[4:])
    input_3_ip_ihl = Signal(intbv(0)[4:])
    input_3_ip_dscp = Signal(intbv(0)[6:])
    input_3_ip_ecn = Signal(intbv(0)[2:])
    input_3_ip_length = Signal(intbv(0)[16:])
    input_3_ip_identification = Signal(intbv(0)[16:])
    input_3_ip_flags = Signal(intbv(0)[3:])
    input_3_ip_fragment_offset = Signal(intbv(0)[13:])
    input_3_ip_ttl = Signal(intbv(0)[8:])
    input_3_ip_protocol = Signal(intbv(0)[8:])
    input_3_ip_header_checksum = Signal(intbv(0)[16:])
    input_3_ip_source_ip = Signal(intbv(0)[32:])
    input_3_ip_dest_ip = Signal(intbv(0)[32:])
    input_3_udp_source_port = Signal(intbv(0)[16:])
    input_3_udp_dest_port = Signal(intbv(0)[16:])
    input_3_udp_length = Signal(intbv(0)[16:])
    input_3_udp_checksum = Signal(intbv(0)[16:])
    input_3_udp_payload_tdata = Signal(intbv(0)[8:])
    input_3_udp_payload_tvalid = Signal(bool(0))
    input_3_udp_payload_tlast = Signal(bool(0))
    input_3_udp_payload_tuser = Signal(bool(0))

    output_udp_payload_tready = Signal(bool(0))
    output_udp_hdr_ready = Signal(bool(0))

    enable = Signal(bool(0))
    select = Signal(intbv(0)[2:])

    # Outputs
    input_0_udp_hdr_ready = Signal(bool(0))
    input_0_udp_payload_tready = Signal(bool(0))
    input_1_udp_hdr_ready = Signal(bool(0))
    input_1_udp_payload_tready = Signal(bool(0))
    input_2_udp_hdr_ready = Signal(bool(0))
    input_2_udp_payload_tready = Signal(bool(0))
    input_3_udp_hdr_ready = Signal(bool(0))
    input_3_udp_payload_tready = Signal(bool(0))

    output_udp_hdr_valid = Signal(bool(0))
    output_eth_dest_mac = Signal(intbv(0)[48:])
    output_eth_src_mac = Signal(intbv(0)[48:])
    output_eth_type = Signal(intbv(0)[16:])
    output_ip_version = Signal(intbv(0)[4:])
    output_ip_ihl = Signal(intbv(0)[4:])
    output_ip_dscp = Signal(intbv(0)[6:])
    output_ip_ecn = Signal(intbv(0)[2:])
    output_ip_length = Signal(intbv(0)[16:])
    output_ip_identification = Signal(intbv(0)[16:])
    output_ip_flags = Signal(intbv(0)[3:])
    output_ip_fragment_offset = Signal(intbv(0)[13:])
    output_ip_ttl = Signal(intbv(0)[8:])
    output_ip_protocol = Signal(intbv(0)[8:])
    output_ip_header_checksum = Signal(intbv(0)[16:])
    output_ip_source_ip = Signal(intbv(0)[32:])
    output_ip_dest_ip = Signal(intbv(0)[32:])
    output_udp_source_port = Signal(intbv(0)[16:])
    output_udp_dest_port = Signal(intbv(0)[16:])
    output_udp_length = Signal(intbv(0)[16:])
    output_udp_checksum = Signal(intbv(0)[16:])
    output_udp_payload_tdata = Signal(intbv(0)[8:])
    output_udp_payload_tvalid = Signal(bool(0))
    output_udp_payload_tlast = Signal(bool(0))
    output_udp_payload_tuser = Signal(bool(0))

    # sources and sinks
    source_0_queue = Queue()
    source_0_pause = Signal(bool(0))
    source_1_queue = Queue()
    source_1_pause = Signal(bool(0))
    source_2_queue = Queue()
    source_2_pause = Signal(bool(0))
    source_3_queue = Queue()
    source_3_pause = Signal(bool(0))
    sink_queue = Queue()
    sink_pause = Signal(bool(0))

    source_0 = udp_ep.UDPFrameSource(clk,
                                     rst,
                                     udp_hdr_ready=input_0_udp_hdr_ready,
                                     udp_hdr_valid=input_0_udp_hdr_valid,
                                     eth_dest_mac=input_0_eth_dest_mac,
                                     eth_src_mac=input_0_eth_src_mac,
                                     eth_type=input_0_eth_type,
                                     ip_version=input_0_ip_version,
                                     ip_ihl=input_0_ip_ihl,
                                     ip_dscp=input_0_ip_dscp,
                                     ip_ecn=input_0_ip_ecn,
                                     ip_length=input_0_ip_length,
                                     ip_identification=input_0_ip_identification,
                                     ip_flags=input_0_ip_flags,
                                     ip_fragment_offset=input_0_ip_fragment_offset,
                                     ip_ttl=input_0_ip_ttl,
                                     ip_protocol=input_0_ip_protocol,
                                     ip_header_checksum=input_0_ip_header_checksum,
                                     ip_source_ip=input_0_ip_source_ip,
                                     ip_dest_ip=input_0_ip_dest_ip,
                                     udp_source_port=input_0_udp_source_port,
                                     udp_dest_port=input_0_udp_dest_port,
                                     udp_length=input_0_udp_length,
                                     udp_checksum=input_0_udp_checksum,
                                     udp_payload_tdata=input_0_udp_payload_tdata,
                                     udp_payload_tvalid=input_0_udp_payload_tvalid,
                                     udp_payload_tready=input_0_udp_payload_tready,
                                     udp_payload_tlast=input_0_udp_payload_tlast,
                                     udp_payload_tuser=input_0_udp_payload_tuser,
                                     fifo=source_0_queue,
                                     pause=source_0_pause,
                                     name='source0')

    source_1 = udp_ep.UDPFrameSource(clk,
                                     rst,
                                     udp_hdr_ready=input_1_udp_hdr_ready,
                                     udp_hdr_valid=input_1_udp_hdr_valid,
                                     eth_dest_mac=input_1_eth_dest_mac,
                                     eth_src_mac=input_1_eth_src_mac,
                                     eth_type=input_1_eth_type,
                                     ip_version=input_1_ip_version,
                                     ip_ihl=input_1_ip_ihl,
                                     ip_dscp=input_1_ip_dscp,
                                     ip_ecn=input_1_ip_ecn,
                                     ip_length=input_1_ip_length,
                                     ip_identification=input_1_ip_identification,
                                     ip_flags=input_1_ip_flags,
                                     ip_fragment_offset=input_1_ip_fragment_offset,
                                     ip_ttl=input_1_ip_ttl,
                                     ip_protocol=input_1_ip_protocol,
                                     ip_header_checksum=input_1_ip_header_checksum,
                                     ip_source_ip=input_1_ip_source_ip,
                                     ip_dest_ip=input_1_ip_dest_ip,
                                     udp_source_port=input_1_udp_source_port,
                                     udp_dest_port=input_1_udp_dest_port,
                                     udp_length=input_1_udp_length,
                                     udp_checksum=input_1_udp_checksum,
                                     udp_payload_tdata=input_1_udp_payload_tdata,
                                     udp_payload_tvalid=input_1_udp_payload_tvalid,
                                     udp_payload_tready=input_1_udp_payload_tready,
                                     udp_payload_tlast=input_1_udp_payload_tlast,
                                     udp_payload_tuser=input_1_udp_payload_tuser,
                                     fifo=source_1_queue,
                                     pause=source_1_pause,
                                     name='source1')

    source_2 = udp_ep.UDPFrameSource(clk,
                                     rst,
                                     udp_hdr_ready=input_2_udp_hdr_ready,
                                     udp_hdr_valid=input_2_udp_hdr_valid,
                                     eth_dest_mac=input_2_eth_dest_mac,
                                     eth_src_mac=input_2_eth_src_mac,
                                     eth_type=input_2_eth_type,
                                     ip_version=input_2_ip_version,
                                     ip_ihl=input_2_ip_ihl,
                                     ip_dscp=input_2_ip_dscp,
                                     ip_ecn=input_2_ip_ecn,
                                     ip_length=input_2_ip_length,
                                     ip_identification=input_2_ip_identification,
                                     ip_flags=input_2_ip_flags,
                                     ip_fragment_offset=input_2_ip_fragment_offset,
                                     ip_ttl=input_2_ip_ttl,
                                     ip_protocol=input_2_ip_protocol,
                                     ip_header_checksum=input_2_ip_header_checksum,
                                     ip_source_ip=input_2_ip_source_ip,
                                     ip_dest_ip=input_2_ip_dest_ip,
                                     udp_source_port=input_2_udp_source_port,
                                     udp_dest_port=input_2_udp_dest_port,
                                     udp_length=input_2_udp_length,
                                     udp_checksum=input_2_udp_checksum,
                                     udp_payload_tdata=input_2_udp_payload_tdata,
                                     udp_payload_tvalid=input_2_udp_payload_tvalid,
                                     udp_payload_tready=input_2_udp_payload_tready,
                                     udp_payload_tlast=input_2_udp_payload_tlast,
                                     udp_payload_tuser=input_2_udp_payload_tuser,
                                     fifo=source_2_queue,
                                     pause=source_2_pause,
                                     name='source2')

    source_3 = udp_ep.UDPFrameSource(clk,
                                     rst,
                                     udp_hdr_ready=input_3_udp_hdr_ready,
                                     udp_hdr_valid=input_3_udp_hdr_valid,
                                     eth_dest_mac=input_3_eth_dest_mac,
                                     eth_src_mac=input_3_eth_src_mac,
                                     eth_type=input_3_eth_type,
                                     ip_version=input_3_ip_version,
                                     ip_ihl=input_3_ip_ihl,
                                     ip_dscp=input_3_ip_dscp,
                                     ip_ecn=input_3_ip_ecn,
                                     ip_length=input_3_ip_length,
                                     ip_identification=input_3_ip_identification,
                                     ip_flags=input_3_ip_flags,
                                     ip_fragment_offset=input_3_ip_fragment_offset,
                                     ip_ttl=input_3_ip_ttl,
                                     ip_protocol=input_3_ip_protocol,
                                     ip_header_checksum=input_3_ip_header_checksum,
                                     ip_source_ip=input_3_ip_source_ip,
                                     ip_dest_ip=input_3_ip_dest_ip,
                                     udp_source_port=input_3_udp_source_port,
                                     udp_dest_port=input_3_udp_dest_port,
                                     udp_length=input_3_udp_length,
                                     udp_checksum=input_3_udp_checksum,
                                     udp_payload_tdata=input_3_udp_payload_tdata,
                                     udp_payload_tvalid=input_3_udp_payload_tvalid,
                                     udp_payload_tready=input_3_udp_payload_tready,
                                     udp_payload_tlast=input_3_udp_payload_tlast,
                                     udp_payload_tuser=input_3_udp_payload_tuser,
                                     fifo=source_3_queue,
                                     pause=source_3_pause,
                                     name='source3')

    sink = udp_ep.UDPFrameSink(clk,
                               rst,
                               udp_hdr_ready=output_udp_hdr_ready,
                               udp_hdr_valid=output_udp_hdr_valid,
                               eth_dest_mac=output_eth_dest_mac,
                               eth_src_mac=output_eth_src_mac,
                               eth_type=output_eth_type,
                               ip_version=output_ip_version,
                               ip_ihl=output_ip_ihl,
                               ip_dscp=output_ip_dscp,
                               ip_ecn=output_ip_ecn,
                               ip_length=output_ip_length,
                               ip_identification=output_ip_identification,
                               ip_flags=output_ip_flags,
                               ip_fragment_offset=output_ip_fragment_offset,
                               ip_ttl=output_ip_ttl,
                               ip_protocol=output_ip_protocol,
                               ip_header_checksum=output_ip_header_checksum,
                               ip_source_ip=output_ip_source_ip,
                               ip_dest_ip=output_ip_dest_ip,
                               udp_source_port=output_udp_source_port,
                               udp_dest_port=output_udp_dest_port,
                               udp_length=output_udp_length,
                               udp_checksum=output_udp_checksum,
                               udp_payload_tdata=output_udp_payload_tdata,
                               udp_payload_tvalid=output_udp_payload_tvalid,
                               udp_payload_tready=output_udp_payload_tready,
                               udp_payload_tlast=output_udp_payload_tlast,
                               udp_payload_tuser=output_udp_payload_tuser,
                               fifo=sink_queue,
                               pause=sink_pause,
                               name='sink')

    # DUT
    dut = dut_udp_mux_4(clk,
                       rst,
                       current_test,

                       input_0_udp_hdr_valid,
                       input_0_udp_hdr_ready,
                       input_0_eth_dest_mac,
                       input_0_eth_src_mac,
                       input_0_eth_type,
                       input_0_ip_version,
                       input_0_ip_ihl,
                       input_0_ip_dscp,
                       input_0_ip_ecn,
                       input_0_ip_length,
                       input_0_ip_identification,
                       input_0_ip_flags,
                       input_0_ip_fragment_offset,
                       input_0_ip_ttl,
                       input_0_ip_protocol,
                       input_0_ip_header_checksum,
                       input_0_ip_source_ip,
                       input_0_ip_dest_ip,
                       input_0_udp_source_port,
                       input_0_udp_dest_port,
                       input_0_udp_length,
                       input_0_udp_checksum,
                       input_0_udp_payload_tdata,
                       input_0_udp_payload_tvalid,
                       input_0_udp_payload_tready,
                       input_0_udp_payload_tlast,
                       input_0_udp_payload_tuser,
                       input_1_udp_hdr_valid,
                       input_1_udp_hdr_ready,
                       input_1_eth_dest_mac,
                       input_1_eth_src_mac,
                       input_1_eth_type,
                       input_1_ip_version,
                       input_1_ip_ihl,
                       input_1_ip_dscp,
                       input_1_ip_ecn,
                       input_1_ip_length,
                       input_1_ip_identification,
                       input_1_ip_flags,
                       input_1_ip_fragment_offset,
                       input_1_ip_ttl,
                       input_1_ip_protocol,
                       input_1_ip_header_checksum,
                       input_1_ip_source_ip,
                       input_1_ip_dest_ip,
                       input_1_udp_source_port,
                       input_1_udp_dest_port,
                       input_1_udp_length,
                       input_1_udp_checksum,
                       input_1_udp_payload_tdata,
                       input_1_udp_payload_tvalid,
                       input_1_udp_payload_tready,
                       input_1_udp_payload_tlast,
                       input_1_udp_payload_tuser,
                       input_2_udp_hdr_valid,
                       input_2_udp_hdr_ready,
                       input_2_eth_dest_mac,
                       input_2_eth_src_mac,
                       input_2_eth_type,
                       input_2_ip_version,
                       input_2_ip_ihl,
                       input_2_ip_dscp,
                       input_2_ip_ecn,
                       input_2_ip_length,
                       input_2_ip_identification,
                       input_2_ip_flags,
                       input_2_ip_fragment_offset,
                       input_2_ip_ttl,
                       input_2_ip_protocol,
                       input_2_ip_header_checksum,
                       input_2_ip_source_ip,
                       input_2_ip_dest_ip,
                       input_2_udp_source_port,
                       input_2_udp_dest_port,
                       input_2_udp_length,
                       input_2_udp_checksum,
                       input_2_udp_payload_tdata,
                       input_2_udp_payload_tvalid,
                       input_2_udp_payload_tready,
                       input_2_udp_payload_tlast,
                       input_2_udp_payload_tuser,
                       input_3_udp_hdr_valid,
                       input_3_udp_hdr_ready,
                       input_3_eth_dest_mac,
                       input_3_eth_src_mac,
                       input_3_eth_type,
                       input_3_ip_version,
                       input_3_ip_ihl,
                       input_3_ip_dscp,
                       input_3_ip_ecn,
                       input_3_ip_length,
                       input_3_ip_identification,
                       input_3_ip_flags,
                       input_3_ip_fragment_offset,
                       input_3_ip_ttl,
                       input_3_ip_protocol,
                       input_3_ip_header_checksum,
                       input_3_ip_source_ip,
                       input_3_ip_dest_ip,
                       input_3_udp_source_port,
                       input_3_udp_dest_port,
                       input_3_udp_length,
                       input_3_udp_checksum,
                       input_3_udp_payload_tdata,
                       input_3_udp_payload_tvalid,
                       input_3_udp_payload_tready,
                       input_3_udp_payload_tlast,
                       input_3_udp_payload_tuser,

                       output_udp_hdr_valid,
                       output_udp_hdr_ready,
                       output_eth_dest_mac,
                       output_eth_src_mac,
                       output_eth_type,
                       output_ip_version,
                       output_ip_ihl,
                       output_ip_dscp,
                       output_ip_ecn,
                       output_ip_length,
                       output_ip_identification,
                       output_ip_flags,
                       output_ip_fragment_offset,
                       output_ip_ttl,
                       output_ip_protocol,
                       output_ip_header_checksum,
                       output_ip_source_ip,
                       output_ip_dest_ip,
                       output_udp_source_port,
                       output_udp_dest_port,
                       output_udp_length,
                       output_udp_checksum,
                       output_udp_payload_tdata,
                       output_udp_payload_tvalid,
                       output_udp_payload_tready,
                       output_udp_payload_tlast,
                       output_udp_payload_tuser,

                       enable,
                       select)

    @always(delay(4))
    def clkgen():
        clk.next = not clk

    @instance
    def check():
        yield delay(100)
        yield clk.posedge
        rst.next = 1
        yield clk.posedge
        rst.next = 0
        yield clk.posedge
        yield delay(100)
        yield clk.posedge

        yield clk.posedge
        enable.next = True

        yield clk.posedge
        print("test 1: select port 0")
        current_test.next = 1

        select.next = 0

        test_frame = udp_ep.UDPFrame()
        test_frame.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame.eth_src_mac = 0x5A5152535455
        test_frame.eth_type = 0x8000
        test_frame.ip_version = 4
        test_frame.ip_ihl = 5
        test_frame.ip_dscp = 0
        test_frame.ip_ecn = 0
        test_frame.ip_length = None
        test_frame.ip_identification = 0
        test_frame.ip_flags = 2
        test_frame.ip_fragment_offset = 0
        test_frame.ip_ttl = 64
        test_frame.ip_protocol = 0x11
        test_frame.ip_header_checksum = None
        test_frame.ip_source_ip = 0xc0a80165
        test_frame.ip_dest_ip = 0xc0a80164
        test_frame.udp_source_port = 1
        test_frame.udp_dest_port = 2
        test_frame.udp_length = None
        test_frame.udp_checksum = None
        test_frame.payload = bytearray(range(32))
        test_frame.build()

        source_0_queue.put(test_frame)
        yield clk.posedge
        yield clk.posedge

        while input_0_udp_payload_tvalid or input_1_udp_payload_tvalid or input_2_udp_payload_tvalid or input_3_udp_payload_tvalid:
            yield clk.posedge
        yield clk.posedge
        yield clk.posedge

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame

        yield delay(100)

        yield clk.posedge
        print("test 2: select port 1")
        current_test.next = 2

        select.next = 1

        test_frame = udp_ep.UDPFrame()
        test_frame.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame.eth_src_mac = 0x5A5152535455
        test_frame.eth_type = 0x8000
        test_frame.ip_version = 4
        test_frame.ip_ihl = 5
        test_frame.ip_dscp = 0
        test_frame.ip_ecn = 0
        test_frame.ip_length = None
        test_frame.ip_identification = 0
        test_frame.ip_flags = 2
        test_frame.ip_fragment_offset = 0
        test_frame.ip_ttl = 64
        test_frame.ip_protocol = 0x11
        test_frame.ip_header_checksum = None
        test_frame.ip_source_ip = 0xc0a80165
        test_frame.ip_dest_ip = 0xc0a80164
        test_frame.udp_source_port = 1
        test_frame.udp_dest_port = 2
        test_frame.udp_length = None
        test_frame.udp_checksum = None
        test_frame.payload = bytearray(range(32))
        test_frame.build()

        source_1_queue.put(test_frame)
        yield clk.posedge
        yield clk.posedge

        while input_0_udp_payload_tvalid or input_1_udp_payload_tvalid or input_2_udp_payload_tvalid or input_3_udp_payload_tvalid:
            yield clk.posedge
        yield clk.posedge
        yield clk.posedge

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame

        yield delay(100)

        yield clk.posedge
        print("test 3: back-to-back packets, same port")
        current_test.next = 3

        select.next = 0

        test_frame1 = udp_ep.UDPFrame()
        test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame1.eth_src_mac = 0x5A5152535455
        test_frame1.eth_type = 0x8000
        test_frame1.ip_version = 4
        test_frame1.ip_ihl = 5
        test_frame1.ip_dscp = 0
        test_frame1.ip_ecn = 0
        test_frame1.ip_length = None
        test_frame1.ip_identification = 0
        test_frame1.ip_flags = 2
        test_frame1.ip_fragment_offset = 0
        test_frame1.ip_ttl = 64
        test_frame1.ip_protocol = 0x11
        test_frame1.ip_header_checksum = None
        test_frame1.ip_source_ip = 0xc0a80165
        test_frame1.ip_dest_ip = 0xc0a80164
        test_frame1.udp_source_port = 1
        test_frame1.udp_dest_port = 2
        test_frame1.udp_length = None
        test_frame1.udp_checksum = None
        test_frame1.payload = bytearray(range(32))
        test_frame1.build()
        test_frame2 = udp_ep.UDPFrame()
        test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame2.eth_src_mac = 0x5A5152535455
        test_frame2.eth_type = 0x8000
        test_frame2.ip_version = 4
        test_frame2.ip_ihl = 5
        test_frame2.ip_dscp = 0
        test_frame2.ip_ecn = 0
        test_frame2.ip_length = None
        test_frame2.ip_identification = 0
        test_frame2.ip_flags = 2
        test_frame2.ip_fragment_offset = 0
        test_frame2.ip_ttl = 64
        test_frame2.ip_protocol = 0x11
        test_frame2.ip_header_checksum = None
        test_frame2.ip_source_ip = 0xc0a80165
        test_frame2.ip_dest_ip = 0xc0a80164
        test_frame2.udp_source_port = 1
        test_frame2.udp_dest_port = 2
        test_frame2.udp_length = None
        test_frame2.udp_checksum = None
        test_frame2.payload = bytearray(range(32))
        test_frame2.build()

        source_0_queue.put(test_frame1)
        source_0_queue.put(test_frame2)
        yield clk.posedge
        yield clk.posedge

        while input_0_udp_payload_tvalid or input_1_udp_payload_tvalid or input_2_udp_payload_tvalid or input_3_udp_payload_tvalid:
            yield clk.posedge
        yield clk.posedge
        yield clk.posedge

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame1

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame2

        yield delay(100)

        yield clk.posedge
        print("test 4: back-to-back packets, different ports")
        current_test.next = 4

        select.next = 1

        test_frame1 = udp_ep.UDPFrame()
        test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame1.eth_src_mac = 0x5A5152535455
        test_frame1.eth_type = 0x8000
        test_frame1.ip_version = 4
        test_frame1.ip_ihl = 5
        test_frame1.ip_dscp = 0
        test_frame1.ip_ecn = 0
        test_frame1.ip_length = None
        test_frame1.ip_identification = 0
        test_frame1.ip_flags = 2
        test_frame1.ip_fragment_offset = 0
        test_frame1.ip_ttl = 64
        test_frame1.ip_protocol = 0x11
        test_frame1.ip_header_checksum = None
        test_frame1.ip_source_ip = 0xc0a80165
        test_frame1.ip_dest_ip = 0xc0a80164
        test_frame1.udp_source_port = 1
        test_frame1.udp_dest_port = 2
        test_frame1.udp_length = None
        test_frame1.udp_checksum = None
        test_frame1.payload = bytearray(range(32))
        test_frame1.build()
        test_frame2 = udp_ep.UDPFrame()
        test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame2.eth_src_mac = 0x5A5152535455
        test_frame2.eth_type = 0x8000
        test_frame2.ip_version = 4
        test_frame2.ip_ihl = 5
        test_frame2.ip_dscp = 0
        test_frame2.ip_ecn = 0
        test_frame2.ip_length = None
        test_frame2.ip_identification = 0
        test_frame2.ip_flags = 2
        test_frame2.ip_fragment_offset = 0
        test_frame2.ip_ttl = 64
        test_frame2.ip_protocol = 0x11
        test_frame2.ip_header_checksum = None
        test_frame2.ip_source_ip = 0xc0a80165
        test_frame2.ip_dest_ip = 0xc0a80164
        test_frame2.udp_source_port = 1
        test_frame2.udp_dest_port = 2
        test_frame2.udp_length = None
        test_frame2.udp_checksum = None
        test_frame2.payload = bytearray(range(32))
        test_frame2.build()

        source_1_queue.put(test_frame1)
        source_2_queue.put(test_frame2)
        yield clk.posedge
        yield clk.posedge

        while input_0_udp_payload_tvalid or input_1_udp_payload_tvalid or input_2_udp_payload_tvalid or input_3_udp_payload_tvalid:
            yield clk.posedge
            select.next = 2
        yield clk.posedge
        yield clk.posedge

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame1

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame2

        yield delay(100)

        yield clk.posedge
        print("test 5: alterate pause source")
        current_test.next = 5

        select.next = 1

        test_frame1 = udp_ep.UDPFrame()
        test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame1.eth_src_mac = 0x5A5152535455
        test_frame1.eth_type = 0x8000
        test_frame1.ip_version = 4
        test_frame1.ip_ihl = 5
        test_frame1.ip_dscp = 0
        test_frame1.ip_ecn = 0
        test_frame1.ip_length = None
        test_frame1.ip_identification = 0
        test_frame1.ip_flags = 2
        test_frame1.ip_fragment_offset = 0
        test_frame1.ip_ttl = 64
        test_frame1.ip_protocol = 0x11
        test_frame1.ip_header_checksum = None
        test_frame1.ip_source_ip = 0xc0a80165
        test_frame1.ip_dest_ip = 0xc0a80164
        test_frame1.udp_source_port = 1
        test_frame1.udp_dest_port = 2
        test_frame1.udp_length = None
        test_frame1.udp_checksum = None
        test_frame1.payload = bytearray(range(32))
        test_frame1.build()
        test_frame2 = udp_ep.UDPFrame()
        test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame2.eth_src_mac = 0x5A5152535455
        test_frame2.eth_type = 0x8000
        test_frame2.ip_version = 4
        test_frame2.ip_ihl = 5
        test_frame2.ip_dscp = 0
        test_frame2.ip_ecn = 0
        test_frame2.ip_length = None
        test_frame2.ip_identification = 0
        test_frame2.ip_flags = 2
        test_frame2.ip_fragment_offset = 0
        test_frame2.ip_ttl = 64
        test_frame2.ip_protocol = 0x11
        test_frame2.ip_header_checksum = None
        test_frame2.ip_source_ip = 0xc0a80165
        test_frame2.ip_dest_ip = 0xc0a80164
        test_frame2.udp_source_port = 1
        test_frame2.udp_dest_port = 2
        test_frame2.udp_length = None
        test_frame2.udp_checksum = None
        test_frame2.payload = bytearray(range(32))
        test_frame2.build()

        source_1_queue.put(test_frame1)
        source_2_queue.put(test_frame2)
        yield clk.posedge
        yield clk.posedge

        while input_0_udp_payload_tvalid or input_1_udp_payload_tvalid or input_2_udp_payload_tvalid or input_3_udp_payload_tvalid:
            source_0_pause.next = True
            source_1_pause.next = True
            source_2_pause.next = True
            source_3_pause.next = True
            yield clk.posedge
            yield clk.posedge
            yield clk.posedge
            source_0_pause.next = False
            source_1_pause.next = False
            source_2_pause.next = False
            source_3_pause.next = False
            yield clk.posedge
            select.next = 2
        yield clk.posedge
        yield clk.posedge

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame1

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame2

        yield delay(100)

        yield clk.posedge
        print("test 6: alterate pause sink")
        current_test.next = 6

        select.next = 1

        test_frame1 = udp_ep.UDPFrame()
        test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame1.eth_src_mac = 0x5A5152535455
        test_frame1.eth_type = 0x8000
        test_frame1.ip_version = 4
        test_frame1.ip_ihl = 5
        test_frame1.ip_dscp = 0
        test_frame1.ip_ecn = 0
        test_frame1.ip_length = None
        test_frame1.ip_identification = 0
        test_frame1.ip_flags = 2
        test_frame1.ip_fragment_offset = 0
        test_frame1.ip_ttl = 64
        test_frame1.ip_protocol = 0x11
        test_frame1.ip_header_checksum = None
        test_frame1.ip_source_ip = 0xc0a80165
        test_frame1.ip_dest_ip = 0xc0a80164
        test_frame1.udp_source_port = 1
        test_frame1.udp_dest_port = 2
        test_frame1.udp_length = None
        test_frame1.udp_checksum = None
        test_frame1.payload = bytearray(range(32))
        test_frame1.build()
        test_frame2 = udp_ep.UDPFrame()
        test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
        test_frame2.eth_src_mac = 0x5A5152535455
        test_frame2.eth_type = 0x8000
        test_frame2.ip_version = 4
        test_frame2.ip_ihl = 5
        test_frame2.ip_dscp = 0
        test_frame2.ip_ecn = 0
        test_frame2.ip_length = None
        test_frame2.ip_identification = 0
        test_frame2.ip_flags = 2
        test_frame2.ip_fragment_offset = 0
        test_frame2.ip_ttl = 64
        test_frame2.ip_protocol = 0x11
        test_frame2.ip_header_checksum = None
        test_frame2.ip_source_ip = 0xc0a80165
        test_frame2.ip_dest_ip = 0xc0a80164
        test_frame2.udp_source_port = 1
        test_frame2.udp_dest_port = 2
        test_frame2.udp_length = None
        test_frame2.udp_checksum = None
        test_frame2.payload = bytearray(range(32))
        test_frame2.build()

        source_1_queue.put(test_frame1)
        source_2_queue.put(test_frame2)
        yield clk.posedge
        yield clk.posedge

        while input_0_udp_payload_tvalid or input_1_udp_payload_tvalid or input_2_udp_payload_tvalid or input_3_udp_payload_tvalid:
            sink_pause.next = True
            yield clk.posedge
            yield clk.posedge
            yield clk.posedge
            sink_pause.next = False
            yield clk.posedge
            select.next = 2
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame1

        rx_frame = None
        if not sink_queue.empty():
            rx_frame = sink_queue.get()

        assert rx_frame == test_frame2

        yield delay(100)

        raise StopSimulation

    return dut, source_0, source_1, source_2, source_3, sink, clkgen, check

def test_bench():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sim = Simulation(bench())
    sim.run()

if __name__ == '__main__':
    print("Running test...")
    test_bench()

