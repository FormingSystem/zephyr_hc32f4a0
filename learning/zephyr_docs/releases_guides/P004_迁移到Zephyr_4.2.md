---
id: learning.zephyr-docs.releases-guides.page-4
title: 迁移到Zephyr 4.2
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/migration-guide-4.2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="migration-guide-to-zephyr-v4-2-0"></a>

<a id="migration-4-2"></a>

# 第4章\_迁移到Zephyr v4.2.0的指南

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/migration-guide-4.2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

本文描述将应用从Zephyr v4.1.0迁移到v4.2.0所需的更改。

其他与应用迁移没有直接关系的变化，见发行说明。（[发行说明（Release Notes）](https://docs.zephyrproject.org/latest/releases/release-notes-4.2.html#zephyr-4-2)）

<a id="contents"></a>


- <a id="id1"></a>

  [构建系统（Build System）](#build-system)
- <a id="id2"></a>

  [内核（Kernel）](#kernel)
- <a id="id3"></a>

  [开发板（Boards）](#boards)
- <a id="id4"></a>

  [设备驱动与设备树（Device Drivers and Devicetree）](#device-drivers-and-devicetree)


  - <a id="id5"></a>

    [音频（Audio）](#audio)
  - <a id="id6"></a>

    [计数器（Counter）](#counter)
  - <a id="id7"></a>

    [数字音频接口（DAI）](#dai)
  - <a id="id8"></a>

    [直接存储器访问（DMA）](#dma)
  - <a id="id9"></a>

    [设备树（Devicetree）](#devicetree)
  - <a id="id10"></a>

    [显示（Display）](#display)
  - <a id="id11"></a>

    [电可擦可编程只读存储器（EEPROM）](#eeprom)
  - <a id="id12"></a>

    [增强型串行外设接口（Enhanced SPI，eSPI）](#enhanced-serial-peripheral-interface-espi)
  - <a id="id13"></a>

    [熵（Entropy）](#entropy)
  - <a id="id14"></a>

    [以太网（Ethernet）](#ethernet)
  - <a id="id15"></a>

    [闪存（Flash）](#flash)
  - <a id="id16"></a>

    [通用输入输出（GPIO）](#gpio)
  - <a id="id17"></a>

    [集成电路间音频总线（I2S）](#i2s)
  - <a id="id18"></a>

    [发光二极管（LED）](#led)
  - <a id="id19"></a>

    [多功能设备（MFD）](#mfd)
  - <a id="id20"></a>

    [其他（Misc）](#misc)
  - <a id="id21"></a>

    [调制解调器（Modem）](#modem)
  - <a id="id22"></a>

    [稳压器（Regulator）](#regulator)
  - <a id="id23"></a>

    [串行外设接口（SPI）](#spi)
  - <a id="id24"></a>

    [传感器（Sensors）](#sensors)
  - <a id="id25"></a>

    [串行接口（Serial）](#serial)
  - <a id="id26"></a>

    [步进电机（Stepper）](#stepper)
  - <a id="id27"></a>

    [定时器（Timer）](#timer)
  - <a id="id28"></a>

    [视频（Video）](#video)
  - <a id="id29"></a>

    [看门狗（Watchdog）](#watchdog)
  - <a id="id30"></a>

    [四线／八线／扩展串行外设接口（qSPI/oSPI/xSPI）](#qspi-ospi-xspi)
- <a id="id31"></a>

  [蓝牙（Bluetooth）](#bluetooth)


  - <a id="id32"></a>

    [蓝牙音频（Bluetooth Audio）](#bluetooth-audio)
  - <a id="id33"></a>

    [经典蓝牙（Bluetooth Classic）](#bluetooth-classic)
  - <a id="id34"></a>

    [蓝牙主机控制器接口（Bluetooth HCI）](#bluetooth-hci)
  - <a id="id35"></a>

    [蓝牙主机（Bluetooth Host）](#bluetooth-host)
- <a id="id36"></a>

  [网络（Networking）](#networking)


  - <a id="id37"></a>

    [轻量级机器到机器协议（LwM2M）](#lwm2m)
  - <a id="id38"></a>

    [OpenThread协议栈](#openthread)
- <a id="id39"></a>

  [其他子系统（Other Subsystems）](#other-subsystems)


  - <a id="id40"></a>

    [Modbus通信协议](#modbus)
  - <a id="id41"></a>

    [状态机框架（State Machine Framework）](#state-machine-framework)
  - <a id="id42"></a>

    [设备更新服务（hawkBit）](#hawkbit)
- <a id="id43"></a>

  [模块（Modules）](#modules)


  - <a id="id44"></a>

    [Cortex微控制器软件接口标准（CMSIS）](#cmsis)
- <a id="id45"></a>

  [架构（Architectures）](#architectures)

<a id="build-system"></a>

## [构建系统（Build System）](#id1)


- 移除硬件模型v1（HWMv1）支持。任何采用HWMv1的树外开发板或SoC都必须迁移到[HWMv2](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html#hw-model-v2)，才能用于Zephyr v4.2及以后版本。

<a id="kernel"></a>

## [内核（Kernel）](#id2)

<a id="boards"></a>

## [开发板（Boards）](#id3)


- 所有原本默认使用Nordic nrfjprog命令行工具烧录的Nordic芯片开发板，现在改为默认使用nRF Util，即nrfutil。可能需要[安装nRF Util](https://www.nordicsemi.com/Products/Development-tools/nrf-util)；若希望继续使用nrfjprog，可明确指定运行器：west flash -r nrfjprog。nRF Util完整文档见此链接。（[此处](https://docs.nordicsemi.com/bundle/nrfutil/page/README.html)）
- 所有nRF54L系列开发板现在默认在烧录时不擦除任何内部存储。若要恢复为擦除待写固件覆盖页的旧默认行为，可在west flash中将新选项--erase-mode设为ranges。注意，nRF54L的电阻式RAM（RRAM）物理上并不分页，只为方便nRF52软件迁移，人工提供4096字节页。
- 弃用CONFIG_NATIVE_POSIX_SLOWDOWN_TO_REAL_TIME，改用CONFIG_NATIVE_SIM_SLOWDOWN_TO_REAL_TIME。
- 弃用zephyr,native-posix-cpu设备树绑定，改用[zephyr,native-sim-cpu](../hardware/P551_主机原生CPU绑定.md#dtbinding-zephyr-native-sim-cpu)。
- Zephyr现在支持[NEORV32](../boards_other_vendors/P014_NEORV32.md#neorv32) 1.11.6；NEORV32处理器SoC实现须升级到该版本，才能兼容Zephyr v4.2.0。
- [NEORV32](../boards_other_vendors/P014_NEORV32.md#neorv32)现在通过开发板变体选择处理器SoC模板，原neorv32目标改名为neorv32/neorv32/up5kdemo。
- arduino_uno_r4_minima、arduino_uno_r4_wifi及mikroe_clicker_ra4m1已迁移到基于FSP的新配置。主要功能未变，但设备树结构显著调整。移除renesas,ra-gpio、renesas,ra-uart-sci、renesas,ra-pinctrl、renesas,ra-clock-generation-circuit及renesas,ra-interrupt-controller-unit绑定；替代绑定为[renesas,ra-gpio-ioport](../gpio_raspberrypi_renesas_binding_reference/P014_renesas_ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport)、[renesas,ra-sci-uart](../uart_raspberrypi_realtek_renesas_binding_reference/P006_renesas_ra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart)、[renesas,ra-pinctrl-pfs](../pinctrl_renesas_silabs_binding_reference/P006_renesas_ra-pinctrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs)及[renesas,ra-cgc-pclk-block](../clock_nxp_pico_realtek_renesas_binding_reference/P030_renesas_ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block)。
- 不再支持Nucleo WBA52CG，即nucleo_wba52cg，因为其已被列为不推荐用于新设计NRND，且自2023年7月STM32CubeWBA 1.1.0起不再受支持。建议迁移到[Nucleo WBA55CG](../boards_st_nucleo/P077_Nucleo_WBA55CG.md#nucleo_wba55cg)，即nucleo_wba55cg，可无需修改完成迁移。
- Espressif的esp32_devkitc_wroom与esp32_devkitc_wrover特性几乎相同，差异可由Kconfig覆盖，因此合并为esp32_devkitc。
- STM32开发板应包含openocd-stm32.board.cmake以添加OpenOCD烧录支持，替代openocd.board.cmake。新文件在默认OpenOCD运行器上增加STM32整片擦除命令等厂商专用配置。
- STM32N6570-DK的默认变体stm32n6570_dk/stm32n657xx现在用于链式加载应用，应使用--sysbuild构建。以前默认将应用作为第一阶段启动加载器运行的方式，改为必须明确选择的stm32n6570_dk/stm32n657xx/fsbl变体。详情见开发板文档。
- 包含TF-M BL2启动阶段的STM32目标b_u585i_iot02a//ns、nucleo_l552ze_q//ns及stm32l562e_dk//ns，不再像以前一样在BL2中包含硬件密码加速驱动，改用Mbed TLS软件实现。这与升级TF-M v2.2有关；TF-M仍支持硬件密码加速，但仅限运行时安全固件。

<a id="device-drivers-and-devicetree"></a>

## [设备驱动与设备树（Device Drivers and Devicetree）](#id4)

<a id="audio"></a>

### [音频（Audio）](#id5)


- [cirrus,cs43l22](../audio_pdm_codec_binding_reference/P007_cirrus_cs43l22.md#std-dtcompatible-cirrus-cs43l22)绑定文件重命名，以匹配compatible字符串。

<a id="counter"></a>

### [计数器（Counter）](#id6)


- counter_native_posix及其Kconfig选项、设备树绑定改名为counter_native_sim。弃用zephyr,native-posix-counter，改用[zephyr,native-sim-counter](../hardware/P550_主机原生计数器绑定.md#dtbinding-zephyr-native-sim-counter)；CONFIG_COUNTER_NATIVE_POSIX及相关选项改为[CONFIG_COUNTER_NATIVE_SIM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_NATIVE_SIM)。（[GitHub #86616](https://github.com/zephyrproject-rtos/zephyr/issues/86616)）

<a id="dai"></a>

### [数字音频接口（DAI）](#id7)


- 设备树属性dai_id重命名为dai-id。
- 设备树属性afe_name重命名为afe-name。
- 设备树属性agent_disable重命名为agent-disable。
- 设备树属性ch_num重命名为ch-num。
- 设备树属性mono_invert重命名为mono-invert。
- 设备树属性quad_ch重命名为quad-ch。
- 设备树属性int_odd重命名为int-odd。

<a id="dma"></a>

### [直接存储器访问（DMA）](#id8)


- 设备树属性nxp,a_on重命名为nxp,a-on。
- 设备树属性dma_channels重命名为dma-channels。
- Xilinx DMA控制器绑定文件重命名，使用正确厂商前缀xlnx替代xilinx，并匹配compatible字符串。

<a id="devicetree"></a>

### [设备树（Devicetree）](#id9)


- dts/common中的许多厂商或架构专用文件已移到更具体的位置。因此，设备树若以#include <common/some_file.dtsi>包含Zephyr树内文件，须改为#include <some_file.dtsi>。
- Silicon Labs Series 2的SoC级设备树文件按设备超级家族重新组织到子目录。相关开发板须将#include <silabs/some_soc.dtsi>改为#include <silabs/xg2[1-9]/some_soc.dtsi>。
- [DT_ENUM_HAS_VALUE](../dt_property_reference/P001_设备树属性读取宏.md#ga72e66a2b7a159d8b6210ef9be015c955)及[DT_INST_ENUM_HAS_VALUE](../dt_instance_reference/P001_设备树驱动实例宏.md#ga80b0321efd592a63e39400e5327bb601)用于数组时，现在检查所有值，而非仅第一个。
- 设备树及绑定属性名统一使用连字符“-”作为分隔符，替换原有下划线“_”。本地绑定可运行scripts/utils/migrate_bindings_style.py脚本迁移属性名。

<a id="display"></a>

### [显示（Display）](#id10)


- STM32 LTDC驱动[st,stm32-ltdc](../display_st_ultrachip_zephyr_binding_reference/P004_st_stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc)中的PIXEL_FORMAT_RGB565替换为PIXEL_FORMAT_BGR565，以匹配Zephyr预期格式，保证显示及视频采集示例行为正确。

<a id="eeprom"></a>

### [电可擦可编程只读存储器（EEPROM）](#id11)


- ti,tmp116-eeprom改名为[ti,tmp11x-eeprom](../mtd_nxp_st_ti_partition_binding_reference/P020_ti_tmp11x-eeprom.md#std-dtcompatible-ti-tmp11x-eeprom)，因为它同时支持tmp117及tmp119。

<a id="enhanced-serial-peripheral-interface-espi"></a>

### [增强型串行外设接口（Enhanced SPI，eSPI）](#id12)


- 设备树属性io_girq重命名为io-girq。
- 设备树属性vw_girqs重命名为vw-girqs。
- 设备树属性pc_girq重命名为pc-girq。
- 设备树属性poll_timeout重命名为poll-timeout。
- 设备树属性poll_interval重命名为poll-interval。
- 设备树属性consec_rd_timeout重命名为consec-rd-timeout。
- 设备树属性sus_chk_delay重命名为sus-chk-delay。
- 设备树属性sus_rsm_interval重命名为sus-rsm-interval。

<a id="entropy"></a>

### [熵（Entropy）](#id13)


- fake_entropy_native_posix及其Kconfig选项、设备树绑定改名为fake_entropy_native_sim。弃用zephyr,native-posix-rng，改用[zephyr,native-sim-rng](../hardware/P552_主机原生随机数绑定.md#dtbinding-zephyr-native-sim-rng)；CONFIG_FAKE_ENTROPY_NATIVE_POSIX及相关选项改为[CONFIG_FAKE_ENTROPY_NATIVE_SIM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FAKE_ENTROPY_NATIVE_SIM)。（[GitHub #86615](https://github.com/zephyrproject-rtos/zephyr/issues/86615)）

<a id="ethernet"></a>

### [以太网（Ethernet）](#id14)


- 移除Kconfig选项ETH_STM32_HAL_MII。（[GitHub #86074](https://github.com/zephyrproject-rtos/zephyr/issues/86074)）PHY接口类型现在通过设备树phy-connection-type属性选择。
- [st,stm32-ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P009_st_stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet)驱动现在要求设备树phy-handle指向相应PHY节点。（[GitHub #87593](https://github.com/zephyrproject-rtos/zephyr/issues/87593)）
- 移除ETH_STM32_HAL_PHY_ADDRESS、ETH_STM32_CARRIER_CHECK、ETH_STM32_CARRIER_CHECK_RX_IDLE_TIMEOUT_MS、ETH_STM32_AUTO_NEGOTIATION_ENABLE、ETH_STM32_SPEED_10M及ETH_STM32_MODE_HALFDUPLEX，因为它们已不再需要。驱动现在通过以太网PHY API与PHY驱动通信，由后者负责配置PHY。（[GitHub #87593](https://github.com/zephyrproject-rtos/zephyr/issues/87593)）
- ethernet_native_posix重命名为ethernet_native_tap，相关Kconfig也随之调整；弃用CONFIG_ETH_NATIVE_POSIX及相关选项，改用[CONFIG_ETH_NATIVE_TAP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NATIVE_TAP)。（[GitHub #86578](https://github.com/zephyrproject-rtos/zephyr/issues/86578)）
- NuMaker以太网驱动eth_numaker.c新增gen_random_mac支持，并移除EMAC数据Flash功能。（[GitHub #87953](https://github.com/zephyrproject-rtos/zephyr/issues/87953)）
- [include/zephyr/net/ethernet.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ethernet.h)中的ETHERNET_DSA_MASTER_PORT及ETHERNET_DSA_SLAVE_PORT分别改名为ETHERNET_DSA_CONDUIT_PORT及ETHERNET_DSA_USER_PORT。
- 以太网速率枚举重命名，以减少与具体介质的关联：[LINK_HALF_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c)_T、[LINK_FULL_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)_T、[LINK_HALF_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d)_T、[LINK_FULL_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)_T、[LINK_HALF_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec)_T、[LINK_FULL_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)_T、[LINK_FULL_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e)_T及[LINK_FULL_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)_T，分别改为LINK_HALF_10BASE、LINK_FULL_10BASE、LINK_HALF_100BASE、LINK_FULL_100BASE、LINK_HALF_1000BASE、LINK_FULL_1000BASE、LINK_FULL_2500BASE及LINK_FULL_5000BASE。[ETHERNET_LINK_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb)_T、[ETHERNET_LINK_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1)_T、[ETHERNET_LINK_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b)_T、[ETHERNET_LINK_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55)_T及[ETHERNET_LINK_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9)_T，分别改为ETHERNET_LINK_10BASE、ETHERNET_LINK_100BASE、ETHERNET_LINK_1000BASE、ETHERNET_LINK_2500BASE及ETHERNET_LINK_5000BASE。（[GitHub #87194](https://github.com/zephyrproject-rtos/zephyr/issues/87194)）
- 移除ETHERNET_CONFIG_TYPE_LINK、ETHERNET_CONFIG_TYPE_DUPLEX、ETHERNET_CONFIG_TYPE_AUTO_NEG，以及相关NET_REQUEST_ETHERNET_SET_LINK、NET_REQUEST_ETHERNET_SET_DUPLEX、NET_REQUEST_ETHERNET_SET_AUTO_NEGOTIATION。配置链路应改用[phy_configure_link()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gafce454d5da52532e4588324752c5cec3)配合[net_eth_get_phy()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga7225d06fbaa12d4668fa165d9e8f0845)。（[GitHub #90652](https://github.com/zephyrproject-rtos/zephyr/issues/90652)）
- [phy_configure_link()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gafce454d5da52532e4588324752c5cec3)新增flags参数；设为0可保留旧行为。（[GitHub #91354](https://github.com/zephyrproject-rtos/zephyr/issues/91354)）

<a id="flash"></a>

### [闪存（Flash）](#id15)


- 文件flash_hp_ra.h重命名为soc_flash_renesas_ra_hp.h。
- 文件flash_hp_ra.c重命名为soc_flash_renesas_ra_hp.c。
- 文件flash_hp_ra_ex_op.c重命名为soc_flash_renesas_ra_hp_ex_op.c。
- 移除Renesas RA Flash HP双存储区模式的CONFIG_DUAL_BANK_MODE。
- Renesas RA Flash HP选项CONFIG_RA_FLASH_HP重命名为[CONFIG_SOC_FLASH_RENESAS_RA_HP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_RENESAS_RA_HP)。
- Renesas RA Flash HP写保护选项CONFIG_FLASH_RA_WRITE_PROTECT重命名为CONFIG_FLASH_RENESAS_RA_HP_WRITE_PROTECT。
- 将renesas,ra-nv-flash.yaml拆为renesas,ra-nv-code-flash.yaml及renesas,ra-nv-data-flash.yaml两个文件。
- 将compatible从renesas,ra-nv-flash拆为renesas,ra-nv-code-flash.yaml及renesas,ra-nv-data-flash.yaml；此处.yaml后缀按原文保留。

<a id="gpio"></a>

### [通用输入输出（GPIO）](#id16)


- 为支持引脚更多的RP2350B，调整树莓派GPIO配置。原raspberrypi,rpi-gpio职责移到raspberrypi,rpi-gpio-port，raspberrypi,rpi-gpio现在仅作为占位及映射器；标签也同步调整，因此常规用法无需修改。
- [arduino-nano-header](../gpio_adi_headers_ambiq_binding_reference/P026_arduino-nano-header.md#std-dtcompatible-arduino-nano-header)-r3改名为arduino-nano-header。R3来自改变过连接器的Arduino UNO R3，与Arduino Nano无关。
- include/zephyr/dt-bindings/gpio/nordic-npm1300-gpio.h移到[include/zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h)，宏定义中的NPM1300全部改为NPM13XX。
- CONFIG_GPIO_NPM1300及CONFIG_GPIO_NPM1300_INIT_PRIORITY，分别改为[CONFIG_GPIO_NPM13XX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_NPM13XX)及[CONFIG_GPIO_NPM13XX_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_NPM13XX_INIT_PRIORITY)。

<a id="i2s"></a>

### [集成电路间音频总线（I2S）](#id17)


- [nxp,mcux-i2s](../i2s_binding_reference/P013_nxp_mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s)驱动新增mclk-output属性。设置此属性可
- 将MCLK信号配置为输出。旧版驱动使用宏
- I2S_OPT_BIT_CLK_SLAVE配置MCLK信号方向。（[GitHub #88554](https://github.com/zephyrproject-rtos/zephyr/issues/88554)）

<a id="led"></a>

### [发光二极管（LED）](#id18)


- CONFIG_LED_NPM1300改为[CONFIG_LED_NPM13XX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_NPM13XX)。

<a id="mfd"></a>

### [多功能设备（MFD）](#id19)


- include/zephyr/drivers/mfd/npm1300.h移到[include/zephyr/drivers/mfd/npm13xx.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/mfd/npm13xx.h)，枚举及函数名中的npm1300／NPM1300全部改为npm13xx／NPM13XX。
- CONFIG_MFD_NPM1300及CONFIG_MFD_NPM1300_INIT_PRIORITY，分别改为[CONFIG_MFD_NPM13XX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_NPM13XX)及[CONFIG_MFD_NPM13XX_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_NPM13XX_INIT_PRIORITY)。

<a id="misc"></a>

### [其他（Misc）](#id20)


- drivers/memc/memc_nxp_flexram.h移到[include/zephyr/drivers/misc/flexram/nxp_flexram.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/misc/flexram/nxp_flexram.h)，可直接通过<zephyr/drivers/misc/flexram/nxp_flexram.h>包含，无需再修改CMakeList.txt来包含该驱动；文件名拼写按原文保留。
- 所有memc_flexram_*命名项，包括Kconfig及C API，统一改为flexram_*。
- 启用Ethos-U神经网络处理器NPU驱动时，选择CONFIG_ETHOS_U，替代CONFIG_ARM_ETHOS_U。
- 所有CONFIG_ARM_ETHOS_U_前缀配置项改用CONFIG_ETHOS_U_前缀。

<a id="modem"></a>

### [调制解调器（Modem）](#id21)


- 移除CONFIG_MODEM_CELLULAR_CMUX_MAX_FRAME_SIZE，改用CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE及[CONFIG_MODEM_CMUX_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX_MTU)。

<a id="regulator"></a>

### [稳压器（Regulator）](#id22)


- include/zephyr/dt-bindings/regulator/npm1300.h移到[include/zephyr/dt-bindings/regulator/npm13xx.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/regulator/npm13xx.h)，宏定义中的NPM1300全部改为NPM13XX。
- CONFIG_REGULATOR_NPM1300改为[CONFIG_REGULATOR_NPM13XX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM13XX)，CONFIG_REGULATOR_NPM1300_COMMON_INIT_PRIORITY改为REGULATOR_NPM13XX_COMMON_INIT_PRIORITY，CONFIG_REGULATOR_NPM1300_INIT_PRIORITY改为[CONFIG_REGULATOR_NPM13XX_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR_NPM13XX_INIT_PRIORITY)；中间目标名称缺少CONFIG_前缀，按原文保留。
- [nordic,npm1300-regulator](../hardware/P662_nPM1300稳压器绑定.md#dtbinding-nordic-npm1300-regulator)的BUCK及LDO节点GPIO属性现在使用不带GPIO控制器的整数数组，因此通过GPIO控制输出电源轨时，不再要求存在并启用[nordic,npm1300-gpio](../gpio_microchip_nordic_nuvoton_binding_reference/P011_nordic_npm1300-gpio.md#std-dtcompatible-nordic-npm1300-gpio)节点。例如enable-gpios = <&pmic_gpios 3 GPIO_ACTIVE_LOW>;改为enable-gpio-config = <3 GPIO_ACTIVE_LOW>;。

<a id="spi"></a>

### [串行外设接口（SPI）](#id23)


- CONFIG_SPI_MCUX_LPSPI改为[CONFIG_SPI_NXP_LPSPI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NXP_LPSPI)，该驱动的子配置也相应更名，包括[CONFIG_SPI_NXP_LPSPI_DMA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NXP_LPSPI_DMA)及[CONFIG_SPI_NXP_LPSPI_CPU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NXP_LPSPI_CPU)。
- 设备树属性port_sel重命名为port-sel。
- 设备树属性chip_select重命名为chip-select。
- [andestech,atcspi200](../spi_adi_atmel_esp_binding_reference/P006_andestech_atcspi200.md#std-dtcompatible-andestech-atcspi200)绑定文件重命名，以匹配compatible字符串。

<a id="sensors"></a>

### [传感器（Sensors）](#id24)


- 厂商前缀ltr改为liteon，ltr,f216a改为[liteon,ltrf216a](../sensor_liteon_maxim_temperature_binding_reference/P007_liteon_ltrf216a.md#std-dtcompatible-liteon-ltrf216a)；DT_HAS_LTR_F216A_ENABLED替换为DT_HAS_LITEON_LTRF216A_ENABLED。（[GitHub #85453](https://github.com/zephyrproject-rtos/zephyr/issues/85453)）
- ti,tmp116改名为[ti,tmp11x](../sensor_ti_vishay_wurth_sensing_binding_reference/P009_ti_tmp11x.md#std-dtcompatible-ti-tmp11x)，因为它支持tmp116、tmp117及tmp119。
- meas,ms5837替换为[meas,ms5837-30ba](../sensor_microchip_nordic_nxp_binding_reference/P004_meas_ms5837-30ba.md#std-dtcompatible-meas-ms5837-30ba)及[meas,ms5837-02ba](../sensor_microchip_nordic_nxp_binding_reference/P003_meas_ms5837-02ba.md#std-dtcompatible-meas-ms5837-02ba)。使用其中一种变体时，还需要设置status属性。
- we,wsen-itds驱动重命名为[we,wsen-itds-2533020201601](../compatible_binding_reference/P100_we_wsen-itds-2533020201601.md#std-dtcompatible-we-wsen-itds-2533020201601)，设备树可按以下方式配置：

  ```text
  &i2c0 {
    itds:itds-2533020201601@19 {
      compatible = "we,wsen-itds-2533020201601";
      reg = <0x19>;
      odr = "400";
      op-mode = "high-perf";
      power-mode = "normal";
      events-interrupt-gpios = <&gpio1 1 GPIO_ACTIVE_HIGH>;
      drdy-interrupt-gpios = <&gpio1 2 GPIO_ACTIVE_HIGH>;
    };
  };
  ```
- raspberrypi,pico-temp.yaml绑定文件重命名，以匹配compatible字符串。
- include/zephyr/drivers/sensor/npm1300_charger.h移到[include/zephyr/drivers/sensor/npm13xx_charger.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/sensor/npm13xx_charger.h)，枚举中的NPM1300全部改为NPM13XX。
- CONFIG_NPM1300_CHARGER改为[CONFIG_NPM13XX_CHARGER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NPM13XX_CHARGER)。

<a id="serial"></a>

### [串行接口（Serial）](#id25)


- uart_native_posix及其Kconfig、设备树绑定改名为uart_native_pty。弃用zephyr,native-posix-uart，改用[zephyr,native-pty-uart](../uart_ti_wch_virtual_binding_reference/P013_zephyr_native-pty-uart.md#std-dtcompatible-zephyr-native-pty-uart)；CONFIG_UART_NATIVE_POSIX及相关选项改为[CONFIG_UART_NATIVE_PTY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_PTY)。CONFIG_NATIVE_UART_0替换为[CONFIG_UART_NATIVE_PTY_0](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_PTY_0)，现在还可通过运行时命令行--<uart_name>_stdinout，选择UART连接进程标准输入／输出而非伪终端PTY。CONFIG_NATIVE_UART_AUTOATTACH_DEFAULT_CMD替换为[CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD)。弃用CONFIG_UART_NATIVE_WAIT_PTS_READY_ENABLE，其功能没有负面影响，因此现在始终启用。CONFIG_UART_NATIVE_POSIX_PORT_1_ENABLE已弃用且不再起作用，用户应按所需实例数量创建[zephyr,native-pty-uart](../uart_ti_wch_virtual_binding_reference/P013_zephyr_native-pty-uart.md#std-dtcompatible-zephyr-native-pty-uart)节点。（[GitHub #86739](https://github.com/zephyrproject-rtos/zephyr/issues/86739)）

<a id="stepper"></a>

### [步进电机（Stepper）](#id26)


- stepper_enable(const struct device * dev, bool enable)拆为[stepper_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3395b5f8b401d8175067edfb25c2e0e8)及[stepper_disable()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab892a6b8d8fb34db0e682dd8f7de4218)。

<a id="timer"></a>

### [定时器（Timer）](#id27)


- native_posix_timer重命名为native_sim_timer；弃用CONFIG_NATIVE_POSIX_TIMER，改用[CONFIG_NATIVE_SIM_TIMER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NATIVE_SIM_TIMER)。（[GitHub #86612](https://github.com/zephyrproject-rtos/zephyr/issues/86612)）
- andestech,machine-timer、neorv32-machine-timer、telink,machine-timer、lowrisc,machine-timer、niosv-machine-timer及scr,machine-timer统一为[riscv,machine-timer](../interrupt_fabric_binding_reference/P011_riscv_machine-timer.md#std-dtcompatible-riscv-machine-timer)。

  现在必须通过reg及reg-names明确指定MTIME及MTIMECMP寄存器地址。reg-names变为必需，名称与reg每个条目须一一对应。（[GitHub #84175](https://github.com/zephyrproject-rtos/zephyr/issues/84175)及#89847）（[GitHub #89847](https://github.com/zephyrproject-rtos/zephyr/issues/89847)）

  示例（Example）：

  ```text
  mtimer: timer@d1000000 {
      compatible = "riscv,machine-timer";
      interrupts-extended = <&cpu0_intc 7>;
      reg = <0xd1000000 0x8
             0xd1000008 0x8>;
      reg-names = "mtime", "mtimecmp";
  };
  ```
- 现在可在设备树cpus组中使用timebase-frequency属性，提供[CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC)的值，替代直接配置数值。（[GitHub #91296](https://github.com/zephyrproject-rtos/zephyr/issues/91296)）

<a id="video"></a>

### [视频（Video）](#id28)


- 8位RAW Bayer格式BGGR8／GBRG8／GRBG8／RGGB8在前面增加S前缀：

  VIDEO_PIX_FMT_BGGR8改为[VIDEO_PIX_FMT_SBGGR8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabc0205ce5c6426051fdec88d92f123e3)；VIDEO_PIX_FMT_GBRG8改为[VIDEO_PIX_FMT_SGBRG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa9edb9c562fc3c86b61e071970fae60d)；VIDEO_PIX_FMT_GRBG8改为[VIDEO_PIX_FMT_SGRBG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga19d8dc905695229097dffe659f2a806e)；VIDEO_PIX_FMT_RGGB8改为[VIDEO_PIX_FMT_SRGGB8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabf0dde810e75d37823891ed03811482c)。
- STM32 DCMI驱动[st,stm32-dcmi](../video_st_sony_emulation_binding_reference/P004_st_stm32-dcmi.md#std-dtcompatible-st-stm32-dcmi)现在采用基于端点的video-interfaces.yaml绑定描述传感器接口属性，例如总线宽度及同步信号。capture-rate属性也由帧间隔API [video_set_frmival()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__frmival.html#ga46c5bca5cd3caf762f9dd4998b6e21de)替代。（[GitHub #89627](https://github.com/zephyrproject-rtos/zephyr/issues/89627)）
- 移除video_endpoint_id，它不再作为任何视频API的参数。
- 新增[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)，并成为set_stream()、[video_stream_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html#gaa4d62da5137d0392ce8a19f794478610)及[video_stream_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html#ga77c694bfc3ff8d51a5a74dcd211b2563)的必需参数。
- video_format.pitch改为由驱动明确设置，以前由应用负责。应用因此可按各驱动正确分配缓冲区大小。现有应用不会被破坏，但可像提交33dcbe37cfd3593e8c6e9cfd218dd31fdd533598中的示例那样简化。
- 使用[原生模拟器（Native Simulator）](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)的示例及项目，现在必须指定--snippet [video-sw-generator](../snippets/P005_视频软件发生器配置片段.md#snippet-video-sw-generator)才能正确构建。
- [video_query_ctrl()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga8813a656a66adc6bfb10fb7f27194898)现在只接收[video_ctrl_query](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl__query.html)一个参数；结构体新增video_ctrl_query.dev字段，用于指定及回读所查询设备。（[GitHub #91265](https://github.com/zephyrproject-rtos/zephyr/issues/91265)）

<a id="watchdog"></a>

### [看门狗（Watchdog）](#id29)


- CONFIG_WDT_NPM1300及CONFIG_WDT_NPM1300_INIT_PRIORITY分别改为[CONFIG_WDT_NPM13XX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM13XX)及[CONFIG_WDT_NPM13XX_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPM13XX_INIT_PRIORITY)。

<a id="qspi-ospi-xspi"></a>

### [四线／八线／扩展串行外设接口（qSPI/oSPI/xSPI）](#id30)


- STM32外部存储器设备树描述中的容量及地址，现在拆分为两个独立属性，以遵循规范建议。

  例如，外部Flash原描述reg = <0x70000000 DT_SIZE_M(64)>; /* 512 Mbits /改为reg = <0>; size = <DT_SIZE_M(512)>; / 512 Mbits */；注释分隔符不完整的写法按原文保留。

  注意，新属性给出存储器实际容量，单位为位bit。原有映射地址信息移到SoC dtsi中的xspi、ospi或qspi节点。

<a id="bluetooth"></a>

## [蓝牙（Bluetooth）](#id31)

<a id="bluetooth-audio"></a>

### [蓝牙音频（Bluetooth Audio）](#id32)


- CONFIG_BT_CSIP_SET_MEMBER_NOTIFIABLE改名为[CONFIG_BT_CSIP_SET_MEMBER_SIRK_NOTIFIABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_SIRK_NOTIFIABLE)。（[GitHub #86763](https://github.com/zephyrproject-rtos/zephyr/issues/86763)）
- 移除bt_csip_set_member_get_sirk，改用[bt_csip_set_member_get_info()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gad80917089bc7e629cc3cb9d7fbf6cf45)获取SIRK及其他信息。（[GitHub #86996](https://github.com/zephyrproject-rtos/zephyr/issues/86996)）
- BT_AUDIO_CONTEXT_TYPE_PROHIBITED改名为[BT_AUDIO_CONTEXT_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d)。（[GitHub #89506](https://github.com/zephyrproject-rtos/zephyr/issues/89506)）

<a id="bluetooth-classic"></a>

### [经典蓝牙（Bluetooth Classic）](#id33)


- [bt_hfp_ag_cb](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__ag__cb.html)中的HFP音频网关AG回调sco_disconnected参数，改为SCO连接对象struct bt_conn *sco_conn及断开原因uint8_t reason。

<a id="bluetooth-hci"></a>

### [蓝牙主机控制器接口（Bluetooth HCI）](#id34)


- 经过HCI驱动接口的缓冲区类型，现在由缓冲区载荷自身的H:4编码前缀字节表示。bt_buf_set_type()及bt_buf_get_type()已弃用，但仍可用，限制是每个缓冲区只能调用一次。
- 弃用bt_hci_cmd_create()，改用[bt_hci_cmd_alloc()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a974e6e9262601e73537cbdcba7a7c93c)。新函数不接收参数，因为命令发送函数已负责命令头编码。

<a id="bluetooth-host"></a>

### [蓝牙主机（Bluetooth Host）](#id35)


- [include/zephyr/bluetooth/conn.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/conn.h)中的BT_LE_CS_TONE_ANTENNA_CONFIGURATION_INDEX_<NUMBER>改名为BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A<NUMBER>_B<NUMBER>。
- 等时ISO数据通路不再自动配置，应用须分别调用[bt_iso_setup_data_path()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa74c762451cfb5d04ffcd8d396a75447)及[bt_iso_remove_data_path()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga53be464e005392676830feeddd8cdc22)明确建立和移除。（[GitHub #75549](https://github.com/zephyrproject-rtos/zephyr/issues/75549)）
- BT_ISO_CHAN_TYPE_CONNECTED拆为BT_ISO_CHAN_TYPE_CENTRAL及BT_ISO_CHAN_TYPE_PERIPHERAL，更准确描述ISO通道角色，因为不同角色行为可能不同。原有BT_ISO_CHAN_TYPE_CONNECTED判断可改为两个类型判断的逻辑或||。（[GitHub #75549](https://github.com/zephyrproject-rtos/zephyr/issues/75549)）
- [include/zephyr/bluetooth/gatt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/gatt.h)中的struct _bt_gatt_ccc重命名为struct [bt_gatt_ccc_managed_user_data](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__ccc__managed__user__data.html)。（[GitHub #88652](https://github.com/zephyrproject-rtos/zephyr/issues/88652)）
- [include/zephyr/bluetooth/gatt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/gatt.h)中的BT_GATT_CCC_INITIALIZER宏重命名为[BT_GATT_CCC_MANAGED_USER_DATA_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gae3a23386bfe38e0127b74e0f4b5e5667)。（[GitHub #88652](https://github.com/zephyrproject-rtos/zephyr/issues/88652)）
- 移除完全未使用的CONFIG_BT_ISO_TX_FRAG_COUNT，现有配置引用可直接删除。（[GitHub #89836](https://github.com/zephyrproject-rtos/zephyr/issues/89836)）

<a id="networking"></a>

## [网络（Networking）](#id36)


- struct [net_linkaddr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__linkaddr.html)_storage重命名为struct [net_linkaddr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__linkaddr.html)，并移除旧struct [net_linkaddr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__linkaddr.html)。新结构体直接包含链路地址存储空间，不再使用地址指针，避免克隆[net_pkt](https://docs.zephyrproject.org/latest/doxygen/html/structnet__pkt.html)时可能出现的悬空指针。IEEE 802.15.4的[net_pkt](https://docs.zephyrproject.org/latest/doxygen/html/structnet__pkt.html)大小因此增加4字节，以太网等其他技术不增加。直接使用net_linkaddr的代码若以if (lladdr->addr == NULL)判断地址未设置，须改为if (lladdr->len == 0)，因为addr已不再是指针。
- TLS凭据类型TLS_CREDENTIAL_SERVER_CERTIFICATE改名为更通用的[TLS_CREDENTIAL_PUBLIC_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8)，以准确体现用途。
- MQTT公开API [mqtt_disconnect()](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__socket.html#ga0bc7d91da88c2fbc25108d89ce4318c4)新增param参数，以支持MQTT 5.0。该参数可选，旧版MQTT不使用；MQTT 3.1.1用户应传NULL。
- 不再支持AF_PACKET/SOCK_RAW/IPPROTO_RAW组合，因为AF_PACKET套接字应只接收IEEE 802.3协议号。可按实际用途改用AF_PACKET/SOCK_DGRAM/ETH_P_ALL或AF_INET(6)/SOCK_RAW/IPPROTO_IP。
- HTTP服务器现在遵守配置的_concurrent及_backlog值，请检查[HTTP_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8fdbc5b9c3342c7b8fd258e2184cf0ae)、[HTTPS_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac8cf3b383a4482c511165eaad3c1d05f)、[HTTP_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga24ace8d5ad9ffb68e9a746c7b483b720)及[HTTPS_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b6eabec04ca31871581c382c7246765)传入值是否合适。
- [CONFIG_NET_ZPERF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF)不再默认包含服务器支持。使用服务器命令须启用[CONFIG_NET_ZPERF_SERVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_SERVER)；不需要服务器时，可能可以减小[CONFIG_ZVFS_POLL_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_POLL_MAX)。
- 二层Wi-Fi Shell现在为多数命令支持接口选择。为适应该变化，部分旧选项已重命名，下表概述：

  <table>
  <tr>
  <td>命令（Command）</td>
  <td>旧选项（Old Option）</td>
  <td>新选项（New Option）</td>
  </tr>
  <tr>
  <td>wifi connect及wifi ap enable命令</td>
  <td><code>-i</code></td>
  <td><code>-g</code></td>
  </tr>
  <tr>
  <td><code>wifi twt setup</code></td>
  <td><code>-i</code></td>
  <td><code>-p</code></td>
  </tr>
  <tr>
  <td><code>wifi ap config</code></td>
  <td><code>-i</code></td>
  <td><code>-t</code></td>
  </tr>
  <tr>
  <td>wifi mode、wifi channel及wifi packet_filter命令</td>
  <td><code>--if-index</code></td>
  <td><code>--iface</code></td>
  </tr>
  </table>
- HTTP客户端响应回调[http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)签名改变，返回值由void改为int，使应用能够中止HTTP连接。现有应用须更新回调实现；返回0即可保持原有行为。
- net_mgmt事件处理函数[net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)及请求处理函数[net_mgmt_request_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga78b9302193bd0c5cc35d81d298a5eb6b)签名改变，管理事件类型由uint32_t改为uint64_t，使事件编号可以表示位掩码而非枚举值。层代码仍为枚举；需要时可用NET_MGMT_LAYER_CODE及NET_MGMT_GET_COMMAND，从处理函数收到的实际事件值提取层代码及管理事件命令。
- net_mgmt套接字选项不能再直接使用网络管理事件类型，因为事件已变为uint64_t，而套接字选项要求普通32位整数。因此新增SO_NET_MGMT_ETHERNET_SET_QAV_PARAM及SO_NET_MGMT_ETHERNET_GET_QAV_PARAM，替代原NET_REQUEST_ETHERNET_SET_QAV_PARAM及NET_REQUEST_ETHERNET_GET_QAV_PARAM。
- DNS解析器配置函数[dns_resolve_reconfigure()](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga1d3bb0319531bfe0ae95f48bdc51c56f)及[dns_resolve_reconfigure_with_interfaces()](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3d22eed1d6d017e5bd7a2344775d33b7)现在要求用户提供DNS服务器信息来源。例如通过DHCPv4取得服务器信息时，须指定[DNS_SOURCE_DHCPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b)。

<a id="lwm2m"></a>

### [轻量级机器到机器协议（LwM2M）](#id37)


- 加速度计对象：Y值、Z值、最小量程及最大量程等可选资源，现在可按对象规范选择使用；使用这些资源时，用户须提供读取缓冲区。

<a id="openthread"></a>

### [OpenThread协议栈](#id38)


- Zephyr中的OpenThread集成经过重大重构，实现由网络层subsys/net/l2/openthread/移到专用模块modules/openthread/。
- OpenThread现在是独立Zephyr模块，可不依赖Zephyr网络栈，即二层L2及IEEE 802.15.4适配层运行。因此应用可直接使用OpenThread及自己的IEEE 802.15.4驱动，或在无需完整Zephyr网络栈的场景中使用。
- [include/zephyr/net/openthread.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/openthread.h)中的大多数函数已弃用。旧API仍保留以兼容已有代码，但新应用应使用OpenThread模块提供的新API。变更如下：


  - 互斥锁处理（Mutex Handling）：


    - 原先（Previously）：


      - `openthread_api_mutex_lock`
      - `openthread_api_mutex_try_lock`
      - `openthread_api_mutex_unlock`
    - 现在使用：


      - [`openthread_mutex_lock()`](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#ae3945bc3549118dc5420f9859588282d)
      - [`openthread_mutex_try_lock()`](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#ab5669622dfd83d3a5175fa47325dade3)
      - [`openthread_mutex_unlock()`](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a420c3321272141f63ea86166b84ec845)
  - 启动OpenThread：


    - 以前：openthread_start
    - 现在使用：[openthread_run()](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a558165d2e49e9335649c94ac0be53392)
  - 回调注册（Callback Registration）：


    - 原先（Previously）：


      - `openthread_state_changed_cb_register`
      - `openthread_state_changed_cb_unregister`
    - 现在使用：


      - [`openthread_state_changed_callback_register()`](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a4178b72288585869e2c941acdc21db57)
      - [`openthread_state_changed_callback_unregister()`](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#ae4ad25613f8eada1a0a29426a2f4a518)
  - 回调结构体（Callback Structure）：


    - 以前：openthread_state_changed_cb
    - 现在使用：[openthread_state_changed_callback](https://docs.zephyrproject.org/latest/doxygen/html/structopenthread__state__changed__callback.html)
  - 以下openthread_context字段已弃用，新代码不应继续使用：


    - `instance`
    - `api_lock`
    - `work_q`
    - `api_work`
    - `state_change_cbs`
  - 以前没有、现在新增的函数：


    - [openthread_init()](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a4d213cad99e6eeb747bd0057248251e5)：初始化OpenThread协议栈。
    - [openthread_stop()](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#af52cc96d5d4be673f16eb4856de6cc58)：停止并禁用OpenThread协议栈。
    - [openthread_set_receive_cb()](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a14ea88a5f4e4a9e014f2381cd853e8de)：设置OpenThread协议栈接收回调。
- OpenThread相关Kconfig选项由subsys/net/l2/openthread/Kconfig移到[modules/openthread/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig)。所有选项本身保持不变，仍可沿用原有用法，但在menuconfig或guiconfig中修改时须使用新路径。
- 启用[CONFIG_NET_L2_OPENTHREAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)时，Zephyr二层使用新OpenThread模块API作为后端；L2不再自行实现OpenThread，而将实现交给模块。
- 对于通过Zephyr网络栈使用OpenThread的现有应用：


  - 由于旧API仍为兼容保留，应用应能继续工作。不过建议迁移到新API，采用模块化结构，为今后版本做好准备。
  - 在配置工具中，将OpenThread Kconfig选项的路径引用更新为modules/openthread/Kconfig。
- 对于使用openthread_context或其他弃用API的应用：


  - 开始迁移到新API；弃用API会在后续版本移除。
  - 避免直接使用openthread_context及其字段，改用新的初始化及回调注册函数。
- 对于新应用，或不通过Zephyr L2使用OpenThread的应用：


  - 使用新初始化函数[openthread_init()](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a4d213cad99e6eeb747bd0057248251e5)、运行函数[openthread_run()](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h.html#a558165d2e49e9335649c94ac0be53392)及回调注册API openthread_state_change_callback_register()。
  - 使用场景允许时，现在可直接使用OpenThread，无需启用Zephyr L2或IEEE 802.15.4层。

<a id="other-subsystems"></a>

## [其他子系统（Other Subsystems）](#id39)

<a id="modbus"></a>

### [Modbus通信协议](#id40)


- [modbus_serial_param](../modbus/P014_Modbus串行线路参数.md)中的client_stop_bits改名为stop_bits，此设置在客户端及服务器模式均有效。
- 自定义停止位默认禁用，须通过[CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE)启用。

<a id="state-machine-framework"></a>

### [状态机框架（State Machine Framework）](#id41)


- 移除smf_set_handled()。
- 状态运行动作现在返回[smf_state_result](../smf/P005_状态机API参考.md#ga01e4e2d2f35a9ec790d5e3c5b9b91b55)而非void，返回值决定事件已被处理还是向父状态运行动作传播。完全处理事件应返回SMF_EVENT_HANDLED，需要父状态继续处理则返回SMF_EVENT_PROPAGATE。
- 平面状态机忽略返回值；从技术语义看，返回SMF_EVENT_HANDLED最准确。

<a id="hawkbit"></a>

### [设备更新服务（hawkBit）](#id42)


- 启用[CONFIG_HAWKBIT_CUSTOM_DEVICE_ID](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_CUSTOM_DEVICE_ID)时，device_id不再自动添加[CONFIG_BOARD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD)前缀；需要板名时，由用户编写相应回调。

<a id="modules"></a>

## [模块（Modules）](#id43)

<a id="cmsis"></a>

### [Cortex微控制器软件接口标准（CMSIS）](#id44)


- Cortex-M开发板及SoC现在须使用CMSIS_6模块才能正确构建，替代原cmsis模块，即CMSIS 5.9.0。构建Cortex-M目标前，应先执行west update，确保CMSIS_6可用，再运行west build等命令。

  使用旧cmsis本地副本或CONFIG_ZEPHYR_CMSIS_MODULE_DIR的开发板、SoC及模块，应迁移到CMSIS_6，通过CONFIG_ZEPHYR_CMSIS_6_MODULE_DIR访问。

  注意：Cortex-A及Cortex-R目标仍使用旧cmsis模块。

<a id="architectures"></a>

## [架构（Architectures）](#id45)


- [CONFIG_SRAM_VECTOR_TABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SRAM_VECTOR_TABLE)从zephyr/Kconfig.zephyr移到zephyr/arch/Kconfig，并增加[CONFIG_XIP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)、CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION及[CONFIG_ROMSTART_RELOCATION_ROM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ROMSTART_RELOCATION_ROM)依赖，以支持将向量表重定位到RAM。
- CONFIG_DEBUG_INFO重命名为[CONFIG_X86_DEBUG_INFO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_DEBUG_INFO)，以准确体现用途；现在仅适用于x86架构。

## 译注

本页用于4.1到4.2迁移。原网页个别名称包含.yaml、缺少CONFIG_前缀或存在排版残留时，译文保留标识并作说明，不扩展为仓库实验指导。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [README.html](https://docs.nordicsemi.com/bundle/nrfutil/page/README.html)：HTTP Error 403: Forbidden。
- [nrf-util](https://www.nordicsemi.com/Products/Development-tools/nrf-util)：HTTP Error 403: Forbidden。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：迁移到Zephyr 3.7](P003_迁移到Zephyr_3.7.md) · [本模块主线目录](../reading/releases_guides.md) · [全部主线](../reading/README.md) · [下一篇：迁移到Zephyr 4.3](P005_迁移到Zephyr_4.3.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P003_迁移到Zephyr_3.7.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_迁移到Zephyr_4.3.md)

</details>

<!-- reading-navigation:end -->
