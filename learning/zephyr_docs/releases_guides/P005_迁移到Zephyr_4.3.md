---
id: learning.zephyr-docs.releases-guides.page-5
title: 迁移到Zephyr 4.3
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/migration-guide-4.3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="migration-guide-to-zephyr-v4-3-0"></a>

<a id="migration-4-3"></a>

# 第5章\_迁移到Zephyr v4.3.0的指南

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/migration-guide-4.3.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

本文描述将应用从Zephyr v4.2.0迁移到v4.3.0所需的更改。

其他与应用迁移没有直接关系的变化，见发行说明。（[发行说明（Release Notes）](https://docs.zephyrproject.org/latest/releases/release-notes-4.3.html#zephyr-4-3)）

<a id="contents"></a>


- <a id="id1"></a>

  [构建系统（Build System）](#build-system)
- <a id="id2"></a>

  [内核（Kernel）](#kernel)
- <a id="id3"></a>

  [基础库（Base Libraries）](#base-libraries)
- <a id="id4"></a>

  [开发板（Boards）](#boards)
- <a id="id5"></a>

  [设备驱动与设备树（Device Drivers and Devicetree）](#device-drivers-and-devicetree)


  - <a id="id6"></a>

    [模数转换器（ADC）](#adc)
  - <a id="id7"></a>

    [时钟控制（Clock Control）](#clock-control)
  - <a id="id8"></a>

    [比较器（Comparator）](#comparator)
  - <a id="id9"></a>

    [直接存储器访问（DMA）](#dma)
  - <a id="id10"></a>

    [以太网（Ethernet）](#ethernet)
  - <a id="id11"></a>

    [多功能设备（MFD）](#mfd)
  - <a id="id12"></a>

    [其他（MISC）](#misc)
  - <a id="id13"></a>

    [脉宽调制（PWM）](#pwm)
  - <a id="id14"></a>

    [物理层（PHY）](#phy)
  - <a id="id15"></a>

    [串行外设接口（SPI）](#spi)
  - <a id="id16"></a>

    [传感器（Sensors）](#sensors)
  - <a id="id17"></a>

    [步进电机（Stepper）](#stepper)
  - <a id="id18"></a>

    [通用串行总线（USB）](#usb)
- <a id="id19"></a>

  [蓝牙（Bluetooth）](#bluetooth)


  - <a id="id20"></a>

    [蓝牙控制器（Bluetooth Controller）](#bluetooth-controller)
  - <a id="id21"></a>

    [蓝牙音频（Bluetooth Audio）](#bluetooth-audio)
  - <a id="id22"></a>

    [蓝牙主机控制器接口（Bluetooth HCI）](#bluetooth-hci)
  - <a id="id23"></a>

    [蓝牙网状网络（Bluetooth Mesh）](#bluetooth-mesh)
  - <a id="id24"></a>

    [蓝牙主机（Bluetooth Host）](#bluetooth-host)
- <a id="id25"></a>

  [电源管理（Power Management）](#power-management)
- <a id="id26"></a>

  [网络（Networking）](#networking)


  - <a id="id27"></a>

    [受限应用协议（CoAP）](#coap)
- <a id="id28"></a>

  [调制解调器（Modem）](#modem)
- <a id="id29"></a>

  [显示（Display）](#display)
- <a id="id30"></a>

  [精确时间协议时钟（PTP Clock）](#ptp-clock)
- <a id="id31"></a>

  [视频（Video）](#video)
- <a id="id32"></a>

  [其他子系统（Other Subsystems）](#other-subsystems)


  - <a id="id33"></a>

    [蜂窝通信（Cellular）](#cellular)
  - <a id="id34"></a>

    [密码功能（Crypto）](#crypto)
  - <a id="id35"></a>

    [Flash映射（Flash Map）](#flash-map)
  - <a id="id36"></a>

    [日志（Logging）](#logging)
  - <a id="id37"></a>

    [微控制器管理（MCUmgr）](#mcumgr)
  - <a id="id38"></a>

    [Mbed TLS密码与TLS库](#mbed-tls)
  - <a id="id39"></a>

    [实时输入输出（RTIO）](#rtio)
  - <a id="id40"></a>

    [安全存储（Secure Storage）](#secure-storage)
  - <a id="id41"></a>

    [命令行（Shell）](#shell)
  - <a id="id42"></a>

    [固件更新服务（UpdateHub）](#updatehub)
- <a id="id43"></a>

  [模块（Modules）](#modules)


  - <a id="id44"></a>

    [MCU启动加载器（MCUboot）](#mcuboot)
  - <a id="id45"></a>

    [芯科科技（Silabs）](#silabs)
  - <a id="id46"></a>

    [轻量图形库（LVGL）](#lvgl)
  - <a id="id47"></a>

    [LED灯带（LED Strip）](#led-strip)
  - <a id="id48"></a>

    [可信固件M（Trusted Firmware-M）](#trusted-firmware-m)

<a id="build-system"></a>

## [构建系统（Build System）](#id1)

<a id="kernel"></a>

## [内核（Kernel）](#id2)


- [device_init()](../device_reference/P001_设备模型公共接口.md#gaeea4f9c9f14ab12d224378ab90231c09)：旧版因缺陷在设备初始化失败时返回正值+errno，现在修复为正确的负值-errno。针对旧缺陷采用规避措施的应用应相应更新。

<a id="base-libraries"></a>

## [基础库（Base Libraries）](#id3)


- UTF-8工具[utf8_trunc()](../util_reference/P001_通用工具公共接口.md#ga1bbcfa5d7bfe757afab489d2ce41e30a)及[utf8_lcpy()](../util_reference/P001_通用工具公共接口.md#ga376935d7e6eece7dbdd382de057ec2f9)的声明从util.h移到独立文件[include/zephyr/sys/util_utf8.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/util_utf8.h)。
- Z_MIN、Z_MAX及Z_CLAMP宏分别重命名为[min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)及[clamp](../numeric_reference/P001_最小最大值与限幅宏参考.md#a04e8e3eede9e473bd18f298fddd67b46)。
- 不应再使用<zephyr/posix/time.h>及<zephyr/posix/signal.h>，改从C库标准路径包含<time.h>及<signal.h>。非POSIX C库维护者可包含[include/zephyr/posix/posix_time.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/posix/posix_time.h)及[include/zephyr/posix/posix_signal.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/posix/posix_signal.h)，以可移植方式提供POSIX定义。
- POSIX限制值不再定义于<zephyr/posix/posix_features.h>；同样应从C库标准路径包含<limits.h>。非POSIX C库维护者可包含[include/zephyr/posix/posix_limits.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/posix/posix_limits.h)获取Zephyr定义。部分运行时不变的值可能须通过[sysconf()](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html#a599f55d9eaa01b6921367233437b9b13)查询。
- 文件描述符表大小及可用性现在由ZVFS_OPEN_SIZE宏决定，不再直接由[CONFIG_ZVFS_OPEN_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_OPEN_MAX)决定。子系统可用CONFIG_ZVFS_OPEN_ADD_SIZE_前缀的Kconfig选项声明自身所需表大小。旧选项仍存在，但当自定义需求更大时会被覆盖；新选项[CONFIG_ZVFS_OPEN_IGNORE_MIN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_OPEN_IGNORE_MIN)可强制使用旧配置，即使其值小于需求，默认禁用。

<a id="boards"></a>

## [开发板（Boards）](#id4)


- b_u585i_iot02a/ns：Flash布局与上游TF-M 2.2.1板配置同步，扩展分区并将次分区移到外部NOR Flash。此改动目前使旧Zephyr镜像无法直接升级为Zephyr 4.3镜像，详情见TF-M迁移及发行说明。
- nucleo_h753zi：Flash布局更新，与旧布局不兼容，固件升级可能失败。新布局将存储分区扩大到2个扇区、移除scratch暂存分区，并重新排列所有Flash分区以改善结构。
- mimxrt11x0：lpadc1改名为lpadc2，lpadc0改名为lpadc1。
- NXP frdm_mcxa166改名为frdm_mcxa346。
- NXP frdm_mcxa276改名为frdm_mcxa266。
- Panasonic panb511evb改名为panb611evb。
- STM32开发板OpenOCD配置已调整，以支持高于v0.12.0的新版OpenOCD，其中HLA／SWD传输已弃用，见[https://review.openocd.org/c/openocd/+/8523](https://review.openocd.org/c/openocd/+/8523)及提交[https://sourceforge.net/p/openocd/code/ci/34ec5536c0ba3315bc5a841244bbf70141ccfbb4/](https://sourceforge.net/p/openocd/code/ci/34ec5536c0ba3315bc5a841244bbf70141ccfbb4/)。固件早于v2j24的ST-Link不支持新传输，连接可能出问题。应升级ST-Link固件；若无法升级，修改OpenOCD脚本，加载interface/stlink-hla.cfg并明确选择hla_swd接口。仍保持与OpenOCD v0.12.0及更旧版本的向后兼容。

<a id="device-drivers-and-devicetree"></a>

## [设备驱动与设备树（Device Drivers and Devicetree）](#id5)

<a id="adc"></a>

### [模数转换器（ADC）](#id6)


- iadc_gecko.c驱动替换为adc_silabs_iadc.c，silabs,gecko-iadc替换为[silabs,iadc](../hardware/P900_SiliconLabsIADC绑定.md#dtbinding-silabs-iadc)。
- [st,stm32-adc](../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc)及派生绑定现在要求定义clock-names，数量须与clocks一致。预期名称：adcx为寄存器时钟，adc-ker为内核源时钟，adc-pre用于设置ADC预分频器，适用于预分频器位于RCC寄存器的系列。

<a id="clock-control"></a>

### [时钟控制（Clock Control）](#id7)


- [CONFIG_CLOCK_STM32_HSE_CLOCK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_STM32_HSE_CLOCK)不再由用户配置，始终从已启用的&clk_hse设备树节点clock-frequency读取；节点未启用时该符号不定义。此变化应仅影响STM32 MPU平台，使其与MCU平台既有方式一致。
- st,stm32f1-rcc及st,stm32f3-rcc不再存在，因此adc-prescaler、adc12-prescaler及adc34-prescaler也不再定义，改为在ADC clocks属性中添加预分频器时钟。

<a id="comparator"></a>

### [比较器（Comparator）](#id8)


- [nordic,nrf-comp](../hardware/P752_NordicnRF比较器绑定.md#dtbinding-nordic-nrf-comp)及[nordic,nrf-lpcomp](../hardware/P753_NordicnRF低功耗比较器绑定.md#dtbinding-nordic-nrf-lpcomp)的psel、extrefsel属性类型改为整数，范围[NRF_COMP_AIN0](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html#a9e58b7f2020be103d45749056198e906)至[NRF_COMP_AIN_VDDH_DIV5](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html#ac09477dc56124b4ff70ee7a74ae85455)。[NRF_COMP_AIN0](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html#a9e58b7f2020be103d45749056198e906)～[NRF_COMP_AIN7](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html#adbe13370c5ed6a56c4adcc010b615e88)表示外部AIN0～AIN7，[NRF_COMP_AIN_VDD_DIV2](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html#a3bdfa97f6089e8bea15f706bf467b1f1)表示内部参考VDD/2，[NRF_COMP_AIN_VDDH_DIV5](https://docs.zephyrproject.org/latest/doxygen/html/nrf-comp_8h.html#ac09477dc56124b4ff70ee7a74ae85455)表示VDDH/5。旧字符串类型已弃用。

<a id="dma"></a>

### [直接存储器访问（DMA）](#id9)


- DMA API不再实现用户模式系统调用。原系统调用的访问范围定义过宽，无法安全实现参数验证步骤，因此移除。

<a id="ethernet"></a>

### [以太网（Ethernet）](#id10)


- [microchip,vsc8541](../ethernet_phy_renesas_rockchip_binding_reference/P006_microchip_vsc8541.md#std-dtcompatible-microchip-vsc8541) PHY使用低有效复位时，现在要求reset-gpios明确指定GPIO_ACTIVE_LOW；以前低有效性质硬编码在驱动中。（[GitHub #91726](https://github.com/zephyrproject-rtos/zephyr/issues/91726)）
- Xilinx GEM以太网驱动[xlnx,gem](../ethernet_synopsys_st_xilinx_binding_reference/P022_xlnx_gem.md#std-dtcompatible-xlnx-gem)的CRC校验和硬件卸载，现在由明确禁用代替明确启用。为提升性能，默认启用卸载；但QEMU未模拟硬件校验和生成，因此无论设备树是否明确禁用，QEMU目标都始终禁用。（[GitHub #95435](https://github.com/zephyrproject-rtos/zephyr/issues/95435)）


  - 原启用接收校验和卸载的rx-checksum-offload设备树属性，替换为明确禁用该功能的disable-rx-checksum-offload。
  - 原启用发送校验和卸载的tx-checksum-offload设备树属性，替换为明确禁用该功能的disable-tx-checksum-offload。
- Xilinx GEM驱动[xlnx,gem](../ethernet_synopsys_st_xilinx_binding_reference/P022_xlnx_gem.md#std-dtcompatible-xlnx-gem)现在运行时从设计配置寄存器读取当前Zynq-7000或ZynqMP SoC的AMBA AHB数据总线宽度，因此移除不再需要的amba-ahb-dbus-width设备树属性。
- [nxp,enet-mac](../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac)及[xlnx,gem](../ethernet_synopsys_st_xilinx_binding_reference/P022_xlnx_gem.md#std-dtcompatible-xlnx-gem)驱动初始化时，不再通过[phy_configure_link()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gafce454d5da52532e4588324752c5cec3)配置PHY链路速率及双工模式。若MAC只支持PHY速率的子集，用户须通过PHY的default-speeds设备树属性，限制自动协商时通告的速率。（[GitHub #91572](https://github.com/zephyrproject-rtos/zephyr/issues/91572)）

<a id="mfd"></a>

### [多功能设备（MFD）](#id11)


- AXP2101驱动支持从AXP192中分离，移除MFD_AXP192_AXP2101。AXP192设备使用MFD_AXP192，AXP2101设备使用MFD_AXP2101。

<a id="misc"></a>

### [其他（MISC）](#id12)


- nrf_etr驱动迁移到drivers/debug，NRF_ETR及其他相关Kconfig符号改为DEBUG_NRF_ETR前缀。该驱动不再默认构建，须通过DEBUG_DRIVER明确启用。

<a id="pwm"></a>

### [脉宽调制（PWM）](#id13)


- 移除nxp,pca9685的invert属性，改用[PWM_POLARITY_INVERTED](../hardware/P255_PWM公共接口.md#ga930c0ab50f81aeb571af9747947d7fae)或[PWM_POLARITY_NORMAL](../hardware/P255_PWM公共接口.md#ga2c706bbada711f383d7b42f09dace861)标志。pwm空间的描述单元从channel、period改为channel、period、flags，#pwm-cells固定值由2变为3。

<a id="phy"></a>

### [物理层（PHY）](#id14)


- compatible为[st,stm32u5-otghs-phy](../phy_binding_reference/P007_st_stm32u5-otghs-phy.md#std-dtcompatible-st-stm32u5-otghs-phy)的节点，现在须通过新属性clock-reference选择SYSCFG_OTGHSPHYCR中的CLKSEL，即PHY参考时钟。选择值直接取决于RCC_CCIPR2的OTGHSSEL，即OTG_HS PHY内核时钟源选择。

<a id="spi"></a>

### [串行外设接口（SPI）](#id15)


- [SPI_CS_CONTROL_INIT](../hardware/P318_SPI公共接口.md#ga81308d27cd78e65f0a3ddaa918f2a74a)、[SPI_CS_CONTROL_INIT_INST](../hardware/P318_SPI公共接口.md#ga92195f45dac561b19204f6be21f62b55)、[SPI_CONFIG_DT](../hardware/P318_SPI公共接口.md#gaf7d4888063e5b739f2a3bee295962bfe)、[SPI_CONFIG_DT_INST](../hardware/P318_SPI公共接口.md#ga67837cbae6f29c5f8ad9a05dbc9b05f8)、[SPI_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga43857c934651c4bfb3823a5080a4a294)及[SPI_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#gac9537325ca3188121d0f8c382c798ca1)不再要求delay参数。SPI外设片选时序现在应通过设备树spi-cs-setup-delay-ns及spi-cs-hold-delay-ns指定。（[GitHub #87427](https://github.com/zephyrproject-rtos/zephyr/issues/87427)）

<a id="sensors"></a>

### [传感器（Sensors）](#id16)


- compatible含[invensense,icm42688](../sensor_espressif_honeywell_invensense_binding_reference/P028_invensense_icm42688.md#std-dtcompatible-invensense-icm42688)的节点，现在还须包含[invensense,icm4268x](../sensor_espressif_honeywell_invensense_binding_reference/P029_invensense_icm4268x.md#std-dtcompatible-invensense-icm4268x)才能工作。

<a id="stepper"></a>

### [步进电机（Stepper）](#id17)


- zephyr,gpio-stepper替换为zephyr,h-bridge-stepper。

<a id="usb"></a>

### [通用串行总线（USB）](#id18)


- USB视频类以前负责配置源视频设备帧率及格式，现在改由应用在主机选择格式后执行。（[GitHub #93192](https://github.com/zephyrproject-rtos/zephyr/issues/93192)）

<a id="bluetooth"></a>

## [蓝牙（Bluetooth）](#id19)


- [bt_le_cs_test_param](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__test__param.html)及[bt_le_cs_create_config_params](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__create__config__params.html)现在要求通过单个参数同时提供主模式及子模式。
- [bt_conn_le_cs_config](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__config.html)现在通过单个参数同时报告主模式及子模式。
- bt_conn_le_cs_main_mode及bt_conn_le_cs_sub_mode替换为bt_conn_le_cs_mode。

<a id="bluetooth-controller"></a>

### [蓝牙控制器（Bluetooth Controller）](#id20)


- 以下名称已修改：


  - CONFIG_BT_CTRL_ADV_ADI_IN_SCAN_RSP改名为[CONFIG_BT_CTLR_ADV_ADI_IN_SCAN_RSP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_ADI_IN_SCAN_RSP)。
  - bt_hci_vs_fata_error_cpu_data_cortex_m改名为[bt_hci_vs_fatal_error_cpu_data_cortex_m](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__fatal__error__cpu__data__cortex__m.html)，并且现在包含程序计数器（Program Counter）的值。

<a id="bluetooth-audio"></a>

### [蓝牙音频（Bluetooth Audio）](#id21)


- [bt_audio_codec_cfg](https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__cfg.html)现在要求明确设置目标时延（Target Latency）及目标PHY，不再始终将二者设置为Balanced及LE 2M。为保留原有行为，将target_latency设置为[BT_AUDIO_CODEC_CFG_TARGET_LATENCY_BALANCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga62108a3dcc3e35f7b31a99f7a33679e6a971aeaf3e2df14f5ed75965a31188f80)，将target_phy设置为[BT_AUDIO_CODEC_CFG_TARGET_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gga640af4e254e73f5c4646e9be4e99f3d1a0b7e1713ff85524953baeb4e7e085d96)。[BT_AUDIO_CODEC_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#gaefed7a013e282c63c9b5cbbdcdc67448)宏默认采用这些值。（[GitHub #93825](https://github.com/zephyrproject-rtos/zephyr/issues/93825)）
- 为GMAP设置BGS角色时，现在还要求支持并实现[CONFIG_BT_BAP_BROADCAST_ASSISTANT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_ASSISTANT)。可参考基本音频配置文件（Basic Audio Profile，BAP）的广播音频助手（Broadcast Audio Assistant）示例。（[基本音频配置文件（BAP）广播音频助手（Broadcast Audio Assistant）](../bluetooth_samples/P065_BAP广播音频助手.md#bluetooth_bap_broadcast_assistant)）
- BAP扫描委托器（Scan Delegator）不再自动更新周期广播（Periodic Advertising，PA）同步状态，必须使用[bt_bap_scan_delegator_set_pa_state()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga381c1f3b386ecbdfd570eb125882161e)更新。若BAP扫描委托器与BAP广播接收端（Broadcast Sink）一起使用，则PA状态变化时，[bt_bap_broadcast_sink](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__sink.html)接收状态中的PA状态仍会自动更新。（[GitHub #95453](https://github.com/zephyrproject-rtos/zephyr/issues/95453)）

<a id="bluetooth-hci"></a>

### [蓝牙主机控制器接口（Bluetooth HCI）](#id22)


- bt-hci-bus设备树属性中已移除被弃用的ipm取值，应改用ipc。

<a id="bluetooth-mesh"></a>

### [蓝牙网状网络（Bluetooth Mesh）](#id23)


- Kconfig选项CONFIG_BT_MESH_USES_MBEDTLS_PSA及CONFIG_BT_MESH_USES_TFM_PSA已移除。PSA Crypto提供方的选择现在由[CONFIG_PSA_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)自动控制。

<a id="bluetooth-host"></a>

### [蓝牙主机（Bluetooth Host）](#id24)


- CONFIG_BT_FIXED_PASSKEY已弃用。应用可改用[bt_conn_auth_cb.app_passkey](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__auth__cb.html#a1be006307d1c9b6b13b4d35024f130e5)回调提供配对口令（Passkey）；该回调在启用[CONFIG_BT_APP_PASSKEY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_APP_PASSKEY)时可用。应用可返回配对口令，或返回[BT_PASSKEY_RAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga988dbb7aea2ac136e3bc8efdf6f7478c)，让主机（Host）生成随机口令。

<a id="power-management"></a>

## [电源管理（Power Management）](#id25)


- [CONFIG_PM_S2RAM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_S2RAM)及PM_S2RAM_CUSTOM_MARKING已重构为由SoC和设备树自动管理。应用不应再直接启用它们，而应在设备树中启用或禁用“suspend-to-ram”电源状态，即挂起到RAM。
- NXP RW61x的exit-latency-us设备树属性已更新，以反映更准确的实测唤醒时间。对使用待机模式（Standby，PM3）的应用，该变化以及min-residency-us设备树属性值的增加，可能影响系统在电源模式间的切换，有时也会改变功耗。

<a id="networking"></a>

## [网络（Networking）](#id26)


- HTTP服务器现在遵循所配置的_config值。请检查传给[HTTP_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8fdbc5b9c3342c7b8fd258e2184cf0ae)、[HTTPS_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac8cf3b383a4482c511165eaad3c1d05f)、[HTTP_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga24ace8d5ad9ffb68e9a746c7b483b720)及[HTTPS_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b6eabec04ca31871581c382c7246765)的值是否适用。
- 套接字地址长度类型[socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a3f5f480bed01f54df564b99350f1d1bb)的大小已变化。为与Linux一致，现在固定定义为32位uint32_t；以前定义为size_t，其大小随系统配置可能为32位或64位。
- [net_icmp_init_ctx()](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga897d79bdeddb0890d4ef66f51d9505a7) API已变化，新增family参数，指定该上下文处理的报文族。ICMPv4上下文使用AF_INET，ICMPv6上下文使用AF_INET6。

<a id="coap"></a>

### [受限应用协议（CoAP）](#id27)


- [coap_client_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga37e6c0891c3e8eef3316e34d4b7a0318)签名已变化，原来的参数列表改为通过[coap_client_response_data](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__response__data.html)指针传递。
- [coap_client_request](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__request.html)已调整，以增强库对错误配置的容错能力，例如避免在结构体内使用生命周期短暂的指针：


  - [coap_client_request.path](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__request.html#a5ed6e1221dff24cc5d86a00c68620a36)现在是char数组，不再是指针；数组长度可通过[CONFIG_COAP_CLIENT_MAX_PATH_LENGTH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MAX_PATH_LENGTH)配置。
  - [coap_client_request.options](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__request.html#a333d2ed265a1a002c1ce116057d6e454)现在是[coap_client_option](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__option.html)数组，不再是指针；数组长度可通过[CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS)配置。

<a id="modem"></a>

## [调制解调器（Modem）](#id28)


- CONFIG_MODEM_AT_SHELL_USER_PIPE改名为[CONFIG_MODEM_AT_USER_PIPE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_AT_USER_PIPE)。
- CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE替换为[CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA)。新选项只指定在默认大小[CONFIG_MODEM_CMUX_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX_MTU) + 7之外需要增加的字节数。

<a id="display"></a>

## [显示（Display）](#id29)


- 显示示例以前混用了RGB565及BGR565像素格式，此问题现已修复。基于旧示例测试或开发的开发板及应用可能受影响，详见[GitHub #79996](https://github.com/zephyrproject-rtos/zephyr/issues/79996)。
- SSD1363属性名称中的greyscale现在统一改为grayscale，均表示灰度。

<a id="ptp-clock"></a>

## [精确时间协议时钟（PTP Clock）](#id30)


- [ptp_clock_rate_adjust()](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga310ee4974e6f3b01c4aa1b985194e57a)的文档以前未给出准确清晰的功能说明，驱动将其实现为相对当前频率调整速率比。现在PTP及gPTP都引入比例积分伺服（PI Servo），此API改为相对标称频率（Nominal Frequency）调整速率比。实现该API的驱动应相应更新。（[`ptp_clock_rate_adjust()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html#ga310ee4974e6f3b01c4aa1b985194e57a)）

<a id="video"></a>

## [视频（Video）](#id31)


- [video_caps](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__caps.html)中的min_line_count及max_line_count字段已移除。应用应根据新的[video_format.size](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__format.html#a42a2dfacc89f692c36c448b3ea297a90)分配缓冲区。

<a id="other-subsystems"></a>

## [其他子系统（Other Subsystems）](#id32)

<a id="cellular"></a>

### [蜂窝通信（Cellular）](#id33)

> - [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)的取值已重新定义，以与3GPP TS 27.007一致。
> - [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)的取值已扩展，以与3GPP TS 27.007一致。

<a id="crypto"></a>

### [密码功能（Crypto）](#id34)


- 哈希运算（Hashing）现在要求[hash_pkt](../crypto/P027_散列数据包结构.md)中的输入为const。这通常不影响现有代码，除非树外哈希后端确实会原地执行该运算，参见[GitHub #94218](https://github.com/zephyrproject-rtos/zephyr/issues/94218)。

<a id="flash-map"></a>

### [Flash映射（Flash Map）](#id35)


- 为逐步将PSA Crypto API作为Zephyr唯一的密码功能支持接口，FLASH_AREA_CHECK_INTEGRITY_MBEDTLS已弃用。FLASH_AREA_CHECK_INTEGRITY_PSA现在是默认选项；若未启用TF-M或平台不支持TF-M，则使用Mbed TLS提供PSA Crypto API。

<a id="logging"></a>

### [日志（Logging）](#id36)


- UART字典日志解析脚本scripts/logging/dictionary/log_parser_uart.py已弃用，应改用更通用的[scripts/logging/dictionary/live_log_parser.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/logging/dictionary/live_log_parser.py)。新脚本支持原有及更多功能，但调用时使用的命令行参数不同。

<a id="mcumgr"></a>

### [微控制器管理（MCUmgr）](#id37)


- OS管理组的[OS/Application Info](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_groups/smp_group_0.html#mcumgr-os-application-info)命令中，硬件平台响应现在输出开发板目标（Board Target），替代原来的开发板名称及修订版本，因而也包含SoC及开发板变体。旧行为已弃用，但仍可通过CONFIG_MCUMGR_GRP_OS_INFO_HARDWARE_INFO_SHORT_HARDWARE_PLATFORM启用。（[操作系统管理组（OS Mgmt）](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_groups/smp_group_0.html#mcumgr-smp-group-0)）
- 旧式Mbed TLS哈希密码实现的支持已移除，现在只使用PSA Crypto API。构建未启用TF-M时，[CONFIG_MCUMGR_GRP_FS_HASH_SHA256](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_FS_HASH_SHA256)会自动启用Mbed TLS及其PSA Crypto实现。

<a id="mbed-tls"></a>

### [Mbed TLS密码与TLS库](#id38)


- 为使Zephyr Kconfig选项与Mbed TLS构建符号更好地一一对应，以下Kconfig选项已改名：


  - CONFIG_MBEDTLS_MD改名为[CONFIG_MBEDTLS_MD_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_MD_C)。
  - CONFIG_MBEDTLS_LMS改名为[CONFIG_MBEDTLS_LMS_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_LMS_C)。
  - CONFIG_MBEDTLS_TLS_VERSION_1_2改名为[CONFIG_MBEDTLS_SSL_PROTO_TLS1_2](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)。
  - CONFIG_MBEDTLS_DTLS改名为[CONFIG_MBEDTLS_SSL_PROTO_DTLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_DTLS)。
  - CONFIG_MBEDTLS_TLS_VERSION_1_3改名为[CONFIG_MBEDTLS_SSL_PROTO_TLS1_3](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)。
  - CONFIG_MBEDTLS_TLS_SESSION_TICKETS改名为[CONFIG_MBEDTLS_SSL_SESSION_TICKETS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_SESSION_TICKETS)。
  - CONFIG_MBEDTLS_CTR_DRBG_ENABLED改名为[CONFIG_MBEDTLS_CTR_DRBG_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CTR_DRBG_C)。
  - CONFIG_MBEDTLS_HMAC_DRBG_ENABLED改名为[CONFIG_MBEDTLS_HMAC_DRBG_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_HMAC_DRBG_C)。

<a id="rtio"></a>

### [实时输入输出（RTIO）](#id39)


- 回调操作现在新增一个参数，表示链中第一个错误的结果码。
- 无论链中此前提交的操作成功还是失败，回调操作都会被调用。

<a id="secure-storage"></a>

### [安全存储（Secure Storage）](#id40)


- 用于标识存储条目的[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)从64位改为30位。这破坏了与已有存储条目的向后兼容性，旧条目将无法通过认证。若从早期Zephyr版本升级已有安装并需要保留原有条目，请启用[CONFIG_SECURE_STORAGE_64_BIT_UID](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_64_BIT_UID)。（[GitHub #94171](https://github.com/zephyrproject-rtos/zephyr/issues/94171)）

<a id="shell"></a>

### [命令行（Shell）](#id41)


- SHELL_BACKEND_MQTT相关的MQTT主题（Topic）已改名：<device_id>_rx改为<device_id>/sh/rx，<device_id>_tx改为<device_id>/sh/tx。<device_id>之后的部分现在可通过SHELL_MQTT_TOPIC_RX_ID及SHELL_MQTT_TOPIC_TX_ID配置，因此也能沿用旧主题以保持向后兼容。（[GitHub #92677](https://github.com/zephyrproject-rtos/zephyr/issues/92677)）

<a id="updatehub"></a>

### [固件更新服务（UpdateHub）](#id42)


- 旧式Mbed TLS密码支持选项已移除，现在所有情况下均使用PSA Crypto。若构建未启用TF-M，[CONFIG_UPDATEHUB](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB)会自动启用Mbed TLS的PSA Crypto实现。

<a id="modules"></a>

## [模块（Modules）](#id43)


- 由于上游版本已不再维护，TinyCrypt库已移除。Zephyr现在推荐使用PSA Crypto API作为密码库接口。

<a id="mcuboot"></a>

### [MCU启动加载器（MCUboot）](#id44)


- MCUboot的默认工作模式从移动交换（Swap Using Move）改为偏移交换（Swap Using Offset）。新模式更新更快、额外开销更小，完成一次更新所需的Flash擦写周期也更少。若开发板此前为移动交换优化，将主槽设置为比次槽大一个扇区，现在应改为次槽比主槽大一个扇区以获得最佳使用效率；两个槽具有相同扇区数的布局仍然受支持。也可通过sysbuild中的[SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE)选择原来的移动交换模式。

<a id="silabs"></a>

### [芯科科技（Silabs）](#id45)


- Rail选项名称现已与其他SiSDK相关选项统一：


  - CONFIG_RAIL_PA_CURVE_HEADER改名为[CONFIG_SILABS_SISDK_RAIL_PA_CURVE_HEADER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_RAIL_PA_CURVE_HEADER)。
  - CONFIG_RAIL_PA_CURVE_TYPES_HEADER改名为[CONFIG_SILABS_SISDK_RAIL_PA_CURVE_TYPES_HEADER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_RAIL_PA_CURVE_TYPES_HEADER)。
  - CONFIG_RAIL_PA_ENABLE_CALIBRATION改名为[CONFIG_SILABS_SISDK_RAIL_PA_ENABLE_CALIBRATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_RAIL_PA_ENABLE_CALIBRATION)。
- 修正CONFIG_SOC_*选项名称，移除了其中不应出现的PART_NUMBER。
- Series 2 SoC中独立的em3电源状态已移除。系统根据硬件外设对振荡器的请求，自动进入EM2或EM3。

<a id="lvgl"></a>

### [轻量图形库（LVGL）](#id46)


- [modules/lvgl/lvgl_display_mono.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/lvgl_display_mono.c)以前颠倒了PIXEL_FORMAT_MONO10及PIXEL_FORMAT_MONO01格式，导致LVGL配合单色显示器时黑白反转。此问题现已修复；应移除以前为获得正确显示效果而添加的变通措施，否则黑白会再次反转。

<a id="led-strip"></a>

### [LED灯带（LED Strip）](#id47)


- arduino,modulino-smartleds改名为[arduino,modulino-pixels](../led_strip_binding_reference/P002_arduino_modulino-pixels.md#std-dtcompatible-arduino-modulino-pixels)。

<a id="trusted-firmware-m"></a>

### [可信固件M（Trusted Firmware-M）](#id48)


- BL2（MCUboot）的签名流程已更新。以TF-M非安全（NS）模式运行且需要BL2的开发板，必须在Flash布局中提供Flash控制器信息，确保签署hex/bin文件时，安全（S）及非安全（NS）镜像都包含全部必要信息。镜像现在具有使固件更新（FWU）状态机正确运行并支持空中固件更新（FOTA）的信息。（[GitHub #94470](https://github.com/zephyrproject-rtos/zephyr/issues/94470)）


  - --align参数以前固定为1，现在从Flash设备树的write_block_size属性设置；对特定厂商仍以1作为回退值。
  - --max-sectors现在根据镜像数量计算，并考虑最大的镜像大小。
  - --confirm选项现在同时确认S及NS HEX镜像，确保运行的镜像适用于生产及开发。
  - 现在会生成S及NS BIN镜像，这些才是FOTA应使用的镜像。注意：S及NS镜像默认未确认，应用负责通过psa_fwu_accept()确认，否则下次重启时将回滚。
- TF-M v2.1.0之后引入的证明（Attestation）流程存在兼容性问题，因此使用TF-M v2.1的系统升级到任何后续TF-M版本都会失败。受影响的是采用TF-M v2.1.0至v2.1.2的Zephyr版本，即Zephyr v3.7至v4.2，这些版本之间无法无缝升级。上游文档称该问题已于10月25日在TF-M主线修复，修复包含在Zephyr v4.3.0中。官方建议从任何更早Zephyr版本直接迁移到v4.3.0或更高版本，以确保TF-M证明功能及升级兼容性完整。（[GitHub #94859](https://github.com/zephyrproject-rtos/zephyr/issues/94859)）最初基于Zephyr v4.0至v4.2构建的应用，必须设置[CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY)才能升级到高于v4.2的版本，并且在之后所有升级中都必须保持该设置。（[GitHub #103793](https://github.com/zephyrproject-rtos/zephyr/issues/103793)）
- 构建时通过CMake自动下载MCUboot及ethos的支持已移除，现在改用树内模块版本。若需自定义版本，应创建[west清单（Manifest）](https://docs.zephyrproject.org/latest/develop/west/manifest.html#west-manifest-files)，拉取所需的仓库版本。

## 译注

本页用于4.2到4.3迁移。Flash布局、MCUboot交换方式、TF-M兼容配置及PSA存储标识位宽变化需要结合原文适用条件阅读。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [](https://sourceforge.net/p/openocd/code/ci/34ec5536c0ba3315bc5a841244bbf70141ccfbb4/)：HTTP Error 403: Forbidden。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：迁移到Zephyr 4.2](P004_迁移到Zephyr_4.2.md) · [本模块主线目录](../reading/releases_guides.md) · [全部主线](../reading/README.md) · [下一篇：迁移到Zephyr 4.4](P006_迁移到Zephyr_4.4.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P004_迁移到Zephyr_4.2.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_迁移到Zephyr_4.4.md)

</details>

<!-- reading-navigation:end -->
