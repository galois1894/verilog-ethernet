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

import eth_ep
import ip_ep

module = 'ip_eth_rx_64'

srcs = []

srcs.append("../rtl/%s.v" % module)
srcs.append("test_%s.v" % module)

src = ' '.join(srcs)

build_cmd = "iverilog -o test_%s.vvp %s" % (module, src)

def dut_ip_eth_rx_64(clk,
                    rst,
                    current_test,

                    input_eth_hdr_valid,
                    input_eth_hdr_ready,
                    input_eth_dest_mac,
                    input_eth_src_mac,
                    input_eth_type,
                    input_eth_payload_tdata,
                    input_eth_payload_tkeep,
                    input_eth_payload_tvalid,
                    input_eth_payload_tready,
                    input_eth_payload_tlast,
                    input_eth_payload_tuser,

                    output_ip_hdr_valid,
                    output_ip_hdr_ready,
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
                    output_ip_payload_tdata,
                    output_ip_payload_tkeep,
                    output_ip_payload_tvalid,
                    output_ip_payload_tready,
                    output_ip_payload_tlast,
                    output_ip_payload_tuser,

                    busy,
                    error_header_early_termination,
                    error_payload_early_termination,
                    error_invalid_header,
                    error_invalid_checksum):

    if os.system(build_cmd):
        raise Exception("Error running build command")
    return Cosimulation("vvp -m myhdl test_%s.vvp -lxt2" % module,
                clk=clk,
                rst=rst,
                current_test=current_test,

                input_eth_hdr_valid=input_eth_hdr_valid,
                input_eth_hdr_ready=input_eth_hdr_ready,
                input_eth_dest_mac=input_eth_dest_mac,
                input_eth_src_mac=input_eth_src_mac,
                input_eth_type=input_eth_type,
                input_eth_payload_tdata=input_eth_payload_tdata,
                input_eth_payload_tkeep=input_eth_payload_tkeep,
                input_eth_payload_tvalid=input_eth_payload_tvalid,
                input_eth_payload_tready=input_eth_payload_tready,
                input_eth_payload_tlast=input_eth_payload_tlast,
                input_eth_payload_tuser=input_eth_payload_tuser,

                output_ip_hdr_valid=output_ip_hdr_valid,
                output_ip_hdr_ready=output_ip_hdr_ready,
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
                output_ip_payload_tdata=output_ip_payload_tdata,
                output_ip_payload_tkeep=output_ip_payload_tkeep,
                output_ip_payload_tvalid=output_ip_payload_tvalid,
                output_ip_payload_tready=output_ip_payload_tready,
                output_ip_payload_tlast=output_ip_payload_tlast,
                output_ip_payload_tuser=output_ip_payload_tuser,

                busy=busy,
                error_header_early_termination=error_header_early_termination,
                error_payload_early_termination=error_payload_early_termination,
                error_invalid_header=error_invalid_header,
                error_invalid_checksum=error_invalid_checksum)

