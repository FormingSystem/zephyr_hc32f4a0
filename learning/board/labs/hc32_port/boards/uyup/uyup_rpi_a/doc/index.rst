.. Copyright The zephyr_hc32f4a0 Contributors
.. SPDX-License-Identifier: Apache-2.0

UYUP-RPI-A-2.5 HC32F4A0PITB
###########################

The board target is ``uyup_rpi_a/hc32f4a0pitb``. It uses an HC32F4A0PITB
in the LQFP100 package, with 2 MiB of flash and 512 KiB of main SRAM starting
at ``0x1ffe0000``. The separate 4 KiB backup SRAM is not part of main SRAM.

Initial support
***************

The initial port uses the fitted external 12 MHz crystal directly, Zephyr's
Cortex-M startup and SysTick, polling USART1, and basic GPIO. The crystal
frequency is declared in the board devicetree and provides an accurate UART
clock. The initial port does not enable a PLL. Peripheral interrupt routing, GPIO
interrupts, DMA, USB and flash-controller APIs are not yet implemented.

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

Build support
*************

This board is supplied by the ``hc32_port`` hardware support module.
The board and SoC definitions follow Zephyr hardware model v2. The module
registers the UYUP and XHSC vendor namespaces through its DTS root.
Follow ``learning/P01_zephyr_make_project/P003_编译示例与新增开发板_Windows.md``
from the experiment source root. Pass the CMSIS, hal_xhsc and hardware support
module roots through ``ZEPHYR_MODULES`` when configuring the upstream
``samples/hello_world`` application for ``uyup_rpi_a/hc32f4a0pitb``.
The module does not configure a flash or debug runner yet. Hardware
verification and supported peripheral features are tracked separately
from schema, configuration and compilation checks.

Compilation and image-layout validation do not verify physical SWD,
serial output, LED behavior, timing or oscillator operation. Record those
results separately when the board is connected.
