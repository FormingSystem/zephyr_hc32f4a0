---
id: learning.zephyr-docs.timer_reference.clocksample-117
title: LiteX时钟控制示例
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/clock_control_litex/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="clock-control-litex"></a>

# 第117章\_LiteX时钟控制示例

原文：[LiteX clock control driver](https://docs.zephyrproject.org/latest/samples/drivers/clock_control_litex/README.html)。读取日期：2026-10-13，`latest`。

本示例介绍 LiteX 时钟控制驱动（Clock Control Driver）的功能。驱动使用混合模式时钟管理器（Mixed Mode Clock Manager，MMCM）模块，最多生成7路具有指定相位（Phase）、频率（Frequency）和占空比（Duty Cycle）的时钟。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/clock_control_litex)。

## 117.1\_硬件与系统要求

- 支持 LiteX 且带 MMCM 模块的现场可编程门阵列（Field-Programmable Gate Array，FPGA）平台，例如 Digilent Arty A7 开发板。
- 片上系统（System on Chip，SoC）配置包含 VexRiscv 软核中央处理器（Soft CPU），以及 LiteX 中的 Xilinx 7 系列 MMCM 接口`S7MMCM`模块。
- 可选：将时钟输出信号引至输出引脚，以便测试。

## 117.2\_设备树配置

驱动的基本配置，包括各时钟输出的默认设置，放在设备树（Devicetree）的时钟控制节点中。以下三段为官方原例；`clk0`和`clk1`是输出节点，`clock0`是时钟控制节点；`CLK_0`和`CLK_1`是两路时钟的输出名称（Clock Output Names）。`reg-names`中的`drp_*`为动态重配置端口（Dynamic Reconfiguration Port，DRP）相关寄存器名称；`vco`指压控振荡器（Voltage-Controlled Oscillator，VCO）。

```dts
clk0: clock-controller@0 {
	#clock-cells = <1>;
	reg = <0>;
	compatible = "litex,clkout";
	clock-output-names = "CLK_0";
	litex,clock-frequency = <11289600>;
	litex,clock-phase = <0>;
	litex,clock-duty-num = <1>;
	litex,clock-duty-den = <2>;
	litex,clock-margin = <1>;
	litex,clock-margin-exp = <2>;
	status = "okay";
};
```

```dts
clk1: clock-controller@1 {
	#clock-cells = <1>;
	reg = <1>;
	compatible = "litex,clkout";
	clock-output-names = "CLK_1";
	litex,clock-frequency = <22579200>;
	litex,clock-phase = <0>;
	litex,clock-duty-num = <1>;
	litex,clock-duty-den = <2>;
	litex,clock-margin = <1>;
	litex,clock-margin-exp = <2>;
	status = "okay";
};
```

```dts
clock0: clock@e0004800 {
	compatible = "litex,clk";
	reg = <0xe0004800 0x4>,
	      <0xe0004804 0x4>,
	      <0xe0004808 0x4>,
	      <0xe000480c 0x4>,
	      <0xe0004810 0x4>,
	      <0xe0004814 0x4>,
	      <0xe0004818 0x4>,
	      <0xe000481c 0x4>;
	reg-names = "drp_reset",
		    "drp_locked",
		    "drp_read",
		    "drp_write",
		    "drp_drdy",
		    "drp_adr",
		    "drp_dat_w",
		    "drp_dat_r";
	#clock-cells = <1>;
	clocks = <&clk0 0>, <&clk1 1>;
	clock-output-names = "CLK_0", "CLK_1";
	litex,lock-timeout = <10>;
	litex,drdy-timeout = <10>;
	litex,divclk-divide-min = <1>;
	litex,divclk-divide-max = <107>;
	litex,clkfbout-mult-min = <2>;
	litex,clkfbout-mult-max = <65>;
	litex,vco-freq-min = <600000000>;
	litex,vco-freq-max = <1200000000>;
	litex,clkout-divide-min = <1>;
	litex,clkout-divide-max = <126>;
	litex,vco-margin = <0>;
	status = "okay";
};
```

原文说明这组配置定义`clk0`和`clk1`两路输出，并称默认频率为100 MHz、相位偏移（Phase Offset）为0°、占空比为50%。设置 FPGA 专用参数时要特别注意，即从`litex,divclk-divide-min`到`litex,vco-margin`的各项值。

译注：原文叙述的100 MHz与紧邻设备树示例不一致。示例的两个`litex,clock-frequency`分别写为11289600和22579200，即11.2896 MHz及22.5792 MHz；这里完整保留源码与原说明，并指出差异，不能用100 MHz替换原值。

**`clk0`和`clk1`节点的`reg`属性表示时钟输出编号`clkout_nr`**，不是此处要自行填写的寄存器基址。

## 117.3\_驱动使用方式

该驱动通过[时钟控制应用程序编程接口（Clock Control API）](../hardware/P007_时钟控制.md)中的`clock_control_on()`函数，以及 LiteX 专用结构体[`litex_clk_setup`](P120_LiteX时钟设置结构.md)使用。

修改时钟参数时，将`litex_clk_setup`结构体的指针转换为时钟子系统句柄类型[`clock_control_subsys_t`](P092_时钟控制公共接口.md)，再传给[`clock_control_on()`](P092_时钟控制公共接口.md)。以下代码尝试将`clk0`设为50 MHz、90°相位偏移和75%占空比。

