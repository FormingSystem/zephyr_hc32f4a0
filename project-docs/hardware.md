<!--
SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# UYUP-RPI-A-2.5 / HC32F4A0PITB 硬件依据

核对日期：2026-09-09。目标为 HC32F4A0PITB-LQFP100，Cortex-M4F，2 MiB Flash、
512 KiB 主 SRAM，另有 4 KiB 备份 SRAM。本文记录原理图核对结果与用户确认的板卡事实，
是本工程的板级配置依据；已实现首轮可构建的 HC32 Zephyr 移植，尚未完成实板运行验证。

## 资料与解释顺序

| 资料 | 用途与版本 |
| --- | --- |
| `UYUP-RPI-A-2.5.pdf` | 单页原理图，图号 `UY-RPI-A-2.5`，更新日期 2026-08-05；MCU、晶振、供电、USB/DAP、LED、排针及兼容区已视觉核对 |
| `DS_HC32F4A0系列数据手册_Rev1.60.pdf` | 第 38 页 LQFP100 引脚图、第 42–46 页功能表、第 59 页 VCAP 要求 |
| `RM_HC32F4A0系列参考手册_Rev1.50.pdf` | 内存映射、时钟、中断和外设行为 |
| `HC32F4A0_DDL_Rev2.4.0` | 官方设备头文件、系统初始化、启动文件及外设接口；保留其 BSD-3-Clause 许可 |
| UYUP 模板 `SW-TEMPLATE/UYUP-RPI-A/HC32F4A0` | `main.c` 与 `UYUP-RPI-A.uvprojx` 仅用于交叉核对；模板仍含 A_2_2 与 24 MHz 配置 |

