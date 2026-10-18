---
id: learning.zephyr-docs.sensor-adi-accel-bioz-binding-reference.page-23
title: adi_max30009-spi
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/adi,max30009-spi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第23章\_adi_max30009-spi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/adi,max30009-spi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="adi-max30009-on-spi-bus"></a>
<a id="dtbinding-adi-max30009-spi"></a>

兼容字符串（Compatible String）：`adi,max30009`。厂商：[ Analog Devices, Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-adi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=adi,max30009)。

驱动源码（Driver Source）：[drivers/sensor/adi/max30009/max30009.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/max30009/max30009.c)。

<a id="description"></a>

通过SPI连接的MAX30009生物阻抗模拟前端（Bio-Impedance Analog Front End，AFE）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 23.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `spi-max-frequency` | `int` | **必需**。设备SPI接口的最大时钟频率，单位Hz |
| `duplex` | `int` | 双工模式（Duplex Mode），可为全双工或半双工。默认全双工，对应0，这是最常见模式。应使用宏而非原始枚举值，`dt-bindings/spi/spi.h` 定义的对应关系为0对应SPI_FULL_DUPLEX，2048对应SPI_HALF_DUPLEX；原始对照表见下文；默认值：`0`；合法值：`0, 2048` |
| `frame-format` | `int` | Motorola或TI帧格式（Frame Format）。默认Motorola，对应0，这是最常见格式。应使用宏而非原始枚举值，`dt-bindings/spi/spi.h` 对应关系为0对应SPI_FRAME_FORMAT_MOTOROLA，32768对应SPI_FRAME_FORMAT_TI；原始对照表见下文；默认值：`0`；合法值：`0, 32768` |
| `spi-cpol` | `boolean` | SPI时钟极性（Clock Polarity），指示时钟空闲状态；设置时空闲为逻辑高电平，否则为低电平 |
| `spi-cpha` | `boolean` | SPI时钟相位（Clock Phase），决定采样边沿；设置时在第二个边沿采样，否则在第一个边沿采样 |
| `spi-lsb-first` | `boolean` | 设备要求最低有效位优先（Least Significant Bit First，LSB-first）的数据模式 |
| `spi-hold-cs` | `boolean` | 某些场景需由控制器通过软件管理SPI片选（Chip Select，CS），以连续执行多次SPI事务而不释放片选。典型情况为变长数据包：第一笔事务读取长度，第二笔读取该长度的字节数据 |
| `spi-cs-high` | `boolean` | 设备要求片选高电平有效（Active High） |
| `spi-interframe-delay-ns` | `int` | SPI字（Word）之间的延迟，单位纳秒。默认0是特殊值，表示SCK周期的一半；默认值：`0` |
| `spi-cs-setup-delay-ns` | `int` | 片选置有效之后，由控制器引入的延迟，单位纳秒，也称使能前置时间（Enable Lead Time） |
| `spi-cs-hold-delay-ns` | `int` | 片选释放之前，由控制器引入的延迟，单位纳秒，也称使能后置时间（Enable Lag Time） |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `int-gpios` | `phandle-array` | 中断引脚（INT）。MAX30009的INT输出默认为低电平有效开漏（Active-low Open-drain）；属性值应描述SoC实际接收到的信号。 |
| `fifo-watermark` | `int` | 以帧数指定FIFO水位（Watermark），默认采用复位值。；默认值：`129`；范围：`1 to 256` |
| `fifo-a-full-type` | `boolean` | A_FULL_TYPE设置FIFO接近满中断（A_FULL）的行为。清零时，只要接近满状态持续，每个采样都会重新产生中断；置位时只产生一次，直到读取FIFO并再次出现新的接近满状态后才重新产生。复位时清零。 |
| `fifo-rollover` | `boolean` | FIFO_RO使能FIFO循环覆盖（Roll-over）。置位后，FIFO已满仍继续写入采样并覆盖最旧数据，读写指针均推进；清零时，丢弃新采样，直到FIFO被读取。复位时禁用。 |
| `ref-clk-source` | `int` | 锁相环参考时钟源（PLL Reference Clock Source，REF_CLK_SEL）。`internal` 选择片上低速振荡器之一，`external` 选择FCLK引脚输入的时钟。默认 `internal`，与复位状态一致。；默认值：`0`；合法值：`0, 1` |
| `clk-freq-sel` | `int` | PLL参考时钟频率，单位Hz，对应CLK_FREQ_SEL。`ref-clk-source` 为 `internal` 时选择片上振荡器；为 `external` 时必须匹配FCLK输入频率。默认32768 Hz。；默认值：`32768`；合法值：`32000, 32768` |
| `clk-fine-tune` | `int` | 内部低速振荡器微调（Fine-tune Trim，CLK_FINE_TUNE），为5位二进制补码，每个最低有效位（LSB）对应0.2%。默认0，不偏移。；默认值：`0`；范围：`0 to 31` |
| `pll-multiplier` | `int` | PLL反馈倍频系数（Feedback Multiplier）M，写入MDIV时满足 `M = MDIV + 1`。选择M使 `PLL_CLK = M × REF_CLK` 位于14至28 MHz。默认444，对应MDIV复位值443。；默认值：`444`；范围：`427 to 875` |
| `bioz-adc-clk-div` | `int` | 生物阻抗（BioZ）ADC时钟分频器NDIV，将PLL_CLK分频得到BioZ ADC采样时钟。默认512，即NDIV复位值。；默认值：`512`；合法值：`512, 1024` |
| `bioz-synth-clk-div` | `int` | BioZ频率合成时钟分频器KDIV，将PLL_CLK分频得到直接数字合成（DDS）DAC时钟。默认1，即KDIV复位值。；默认值：`1`；合法值：`1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192` |
| `bioz-adc-osr` | `int` | 同相（I）与正交（Q）ADC的BioZ过采样比（Oversampling Ratio，BIOZ_ADC_OSR），默认8，即复位值。；默认值：`8`；合法值：`8, 16, 32, 64, 128, 256, 512, 1024` |
| `bioz-dac-osr` | `int` | BioZ DDS DAC过采样比（Oversampling Ratio，BIOZ_DAC_OSR），默认32，即复位值。；默认值：`32`；合法值：`32, 64, 128, 256` |
| `bioz-i-en` | `boolean` | 启用同相（In-phase，I）BioZ驱动与接收通道（BIOZ_I_EN），同时开启PLL和带隙偏置（Bandgap Bias）。复位时禁用，省略属性时通道关闭。 |
| `bioz-q-en` | `boolean` | 启用正交相位（Quadrature-phase，Q）BioZ驱动与接收通道（BIOZ_Q_EN），同时开启PLL和带隙偏置（Bandgap Bias）。复位时禁用，省略属性时通道关闭。 |
| `bioz-bg-en` | `boolean` | 启用BioZ带隙偏置（Bandgap Bias）。复位时禁用；原文称省略此属性时通道关闭。 |
| `bioz-dhpf` | `int` | BioZ数字高通滤波器截止频率（Digital High-pass Filter Cutoff，BIOZ_DHPF[1:0]），用寄存器编码表示，截止频率相对于BioZ采样率给出。默认0，即旁路（Bypass），与复位值一致。；默认值：`0`；合法值：`0, 1, 2` |
| `bioz-dlpf` | `int` | BioZ数字低通滤波器截止频率（Digital Low-pass Filter Cutoff，BIOZ_DLPF[2:0]），用寄存器编码表示，截止频率相对于BioZ采样率给出。默认0，即旁路（Bypass），与复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3, 4` |
| `en-bioz-thresh` | `boolean` | 使能BioZ阈值检测器（Threshold Detector，EN_BIOZ_THRESH），将 `bioz-cmp-selected` 选择的数据与 `bioz-high-threshold` 和 `bioz-low-threshold` 比较。复位时禁用。 |
| `bioz-cmp` | `int` | BioZ比较器选择（Comparator Selection，BIOZ_CMP[1:0]）：0=I，1=Q，2=Z。默认0，即I通道。；默认值：`0`；合法值：`0, 1, 2` |
| `bioz-drv-mode` | `int` | BioZ发送通道施加到电极的激励类型（Stimulus Type，BIOZ_DRV_MODE[1:0]）。默认0，即电流驱动（Current Drive），与复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bioz-idrv-rge` | `int` | 内部电流量程电阻（Current-range Resistor，BIOZ_IDRV_RGE），在禁用 `bioz-ext-res` 时决定电流幅值。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bioz-vdrv-mag` | `int` | 电压驱动模式（Voltage Drive Mode）下，BIOZ_VDRV_MAG设置连接至EL1的DRVR电压幅值，忽略BIOZ_IDRV_RGE。电流驱动模式下，BIOZ_VDRV_MAG与BIOZ_IDRV_RGE共同设置电流幅值。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bioz-ext-res` | `boolean` | 启用外部电阻（External Resistor，REXT）设置BioZ电流幅值。禁用（0）时，使用BIOZ_IDRV_RGE和BIOZ_VDRV_MAG设置的内部量程电阻；启用（1）时，由REXT和BIOZ_VDRV_MAG设置电流幅值。 |
| `loff-rapid` | `boolean` | LOFF_RAPID旁路直流导联脱落检测（DC Lead-off Detection）约128 ms的窗口延迟。 |
| `bioz-fast-start-en` | `boolean` | BIOZ_FAST_START_EN使能快速启动模式（Fast-start Mode），在启用I或Q通道后，通过10 kΩ电阻将BIP、BIN输入连接至VMID_RX。 |
| `bioz-fast-manual` | `boolean` | BIOZ_FAST_MANUAL用于手动开启快速启动模式（Fast-start Mode）。 |
| `bioz-ahpf` | `int` | BioZ模拟高通滤波器截止频率（Analog High-pass Filter Cutoff，BIOZ_AHPF[1:0]），用寄存器编码表示，截止频率相对于BioZ采样率给出。默认0，即旁路，与复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15` |
| `bioz-ina-mode` | `int` | BioZ仪表放大器模式（Instrumentation Amplifier Mode，BIOZ_INA_MODE），选择高功耗低噪声或低功耗运行。默认0，即高功耗模式，与复位值一致。；默认值：`0`；合法值：`0, 1` |
| `bioz-dm-dis` | `boolean` | BIOZ_DM_DIS禁用接收通道解调器（Demodulators）。 |
| `bioz-gain` | `int` | BIOZ_GAIN设置BioZ接收通道仪表放大器（INA）和可编程增益放大器（PGAs）的组合增益（Combined Gain）。默认0，对应1倍增益，与复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bioz-ext-cap` | `boolean` | BIOZ_EXT_CAP选择连接于DRVXC与DRVSJ之间的外部电容（External Capacitor，CEXT）。 |
| `bioz-dc-restore` | `int` | BIOZ_DC_RESTORE控制电流发生器（Current Generator）中的直流恢复开关（DC Restore Switch）。；默认值：`0`；合法值：`0, 1` |
| `bioz-amp-rge` | `int` | 选择BioZ发送通道电压驱动放大器与电流驱动放大器的输出级选项（Output Stage Option）。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bioz-amp-bw` | `int` | BIOZ_AMP_BW设置BioZ发送通道电压／电流驱动放大器的增益带宽（Gain Bandwidth）。默认0，即低带宽。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bioz-low-threshold` | `int` | BioZ欠量程阈值（Under-range Threshold，BIOZ_LO_THRESH[7:0]），采用8位寄存器编码，对应对称范围 `±32 × code`。仅在设置 `en-bioz-thresh` 时有效。默认0，即复位值。；默认值：`0`；范围：`0 to 255` |
| `bioz-high-threshold` | `int` | BioZ超量程阈值（Over-range Threshold，BIOZ_HI_THRESH[7:0]），采用8位寄存器编码，对应对称范围 `±2048 × code`。仅在设置 `en-bioz-thresh` 时有效。默认255，即复位值。；默认值：`255`；范围：`0 to 255` |
| `bioz-stby-on` | `boolean` | BIOZ_STBY_ON在发送通道待机（`bioz-drv-mode = 3`）时，保持接收通道的放大器、解调器和ADC使能，以加快唤醒。复位时禁用。 |
| `bioz-q-clk-phase` | `int` | BIOZ_Q_CLK_PHASE设置Q通道解调器时钟相对于激励的相位（Clock Phase）：0=正交相位，正常模式；1=同相。默认0，即复位值。；默认值：`0`；合法值：`0, 1` |
| `bioz-i-clk-phase` | `int` | BIOZ_I_CLK_PHASE设置I通道解调器时钟相对于激励的相位（Clock Phase）：0=同相，正常模式；1=正交相位。默认0，即复位值。；默认值：`0`；合法值：`0, 1` |
| `bioz-ina-chop-en` | `boolean` | BIOZ_INA_CHOP_EN启用BioZ接收仪表放大器的斩波（Chopping），频率为 `BIOZ_ADC_CLK / 2`。除 `F_BIOZ = BIOZ_ADC_CLK / 2` 外，原文推荐启用INA斩波。复位时禁用。 |
| `bioz-ch-fsel` | `boolean` | BIOZ_CH_FSEL选择接收PGA／抗混叠滤波器（AAF）的斩波频率：禁用（0）为 `BIOZ_ADC_CLK / 8`，启用（1）为 `BIOZ_ADC_CLK / 4`。当 `F_BIOZ = BIOZ_ADC_CLK / 8` 时设为1。复位时禁用。 |
| `bmux-rsel` | `int` | BMUX_RSEL选择非皮肤电反应（Non-GSR）应用中跨接DRVP/BIP与DRVN/BIN的电阻校准负载（Resistive Calibration Load），对应BMUX_RSEL[1:0]，仅在设置 `bmux-bist-en` 时应用。默认0，即5100 Ω，与复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `bmux-bist-en` | `boolean` | BMUX_BIST_EN为非GSR应用在DRVP/BIP与DRVN/BIN之间连接内建自检电阻（Built-in Self-test Resistor），阻值由 `bmux-rsel` 决定。复位时禁用。 |
| `connect-cal-only` | `boolean` | CONNECT_CAL_ONLY与 `mux-en`、`cal-en` 同时设置时，只连接CAL1至CAL4引脚，并断开ELx引脚。复位时禁用。 |
| `mux-en` | `boolean` | MUX_EN使能BioZ输入／输出复用器（I/O MUX）到ELx及／或CALx引脚的连接；禁用时，所有ELx、CALx引脚均断开。复位时禁用。 |
| `cal-en` | `boolean` | 设置 `mux-en` 时，CAL_EN连接校准引脚（CAL1=DRVP、CAL2=BIP、CAL3=BIN、CAL4=DRVN），用于测量外部校准电阻，同时断开电极引脚。复位时禁用。 |
| `bmux-gsr-rsel` | `int` | BMUX_GSR_RSEL选择皮肤电反应（Galvanic Skin Response，GSR）应用中跨接DRVP/BIP与DRVN/BIN的电阻校准负载，对应BMUX_GSR_RSEL[1:0]，仅在设置 `gsr-load-en` 时应用。默认0，即25.7 kΩ，与复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `gsr-load-en` | `boolean` | GSR_LOAD_EN在DRVP/BIP与DRVN/BIN之间连接内建GSR负载电阻，阻值由 `bmux-gsr-rsel` 决定。复位时禁用。 |
| `en-ext-inload` | `boolean` | EN_EXT_INLOAD启用外部保护走线驱动电路（Guard-trace-drive Circuit），将BIP和BIN的缓冲电压输出到EL2A和EL3A。复位时禁用。 |
| `en-int-inload` | `boolean` | EN_INT_INLOAD启用用于补偿BIN、BIP输入电容负载（Input Capacitive Loading）的电路。复位时禁用。 |
| `bip-assign` | `int` | 设置 `mux-en` 时，BIP_ASSIGN选择BioZ正输入（BIP）的电极引脚，对应BIP_ASSIGN[1:0]；设置 `cal-en` 时忽略。默认0，即EL1，与复位值一致。；默认值：`0`；合法值：`0, 1, 2` |
| `bin-assign` | `int` | 设置 `mux-en` 时，BIN_ASSIGN选择BioZ负输入（BIN）的电极引脚，对应BIN_ASSIGN[1:0]；设置 `cal-en` 时忽略。默认0，即EL4，与复位值一致。；默认值：`0`；合法值：`0, 1, 2` |
| `drvp-assign` | `int` | 电流模式且设置 `mux-en` 时，DRVP_ASSIGN选择BioZ正驱动（DRVP）的电极引脚，对应DRVP_ASSIGN[1:0]；设置 `cal-en` 时忽略，电压或H桥模式下强制为EL1。EL1导通电阻最低，电流达到64 µA或更高时，应将DRVP分配给EL1。默认0，即EL1，与复位值一致。；默认值：`0`；合法值：`0, 1, 2` |
| `drvn-assign` | `int` | 电流模式且设置 `mux-en` 时，DRVN_ASSIGN选择BioZ负驱动（DRVN）的电极引脚，对应DRVN_ASSIGN[1:0]；设置 `cal-en` 时忽略，电压或H桥模式下强制为EL4。EL4导通电阻最低，电流达到64 µA或更高时，应将DRVN分配给EL4。默认0，即EL4，与复位值一致。；默认值：`0`；合法值：`0, 1, 2` |
| `en-lon-det` | `boolean` | EN_LON_DET启用BIP、BIN上的超低功耗直流导联接入检测（DC Lead-on Detection）。仅在BioZ禁用，即 `bioz-i-en = bioz-q-en = 0` 时工作。复位时禁用。 |
| `en-loff-det` | `boolean` | EN_LOFF_DET启用BIP、BIN上的直流导联脱落检测（DC Lead-off Detection）。仅在BioZ启用，即设置 `bioz-i-en` 或 `bioz-q-en` 时工作。复位时禁用。 |
| `en-ext-loff` | `boolean` | 对于EL2A/EL3A上的交流耦合BioZ输入，EN_EXT_LOFF通过EL2B、EL3B在外部施加直流导联脱落检测，替代内部BIP/BIN节点。复位时禁用。 |
| `en-drv-oor` | `boolean` | EN_DRV_OOR启用DRVN电压监测，通过越界交流电压检测驱动电极脱落，状态为DRV_OOR。复位时禁用。 |
| `loff-ipol` | `int` | LOFF_IPOL设置匹配的直流导联脱落检测电流源极性（Current-source Polarity）。默认0，即不反相，与复位值一致。；默认值：`0`；合法值：`0, 1` |
| `loff-imag` | `int` | LOFF_IMAG选择直流导联脱落检测电流幅值（Current Amplitude），对应LOFF_IMAG[2:0]。默认0，即禁用电流源，与复位值一致。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5` |
| `loff-thresh` | `int` | LOFF_THRESH选择以VMID_RX为中心的直流导联脱落比较器电压阈值，采用LOFF_THRESH[3:0]的4位编码：0对应VMID_RX±215 mV，15对应±665 mV，每步30 mV。默认0，即复位值。；默认值：`0`；范围：`0 to 15` |
| `rbias-value` | `int` | RBIAS_VALUE选择BIP/BIN与VMID_RX之间的输入导联偏置电阻（Lead Bias Resistance），对应RBIAS_VALUE[1:0]；设置 `en-rbias-bip` 或 `en-rbias-bin` 时应用。默认0，即50 MΩ，与复位值一致。；默认值：`0`；合法值：`0, 1, 2` |
| `en-rbias-bip` | `boolean` | EN_RBIAS_BIP通过 `rbias-value` 选择的电阻，将BIP连接至VMID_RX。复位时禁用。 |
| `en-rbias-bin` | `boolean` | EN_RBIAS_BIN通过 `rbias-value` 选择的电阻，将BIN连接至VMID_RX。复位时禁用。 |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |

本页没有已弃用的节点专用属性。

## 23.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁（Hardware Spinlock）标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |
| `wakeup-source` | `boolean` | 标记设备可用作唤醒源（Wakeup Source）。设置该属性后，设备中会设置专门标志，通知系统此设备有唤醒能力。唤醒功能默认禁用，即中断不会唤醒系统；必要时可在运行期间启用 |
| `zephyr,pm-device-runtime-auto` | `boolean` | 初始化函数执行后，自动为设备配置运行时电源管理（Runtime Power Management） |
| `zephyr,disabling-power-states` | `phandles` | 会关闭该设备电源的电源状态（Power State）列表 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

## SPI枚举原始对照 2

```text
  0    SPI_FULL_DUPLEX
  2048 SPI_HALF_DUPLEX
```

## SPI枚举原始对照 3

```text
  0     SPI_FRAME_FORMAT_MOTOROLA
  32768 SPI_FRAME_FORMAT_TI
```

## 23.3\_寄存器块命名原例

以下设备树源码（Devicetree Source，DTS）演示 `reg-names` 命名；`uart` 指通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

```dts
  / {
       soc {
           #address-cells = <1>;
           #size-cells = <1>;

           uart@1000 {
               reg = <0x1000 0x2000>, <0x3000 0x4000>;
               reg-names = "foo", "bar";
           };
       };
  };
```

`uart@1000` 节点有两个寄存器块（Register Block）：一个基址为 `0x1000`、大小为 `0x2000`、名称为 `foo`；另一个基址为 `0x3000`、大小为 `0x4000`、名称为 `bar`。

---

[上一章](P022_adi_max30009-i2c.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P024_adi_max30210.md)
