.. Copyright The zephyr_hc32f4a0 Contributors
.. SPDX-License-Identifier: Apache-2.0

UYUP-RPI-A-2.5 HC32F4A0PITB
###########################

The board target is ``uyup_rpi_a/hc32f4a0pitb``. It uses an HC32F4A0PITB
in the LQFP100 package, with 2 MiB of flash and 512 KiB of main SRAM starting
at ``0x1ffe0000``. The separate 4 KiB backup SRAM is not part of main SRAM.

Initial support
***************

The fitted crystal is 12 MHz. PLLH uses M=1, N=64 and P/Q/R=16, giving a
768 MHz VCO and 48 MHz system/USB clocks. Flash and SRAM wait cycles are
configured before the frequency increase. The port supports Cortex-M startup,
SysTick, polling USART1, basic GPIO, USBFS CDC ACM and the 96-bit hardware ID.
GPIO interrupts, DMA and flash-controller APIs are not yet implemented.

The console is USART1 at 115200 baud, 8 data bits, no parity and one stop bit.
TX is PA9 and RX is PA10. The onboard CMSIS-DAP provides both SWD and the
serial bridge over its USB connector. ``led0`` is the active-low blue LED
on PD10; ``led1`` is the active-low green LED on PE15.

Package pins
************

The datasheet Rev1.60, table 2-3, gives the LQFP100 port availability:
PA0..PA15, PB0..PB15, PC0..PC15, PD0..PD15, PE0..PE15, PH0, PH1 and PI13.
All other GPIO slots are NC and are excluded by ``gpio-reserved-ranges``
in the package DTS. Ports F and G, the crystal port H and the boot-mode
port I remain disabled in the board DTS.

Build and debug
***************

Build the console and LED sample from this complete project with::

   python scripts/project.py build

The pyOCD runner loads ``debug/pyocd.yaml`` from the project root and uses
the ``hc32f4a0xi`` target with 10 MHz SWD. That configuration applies the
project's SRAM-address correction and disables automatic device unlocking.
The board expects its onboard CMSIS-DAP 2.x probe with WinUSB on Windows.

Compilation and image-layout validation do not verify physical SWD,
serial output, LED behavior, timing or oscillator operation. Record those
results separately when the board is connected.

Onboard DAP mode selection
**************************

The board schematic documents a persistent cycle: CMSIS-DAP 2.x, 1.x,
disabled, then 2.x again. Keep USB2/DAP connected, switch SW1 off, hold
SW2 (target reset), switch SW1 on, and release SW2. Perform one cycle at
a time and check ``python -m pyocd list`` and the host USB enumeration.
If USB1 is also connected, ensure SW1 actually removes board power.
Do not hold SW2 during an ordinary power cycle.

In the 2026-10-06 board test, the 1.x HID mode led to RESET/halt failures
during pyOCD initialization. After switching through disabled to 2.x,
Open Cherry USB CMSIS-DAP used the PyUSBv2 transport and passed programming,
byte-for-byte readback, a main breakpoint and instruction stepping at 10 MHz.
This result is specific to the tested board/probe firmware; it does not mean
pyOCD generally lacks CMSIS-DAP v1 support. Probe IDs and COM port numbers
change with the mode and must be queried again. A missing probe immediately
after the first transition from 1.x is consistent with the disabled state;
perform the next cycle and verify 2.x before programming.

Native USB1 console
*******************

USB1 connects PA11/PA12 to the HC32 USBFS controller. It uses Zephyr's DWC2
UDC and native CDC ACM stack, independently of the USB2/DAP serial bridge.
The USBFS interrupt source 399 is routed to NVIC slot 30. PA9 is USART1 TX,
so this board enables VBUS override and cannot detect physical VBUS removal.

Build ``samples/usb_console`` with this board target; the application selects
the upstream ``cdc-acm-console`` snippet. Open its enumerated COM port with
DTR asserted to receive periodic Zephyr logs and echoed input. The USB serial
number comes from the factory EFM unique ID. Port numbers are host assigned.
The sample was verified with programming, complete firmware readback, serial
logs, echo, and closing/reopening the host serial port. Host mode, USBHS,
DMA and low-power/remote-wakeup behavior have not been validated.