原例中`clkout_nr`选择输出编号，`rate`为频率，`duty`为占空比，`phase`为相位；`DEVICE_DT_GET`按设备树节点取得设备，`MMCM`是原例使用的节点宏，`LOG_ERR`输出错误日志，错误消息中的`CLKOUT`表示时钟输出（Clock Output）。

```c
struct device *dev;
int ret;
struct litex_clk_setup setup = {
        .clkout_nr = 0,
        .rate = 50000000,
        .duty = 75,
        .phase = 90
};
dev = DEVICE_DT_GET(MMCM);
clock_control_subsys_t sub_system = (clock_control_subsys_t)&setup;
if ((ret = clock_control_on(dev, sub_system)) != 0) {
        LOG_ERR("Set CLKOUT%d param error!", setup.clkout_nr);
        return ret;
}
```

按原文描述，可通过`clock_control_get_status()`取得输出状态，涉及频率、占空比和相位偏移；只查询频率时，使用`clock_control_get_rate()`。这两个读取函数（Getter Function）的基本用法类似`clock_control_on()`：用`litex_clk_setup`的`clkout_nr`选择需要读取的输出。这里保留的是本页对 LiteX 驱动用法的说明，通用接口的返回类型与契约应同时参阅时钟控制 API。

## 117.4\_选择测试场景

示例提供检查多种时钟输出设置的方法。将场景选择宏`LITEX_CLK_TEST`定义为以下值之一：

| 宏值 | 测试内容 |
| --- | --- |
| `LITEX_TEST_FREQUENCY` | 频率范围（Frequency Range） |
| `LITEX_TEST_DUTY` | 占空比范围（Duty Cycle Range） |
| `LITEX_TEST_PHASE` | 相位范围（Phase Range） |
| `LITEX_TEST_SINGLE` | 一次设置频率、占空比和相位，随后检查时钟状态与频率 |

代码针对两个输出执行，其`clkout_nr`分别由`LITEX_CLK_TEST_CLK1`和`LITEX_CLK_TEST_CLK2`定义。各场景另有独立的宏定义控制测试。

## 117.5\_构建

官方原命令如下，在包含`zephyr`目录的工作区根目录执行：

```bash
west build -b litex_vexriscv zephyr/samples/drivers/clock_control
```

译注：原命令使用`zephyr/samples/drivers/clock_control`，而当前本页对应的示例源码目录为`samples/drivers/clock_control_litex`。原命令按原样保留；实际构建时应先核对所用 Zephyr 版本中存在的示例目录及板目标，避免把历史命令当作当前版本已验证命令。

驱动会输出许多有用的调试日志。原文强烈建议启用日志（Logging），采用日志消息同步处理（Synchronous Processing），并将日志级别设置为信息级`Info`。

## 117.6\_示例输出

下面保留原始日志，包括历史版本`zephyr-v2.2.0-2810-g1ca5dda196c3`、设备地址和测试结果。`<inf>`表示信息日志，`CLKOUT0`／`CLKOUT1`表示时钟输出0／1，`HZ`为赫兹，`deg`为角度单位度；OS 指操作系统（Operating System）；`CLK_CTRL_LITEX`是 LiteX 时钟控制的日志模块名（Log Module Name）。

```text
[00:00:00.200,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set rate: 100000000 HZ
[00:00:00.240,000] <inf> CLK_CTRL_LITEX: CLKOUT1: updated rate: 100000000 to 100000000 HZ
[00:00:00.280,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set duty: 50%
[00:00:00.320,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set phase: 0 deg
[00:00:00.360,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set rate: 100000000 HZ
[00:00:00.400,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set duty: 50%
[00:00:00.440,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set phase: 0 deg
[00:00:00.440,000] <inf> CLK_CTRL_LITEX: LiteX Clock Control driver initialized
*** Booting Zephyr OS build zephyr-v2.2.0-2810-g1ca5dda196c3  ***
Clock Control Example! riscv32
device name: clock0
clock control device is 0x40013460, name is clock0
Clock test
Single test
[00:00:00.510,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set rate: 15000000 HZ
[00:00:00.550,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set phase: 90 deg
[00:00:00.590,000] <inf> CLK_CTRL_LITEX: CLKOUT0: set duty: 25%
[00:00:00.630,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set rate: 15000000 HZ
[00:00:00.670,000] <inf> CLK_CTRL_LITEX: CLKOUT1: set duty: 75%
Getters test
CLKOUT0: get_status: rate:15000000 phase:90 duty:25
CLKOUT0: get_rate:15000000
CLKOUT1: get_status: rate:15000000 phase:0 duty:75
CLKOUT1: get_rate:15000000
Clock test done returning: 0
```

日志显示两路输出先以100 MHz、0°和50%占空比初始化，随后单次测试将两路频率设为15 MHz；输出0的相位为90°、占空比25%，输出1的相位为0°、占空比75%。最后的读取结果列出这些值，测试返回0。该日志是原页历史示例，不表示前述设备树数值、驱动用法代码和此日志来自同一次构建运行。

## 117.7\_参考与另见

- [LiteX VexRiscv 开发板说明](https://docs.zephyrproject.org/latest/boards/enjoydigital/litex_vexriscv/doc/index.html#litex_vexriscv)。
- [时钟控制（Clock Control）接口参考](P092_时钟控制公共接口.md)。

---

[上一章：nRF时钟控制示例](P116_nRF时钟控制示例.md) · [下一章：MicrochipXEC时钟控制示例](P118_MicrochipXEC时钟控制示例.md) · [返回大纲](大纲.md)