def bench():

    # Inputs
    clk = Signal(bool(0))
    rst = Signal(bool(0))
    current_test = Signal(intbv(0)[8:])

    input_eth_hdr_valid = Signal(bool(0))
    input_eth_dest_mac = Signal(intbv(0)[48:])
    input_eth_src_mac = Signal(intbv(0)[48:])
    input_eth_type = Signal(intbv(0)[16:])
    input_eth_payload_tdata = Signal(intbv(0)[64:])
    input_eth_payload_tkeep = Signal(intbv(0)[8:])
    input_eth_payload_tvalid = Signal(bool(0))
    input_eth_payload_tlast = Signal(bool(0))
    input_eth_payload_tuser = Signal(bool(0))
    output_ip_hdr_ready = Signal(bool(0))
    output_ip_payload_tready = Signal(bool(0))

    # Outputs
    input_eth_hdr_ready = Signal(bool(0))
    input_eth_payload_tready = Signal(bool(0))
    output_ip_hdr_valid = Signal(bool(0))
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
    output_ip_payload_tdata = Signal(intbv(0)[64:])
    output_ip_payload_tkeep = Signal(intbv(0)[8:])
    output_ip_payload_tvalid = Signal(bool(0))
    output_ip_payload_tlast = Signal(bool(0))
    output_ip_payload_tuser = Signal(bool(0))
    busy = Signal(bool(0))
    error_header_early_termination = Signal(bool(0))
    error_payload_early_termination = Signal(bool(0))
    error_invalid_header = Signal(bool(0))
    error_invalid_checksum = Signal(bool(0))

    # sources and sinks
    source_queue = Queue()
    source_pause = Signal(bool(0))
    sink_queue = Queue()
    sink_pause = Signal(bool(0))

    source = eth_ep.EthFrameSource(clk,
                                   rst,
                                   eth_hdr_ready=input_eth_hdr_ready,
                                   eth_hdr_valid=input_eth_hdr_valid,
                                   eth_dest_mac=input_eth_dest_mac,
                                   eth_src_mac=input_eth_src_mac,
                                   eth_type=input_eth_type,
                                   eth_payload_tdata=input_eth_payload_tdata,
                                   eth_payload_tkeep=input_eth_payload_tkeep,
                                   eth_payload_tvalid=input_eth_payload_tvalid,
                                   eth_payload_tready=input_eth_payload_tready,
                                   eth_payload_tlast=input_eth_payload_tlast,
                                   eth_payload_tuser=input_eth_payload_tuser,
                                   fifo=source_queue,
                                   pause=source_pause,
                                   name='source')

    sink = ip_ep.IPFrameSink(clk,
                             rst,
                             ip_hdr_ready=output_ip_hdr_ready,
                             ip_hdr_valid=output_ip_hdr_valid,
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
                             ip_payload_tdata=output_ip_payload_tdata,
                             ip_payload_tkeep=output_ip_payload_tkeep,
                             ip_payload_tvalid=output_ip_payload_tvalid,
                             ip_payload_tready=output_ip_payload_tready,
                             ip_payload_tlast=output_ip_payload_tlast,
                             ip_payload_tuser=output_ip_payload_tuser,
                             fifo=sink_queue,
                             pause=sink_pause,
                             name='sink')

    # DUT
    dut = dut_ip_eth_rx_64(clk,
                        rst,
                        current_test,

                        input_eth_hdr_valid,
                        input_eth_hdr_ready,
                        input_eth_dest_mac,
                        input_eth_src_mac,
                        input_eth_type,
                        input_eth_payload_tdata,
                        input_eth_payload_tkeep,
                        input_eth_payload_tvalid,
                        input_eth_payload_tready,
                        input_eth_payload_tlast,
                        input_eth_payload_tuser,

                        output_ip_hdr_valid,
                        output_ip_hdr_ready,
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
                        output_ip_payload_tdata,
                        output_ip_payload_tkeep,
                        output_ip_payload_tvalid,
                        output_ip_payload_tready,
                        output_ip_payload_tlast,
                        output_ip_payload_tuser,

                        busy,
                        error_header_early_termination,
                        error_payload_early_termination,
                        error_invalid_header,
                        error_invalid_checksum)

    @always(delay(4))
    def clkgen():
        clk.next = not clk

    error_header_early_termination_asserted = Signal(bool(0))
    error_payload_early_termination_asserted = Signal(bool(0))
    error_invalid_header_asserted = Signal(bool(0))
    error_invalid_checksum_asserted = Signal(bool(0))

    @always(clk.posedge)
    def monitor():
        if (error_header_early_termination):
            error_header_early_termination_asserted.next = 1
        if (error_payload_early_termination):
            error_payload_early_termination_asserted.next = 1
        if (error_invalid_header):
            error_invalid_header_asserted.next = 1
        if (error_invalid_checksum):
            error_invalid_checksum_asserted.next = 1

    def wait_normal():
        while input_eth_payload_tvalid or output_ip_payload_tvalid or input_eth_hdr_valid:
            yield clk.posedge

    def wait_pause_source():
        while input_eth_payload_tvalid or output_ip_payload_tvalid or input_eth_hdr_valid:
            source_pause.next = True
            yield clk.posedge
            yield clk.posedge
            yield clk.posedge
            source_pause.next = False
            yield clk.posedge

    def wait_pause_sink():
        while input_eth_payload_tvalid or output_ip_payload_tvalid or input_eth_hdr_valid:
            sink_pause.next = True
            yield clk.posedge
            yield clk.posedge
            yield clk.posedge
            sink_pause.next = False
            yield clk.posedge

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

        for payload_len in range(1,18):
            yield clk.posedge
            print("test 1: test packet, length %d" % payload_len)
            current_test.next = 1

            test_frame = ip_ep.IPFrame()
            test_frame.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame.eth_src_mac = 0x5A5152535455
            test_frame.eth_type = 0x0800
            test_frame.ip_version = 4
            test_frame.ip_ihl = 5
            test_frame.ip_length = None
            test_frame.ip_identification = 0
            test_frame.ip_flags = 2
            test_frame.ip_fragment_offset = 0
            test_frame.ip_ttl = 64
            test_frame.ip_protocol = 0x11
            test_frame.ip_header_checksum = None
            test_frame.ip_source_ip = 0xc0a80164
            test_frame.ip_dest_ip = 0xc0a80165
            test_frame.payload = bytearray(range(payload_len))
            test_frame.build()
            eth_frame = test_frame.build_eth()

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                source_queue.put(eth_frame)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 2: back-to-back packets, length %d" % payload_len)
            current_test.next = 2

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

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

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 3: tuser assert, length %d" % payload_len)
            current_test.next = 3

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.user = 1

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame1
                assert rx_frame.payload.user[-1]

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 4: trailing bytes (1), length %d" % payload_len)
            current_test.next = 4

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.data += bytearray(b'\x00')

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

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

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 5: trailing bytes (10), length %d" % payload_len)
            current_test.next = 5

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.data += bytearray(b'\x00'*10)

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

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

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 6: trailing bytes with tuser assert (1), length %d" % payload_len)
            current_test.next = 6

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.data += bytearray(b'\x00')
            eth_frame1.payload.user = 1

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame1
                assert rx_frame.payload.user[-1]

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 7: trailing bytes with tuser assert (10), length %d" % payload_len)
            current_test.next = 7

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.data += bytearray(b'\x00'*10)
            eth_frame1.payload.user = 1

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame1
                assert rx_frame.payload.user[-1]

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 8: truncated payload (1), length %d" % payload_len)
            current_test.next = 8

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len+1))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.data = eth_frame1.payload.data[:-1]

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                error_payload_early_termination_asserted.next = 0

                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame.payload.user[-1]
                assert error_payload_early_termination_asserted

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 9: truncated payload (10), length %d" % payload_len)
            current_test.next = 9

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len+10))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.data = eth_frame1.payload.data[:-10]

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                error_payload_early_termination_asserted.next = 0

                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame.payload.user[-1]
                assert error_payload_early_termination_asserted

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 10: bad IHL, length %d" % payload_len)
            current_test.next = 10

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 6
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                error_invalid_header_asserted.next = 0

                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                assert error_invalid_header_asserted

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

            yield clk.posedge
            print("test 11: bad checksum, length %d" % payload_len)
            current_test.next = 11

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = 0x1234
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(payload_len))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(payload_len))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                error_invalid_checksum_asserted.next = 0

                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                assert error_invalid_checksum_asserted

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

        for length in range(1,21):
            yield clk.posedge
            print("test 12: truncated header, length %d" % length)
            current_test.next = 12

            test_frame1 = ip_ep.IPFrame()
            test_frame1.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame1.eth_src_mac = 0x5A5152535455
            test_frame1.eth_type = 0x0800
            test_frame1.ip_version = 4
            test_frame1.ip_ihl = 5
            test_frame1.ip_length = None
            test_frame1.ip_identification = 0
            test_frame1.ip_flags = 2
            test_frame1.ip_fragment_offset = 0
            test_frame1.ip_ttl = 64
            test_frame1.ip_protocol = 0x11
            test_frame1.ip_header_checksum = None
            test_frame1.ip_source_ip = 0xc0a80164
            test_frame1.ip_dest_ip = 0xc0a80165
            test_frame1.payload = bytearray(range(16))
            test_frame1.build()
            test_frame2 = ip_ep.IPFrame()
            test_frame2.eth_dest_mac = 0xDAD1D2D3D4D5
            test_frame2.eth_src_mac = 0x5A5152535455
            test_frame2.eth_type = 0x0800
            test_frame2.ip_version = 4
            test_frame2.ip_ihl = 5
            test_frame2.ip_length = None
            test_frame2.ip_identification = 0
            test_frame2.ip_flags = 2
            test_frame2.ip_fragment_offset = 0
            test_frame2.ip_ttl = 64
            test_frame2.ip_protocol = 0x11
            test_frame2.ip_header_checksum = None
            test_frame2.ip_source_ip = 0xc0a80164
            test_frame2.ip_dest_ip = 0xc0a80166
            test_frame2.payload = bytearray(range(16))
            test_frame2.build()

            eth_frame1 = test_frame1.build_eth()
            eth_frame2 = test_frame2.build_eth()

            eth_frame1.payload.data = eth_frame1.payload.data[:length]

            for wait in wait_normal, wait_pause_source, wait_pause_sink:
                error_header_early_termination_asserted.next = 0

                source_queue.put(eth_frame1)
                source_queue.put(eth_frame2)
                yield clk.posedge
                yield clk.posedge

                yield wait()

                yield clk.posedge
                yield clk.posedge
                yield clk.posedge

                assert error_header_early_termination_asserted

                rx_frame = None
                if not sink_queue.empty():
                    rx_frame = sink_queue.get()

                assert rx_frame == test_frame2

                assert sink_queue.empty()

                yield delay(100)

        raise StopSimulation

    return dut, source, sink, clkgen, monitor, check

def test_bench():
    sim = Simulation(bench())
    sim.run()

if __name__ == '__main__':
    print("Running test...")
    test_bench()