原始 PDF、压缩包和旧板卡模板不纳入版本控制；芯片手册和厂商示例的本机副本放在被忽略的缓存目录。
资料来源和具体检索位置记录在私人环境配置中，入口见 [AGENTS.md](../AGENTS.md) 的“私人环境配置”一节。
构建所需的华大 HAL 源码已经按固定节点内置，见 [源码基线](source-baseline.md)。
芯片官方资料入口为[厂商产品页](https://www.xhsc.com.cn/product/1220.html)。
板卡用户确认事实优先于通用原理图的默认装配和旧模板；引脚功能以目标型号的数据手册为准。

原理图 U1 使用 `STM32F103VCT6 或其它相兼容的产品` 通用符号，并通过装配选项兼容不同芯片。
**必须按物理脚号查询 HC32 功能，不能照抄通用符号名称、STM32 外设号或默认 BOM。**

## 用户确认的板卡操作

- 芯片没有的引脚按 **NC** 处理，不为未引出的功能假设连接。
- 实板主晶振为 **12 MHz**。PLL 必须按 12 MHz 重新计算并核对输入、VCO、输出范围，
  防止超频。误超频导致无法调试时，可按本板说明进入 BOOT 后擦除恢复；
  工程脚本不自动执行这项恢复操作，也不将 STM32 BOOT0 语义套到 HC32 的 PI13/MD。
- 板载 CMSIS-DAP 出厂默认 **2.x / WinUSB**，支持 **10 MHz SWD**。
- 连接 USB2/DAP，**一根 USB 线同时提供单步调试与串口输出**。串口号按实际主机枚举读取。
- 使用外部 JLINK/STLINK 前先停用板载 DAP：
  **关电 → 按住复位 → 开电 → 松开复位；完整步骤执行两次；橙灯不闪表示已停用。**

## 首次启动所需信号

| 用途 | HC32 引脚 / LQFP100 脚号 | 原理图连接与软件含义 |
| --- | --- | --- |
| 主晶振 X2 | PH0 / 12，PH1 / 13 | 12 MHz，C11/C12 各 15 pF；HC32 PH0 是 XTAL_OUT/XTAL_EXT，PH1 是 XTAL_IN；图中通用 `OSC_IN`/`OSC_OUT` 命名与 HC32 方向相反 |
| 低速晶振 X1 | PC14 / 8，PC15 / 9 | 32.768 kHz，C7/C8 各 6 pF；XTAL32_IN、XTAL32_OUT |
| SWDIO | PA13 / 72 | 接板载 DAP U3 PA0/6 脚及 H2-3 |
| SWCLK | PA14 / 76 | 接板载 DAP U3 PA1/7 脚及 H2-1 |
| 目标复位 | NRST / 14 | SW2 拉低，R17 10 kΩ 上拉；U3 PA4/10 与 H2-10 的 NRST_REQ 经 R46 1 kΩ 接目标 NRST |
| 控制台 TX | PA9 / 68 | USART1_TX，网络 PA9_U1_TX，接 U3 PA3/9 及 H2-4 |
| 控制台 RX | PA10 / 69 | USART1_RX，网络 PA10_U1_RX，接 U3 PA2/8 及 H2-2 |
| 蓝色 LED3 | PD10 / 57 | R37 1 kΩ 接 VDD，低电平点亮，首选 `led0` |
| 绿色 LED4 | PE15 / 46 | R38 1 kΩ 接 VDD，低电平点亮，可作 `led1` |
| 用户按键 SW3 | PA3 / 26 | 按下接地，图中没有独立上拉，软件启用内部上拉、低有效 |
| 用户按键 SW4 | PE2 / 1 | 按下接地，图中没有独立上拉，软件启用内部上拉、低有效 |

首次控制台使用 USART1、115200 8N1；115200 是工程起步设置，原理图不规定波特率。
已有 HC32 项目的 USART1 PA9/PA10 配置使用 GPIO_FUNC_32/33，可交叉核对，不能连带导入
那个项目的整套 BSP。TF 卡检测使用 **PE14**，其他项目在 PE14 上的外部看门狗配置不适用于本板。

H2 是 2x5 排针，图中标记 NC，是否焊接以实物为准。引脚依次为：
1 SWCLK、2 MCU_RX/PA10、3 SWDIO、4 MCU_TX/PA9、5 GND、6 TDO、7 DAP_CONF、8 TDI、
9 VDD、10 NRST_REQ。**这不是标准 ARM 10-pin 接线顺序**；外部探针按信号名逐根连接。

## USB、调试与供电

USB2 数据线接板载 DAP U3（STM32F042F6P6 或兼容器件）；USB1 数据线接目标 MCU 的 USB 网络。
首次调试使用 USB2/DAP。U3 同时连接目标 USART1，提供用户确认的串口桥。
图中的 DAP 模式切换说明包括 2.x、1.x、停用状态；外部探针的停用步骤以本页完整两次操作为准。

USB1/USB2 VBUS 分别经 D1/D2 接 `+5V_IN`，SW1 控制 `+5V`，LDO1 产生 VDD。
U5 将 VDD 标为 3.3 V；目标 SWD 和串口使用 3.3 V 逻辑。
LED1 是电源指示，LED2 由 DAP 控制；目标应用使用 LED3/LED4。

## 旧模板中的时钟冲突

实板与 A-2.5 原理图均为 **12 MHz**。旧模板的 Keil 宏却设置 `XTAL_VALUE=24000000`，
并启用 `UYUP_RPI_A_2_2`；`main.c` 使用 PLLM=3、PLLN=120、PLLP=4，注释为 `24/3=8`，
是以 24 MHz 输入计算的 240 MHz 配置。Keil CPU 元数据另写 `CLOCK(12000000)`，
不能据此认定编译宏与源码已匹配 12 MHz。

相同分频参数输入 12 MHz 的算术结果是 120 MHz，仍须重新核对 PLL 输入/VCO 合法范围。
移植时重算 PLL、Flash 等待周期和总线分频，可先用内部时钟或经核对的保守配置启动。
主频上限 240 MHz 不等于所有时钟节点都可工作在该频率。

模板还配置 PH14/PH15 为模拟模式；本 LQFP100 晶振引脚为 **PH0/PH1**，
PH14/PH15 没有引出，不能复制该 GPIO 初始化。

## 通用符号与 HC32 装配差异

| 脚号 | HC32F4A0PITB 功能 | 兼容区解释 |
| --- | --- | --- |
| 19 | VCC | 通用符号写 VSSA，R8/R9 选择 GND/VDD；HC32 按 VCC 处理 |
| 49 | VCAP_1 | 通用符号写 VSS_1，兼容区含 R15/R16/C13；不能当普通 VSS |
| 73 | VCAP_2 | 通用符号写 NC，兼容区含 R18/R19/C14；不能按默认直接接 VDD |
| 94 | PI13/MD | 通用符号写 BOOT0，经网络接 H1 与 R5/R57；启动和 ICG/MD 语义遵循 HC32 手册 |
| 70 / 71 | PA11/USBFS_DM、PA12/USBFS_DP | 经 R69/R70 等选件路由到 USB1 |
| 53 / 54 | PB14/USBHS_DM、PB15/USBHS_DP | 经 R71/R73 等替代选件路由到 USB；按实际装配选择 HC32 实例 |

这些是装配核对点，不表示现有成品板装错。通用图中 VCAP 候选电容为 2.2 µF/NC；
数据手册 Rev1.60 第 59 页对双 VCAP 器件给出每脚 0.047 µF 或 0.1 µF，并关联低功耗唤醒配置。
以 HC32 专用 BOM 和实物为依据，不将通用默认值写成 HC32 配置要求。

## 存储、中断与其他资源

| 存储区 | 起始地址 | 大小 |
| --- | --- | --- |
| 主 Flash | `0x00000000` | 2 MiB |
| SRAMH | `0x1FFE0000` | 128 KiB |
| SRAM1 | `0x20000000` | 128 KiB |
| SRAM2 | `0x20020000` | 128 KiB |
| SRAM3 | `0x20040000` | 96 KiB |
| SRAM4 | `0x20058000` | 32 KiB |
| 备份 SRAM | `0x200F0000` | 4 KiB |

主 SRAM 整体是 `0x1FFE0000..0x2005FFFF`，不能把 512 KiB 全从 `0x20000000` 开始布局。
官方头文件声明 MPU=1、FPU=1、NVIC 优先级位数 4，外设向量为 INT000 至 INT143。
中断源选择/路由仍需在 SoC 与驱动实现时依据参考手册处理。

其他资源供后续扩展：W25Q32 使用 PB3/PB4/PB5 与 PE3 片选；AT24C64 使用 PB8/PB9；
PD8/PD9 与 PA0 接 SP3485；U5 的 PD5/PD6 是其他串口候选；LED5/LED6 是接 PB1 的串行 RGB LED。
这些网络的 HC32 实例号和复用尚未完成逐项移植核验。

## 验证边界

已完成原理图/数据手册核对，记录用户确认的 12 MHz、NC、DAP 2.x/WinUSB、10 MHz、
单 USB 调试串口与停用步骤。当前主机只读枚举未发现可用调试探针；没有测量晶振、连接目标、
擦写 Flash 或运行 HC32 固件。下一步接板读取实际枚举，验证 SWD、SRAM、蓝灯与 USART1。
项目状态见 [porting-status.md](porting-status.md)，调试配置见 [development.md](development.md)。
