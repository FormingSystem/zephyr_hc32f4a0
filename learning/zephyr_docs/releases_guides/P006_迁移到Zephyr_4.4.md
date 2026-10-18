---
id: learning.zephyr-docs.releases-guides.page-6
title: 迁移到Zephyr 4.4
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/migration-guide-4.4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="migration-guide-to-zephyr-v4-4-0"></a>

<a id="migration-4-4"></a>

# 第6章\_迁移到Zephyr v4.4.0的指南（Migration Guide）

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/migration-guide-4.4.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

本文说明将应用从Zephyr v4.3.0迁移到Zephyr v4.4.0所需的更改。

其他与应用迁移没有直接关系的变化，见发行说明。（[发行说明（Release Notes）](https://docs.zephyrproject.org/latest/releases/release-notes-4.4.html#zephyr-4-4)）

<a id="contents"></a>


- <a id="id2"></a>

  [通用部分（Common）](#common)
- <a id="id3"></a>

  [构建系统（Build System）](#build-system)
- <a id="id4"></a>

  [内核（Kernel）](#kernel)
- <a id="id5"></a>

  [开发板（Boards）](#boards)
- <a id="id6"></a>

  [设备驱动与设备树（Device Drivers and Devicetree）](#device-drivers-and-devicetree)


  - <a id="id7"></a>

    [模数转换器（ADC）](#adc)
  - <a id="id8"></a>

    [时钟控制（Clock Control）](#clock-control)
  - <a id="id9"></a>

    [控制器局域网（Controller Area Network，CAN）](#controller-area-network-can)
  - <a id="id10"></a>

    [计数器（Counter）](#counter)
  - <a id="id11"></a>

    [设备树（Devicetree）](#devicetree)
  - <a id="id12"></a>

    [显示（Display）](#display)
  - <a id="id13"></a>

    [直接存储器访问（DMA）](#dma)
  - <a id="id14"></a>

    [电可擦可编程只读存储器（EEPROM）](#eeprom)
  - <a id="id15"></a>

    [ESP32-S3](#esp32-s3)
  - <a id="id16"></a>

    [以太网（Ethernet）](#ethernet)
  - <a id="id17"></a>

    [文件系统（File System）](#file-system)
  - <a id="id18"></a>

    [通用输入输出（GPIO）](#gpio)
  - <a id="id19"></a>

    [英飞凌（Infineon）](#infineon)
  - <a id="id20"></a>

    [输入（Input）](#input)
  - <a id="id21"></a>

    [中断控制器（Interrupt Controller）](#interrupt-controller)
  - <a id="id22"></a>

    [键盘矩阵（Keyboard Matrix）](#keyboard-matrix)
  - <a id="id23"></a>

    [管理数据输入输出（MDIO）](#mdio)
  - <a id="id24"></a>

    [内存控制器（MEMC）](#memc)
  - <a id="id25"></a>

    [恩智浦（NXP）](#nxp)
  - <a id="id26"></a>

    [四线串行外设接口（QSPI）](#qspi)
  - <a id="id27"></a>

    [无线电（Radio）](#radio)
  - <a id="id28"></a>

    [SD主机控制器（SD Host Controller）](#sd-host-controller)
  - <a id="id29"></a>

    [命令行（Shell）](#shell)
  - <a id="id30"></a>

    [步进电机（Stepper）](#stepper)
  - <a id="id31"></a>

    [STM32](#stm32)
  - <a id="id32"></a>

    [定时器（Timer）](#timer)
  - <a id="id33"></a>

    [通用串行总线（USB）](#usb)
  - <a id="id34"></a>

    [USB Type-C接口（USB-C）](#usb-c)
  - <a id="id35"></a>

    [视频（Video）](#video)
  - <a id="id36"></a>

    [看门狗（Watchdog）](#watchdog)
- <a id="id37"></a>

  [蓝牙（Bluetooth）](#bluetooth)


  - <a id="id38"></a>

    [蓝牙主机（Bluetooth Host）](#bluetooth-host)
  - <a id="id39"></a>

    [蓝牙音频（Bluetooth Audio）](#bluetooth-audio)
  - <a id="id40"></a>

    [蓝牙网状网络（Bluetooth Mesh）](#bluetooth-mesh)
  - <a id="id41"></a>

    [蓝牙主机控制器接口（Bluetooth HCI）](#bluetooth-hci)
- <a id="id42"></a>

  [网络（Networking）](#networking)


  - <a id="id43"></a>

    [无线局域网（Wi-Fi）](#wi-fi)
  - <a id="id44"></a>

    [受限应用协议（CoAP）](#coap)
- <a id="id45"></a>

  [调制解调器（Modem）](#modem)


  - <a id="id46"></a>

    [HL78XX调制解调器（Modem）](#modem-hl78xx)
- <a id="id47"></a>

  [LoRa广域网（LoRaWAN）](#lorawan)
- <a id="id48"></a>

  [其他子系统（Other Subsystems）](#other-subsystems)


  - <a id="id49"></a>

    [字符帧缓冲区（CFB）](#cfb)
  - <a id="id50"></a>

    [闪存（Flash）](#flash)
  - <a id="id51"></a>

    [Flash映射（Flash Map）](#flash-map)
  - <a id="id52"></a>

    [JSON Web令牌（JWT）](#jwt)
  - <a id="id53"></a>

    [子带编码库（Libsbc）](#libsbc)
  - <a id="id54"></a>

    [管理（Management）](#management)
  - <a id="id55"></a>

    [随机数（Random）](#random)
  - <a id="id56"></a>

    [跟踪（Tracing）](#tracing)
  - <a id="id57"></a>

    [串行接口（Serial）](#serial)
  - <a id="id58"></a>

    [设置（Settings）](#settings)
- <a id="id59"></a>

  [模块（Modules）](#modules)


  - <a id="id60"></a>

    [接入点软件（HostAP）](#hostap)
  - <a id="id61"></a>

    [Mbed TLS密码与TLS库](#mbed-tls)
  - <a id="id62"></a>

    [OpenThread协议栈](#openthread)
  - <a id="id63"></a>

    [可信固件M（Trusted Firmware-M）](#trusted-firmware-m)
- <a id="id64"></a>

  [架构（Architectures）](#architectures)

<a id="common"></a>

## [通用部分（Common）](#id2)


- 最低要求的Zephyr SDK版本现在为1.0.0。
- 最低要求的Python版本由3.10提高到3.12。

<a id="build-system"></a>

## [构建系统（Build System）](#id3)


- Zephyr现在正式默认采用C17（ISO/IEC 9899:2018）作为最低C语言标准。若工具链不支持此标准，则需使用现有但已弃用的CONFIG_STD_C99或CONFIG_STD_C11选项。
- board.yml中新增开发板对应的board或boards条目，现在必须提供full_name属性。
- CMake变量BOARD_QUALIFIERS现在与[CONFIG_BOARD_QUALIFIERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QUALIFIERS)一致，不再带前导斜杠/。因此所有${BOARD}${BOARD_QUALIFIERS}用法必须明确补上斜杠，改为${BOARD}/${BOARD_QUALIFIERS}。
- SNIPPET_ROOT现在与其他Zephyr <type>_ROOT设置一致，默认不包含应用源码目录。需要将应用源码目录加入SNIPPET_ROOT的示例，应在zephyr/module.yml中添加snippet_root = <dir>条目，或手动将目录追加到CMake变量SNIPPET_ROOT。
- 应重新生成Shell自动补全文件（west completion），因为开发板目标自动补全现在支持开发板修订版本。

<a id="kernel"></a>

## [内核（Kernel）](#id4)


- 堆加固（Heap Hardening）通过构建期间生成的zephyr/heap_constants.h实现，kernel.h现在会包含此头文件。对作为CMake库构建的下游应用，这可能造成构建竞争：CMake可能在头文件生成前就开始构建该库。此时可能需要在CMake中增加add_dependencies(${lib} zephyr_generated_headers)，详见[GitHub #106439](https://github.com/zephyrproject-rtos/zephyr/issues/106439)。
- __pinned_*属性系列及CONFIG_LINKER_USE_PINNED_SECTION、CONFIG_LINKER_GENERIC_SECTIONS_PRESENT_AT_BOOT选项已移除（[GitHub #108773](https://github.com/zephyrproject-rtos/zephyr/issues/108773)）。内核镜像现在始终驻留在物理内存中；按需分页（Demand Paging）只适用于[k_mem_map()](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gacf5f9c43ac2c31c376fed4a19f607feb)创建的匿名映射，以及通过[CONFIG_LINKER_USE_ONDEMAND_SECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LINKER_USE_ONDEMAND_SECTION)放入__ondemand_*链接段的符号。

  以前采用默认可换出（Evictable-by-default）模型，任何未明确标记__pinned_*的内核页都可能被换出。该模型在结构上并不安全：某次构建是否能正常运行，取决于代码和数据相对缺页异常分派路径的偶然布局，而非任何保证。如果应用依赖旧模型，且在现有版本上工作正常，官方建议留在该版本，最好选择长期支持（LTS）版本。升级可能因新增代码、函数重排或新编译器而改变布局，使未标记的页进入缺页异常分派路径，并以难以诊断的方式破坏系统。正因存在这种潜在脆弱性，该模型被移除。选择升级的应用需要作以下修改：（[长期支持（Long Term Support）](../project_governance/P008_发布流程.md#release-process-lts)）


  - 从开发板默认配置（Defconfig）及prj.conf覆盖配置中，删除CONFIG_LINKER_USE_PINNED_SECTION=y和CONFIG_LINKER_GENERIC_SECTIONS_PRESENT_AT_BOOT=n。
  - 从源码中删除__pinned_func、__pinned_data、__pinned_rodata、__pinned_bss及__pinned_noinit属性。需要按需分页的代码必须改用__ondemand_func或__ondemand_rodata；贡献者负责确保缺页异常处理程序的执行路径不会访问这些符号。
  - 汇编中作为SECTION_FUNC()或SECTION_VAR()段名参数使用的PINNED_TEXT、PINNED_RODATA、PINNED_DATA、PINNED_BSS及PINNED_NOINIT，应分别替换为普通的TEXT、RODATA、DATA、BSS及NOINIT别名。
  - 将K_KERNEL_PINNED_STACK_DEFINE、K_KERNEL_PINNED_STACK_ARRAY_DEFINE、K_KERNEL_PINNED_STACK_ARRAY_DECLARE、K_THREAD_PINNED_STACK_DEFINE及K_THREAD_PINNED_STACK_ARRAY_DEFINE，分别替换为无PINNED的对应宏：K_KERNEL_STACK_DEFINE、K_KERNEL_STACK_ARRAY_DEFINE、K_KERNEL_STACK_ARRAY_DECLARE、K_THREAD_STACK_DEFINE及K_THREAD_STACK_ARRAY_DEFINE。
  - 树外开发板若在自定义链接脚本中使用了pinned_text、pinned_rodata、pinned_data、pinned_bss及pinned_noinit段，应将这些输入段匹配规则合并回普通的text、rodata、data、bss及noinit输出段。
  - 树外代码若依赖lnkr_pinned_*链接符号或lnkr_is_pinned()、lnkr_is_region_pinned()，必须移除相应引用。对应的app_smem_pinned*.ld包含文件，以及scripts/build/gen_app_partitions.py的--pinoutput、--pinpartitions选项，也已移除。

<a id="boards"></a>

## [开发板（Boards）](#id5)


- OpenOCD运行器（Runner）现在通过标准的--file及--file-type接口指定烧录文件，与JLink等其他运行器保持一致。变更如下：


  - --use-hex、--use-elf及--use-bin标志已弃用，改用--file-type：


    - --use-elf改为--file-type=elf。
    - --use-bin改为--file-type=bin。
    - --use-hex改为--file-type=hex；也可省略，因为hex是默认类型。
  - 现在支持通过--file指定自定义文件路径，用法类似JLink运行器。
  - 开发板CMake文件中的旧标志仍可工作，但会产生弃用警告。
  - 现在可单独使用--file-type而不指定--file，以选择构建产物类型hex、elf或bin。
- native_sim的主机FUSE访问现在默认使用libfuse v3，替代v2；仍可通过[CONFIG_FUSE_LIBRARY_VERSION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FUSE_LIBRARY_VERSION)选择版本。（[GitHub #104965](https://github.com/zephyrproject-rtos/zephyr/issues/104965)）
- m5stack_fire：移除未使用的UART2引脚控制（Pinctrl）条目，并将UART1引脚映射从GPIO32/GPIO33更新为GPIO16/GPIO17，以符合文档中Grove PORT.C的接线。
- Ai-Thinker的ai_m62_12f及ai_wb2_12f开发板，分别改名为ai_m62_12f_kit及ai_wb2_12f_kit。
- 编译定义XIP_EXTERNAL_FLASH、USE_HYPERRAM及XIP_BOOT_HEADER_XMCD_ENABLE仅由[boards/nxp/mimxrt1180_evk/xip/evkmimxrt1180_flexspi_nor_config.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1180_evk/xip/evkmimxrt1180_flexspi_nor_config.c)和[boards/nxp/mimxrt1170_evk/xmcd/xmcd.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/xmcd/xmcd.c)使用，因此现在将它们限制在相应开发板CMakeLists.txt的局部作用域。依赖这些定义全局可见的应用可能需要修改。（[GitHub #101322](https://github.com/zephyrproject-rtos/zephyr/issues/101322)）
- Renesas开发板目标ek_ra8t2/r7ka8t2lfecac/cm85改名为ek_ra8t2/r7ka8t2lflcac/cm85。
- NXP缩小了部分树内编译标志的作用域，使其仅在需要的位置可见。树外应用或开发板若依赖这些标志全局可见，可能需要在自己的CMakeLists.txt中添加相应定义，以保证继续正确构建。（[GitHub #100252](https://github.com/zephyrproject-rtos/zephyr/issues/100252)）受影响的标志如下：


  - 对RT10xx及RT11xx系列，BOARD_FLASH_SIZE原定义在boards/nxp/mimxrt10xx_evk/CMakeLists.txt及boards/nxp/mimxrt11xx_evk/CMakeLists.txt中，但只有HAL头文件fsl_flexspi_nor_boot.h使用它；该头文件由[soc/nxp/imxrt/imxrt10xx/soc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt10xx/soc.c)及[soc/nxp/imxrt/imxrt11xx/soc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/soc.c)包含。为避免与其他全局标志冲突，现在改为在SoC层的[soc/nxp/imxrt/imxrt10xx/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt10xx/CMakeLists.txt)及[soc/nxp/imxrt/imxrt11xx/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/nxp/imxrt/imxrt11xx/CMakeLists.txt)中，通过zephyr_library_compile_definitions()定义。此变更已应用到所有RTxxxx开发板。
  - 对RTxxx系列，原定义在boards/nxp/mimxrtxxx_evk/CMakeLists.txt中的BOARD_FLASH_SIZE在Zephyr源码树中未被使用，因此已从所有RTxxx开发板CMakeLists.txt中移除。
  - 对RTxxx系列，BOOT_HEADER_ENABLE原定义在boards/nxp/mimxrtxxx_evk/CMakeLists.txt中，由boards/nxp/rtxxx/<boot_header>.c使用，现在已改为Kconfig选项。因此，RTxxx开发板CMakeLists.txt中的zephyr_compile_definitions(BOOT_HEADER_ENABLE=1)已移除。
  - [boards/nxp/rd_rw612_bga/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/CMakeLists.txt)中的BOOT_HEADER_ENABLE编译标志定义已移除，因为Zephyr源码树中未使用它。
  - XIP_BOOT_HEADER_ENABLE及XIP_BOOT_HEADER_DCD_ENABLE原由boards/nxp/rt1xxx/<boot_header>.c使用。NXP RTxxxx评估板现在将它们改为Kconfig选项，通过Kconfig构建系统配置启动头（Boot Header），替代编译期定义。因此，RTxxxx开发板CMakeLists.txt中的zephyr_compile_definitions(XIP_BOOT_HEADER_ENABLE=1)及zephyr_compile_definitions(XIP_BOOT_HEADER_DCD_ENABLE=1)已移除。由于hal_nxp/rt10xx/fsl_flexspi_nor_boot.h及hal_nxp/rt11xx/fsl_flexspi_nor_boot.h仍需要这些宏，现在在对应SoC层CMakeLists.txt中使用zephyr_library_compile_definitions()添加，以限制作用域。
- 以下Nordic SoC Kconfig选项已弃用并替换；引用旧选项的Kconfig、CMake及代码需要更新：


  - [CONFIG_SOC_SERIES_NRF51X](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51X)替换为[CONFIG_SOC_SERIES_NRF51](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)。
  - [CONFIG_SOC_SERIES_NRF52X](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52X)替换为[CONFIG_SOC_SERIES_NRF52](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)。
  - [CONFIG_SOC_SERIES_NRF53X](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53X)替换为[CONFIG_SOC_SERIES_NRF53](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)。
  - [CONFIG_SOC_SERIES_NRF54HX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54HX)替换为[CONFIG_SOC_SERIES_NRF54H](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54H)。
  - [CONFIG_SOC_SERIES_NRF54LX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54LX)替换为[CONFIG_SOC_SERIES_NRF54L](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)。
  - [CONFIG_SOC_SERIES_NRF91X](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91X)替换为[CONFIG_SOC_SERIES_NRF91](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)。
  - [CONFIG_SOC_SERIES_NRF92X](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92X)替换为[CONFIG_SOC_SERIES_NRF92](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)。
- 以下SiFive Freedom SoC Kconfig选项已弃用并替换；引用旧选项的Kconfig、CMake及代码需要更新：


  - CONFIG_SOC_SERIES_SIFIVE_FREEDOM_FE300替换为CONFIG_SOC_SERIES_FE300。
  - CONFIG_SOC_SIFIVE_FREEDOM_FE310_G000替换为CONFIG_SOC_FE310_G000。
  - CONFIG_SOC_SIFIVE_FREEDOM_FE310_G002替换为CONFIG_SOC_FE310_G002。
  - CONFIG_SOC_SERIES_SIFIVE_FREEDOM_FU500替换为CONFIG_SOC_SERIES_FU500。
  - CONFIG_SOC_SIFIVE_FREEDOM_FU540替换为CONFIG_SOC_FU540。
  - CONFIG_SOC_SIFIVE_FREEDOM_FU540_E51替换为CONFIG_SOC_FU540_E51。
  - CONFIG_SOC_SIFIVE_FREEDOM_FU540_U54替换为CONFIG_SOC_FU540_U54。
  - CONFIG_SOC_SERIES_SIFIVE_FREEDOM_FU700替换为CONFIG_SOC_SERIES_FU700。
  - CONFIG_SOC_SIFIVE_FREEDOM_FU740替换为CONFIG_SOC_FU740。
  - CONFIG_SOC_SIFIVE_FREEDOM_FU740_S7替换为CONFIG_SOC_FU740_S7。
  - CONFIG_SOC_SIFIVE_FREEDOM_FU740_U74替换为CONFIG_SOC_FU740_U74。
- ITE的it515xx_evb改名为it51xxx_evb。
- 使用[CONFIG_USE_DT_CODE_PARTITION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_DT_CODE_PARTITION)或设置了zephyr,code-partition chosen节点的开发板，现在应改用[zephyr,mapped-partition](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)兼容项（Compatible）。该绑定利用设备树单元地址（Unit Address）获取分区的内存映射地址，无需手动逐级向父节点查找特定名称的节点再计算地址。使用[zephyr,mapped-partition](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)时，还禁止使用[CONFIG_FLASH_LOAD_OFFSET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_LOAD_OFFSET)及[CONFIG_FLASH_LOAD_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_LOAD_SIZE)，因为链接脚本已能直接求得非易失性存储器（NVM）的偏移及大小，无需由Kconfig进行中间计算。此外，内存映射设备改用[zephyr,mapped-partition](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)后，不再需要[fixed-subpartitions](../mtd_atmel_bouffalo_binding_reference/P013_fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions)；这些分区可直接相互嵌套，配合设备树ranges属性即可获得正确地址及偏移。尚未将zephyr,code-partition chosen设备更新到该绑定的开发板目标，会设置[CONFIG_FLASH_CODE_PARTITION_USING_FIXED_PARTITIONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_CODE_PARTITION_USING_FIXED_PARTITIONS)。以后将弃用将fixed-partitions作为zephyr,code-partition chosen节点的支持。（[`zephyr,mapped-partition`](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)）
- 基于STM32N6x SoC（CONFIG_SOC_SERIES_STM32N6X）的开发板或项目，若预期Zephyr应用在处理器安全状态（Secure State）下运行，现在必须明确启用[CONFIG_TRUSTED_EXECUTION_SECURE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRUSTED_EXECUTION_SECURE)；若预期在非安全状态（Non-secure State）下运行，则必须明确启用CONFIG_TRUSTED_EXECUTION_NON_SECURE。
- 以下WCH SoC Kconfig选项已改名；引用旧选项的Kconfig、CMake及代码需要更新：


  - CONFIG_SOC_SERIES_CH32V00X替换为CONFIG_SOC_SERIES_QINGKE_V2C。

<a id="device-drivers-and-devicetree"></a>

## [设备驱动与设备树（Device Drivers and Devicetree）](#id6)

<a id="adc"></a>

### [模数转换器（ADC）](#id7)


- renesas,ra-adc兼容项替换为[renesas,ra-adc12](../hardware/P868_RenesasRAADC12绑定.md#dtbinding-renesas-ra-adc12)。使用旧兼容项的应用必须更新设备树节点。
- 新增[renesas,ra-adc16](../hardware/P869_RenesasRAADC16绑定.md#dtbinding-renesas-ra-adc16)兼容项。EK-RA2A1开发板提供16位ADC分辨率，必须使用此兼容项。
- CONFIG_ADC_MCUX_SAR_ADC改名为[CONFIG_ADC_NXP_SAR_ADC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_NXP_SAR_ADC)。
- 驱动文件adc_mcux_sar_adc.c改名为[drivers/adc/adc_nxp_sar_adc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/adc_nxp_sar_adc.c)。
- 使用逐次逼近寄存器型ADC（SAR ADC）驱动的应用，必须更新设备树节点，添加zephyr,input-positive以指定硬件通道。对当前支持SAR ADC的SoC，参考电压应使用ADC_REF_VDD_1而非ADC_REF_INTERNAL；本次驱动更新也修正了此问题，用户须相应更新设备树属性值。（[GitHub #100978](https://github.com/zephyrproject-rtos/zephyr/issues/100978)）
- [st,stm32-adc](../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc)的resolutions属性已移除，改用st,adc-resolutions。对修订版Y的STM32H7器件，不再需要替换14位及12位分辨率值；若使用这些分辨率，功耗可能受影响。以前采用功耗优化值，现在采用标准值，精度更好但不以功耗优化为目标。其他系列不受影响。

<a id="clock-control"></a>

### [时钟控制（Clock Control）](#id8)


- bflb,bl60x-pll、bflb,bl61x-root-clk、bflb,bl60x-root-clk、bflb,bl61x-wifipll、bflb,bl70x-root-clk及bflb,bl61x-flash-clk已被[bflb,flash-clk](../clock_adi_atmel_bflb_binding_reference/P023_bflb_flash-clk.md#std-dtcompatible-bflb-flash-clk)、[bflb,pll](../clock_adi_atmel_bflb_binding_reference/P025_bflb_pll.md#std-dtcompatible-bflb-pll)及[bflb,root-clk](../clock_esp_infineon_microchip_binding_reference/P001_bflb_root-clk.md#std-dtcompatible-bflb-root-clk)取代。译注：原文列出六个旧名称和三个新名称，并使用respectively，但未给出逐项对应关系；此处保留两组名称，不推断映射。
- [infineon,peri-div](../clock_esp_infineon_microchip_binding_reference/P009_infineon_peri-div.md#std-dtcompatible-infineon-peri-div)时钟控制绑定已移除resource-type、resource-instance及resource-channel属性。驱动不再使用这些属性，内部数据结构中的对应字段也已移除。树外开发板若使用此兼容项，必须从设备树节点删除这些属性。（[GitHub #105393](https://github.com/zephyrproject-rtos/zephyr/issues/105393)）

<a id="controller-area-network-can"></a>

### [控制器局域网（Controller Area Network，CAN）](#id9)


- CONFIG_CAN_MAX_FILTER、CONFIG_CAN_MAX_STD_ID_FILTER及CONFIG_CAN_MAX_EXT_ID_FILTER已移除（[GitHub #100596](https://github.com/zephyrproject-rtos/zephyr/issues/100596)），改用以下驱动专用Kconfig符号。其中部分选项提高了默认值，以满足典型软件需求：


  - [zephyr,can-loopback](../hardware/P542_CAN回环绑定.md#dtbinding-zephyr-can-loopback)使用[CONFIG_CAN_LOOPBACK_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_LOOPBACK_MAX_FILTERS)。
  - [adi,max32-can](../can_adi_atmel_nxp_binding_reference/P001_adi_max32-can.md#std-dtcompatible-adi-max32-can)使用[CONFIG_CAN_MAX32_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MAX32_MAX_FILTERS)。
  - [microchip,mcp2515](../can_adi_atmel_nxp_binding_reference/P012_microchip_mcp2515.md#std-dtcompatible-microchip-mcp2515)使用[CONFIG_CAN_MCP2515_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MCP2515_MAX_FILTERS)。
  - [microchip,mcp251xfd](../can_adi_atmel_nxp_binding_reference/P013_microchip_mcp251xfd.md#std-dtcompatible-microchip-mcp251xfd)使用[CONFIG_CAN_MCP251XFD_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MCP251XFD_MAX_FILTERS)。
  - [nxp,flexcan](../can_adi_atmel_nxp_binding_reference/P017_nxp_flexcan.md#std-dtcompatible-nxp-flexcan)使用[CONFIG_CAN_MCUX_FLEXCAN_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MCUX_FLEXCAN_MAX_FILTERS)。
  - [zephyr,native-linux-can](../can_nxp_renesas_stm32_ti_binding_reference/P016_zephyr_native-linux-can.md#std-dtcompatible-zephyr-native-linux-can)使用[CONFIG_CAN_NATIVE_LINUX_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_NATIVE_LINUX_MAX_FILTERS)。
  - [renesas,rcar-can](../can_nxp_renesas_stm32_ti_binding_reference/P006_renesas_rcar-can.md#std-dtcompatible-renesas-rcar-can)使用[CONFIG_CAN_RCAR_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_RCAR_MAX_FILTERS)。
  - [kvaser,pcican](../can_adi_atmel_nxp_binding_reference/P011_kvaser_pcican.md#std-dtcompatible-kvaser-pcican)及[espressif,esp32-twai](../can_adi_atmel_nxp_binding_reference/P005_espressif_esp32-twai.md#std-dtcompatible-espressif-esp32-twai)使用[CONFIG_CAN_SJA1000_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_SJA1000_MAX_FILTERS)。
  - [st,stm32-bxcan](../can_nxp_renesas_stm32_ti_binding_reference/P011_st_stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan)使用[CONFIG_CAN_STM32_BXCAN_MAX_EXT_ID_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STM32_BXCAN_MAX_EXT_ID_FILTERS)。
  - [st,stm32-bxcan](../can_nxp_renesas_stm32_ti_binding_reference/P011_st_stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan)使用[CONFIG_CAN_STM32_BXCAN_MAX_STD_ID_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STM32_BXCAN_MAX_STD_ID_FILTERS)。
  - [st,stm32-fdcan](../can_nxp_renesas_stm32_ti_binding_reference/P012_st_stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan)使用[CONFIG_CAN_STM32_FDCAN_MAX_EXT_ID_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STM32_FDCAN_MAX_EXT_ID_FILTERS)。
  - [st,stm32-fdcan](../can_nxp_renesas_stm32_ti_binding_reference/P012_st_stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan)使用[CONFIG_CAN_STM32_FDCAN_MAX_STD_ID_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STM32_FDCAN_MAX_STD_ID_FILTERS)。
  - [infineon,xmc4xxx-can-node](../can_adi_atmel_nxp_binding_reference/P009_infineon_xmc4xxx-can-node.md#std-dtcompatible-infineon-xmc4xxx-can-node)使用[CONFIG_CAN_XMC4XXX_MAX_FILTERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_XMC4XXX_MAX_FILTERS)。
- [nxp,flexcan](../can_adi_atmel_nxp_binding_reference/P017_nxp_flexcan.md#std-dtcompatible-nxp-flexcan)及[nxp,flexcan-fd](../can_adi_atmel_nxp_binding_reference/P016_nxp_flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd)的CONFIG_CAN_MAX_MB选项已替换为按实例设置的number-of-mb设备树属性。（[GitHub #99483](https://github.com/zephyrproject-rtos/zephyr/issues/99483)）
- 若[nxp,flexcan](../can_adi_atmel_nxp_binding_reference/P017_nxp_flexcan.md#std-dtcompatible-nxp-flexcan)提供clk-source设备树属性，现在会据此在名为clksrc0及clksrc1的输入时钟间自动选择，作为CAN协议引擎时钟。
- NXP LPC系列MCAN驱动的CONFIG_CAN_MCUX_MCAN改名为[CONFIG_CAN_NXP_LPC_MCAN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_NXP_LPC_MCAN)，因为该驱动并非基于NXP MCUXpresso HAL。（[GitHub #103679](https://github.com/zephyrproject-rtos/zephyr/issues/103679)）
- [ti,tcan4x5x](../can_nxp_renesas_stm32_ti_binding_reference/P015_ti_tcan4x5x.md#std-dtcompatible-ti-tcan4x5x)新增ti,nwkrq-voltage-vio设备树属性，用于配置nWKRQ引脚的供电电压轨。为保留旧驱动默认使用VIO的行为，必须设置此属性。（[GitHub #104182](https://github.com/zephyrproject-rtos/zephyr/issues/104182)）

<a id="counter"></a>

### [计数器（Counter）](#id10)


- 实现get_value_64 API的驱动现在必须选择[CONFIG_COUNTER_SUPPORTS_64BITS_TICKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_SUPPORTS_64BITS_TICKS)，应用则需要[CONFIG_COUNTER_64BITS_TICKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_64BITS_TICKS)来启用该API。（[GitHub #94189](https://github.com/zephyrproject-rtos/zephyr/issues/94189)）
- NXP低功耗定时器LPTMR驱动（[nxp,lptmr](../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr)）已更新，修正预分频器（Prescaler）及毛刺滤波器（Glitch Filter）配置错误：


  - prescale-glitch-filter的有效范围由[0-16]改为[0-15]。数值16在脉冲计数模式中无效，因此已移除。使用16的设备树必须改为[0-15]范围内的值。
  - 新增布尔属性prescale-glitch-filter-bypass，明确控制预分频器或毛刺滤波器的旁路（Bypass）。以前设置prescale-glitch-filter = <0>会隐式启用旁路模式，含义不够明确。

    在v4.4及以后版本，是否旁路仅由是否存在prescale-glitch-filter-bypass决定。不存在此属性时，预分频器或毛刺滤波器有效，并应用prescale-glitch-filter的值。
  - 预分频器及毛刺滤波器的行为现已明确：


    - 时间计数模式（Time Counter）：预分频器将时钟除以2^(prescale-glitch-filter + 1)。
    - 脉冲计数模式（Pulse Counter）：毛刺滤波器在2^prescale-glitch-filter个上升沿后确认变化；毛刺滤波不支持取值0。
  - 所有树内设备树节点已将prescale-glitch-filter = <0>;更新为prescale-glitch-filter-bypass;。树外开发板也应相应更新。
  - 若同时设置prescale-glitch-filter-bypass及prescale-glitch-filter，旁路模式优先，prescale-glitch-filter的值被忽略。

  迁移示例（Migration Example）：

  ```text
  /* Old (deprecated) */
  lptmr0: counter@40040000 {
      compatible = "nxp,lptmr";
      /* Implicitly bypassed */
      prescale-glitch-filter = <0>;
  };

  /* New (correct) */
  lptmr0: counter@40040000 {
      compatible = "nxp,lptmr";
      /* Explicitly bypassed */
      prescale-glitch-filter-bypass;
  };
  ```

  prescale-glitch-filter使用示例

  注意（Note）

  prescale-glitch-filter-bypass是布尔属性：存在则启用旁路；不存在则禁用旁路，并应用prescale-glitch-filter。

  在脉冲计数模式中，prescale-glitch-filter = <0>不是受支持的毛刺滤波配置。如需不滤波，应使用prescale-glitch-filter-bypass;。


  - 时间计数模式：对计数器时钟分频

    时间计数模式下，预分频器的除数为2^(N + 1)。

    ```text
    /* Divide by 2^(0+1) = 2 */
    lptmr0: counter@40040000 {
        compatible = "nxp,lptmr";
        /* Time Counter mode */
        timer-mode-sel = <0>;
        clk-source = <1>;
        clock-frequency = <32768>;
        /* /2 */
        prescale-glitch-filter = <0>;
        resolution = <16>;
    };

    /* Divide by 2^(3+1) = 16 */
    lptmr1: counter@40041000 {
        compatible = "nxp,lptmr";
        /* Time Counter mode */
        timer-mode-sel = <0>;
        clk-source = <1>;
        clock-frequency = <32768>;
        /* /16 */
        prescale-glitch-filter = <3>;
        resolution = <16>;
    };
    ```
  - 时间计数模式：明确启用旁路，不分频

    ```text
    lptmr0: counter@40040000 {
        compatible = "nxp,lptmr";
        /* Time Counter mode */
        timer-mode-sel = <0>;
        clk-source = <1>;
        clock-frequency = <32768>;
        /* no prescaler */
        prescale-glitch-filter-bypass;
        resolution = <16>;
    };
    ```
  - 脉冲计数模式：毛刺滤波

    脉冲计数模式下，毛刺滤波器在2^N个上升沿后确认变化。毛刺滤波不支持数值0；若不需要滤波，应使用旁路。

    ```text
    /* Recognize change after 2^2 = 4 rising edges */
    lptmr0: counter@40040000 {
        compatible = "nxp,lptmr";
        /* Pulse Counter mode */
        timer-mode-sel = <1>;
        clk-source = <1>;
        input-pin = <0>;
        prescale-glitch-filter = <2>;
        resolution = <16>;
    };

    /* No filtering (explicit bypass) */
    lptmr1: counter@40041000 {
        compatible = "nxp,lptmr";
        /* Pulse Counter mode */
        timer-mode-sel = <1>;
        clk-source = <1>;
        input-pin = <0>;
        prescale-glitch-filter-bypass;
        resolution = <16>;
    };
    ```
- NXP i.MX通用定时器GPT计数器驱动（[nxp,imx-gpt](../nxp_nuvoton_counter_binding_reference/P004_nxp_imx-gpt.md#std-dtcompatible-nxp-imx-gpt)）现在默认使用run-mode = "restart"，替代以前硬编码的自由运行（Free-run）行为。


  - 旧行为，Zephyr ≤ 4.3：GPT计数器始终处于自由运行模式，即enableFreeRun = true；发生比较事件时不复位，继续计数。
  - 新行为，Zephyr ≥ 4.4：除非明确配置，否则GPT计数器默认使用重启模式（Restart）。新增run-mode设备树属性控制行为：


    - "restart"，默认：计数器达到比较通道1的值时复位为0。
    - "free-run"：计数器继续计数而不复位，即旧行为。

  必须进行的迁移：使用GPT计数器的树外开发板及应用，必须在设备树节点中添加run-mode = "free-run";才能保留旧行为。

  ```text
  /* Out-of-tree boards: add this to preserve previous behavior */
  gpt2: gpt@400f0000 {
      compatible = "nxp,imx-gpt";
      /* Explicitly restore Zephyr ≤4.3 behavior */
      run-mode = "free-run";
      /* ... other properties ... */
  };
  ```

  警告（Warning）

  驱动使用比较通道1实现Zephyr计数器闹钟（Alarm）功能。使用run-mode = "restart"时，设置闹钟将使计数器在闹钟比较点复位。若应用同时依赖闹钟及连续计数，必须使用run-mode = "free-run"。

  注意（Note）

  此变化统一了NXP计数器驱动的运行模式配置。GPT现在通过明确的设备树属性而非硬编码值设置，允许按实例定制。

<a id="devicetree"></a>

<a id="migration-4-4-devicetree"></a>

### [设备树（Devicetree）](#id11)


- 设备树绑定不再允许为status、#address-cells及#size-cells属性指定任何默认值。这些属性的语义由设备树规范（Devicetree [Specification](https://www.devicetree.org/specifications)）第2.3.4及2.3.5节定义，用户不应使用自定义默认值覆盖。（[设备树绑定（Devicetree Bindings）](../devicetree/P008_绑定概述.md#dt-bindings)；[Specification](https://www.devicetree.org/specifications)）

  以下绑定语法现在会导致构建错误：

  ```text
  properties:
    "status":
      default: ...             <---- any default is a build error
    "#address-cells":
      default: ...             <---- any default is a build error
    "#size-cells":
      default: ...             <---- any default is a build error
  ```

  若此前依赖绑定中的默认值，现在必须在设备树源码中明确指定这些值，以修复构建错误。
- 设备树兼容项[ilitek,ili9806e](../display_ilitek_matrix_nxp_binding_reference/P007_ilitek_ili9806e.md#std-dtcompatible-ilitek-ili9806e)-dsi已改名，请使用ilitek,ili9806e。

<a id="display"></a>

### [显示（Display）](#id12)


- 对ILI9XXX控制器，设备树中用于选择面板颜色格式的ILI9XXX_PIXEL_FORMAT_x已更新为PANEL_PIXEL_FORMAT_x。树外开发板及扩展板（Shield）应相应更新。（[GitHub #99267](https://github.com/zephyrproject-rtos/zephyr/issues/99267)）
- ILI9341控制器的显示镜像（Mirroring）配置已更新，以符合samples/drivers/display示例所描述的行为。（[GitHub #99267](https://github.com/zephyrproject-rtos/zephyr/issues/99267)）该变化会使部分显示面板出现镜像问题，官方说明将在v4.4.1中正确修复。（[GitHub #106862](https://github.com/zephyrproject-rtos/zephyr/issues/106862)）
- PIXEL_FORMAT_BGR_565及其设备树宏PANEL_PIXEL_FORMAT_BGR_565，分别改名为[PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca0d12a0b6fd3df29b0a607eedf7671809)及[PANEL_PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaf8271408694ee534466e7915309b6440)，以准确表明这是RGB-565的字节交换格式，而非红蓝通道交换格式。（[GitHub #99276](https://github.com/zephyrproject-rtos/zephyr/issues/99276)）使用PIXEL_FORMAT_BGR_565表示字节交换RGB-565的应用及库，必须改用[PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca0d12a0b6fd3df29b0a607eedf7671809)。
- CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_BGR_565及CONFIG_ST7789V_BGR565，分别改名为CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_RGB_565X及CONFIG_ST7789V_RGB565X。（[GitHub #99276](https://github.com/zephyrproject-rtos/zephyr/issues/99276)）
- CONFIG_SSD1327改名为[CONFIG_SSD1327_5](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSD1327_5)，以同时涵盖SSD1325。
- 设备树兼容项[solomon,ssd1327](../compatible_binding_reference/P067_solomon_ssd1327.md#std-dtcompatible-solomon-ssd1327)fb、[solomon,ssd1306](../compatible_binding_reference/P061_solomon_ssd1306.md#std-dtcompatible-solomon-ssd1306)fb及[solomon,ssd1309](../compatible_binding_reference/P063_solomon_ssd1309.md#std-dtcompatible-solomon-ssd1309)fb，分别改名为solomon,ssd1327、solomon,ssd1306及solomon,ssd1309，以与其他显示控制器统一，并移除与Zephyr无关的fb后缀。
- NXP eLCDIF控制器（[nxp,imx-elcdif](../display_ilitek_matrix_nxp_binding_reference/P018_nxp_imx-elcdif.md#std-dtcompatible-nxp-imx-elcdif)）现在正确报告支持PIXEL_FORMAT_XRGB_8888，而非PIXEL_FORMAT_ARGB_8888。
- waveshare,7inch-dsi-lcd-c兼容项替换为[waveshare,dsi2dpi](../display_st_ultrachip_zephyr_binding_reference/P010_waveshare_dsi2dpi.md#std-dtcompatible-waveshare-dsi2dpi)，CONFIG_WAVESHARE_7INCH_DSI_LCD_C选项替换为[CONFIG_WAVESHARE_DSI2DPI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WAVESHARE_DSI2DPI)。（[GitHub #100140](https://github.com/zephyrproject-rtos/zephyr/issues/100140)）
- 使用STM32 LTDC显示控制器的开发板，必须更新设备树，将[st,stm32-ltdc](../display_st_ultrachip_zephyr_binding_reference/P004_st_stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc)节点的pixel-format设置为[PANEL_PIXEL_FORMAT_RGB_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga4775abe39fd68a2d64b4edb649790915)。（[GitHub #99277](https://github.com/zephyrproject-rtos/zephyr/issues/99277)）

<a id="dma"></a>

### [直接存储器访问（DMA）](#id13)


- CONFIG_DMA_MCUX_EDMA_V5已移除（[GitHub #100341](https://github.com/zephyrproject-rtos/zephyr/issues/100341)）。该宏原用于区分nxp,version的5及4，现在两个版本统一维护。用户可将DMA_MCUX_EDMA_V5改为DMA_MCUX_EDMA_V4。

<a id="eeprom"></a>

### [电可擦可编程只读存储器（EEPROM）](#id14)


- I2C EEPROM目标设备驱动新增接受偏移及长度参数的[eeprom_target_read_data()](../hardware/P313_I2CEEPROM目标接口.md#ga1543dbc12e26df856eac01b1a686d7c5)和[eeprom_target_write_data()](../hardware/P313_I2CEEPROM目标接口.md#gad562c9ac13d3fa7a7b43c1d8ba415f11)，并弃用[eeprom_target_program()](../hardware/P313_I2CEEPROM目标接口.md#ga8c2d7c18fcec4ce2241850f031966a89)。
- [microchip,xec-eeprom](../mtd_microchip_nordic_nxp_binding_reference/P005_microchip_xec-eeprom.md#std-dtcompatible-microchip-xec-eeprom)的PCR及GIRQ属性已更新为使用新宏。（[GitHub #104591](https://github.com/zephyrproject-rtos/zephyr/issues/104591)）

<a id="esp32-s3"></a>

### [ESP32-S3](#id15)


- 原espressif,esp32-lcd-cam绑定已重构。LCD_CAM外设现在由公共lcd_cam节点表示，其功能块拆为两个子节点：

  > - [espressif,esp32-lcd-cam-dvp](../video_camera_endpoint_binding_reference/P003_espressif_esp32-lcd-cam-dvp.md#std-dtcompatible-espressif-esp32-lcd-cam-dvp)兼容节点表示数字视频端口DVP摄像头输入模块，标签为lcd_cam_dvp。
  > - [espressif,esp32-lcd-cam-mipi-dbi](../mipi_dbi_dsi_binding_reference/P002_espressif_esp32-lcd-cam-mipi-dbi.md#std-dtcompatible-espressif-esp32-lcd-cam-mipi-dbi)兼容节点表示LCD输出模块，标签为lcd_cam_disp。

  原[espressif,esp32-lcd-cam](../misc_adi_nordic_binding_reference/P007_espressif_esp32-lcd-cam.md#std-dtcompatible-espressif-esp32-lcd-cam)兼容节点保留公共引脚控制（Pinctrl）、时钟及中断属性；摄像头专用属性移到新的lcd_cam_dvp子节点。

  摄像头相关属性必须从lcd_cam节点移到新的lcd_cam_dvp子节点，zephyr,camera chosen属性也应改为指向lcd_cam_dvp。

<a id="ethernet"></a>

### [以太网（Ethernet）](#id16)


- 以下驱动新增通过[net_eth_mac_config](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html)配置MAC地址的支持：


  - [atmel,sam-gmac](../ethernet_mac_mdio_binding_reference/P004_atmel_sam-gmac.md#std-dtcompatible-atmel-sam-gmac)及[atmel,sam0-gmac](../ethernet_mac_mdio_binding_reference/P005_atmel_sam0-gmac.md#std-dtcompatible-atmel-sam0-gmac)。（[GitHub #96598](https://github.com/zephyrproject-rtos/zephyr/issues/96598)）


    - 移除CONFIG_ETH_SAM_GMAC_MAC_I2C_EEPROM。
    - 移除CONFIG_ETH_SAM_GMAC_MAC_I2C_INT_ADDRESS。
    - 移除CONFIG_ETH_SAM_GMAC_MAC_I2C_INT_ADDRESS_SIZE。
    - 移除mac-eeprom属性。
  - [litex,liteeth](../ethernet_mac_mdio_binding_reference/P013_litex_liteeth.md#std-dtcompatible-litex-liteeth)驱动（[GitHub #100620](https://github.com/zephyrproject-rtos/zephyr/issues/100620)）。
  - [microchip,lan865x](../ethernet_mdio_microchip_binding_reference/P017_microchip_lan865x.md#std-dtcompatible-microchip-lan865x)驱动（[GitHub #100318](https://github.com/zephyrproject-rtos/zephyr/issues/100318)）。
  - [microchip,lan9250](../ethernet_mdio_microchip_binding_reference/P018_microchip_lan9250.md#std-dtcompatible-microchip-lan9250)驱动（[GitHub #99127](https://github.com/zephyrproject-rtos/zephyr/issues/99127)）。
  - [nxp,enet-mac](../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac)驱动（[GitHub #102775](https://github.com/zephyrproject-rtos/zephyr/issues/102775)）。
  - [sensry,sy1xx-mac](../ethernet_phy_renesas_rockchip_binding_reference/P019_sensry_sy1xx-mac.md#std-dtcompatible-sensry-sy1xx-mac)驱动（[GitHub #100619](https://github.com/zephyrproject-rtos/zephyr/issues/100619)）。
  - [st,stm32n6-ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P013_st_stm32n6-ethernet.md#std-dtcompatible-st-stm32n6-ethernet)、[st,stm32h7-ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P011_st_stm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet)及[st,stm32-ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P009_st_stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet)。（[GitHub #102810](https://github.com/zephyrproject-rtos/zephyr/issues/102810)、[GitHub #105090](https://github.com/zephyrproject-rtos/zephyr/issues/105090)）
  - [virtio,net](../hardware/P587_VirtIO网络设备绑定.md#dtbinding-virtio-net)驱动（[GitHub #100106](https://github.com/zephyrproject-rtos/zephyr/issues/100106)）。
  - vnd,ethernet驱动（[GitHub #96598](https://github.com/zephyrproject-rtos/zephyr/issues/96598)）。
  - [wiznet,w5500](../ethernet_synopsys_st_xilinx_binding_reference/P018_wiznet_w5500.md#std-dtcompatible-wiznet-w5500)驱动（[GitHub #100919](https://github.com/zephyrproject-rtos/zephyr/issues/100919)）。
  - [snps,designware-ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P004_snps_designware-ethernet.md#std-dtcompatible-snps-designware-ethernet)驱动（[GitHub #105090](https://github.com/zephyrproject-rtos/zephyr/issues/105090)）。

  MAC地址现在应设置为nvmem-layout的子节点，参见[MAC地址配置（MAC Address Configuration）](../networking/P108_MAC地址配置.md#mac-address-config)文档。
- [ethernet-phy](../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy)的fixed-link属性已移除。若需要此功能，应改用新兼容项[ethernet-phy-fixed-link](../ethernet_nxp_phy_binding_reference/P018_ethernet-phy-fixed-link.md#std-dtcompatible-ethernet-phy-fixed-link)，并通过default-speeds属性指定固定链路参数。（[GitHub #100454](https://github.com/zephyrproject-rtos/zephyr/issues/100454)）
- [microchip,ksz8081](../ethernet_phy_renesas_rockchip_binding_reference/P001_microchip_ksz8081.md#std-dtcompatible-microchip-ksz8081)的reset-gpios属性已改为低有效，可能需要在设备树中将该引脚设置为GPIO_ACTIVE_LOW。（[GitHub #100751](https://github.com/zephyrproject-rtos/zephyr/issues/100751)）
- [CONFIG_ETH_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_INIT_PRIORITY)现在默认为60；[CONFIG_PHY_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PHY_INIT_PRIORITY)及[CONFIG_MDIO_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDIO_INIT_PRIORITY)默认取[CONFIG_ETH_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_INIT_PRIORITY)的值。启用[CONFIG_ETH_DRIVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DRIVER)时，[CONFIG_PTP_CLOCK_INIT_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK_INIT_PRIORITY)也采用同样的默认值。这样，优先级由设备树依赖关系决定。（[GitHub #104310](https://github.com/zephyrproject-rtos/zephyr/issues/104310)）
- 支持校验和卸载（Checksum Offloading）的驱动，现在必须选择新选项[CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)。要使用校验和卸载，还必须启用[CONFIG_NET_CHECKSUM_OFFLOAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD)；选中前者时，后者默认启用。（[GitHub #105051](https://github.com/zephyrproject-rtos/zephyr/issues/105051)）（[`CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CHECKSUM_OFFLOAD_SUPPORTED)）
- [microchip,lan865x](../ethernet_mdio_microchip_binding_reference/P017_microchip_lan865x.md#std-dtcompatible-microchip-lan865x)的phy-handle属性现在必须设置为指向PHY节点。
- CONFIG_NET_DSA_DEPRECATED已移除。microchip,ksz8463、microchip,ksz8794及microchip,ksz8863的驱动因尚未迁移到新的分布式交换架构（DSA）子系统，也已移除。（[GitHub #105926](https://github.com/zephyrproject-rtos/zephyr/issues/105926)）
- 通过ETHERNET_CONFIG_TYPE_MAC_ADDRESS更改MAC地址时，以太网驱动不再需要自行调用[net_if_set_link_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga3863e011f89dff02c3df3ca4a88680e9)。（[GitHub #105931](https://github.com/zephyrproject-rtos/zephyr/issues/105931)）

<a id="file-system"></a>

### [文件系统（File System）](#id17)


- 若设备树中存在已启用且带automount属性的[zephyr,fstab,fatfs](../storage_filesystem_binding_reference/P005_zephyr_fstab_fatfs.md#std-dtcompatible-zephyr-fstab-fatfs)节点，现在默认启用[CONFIG_FS_FATFS_FSTAB_AUTOMOUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FS_FATFS_FSTAB_AUTOMOUNT)。应用若不希望采用该行为，需明确禁用此选项。（[GitHub #103139](https://github.com/zephyrproject-rtos/zephyr/issues/103139)）
- NVS及ZMS已移到新的键值存储系统（Key-Value Storage Systems，KVSS）子系统，接口头文件路径从zephyr/fs/变为zephyr/kvss/。其Kconfig选项从“File Systems”菜单移到“Key-Value Storage Systems”菜单，选项本身不变。（[GitHub #103244](https://github.com/zephyrproject-rtos/zephyr/issues/103244)）

<a id="gpio"></a>

### [通用输入输出（GPIO）](#id18)


- LiteX GPIO驱动[litex,gpio](../gpio_infineon_intel_ite_microchip_binding_reference/P014_litex_gpio.md#std-dtcompatible-litex-gpio)已重构，支持改变方向。驱动现在通过reg-names属性检测GPIO控制器支持的模式；port-is-output设备树属性已移除，reg-names直接采用LiteX中的名称。（[GitHub #99329](https://github.com/zephyrproject-rtos/zephyr/issues/99329)）
- [renesas,rz-gpio](../gpio_raspberrypi_renesas_binding_reference/P025_renesas_rz-gpio.md#std-dtcompatible-renesas-rz-gpio)的irqs属性已重构，现在将引脚明确映射到中断phandle，而非中断索引。（[GitHub #101256](https://github.com/zephyrproject-rtos/zephyr/issues/101256)）

  ```text
  /* Old (Zephyr ≤ 4.3) */
  &gpio16 {
      /* Map port16 pin3 to tint7 */
      irqs = <3 7>;
  };

  /* New (Zephyr ≥ 4.4) */
  &tint7 {
      status = "okay";
  };

  &gpio16 {
      /* Map port16 pin3 to tint7 */
      irqs = <&tint7 3>;
  };
  ```

<a id="infineon"></a>

### [英飞凌（Infineon）](#id19)


- Infineon驱动文件名已移除cat1，以便在多个器件类别间复用。以下驱动已改名（[GitHub #99174](https://github.com/zephyrproject-rtos/zephyr/issues/99174)）：


  - adc_ifx_cat1.c改名为adc_ifx.c。
  - clock_control_ifx_cat1.c改名为clock_control_ifx.c。
  - counter_ifx_cat1.c改名为counter_ifx.c。
  - dma_ifx_cat1.c改名为dma_ifx.c。
  - dma_ifx_cat1_pdl.c改名为dma_ifx_pdl.c。
  - flash_ifx_cat1.c改名为flash_ifx.c。
  - flash_ifx_cat1_qspi.c改名为flash_ifx_qspi.c。
  - flash_ifx_cat1_qspi_mtb_hal.c改名为flash_ifx_qspi_mtb_hal.c。
  - gpio_ifx_cat1.c改名为gpio_ifx.c。
  - i2c_ifx_cat1.c改名为i2c_ifx.c。
  - i2c_ifx_cat1_pdl.c改名为i2c_ifx_pdl.c。
  - mbox_ifx_cat1.c改名为mbox_ifx.c。
  - pinctrl_ifx_cat1.c改名为pinctrl_ifx.c。
  - rtc_ifx_cat1.c改名为rtc_ifx.c。
  - ifx_cat1_sdio.c改名为ifx_sdio.c。
  - sdio_ifx_cat1_pdl.c改名为sdio_ifx_pdl.c。
  - serial_ifx_cat1_uart.c改名为serial_ifx_uart.c。
  - spi_ifx_cat1.c改名为spi_ifx.c。
  - spi_ifx_cat1_pdl.c改名为spi_ifx_pdl.c。
  - uart_ifx_cat1.c改名为uart_ifx.c。
  - uart_ifx_cat1_pdl.c改名为uart_ifx_pdl.c。
  - wdt_ifx_cat1.c改名为wdt_ifx.c。

  对应Kconfig符号及绑定文件也已更新：


  - CONFIG_*_INFINEON_CAT1改为CONFIG_*_INFINEON。
  - compatible: "infineon,cat1-adc"改为compatible: "infineon,adc"。
- Infineon蓝牙HCI UART驱动[CONFIG_BT_HCI_UART_INFINEON](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_UART_INFINEON)，兼容项为[infineon,bt-hci-uart](../bluetooth_vendor_hci_binding_reference/P006_infineon_bt-hci-uart.md#std-dtcompatible-infineon-bt-hci-uart)，现在明确限定用于采用HCI UART传输的AIROC连接芯片。（[GitHub #103871](https://github.com/zephyrproject-rtos/zephyr/issues/103871)）

  对应Kconfig符号及设备树兼容项也已更新：


  - CONFIG_BT_CYW43XX改为CONFIG_BT_HCI_UART_INFINEON。译注：原网页此处残留未渲染的:kconfig:option:标记，选项名称按原文保留。
  - dtcompatible: "infineon,cyw43xxx-bt-hci"改为dtcompatible: "infineon,bt-hci-uart"。

<a id="input"></a>

### [输入（Input）](#id20)


- CST816S输入驱动已通用化，以支持CST8xx系列。驱动及Kconfig文件已改名（[GitHub #105348](https://github.com/zephyrproject-rtos/zephyr/issues/105348)）：


  - input_cst816s.c改名为input_cst8xx.c。
  - Kconfig.cst816s改名为Kconfig.cst8xx。

  对应设备树兼容项已更新：


  - hynitron,cst816s改名为[hynitron,cst8xx](../input_adc_touch_matrix_binding_reference/P020_hynitron_cst8xx.md#std-dtcompatible-hynitron-cst8xx)。

  对应Kconfig选项也已更新：


  - CONFIG_INPUT_CST816S改为CONFIG_INPUT_CST8XX。
  - CONFIG_INPUT_CST816S_PERIOD改为CONFIG_INPUT_CST8XX_PERIOD。
  - CONFIG_INPUT_CST816S_INTERRUPT改为CONFIG_INPUT_CST8XX_INTERRUPT。
  - CONFIG_INPUT_CST816S_EV_DEVICE改为CONFIG_INPUT_CST8XX_EV_DEVICE。

  设备树绑定宏前缀也已从CST816S_*更新为CST8XX_*。

<a id="interrupt-controller"></a>

### [中断控制器（Interrupt Controller）](#id21)


- [swerv,pic](../riscv_interrupt_binding_reference/P008_swerv_pic.md#std-dtcompatible-swerv-pic)添加厂商前缀，改名为[cdns,swerv-pic](../riscv_interrupt_binding_reference/P009_cdns_swerv-pic.md#std-dtcompatible-cdns-swerv-pic)。

<a id="keyboard-matrix"></a>

### [键盘矩阵（Keyboard Matrix）](#id22)


- 通用键盘矩阵（Keyboard Matrix）设备树绑定的轮询周期属性，现在使用微秒单位，替代毫秒。

  以下属性已改名，并更改单位：


  - poll-period-ms改为poll-period-us。
  - stable-poll-period-ms改为stable-poll-period-us。

  使用这些属性的应用必须：


  - 将旧属性名替换为新属性名；并且
  - 将数值从毫秒换算为微秒。例如，原先表示10 ms的数值10，现在必须写为10000，以表示10,000 µs。

<a id="mdio"></a>

### [管理数据输入输出（MDIO）](#id23)


- mdio_bus_enable()及mdio_bus_disable()函数已移除。MDIO总线的启用及禁用现在由MDIO驱动内部处理。（[GitHub #99690](https://github.com/zephyrproject-rtos/zephyr/issues/99690)）
- MDIO驱动已并入以太网驱动领域：驱动从drivers/mdio/移到[drivers/ethernet/mdio/](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/mdio/)，设备树绑定从dts/bindings/mdio/移到[dts/bindings/ethernet/mdio/](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/ethernet/mdio/)。（[GitHub #103944](https://github.com/zephyrproject-rtos/zephyr/issues/103944)）

<a id="memc"></a>

### [内存控制器（MEMC）](#id24)


- [st,stm32-xspi-psram](../memory_controller_sdram_psram_binding_reference/P015_st_stm32-xspi-psram.md#std-dtcompatible-st-stm32-xspi-psram)及[st,stm32-ospi-psram](../memory_controller_sdram_psram_binding_reference/P014_st_stm32-ospi-psram.md#std-dtcompatible-st-stm32-ospi-psram)兼容节点现在必须提供st,refresh属性，以存储器时钟周期数指定伪静态RAM（PSRAM）的刷新周期。（[GitHub #102735](https://github.com/zephyrproject-rtos/zephyr/issues/102735)）驱动中原先硬编码的默认值320（XSPI）及129（OSPI）已移除。（[`st,stm32-xspi-psram`](../memory_controller_sdram_psram_binding_reference/P015_st_stm32-xspi-psram.md#std-dtcompatible-st-stm32-xspi-psram)；[`st,stm32-ospi-psram`](../memory_controller_sdram_psram_binding_reference/P014_st_stm32-ospi-psram.md#std-dtcompatible-st-stm32-ospi-psram)）

<a id="nxp"></a>

### [恩智浦（NXP）](#id25)


- NXP DTSI文件已移到dts/arm/nxp下按系列划分的子目录，以提高可维护性及可查找性，并匹配soc/nxp的结构。对已移动的文件，必须更新设备树包含路径：将#include <nxp/nxp_*.dtsi>形式改为正确的系列子目录。（[GitHub #101243](https://github.com/zephyrproject-rtos/zephyr/issues/101243)）

  示例（Example）：

  ```text
  /* Before */
  #include <nxp/nxp_rt1060.dtsi>

  /* After */
  #include <nxp/imxrt/nxp_rt1060.dtsi>
  ```

  此变化只适用于从dts/arm/nxp移动的NXP ARM SoC包含文件。不要修改位于其他位置的DTSI包含路径，例如dts/arm64/nxp下的文件。

  可搜索旧的包含路径前缀，定位受影响的引用：

  ```text
  git grep "#include <nxp/nxp_" -- '*.dtsi' '*.dts' '*.overlay'
  ```
- 作为系统定时器的[nxp,lptmr](../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr)节点，现在必须通过zephyr,system-timer chosen属性指定。i.MX95及MCX-W SoC已在SoC DTSI中设置，相关开发板无需修改。其他所有使用[CONFIG_MCUX_LPTMR_TIMER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_LPTMR_TIMER)的开发板都必须添加设备树覆盖文件（Overlay）：

  ```text
  / {
      chosen {
          zephyr,system-timer = &lptmr0;
      };
  };
  ```

  Kinetis KE1xF在启用[CONFIG_PM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)时，也必须添加该覆盖配置。
- [nxp,imx-flexspi-nor](../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor)兼容节点现在具有[soc-nv-flash](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash)子节点，用于描述Flash存储器。nxp,imx-flexspi-nor节点作为Flash控制器，重命名为flash-controller@0；erase-block-size、write-block-size属性及partitions节点移入Flash芯片节点。树外开发板必须相应更新设备树。
- zephyr,flash chosen属性必须指向[soc-nv-flash](../mtd_nxp_st_ti_partition_binding_reference/P013_soc-nv-flash.md#std-dtcompatible-soc-nv-flash)兼容节点。


  - zephyr,flash-controller chosen属性必须指向[nxp,imx-flexspi-nor](../mtd_microchip_nordic_nxp_binding_reference/P023_nxp_imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor)兼容节点。
  - 控制器节点必须提供ranges属性。

<a id="qspi"></a>

### [四线串行外设接口（QSPI）](#id26)


- 配置了dual-flash的[st,stm32-qspi](../qspi_ospi_xspi_binding_reference/P011_st_stm32-qspi.md#std-dtcompatible-st-stm32-qspi)兼容节点，现在还必须添加ssht-enable才能重新启用采样移位（Sample Shifting）。采样移位现在可配置，且默认禁用。（[GitHub #98999](https://github.com/zephyrproject-rtos/zephyr/issues/98999)）

<a id="radio"></a>

### [无线电（Radio）](#id27)


- 以下设备树绑定已改名，以统一采用radio-前缀：


  - generic-fem-two-ctrl-pins改名为[radio-fem-two-ctrl-pins](../network_radio_frontend_binding_reference/P012_radio-fem-two-ctrl-pins.md#std-dtcompatible-radio-fem-two-ctrl-pins)。
  - gpio-radio-coex改名为[radio-gpio-coex](../network_radio_frontend_binding_reference/P013_radio-gpio-coex.md#std-dtcompatible-radio-gpio-coex)。
- 新增radio.yaml基础绑定，用于通用无线电硬件能力。为保持一致，tx-high-power-supported属性改名为radio-tx-high-power-supported。
- 使用旧兼容字符串的设备树及覆盖文件必须更新为新名称。

<a id="sd-host-controller"></a>

### [SD主机控制器（SD Host Controller）](#id28)


- 根据[SD主机控制器规范（SD Host Controller Specification）](https://www.sdcard.org/downloads/pls/pdf/?p=PartA2_SD%20Host_Controller_Simplified_Specification_Ver4.20.jpg)，附加字段bus_4_bit_support、hs200_support及hs400_support从[sdhc_host_caps](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__host__caps.html)移到[sdhc_host_props](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__host__props.html)。（[GitHub #91701](https://github.com/zephyrproject-rtos/zephyr/issues/91701)）

<a id="shell"></a>

### [命令行（Shell）](#id29)


- [shell_set_bypass()](../shell_core_reference/P001_Shell核心接口.md#ga4d51d4dbb22bed5d040deabc7ab6dc9d)现在要求传入用户数据指针，[shell_bypass_cb_t](../shell_core_reference/P001_Shell核心接口.md#gacaddbcd6e84f377f39a5d69398996557)也相应增加用户数据参数。（[GitHub #100311](https://github.com/zephyrproject-rtos/zephyr/issues/100311)）

<a id="stepper"></a>

### [步进电机（Stepper）](#id30)


- [adi,tmc2209](../stepper_binding_reference/P001_adi_tmc2209.md#std-dtcompatible-adi-tmc2209)的msx-gpios属性现在替换为m0-gpios及m1-gpios，以与其他步进／方向（Step/Dir）步进电机驱动保持一致。
- 若干API函数已改名：


  - stepper_move_by改名为[stepper_ctrl_move_by()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaa968ec0a373206d239ac96abc20ee9ea)。
  - stepper_move_to改名为[stepper_ctrl_move_to()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gac264384ffdd5c4eca154ddf941abf8a5)。
  - stepper_is_moving改名为[stepper_ctrl_is_moving()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae78e47cb34035887cf4e8c6a7c6de9de)。
  - stepper_run改名为[stepper_ctrl_run()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga544a15b5df405c08127fa8529cfbcf0b)。
  - stepper_stop改名为[stepper_ctrl_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga780784ec0b192e68849627ff97116c78)。
  - stepper_set_reference_position改名为[stepper_ctrl_set_reference_position()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae723aee1b73b3b65d8ead0546b976cd0)。
  - stepper_get_actual_position改名为[stepper_ctrl_get_actual_position()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gaf2c33e8fcf6cd03dfb9361c0246281fb)。
  - stepper_set_microstep_interval改名为[stepper_ctrl_set_microstep_interval()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga1cb888e11712c54bd879a5b0015ea298)。
- 以下事件从[stepper_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab1534238fbf8d2270ea4f69d3a558b5f)移到[stepper_ctrl_event](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#ga61dfffaeb3d7f76c34c9a9e3ab7627d0)：


  - STEPPER_EVENT_STEPS_COMPLETED改名为STEPPER_CTRL_EVENT_STEPS_COMPLETED。
  - STEPPER_EVENT_LEFT_END_STOP_DETECTED改为STEPPER_CTRL_EVENT_LEFT_END_STOP_DETECTED。译注：原网页名称末尾多出的反引号属于排版残留。
  - STEPPER_EVENT_RIGHT_END_STOP_DETECTED改名为STEPPER_CTRL_EVENT_RIGHT_END_STOP_DETECTED。
  - STEPPER_EVENT_STOPPED改名为STEPPER_CTRL_EVENT_STOPPED。
- 所有步进／方向硬件驱动设备绑定，即[adi,tmc2209](../stepper_binding_reference/P001_adi_tmc2209.md#std-dtcompatible-adi-tmc2209)、[ti,drv84xx](../stepper_binding_reference/P013_ti_drv84xx.md#std-dtcompatible-ti-drv84xx)及[allegro,a4979](../stepper_binding_reference/P012_allegro_a4979.md#std-dtcompatible-allegro-a4979)，均移除step-gpios、dir-gpios、invert-direction及counter属性。这些属性移到新的通用步进运动控制器绑定[zephyr,gpio-step-dir-stepper-ctrl](../stepper_binding_reference/P014_zephyr_gpio-step-dir-stepper-ctrl.md#std-dtcompatible-zephyr-gpio-step-dir-stepper-ctrl)中。
- 运动控制现在必须通过[zephyr,gpio-step-dir-stepper-ctrl](../stepper_binding_reference/P014_zephyr_gpio-step-dir-stepper-ctrl.md#std-dtcompatible-zephyr-gpio-step-dir-stepper-ctrl)设备执行，该设备用stepper-driver属性引用步进电机硬件驱动节点。应用必须更新设备树，添加运动控制器节点，并使用stepper_ctrl_* API，替代直接对硬件驱动设备调用运动控制函数。
- H桥步进电机控制器（H-bridge Stepper Controller）已移除硬件驱动专用API：


  - zephyr,h-bridge-stepper改名为[zephyr,h-bridge-stepper-ctrl](../stepper_binding_reference/P015_zephyr_h-bridge-stepper-ctrl.md#std-dtcompatible-zephyr-h-bridge-stepper-ctrl)，明确它是运动控制器绑定，而非硬件驱动绑定。
  - [stepper_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga3395b5f8b401d8175067edfb25c2e0e8)、[stepper_disable()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gab892a6b8d8fb34db0e682dd8f7de4218)、[stepper_set_micro_step_res()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#ga609ddefa299ba40a997c626e4a36bdef)及[stepper_get_micro_step_res()](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__hw__driver.html#gaa5e17e04a470832a305cef048694ec0a)，不再适用于[zephyr,h-bridge-stepper-ctrl](../stepper_binding_reference/P015_zephyr_h-bridge-stepper-ctrl.md#std-dtcompatible-zephyr-h-bridge-stepper-ctrl)兼容设备。
  - [zephyr,h-bridge-stepper-ctrl](../stepper_binding_reference/P015_zephyr_h-bridge-stepper-ctrl.md#std-dtcompatible-zephyr-h-bridge-stepper-ctrl)的en-gpios属性已移除。
  - [zephyr,h-bridge-stepper-ctrl](../stepper_binding_reference/P015_zephyr_h-bridge-stepper-ctrl.md#std-dtcompatible-zephyr-h-bridge-stepper-ctrl)的micro-step-res替换为lut-step-gap，以更准确反映H桥控制机制：该机制使用查找表（Lookup Table）插值，而非硬件微步进。

  使用H桥步进电机控制器的应用必须：


  1. 移除对H桥控制器设备调用硬件驱动专用API的代码。
  2. 更新设备树，使用lut-step-gap替代micro-step-res。
  3. 若存在en-gpios属性，将其移除。
- [adi,tmc50xx](../stepper_binding_reference/P004_adi_tmc50xx.md#std-dtcompatible-adi-tmc50xx)及[adi,tmc51xx](../compatible_binding_reference/P008_adi_tmc51xx.md#std-dtcompatible-adi-tmc51xx)设备现在建模为多功能设备（Multi-function Device，MFD）。
- 用于生成CONFIG_STEPPER_*_GENERATE_ISR_SAFE_EVENTS及CONFIG_STEPPER_*_EVENT_QUEUE_LEN符号的Kconfig.stepper_event_template模板已移除。
- CONFIG_STEPPER_STEP_DIR_GENERATE_ISR_SAFE_EVENTS替换为[CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS)。
- CONFIG_STEPPER_STEP_DIR_EVENT_QUEUE_LEN替换为[CONFIG_STEPPER_CTRL_EVENT_QUEUE_LEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STEPPER_CTRL_EVENT_QUEUE_LEN)。
- [CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STEPPER_CTRL_ISR_SAFE_EVENTS)现在默认启用。

<a id="stm32"></a>

### [STM32](#id31)


- STM32供电配置现在通过设备树属性完成。新增[st,stm32h7-pwr](../stm32_soc_power_binding_reference/P014_st_stm32h7-pwr.md#std-dtcompatible-st-stm32h7-pwr)、[st,stm32h7rs-pwr](../stm32_soc_power_binding_reference/P015_st_stm32h7rs-pwr.md#std-dtcompatible-st-stm32h7rs-pwr)及[st,stm32-dualreg-pwr](../stm32_soc_power_binding_reference/P007_st_stm32-dualreg-pwr.md#std-dtcompatible-st-stm32-dualreg-pwr)绑定，所有与供电配置有关的Kconfig符号已移除：


  - `CONFIG_POWER_SUPPLY_LDO`
  - CONFIG_POWER_SUPPLY_DIRECT_SMPS,
  - `CONFIG_POWER_SUPPLY_SMPS_1V8_SUPPLIES_LDO`
  - CONFIG_POWER_SUPPLY_SMPS_2V5_SUPPLIES_LDO,
  - `CONFIG_POWER_SUPPLY_SMPS_1V8_SUPPLIES_EXT_AND_LDO`
  - `CONFIG_POWER_SUPPLY_SMPS_2V5_SUPPLIES_EXT_AND_LDO`
  - `CONFIG_POWER_SUPPLY_SMPS_1V8_SUPPLIES_EXT`
  - `CONFIG_POWER_SUPPLY_SMPS_2V5_SUPPLIES_EXT`
  - `CONFIG_POWER_SUPPLY_EXTERNAL_SOURCE`
- ST专用chosen属性/chosen/zephyr,ccm替换为/chosen/zephyr,dtcm。属性宏__ccm_data_section、__ccm_bss_section及__ccm_noinit_section已弃用，为向后兼容暂时保留，计划在Zephyr 4.5移除。应改用通用的__dtcm_{data,bss,noinit}_section宏。（[GitHub #100590](https://github.com/zephyrproject-rtos/zephyr/issues/100590)）
- STM32平台现在使用MCUboot默认的偏移交换模式（Swap Using Offset），即[SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET)。为支持此启动加载器模式，需要修改开发板设备树。部分开发板已支持，见[GitHub #100385](https://github.com/zephyrproject-rtos/zephyr/issues/100385)。仍可在sysbuild中启用[SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE)，选择原来的移动交换模式。
- STM32F2x/F4x/F7x的多个PLL绑定st,stm32f2-pll-clock、st,stm32f4-pll-clock、st,stm32f4-plli2s-clock、st,stm32f411-plli2s-clock、st,stm32f7-pll-clock及st,stm32fx-pllsai-clock，现已合并为[st,stm32fx-pll-clock](../timer_reference/P128_STM32Fx锁相环时钟绑定.md#dtbinding-st-stm32fx-pll-clock)。合并带来若干变化，尤其是div-divq及div-divr分别改名为post-div-q及post-div-r。此外，若SoC适用这些属性，使用对应div-q或div-r时还必须定义它们。
- 对STM32L4x，st,stm32l4-pllsai-clock绑定替换为已有的[st,stm32l4-pll-clock](../timer_reference/P148_STM32L4锁相环时钟绑定.md#dtbinding-st-stm32l4-pll-clock)，div-divr属性随之改名为post-div-r。
- STM32平台的[drivers/ethernet/eth_stm32_hal_common.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_stm32_hal_common.c)现在在MAC设备树节点使用以下任一属性时，通过[net_eth_mac_config](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html)生成MAC地址：

  > - zephyr,random-mac-address，记为(a)。
  > - local-mac-address，记为(b)。
  > - nvmem-cells，记为(c)，新增。

  此变化破坏了使用(a)或(b)的实现的向后兼容性。旧实现将ST组织唯一标识符（OUI）用于MAC地址的高3字节，低3字节则随机生成(a)或明确指定(b)。现在(a)生成完整随机地址，(b)则由设备树完整或部分指定地址。

  新实现(c)允许引用保存在非易失性存储器中的MAC地址，例如STM32N6x平台由BSEC外设管理的一次性可编程（OTP）熔丝。详见[net_eth_mac_load()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0)。

  若MAC节点未指定上述任何属性，则沿用旧实现。（[GitHub #102810](https://github.com/zephyrproject-rtos/zephyr/issues/102810)）

  注意（Note）

  此变化使STM32平台与Zephyr通用行为一致。官方说明旧实现尚不适合直接用于产品，因此预计不会造成太大影响。
- CONFIG_SPI_STM32_USE_HW_SS已移除。SPI运行模式现在根据设备树配置自动选择：具有cs-gpios或新属性st,soft-nss的实例采用软件NSS（Soft NSS）模式，其余实例采用硬件NSS（Hard NSS）模式。
- 为保证SPI在任意频率下都能工作，所有SPI引脚现在默认采用非常高速度的转换速率（Slew Rate）。这可能增加功耗；可在开发板DTS或覆盖文件中将slew-rate设为较低速度，以降低功耗。
- [CONFIG_NUM_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)现在通过新的Kconfig预处理函数dt_highest_controller_irq_number，根据已启用的设备，即status = "okay";自动计算。使用[IRQ_CONNECT()](../fatal_irq_reference/P007_中断服务接口.md#ga131739d1faf501a15590053817aba984)注册自定义中断服务程序（ISR）的应用，可能因[CONFIG_NUM_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)变小而出现如下构建失败：

  ```text
  gen_isr_tables.py: error: IRQ 114 (offset=0) exceeds the maximum of 106
  ```

  明确将[CONFIG_NUM_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)设置为适当值即可解决；[以下文档页](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#setting-configuration-values)说明具体方法。

<a id="timer"></a>

### [定时器（Timer）](#id32)


- 树外SoC或平台代码若通过z_cms_lptim_hook_on_lpm_entry及z_cms_lptim_hook_on_lpm_exit兼容宏实现旧式Cortex-M SysTick低功耗辅助接口，应迁移到[include/zephyr/drivers/timer/system_timer_lpm.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/timer/system_timer_lpm.h)中的z_sys_clock_lpm_enter()及z_sys_clock_lpm_exit()。[drivers/timer/cortex_m_systick.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/cortex_m_systick.h)中的兼容层在Zephyr 4.4.0弃用，当前计划在4.6.0移除。旧选项[CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE)、[CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER)、[CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS)及[CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM)也已弃用，分别迁移到[CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE)、[CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER)、[CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS)及[CONFIG_SYSTEM_TIMER_RESET_BY_LPM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_RESET_BY_LPM)。chosen属性/chosen/zephyr,cortex-m-idle-timer已弃用，改用/chosen/zephyr,system-timer-companion。
- [renesas,rza2m-ostm](../renesas_timer_binding_reference/P012_renesas_rza2m-ostm.md#std-dtcompatible-renesas-rza2m-ostm)改名为[renesas,rza2m-ostm-timer](../renesas_timer_binding_reference/P011_renesas_rza2m-ostm-timer.md#std-dtcompatible-renesas-rza2m-ostm-timer)，DT_HAS_RENESAS_RZA2M_OSTM_ENABLED替换为DT_HAS_RENESAS_RZA2M_OSTM_TIMER_ENABLED。（[GitHub #100934](https://github.com/zephyrproject-rtos/zephyr/issues/100934)）

<a id="usb"></a>

### [通用串行总线（USB）](#id33)


- maxim,max3421e_spi改名为[maxim,max3421e-spi](../usb_controller_binding_reference/P016_maxim_max3421e-spi.md#std-dtcompatible-maxim-max3421e-spi)。
- USB控制传输缓冲区分配已从USB设备控制器（UDC）移到USB device_next。树外UDC驱动必须重构。（[GitHub #103493](https://github.com/zephyrproject-rtos/zephyr/issues/103493)）
- USB视频类（UVC）设备应用API已修改：


  - uvc_set_video_dev改名为[uvc_device_init()](../usb/P122_USB视频设备API.md#ga9c84595e78a2294f1470056199c074ae)。
  - uvc_add_format改名为[uvc_device_add_format()](../usb/P122_USB视频设备API.md#gacdfc08f59e0032e68b838f5893edbda1)。
  - 新增[uvc_device_enable()](../usb/P122_USB视频设备API.md#gaec4b7ac54a524724bb29751fd1cafafe)。
  - 新增[uvc_device_shutdown()](../usb/P122_USB视频设备API.md#gad6415b544866cfa15efac2a53c760f2a)。

<a id="usb-c"></a>

### [USB Type-C接口（USB-C）](#id34)


- [tcpc_driver_api](https://docs.zephyrproject.org/latest/doxygen/html/structtcpc__driver__api.html)中的alert_handler_cb字段已移除，因为它未被使用，且与通过[tcpc_set_alert_handler_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga75f0dc246dac576f14c5ac51b45fd489)注册的回调重复。

<a id="video"></a>

### [视频（Video）](#id35)


- CONFIG_VIDEO_HIMAX_HM01B0改名为[CONFIG_VIDEO_HM01B0](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_HM01B0)。
- CONFIG_VIDEO_OV7670已移除，替换为[CONFIG_VIDEO_OV767X](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_OV767X)，以同时支持OV7670及0V7675。译注：原文后一个型号首字符写作数字0，此处保留。
- CONFIG_VIDEO_BUFFER_POOL_SZ_MAX替换为[CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE)，表示为整个视频缓冲池分配的字节数。
- [ovti,ov2640](../video_camera_endpoint_binding_reference/P013_ovti_ov2640.md#std-dtcompatible-ovti-ov2640)的复位引脚处理已修正，有效电平与此前相反，以匹配传感器要求的有效电平。
- 以下像素格式已改名，以与数据保持一致。译注：原网页的GitHub引用标记损坏，编号为105522。


  - [VIDEO_PIX_FMT_ARGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5cd54fb54967a80576082cadd5941670)，与[VIDEO_PIX_FMT_BGRA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga515e379bc7f59a8062f3e2a5980b0626)互换。
  - [VIDEO_PIX_FMT_BGRA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga515e379bc7f59a8062f3e2a5980b0626)，与[VIDEO_PIX_FMT_ARGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5cd54fb54967a80576082cadd5941670)互换。
  - [VIDEO_PIX_FMT_RGBA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8ee1e3b82eeeb02188157aa4b4b5d842)，保持不变。
  - [VIDEO_PIX_FMT_ABGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaffb650a5f9b2b03890283ecfe95aee04)，保持不变。
  - [VIDEO_PIX_FMT_XRGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8be24c04210f8818d75082bd710db8b1)，保持不变。
  - [VIDEO_PIX_FMT_XBGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4ae1acc3d44a1698e0d48f299f061a49)，新增。
  - [VIDEO_PIX_FMT_BGRX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadf53a84505c1299a5c97a0213c989103)，新增。
  - [VIDEO_PIX_FMT_RGBX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadfdb271a780b10a29a356675014a25c2)，新增。

<a id="watchdog"></a>

### [看门狗（Watchdog）](#id36)


- [CONFIG_WDT_DISABLE_AT_BOOT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_DISABLE_AT_BOOT)的语义已明确。以前[CONFIG_WDT_DISABLE_AT_BOOT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_DISABLE_AT_BOOT)=n的预期行为不清晰，各驱动实现也不一致；现在已在该选项说明中明确规定，详见其说明。

  所有树内看门狗（Watchdog）驱动已更新，遵循现已明确的语义。

  特别是，CONFIG_WDT_DISABLE_AT_BOOT=n不再能让看门狗在启动时“自动”启用。依赖该行为的用户必须更新应用，像看门狗示例那样明确配置看门狗。与这种错误用法相关的以下Kconfig选项已移除：（[看门狗（Watchdog）](../timer_reference/P067_看门狗示例.md#watchdog)）

  > - `CONFIG_IWDG_STM32_INITIAL_TIMEOUT`
  > - `CONFIG_WDT_RPI_PICO_INITIAL_TIMEOUT`
  > - `CONFIG_WDT_CC13XX_CC26XX_INITIAL_TIMEOUT`
  > - `CONFIG_WDT_CC23X0_INITIAL_TIMEOUT`
  > - `CONFIG_WDT_CC32XX_INITIAL_TIMEOUT`
- [microchip,xec-watchdog](../soc_pmic_watchdog_binding_reference/P011_microchip_xec-watchdog.md#std-dtcompatible-microchip-xec-watchdog)的PCR及GIRQ属性已更新为使用新宏。（[GitHub #105668](https://github.com/zephyrproject-rtos/zephyr/issues/105668)）

<a id="bluetooth"></a>

## [蓝牙（Bluetooth）](#id37)

<a id="bluetooth-host"></a>

### [蓝牙主机（Bluetooth Host）](#id38)


- [CONFIG_BT_SIGNING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SIGNING)已弃用。
- [BT_GATT_CHRC_AUTH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gaab3a26a00f88a6eacd36f2841004204c)已弃用。
- [bt_conn_le_info.interval](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__info.html#a95a1f635e53f16d5839cdd58f4bda962)已弃用，应改用[bt_conn_le_info.interval_us](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__info.html#a3bede29a6a5df282bde6a26f50ea9aee)。注意单位变化：interval以1.25毫秒为单位，interval_us以微秒为单位。
- 从蓝牙核心规范v6.2起，使用口令输入（Passkey Entry）的传统低功耗蓝牙配对（Legacy LE Pairing），不再获得经过认证的中间人攻击防护（MITM Protection）。通过这种方法生成的绑定信息，从持久存储加载时会降级为未认证，安全等级随之降低。
- 蓝牙主机（Bluetooth Host）不再依赖[k_poll()](../eventpoll_reference/P003_轮询公共接口.md#gac550dc93662ce164fb22a5a91d6830db)，因此也不再选择[CONFIG_POLL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POLL)。若应用自身依赖此功能，必须在应用配置中明确启用[CONFIG_POLL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POLL)。
- 所有[CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE)用法，改为[CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE)。
- 所有[CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT)用法，改为[CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT)。
- 所有[CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN)用法，改为[CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN)。
- 所有[CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN)用法，改为[CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN)。
- [bt_iso_chan](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan.html)中的required_sec_level字段已移除。应用若需要设置连接等时流（CIS）连接的安全性，应先对ACL连接调用[bt_conn_set_security()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae001f1268e1ff42c3c974c95dcb6735d)，再调用[bt_iso_chan_connect()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga98953a261f3699b62cd19ab4977e0b4c)。
- [bt_iso_server](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__server.html)中的sec_level字段已移除。

<a id="bluetooth-audio"></a>

### [蓝牙音频（Bluetooth Audio）](#id39)


- [bt_bap_broadcast_assistant_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab59c5ebc4fef28da34d8a54b1244c33b)不再在流程结束时读取远端广播音频扫描服务（BASS）的接收状态。用户执行任何操作前，必须手动调用[bt_bap_broadcast_assistant_read_recv_state()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga94fce2b4346b1026d53e0b860ca7fbf2)，读取可能存在的接收状态。（[GitHub #91587](https://github.com/zephyrproject-rtos/zephyr/issues/91587)）
- [CONFIG_BT_AUDIO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUDIO)现在依赖[CONFIG_UTF8](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UTF8)。启用[CONFIG_BT_AUDIO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUDIO)的应用还必须启用[CONFIG_UTF8](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UTF8)。（[GitHub #102350](https://github.com/zephyrproject-rtos/zephyr/issues/102350)）
- [bt_tbs_set_uri_scheme_list()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae413f94b141b6fa8233de15c36f6327a)现在只接受单个字符串，不再接受URI列表或数组。应用需要修改现有输入，例如将{"tel", "skype"}改为"tel,skype"。（[GitHub #102724](https://github.com/zephyrproject-rtos/zephyr/issues/102724)）
- CONFIG_BT_TBS_SUPPORTED_FEATURES已移除。应用应使用已定义的BT_TBS_FEATURE_HOLD及BT_TBS_FEATURE_JOIN宏，设置支持的功能。（[GitHub #102666](https://github.com/zephyrproject-rtos/zephyr/issues/102666)）
- [bt_bap_unicast_server_foreach_ep()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#gafe7640d6269ec95c8af6d7549fac785d)及[bt_has_preset_foreach()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga0bf932a9a1977e4d1926c11242c7b70d)现在在迭代提前停止或参数无效时，可能返回错误。（[GitHub #105462](https://github.com/zephyrproject-rtos/zephyr/issues/105462)）
- [bt_bap_unicast_server_foreach_ep()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__server.html#gafe7640d6269ec95c8af6d7549fac785d)、[bt_bap_unicast_group_foreach_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gad608ee07c8a50abf586a3bc31921f032)、[bt_bap_broadcast_source_foreach_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#ga9d543b9282e0dadca3afe3a97e385b15)、[bt_cap_unicast_group_foreach_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c13996298c3e3aa33eb40f74b7bfe44)、[bt_cap_initiator_broadcast_foreach_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga45fa73b787bb4fefc73928acf3592e20)及[bt_has_preset_foreach()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga0bf932a9a1977e4d1926c11242c7b70d)的回调，现在返回true表示继续迭代，false表示停止。相关回调必须更新返回类型及返回值。（[GitHub #105462](https://github.com/zephyrproject-rtos/zephyr/issues/105462)）

<a id="bluetooth-mesh"></a>

### [蓝牙网状网络（Bluetooth Mesh）](#id40)


- [CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE)已弃用，启用它不再影响消息处理性能。

<a id="bluetooth-hci"></a>

### [蓝牙主机控制器接口（Bluetooth HCI）](#id41)


- [BT_HCI_LE_SUPERVISON_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a03dc93eec388a17c286d50395c683fcb)及[BT_HCI_LE_SUPERVISON_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a2564ee96b802cb887f67e3cc38f8f400)因拼写错误已弃用，应分别改用[BT_HCI_LE_SUPERVISION_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a07b822f1a826f4824ec070c4b6822fe2)及[BT_HCI_LE_SUPERVISION_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a1357a2a7227e86df1c132207ba44d6db)。

<a id="networking"></a>

## [网络（Networking）](#id42)

<a id="wi-fi"></a>

### [无线局域网（Wi-Fi）](#id43)


- [wifi_channel_info](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__channel__info.html)新增band字段，用于设置通道。对2.4 GHz的1～14信道及5 GHz的36～165信道，行为向后兼容：省略band或设为WIFI_FREQ_BAND_UNKNOWN时，驱动推断频段。对6 GHz必须设置band为WIFI_FREQ_BAND_6_GHZ，因为其信道编号与2.4 GHz的1～14存在重叠。须重新编译，确保调用net_mgmt时sizeof(struct wifi_channel_info)正确。
- WPA3现在通过WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION选择内部（Internal）、外部（External）或不使用（None）实现。将prj.conf中的[CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3)=y替换为CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION_INT=y，或按需使用_EXT、_NONE选项。CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3现在没有用户提示，仅在选择Internal时自动选中，不应直接赋值。C代码应优先用[CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON)检测内部或外部WPA3支持。
- 以下位置中的网络API：


  - [include/zephyr/net/net_ip.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_ip.h)
  - [include/zephyr/net/socket.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/socket.h)

  以及subsys/net等位置的相关代码，已统一使用命名空间，即在网络API名称前加net_、NET_或ZSOCK_前缀，以避免与可能定义同名符号的POSIX或libc产生循环依赖。新增兼容头文件[include/zephyr/net/net_compat.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_compat.h)，提供旧符号供用户继续使用。外部网络应用可继续使用POSIX网络符号，但需包含sys/socket.h等相关POSIX头文件，因为Zephyr网络头文件不再间接包含它们。若应用或Zephyr内部代码无法使用POSIX API，则必须为调用的网络API加上相应前缀。
- [net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)的返回类型从int改为[net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)。（[GitHub #104815](https://github.com/zephyrproject-rtos/zephyr/issues/104815)）
- HTTP服务器事务状态枚举从http_data_status改名为http_transaction_status，以更准确体现用途。枚举值也改名如下：


  - HTTP_SERVER_DATA_ABORTED改名为HTTP_SERVER_TRANSACTION_ABORTED。
  - HTTP_SERVER_DATA_MORE改名为HTTP_SERVER_REQUEST_DATA_MORE。
  - HTTP_SERVER_DATA_FINAL改名为HTTP_SERVER_REQUEST_DATA_FINAL。

  动态资源处理回调类型也已更新，使用新枚举及新枚举值。使用动态HTTP资源的应用必须更新处理回调，使用新枚举并处理改名后的值。
- HTTP服务器为动态资源向客户端完整发送响应后，现在会报告HTTP_SERVER_TRANSACTION_COMPLETE状态。应用也应在处理回调中处理此状态，以在响应成功发送后正确复位资源状态。
- 创建安全套接字（Secure Socket）时，传给[zsock_socket()](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga5693d19a0bdff45a5cb09227683d8631)的协议版本现在作为TLS会话允许使用的最低版本强制执行。
- NET_SOCKETS_SOCKOPT_TLS不再自动选择密码相关Kconfig选项，因为这些选项强烈依赖最终应用需求。因此，必须明确选择所需的TLS协议版本及密码套件（Cipher Suite）。可用[CONFIG_MBEDTLS_CIPHERSUITE_TLS_.*](https://docs.zephyrproject.org/latest/kconfig.html#!CONFIG_MBEDTLS_CIPHERSUITE_TLS_.*)辅助选项自动启用特定密码套件的全部依赖，也可按相同模式增加所需辅助选项。

<a id="coap"></a>

### [受限应用协议（CoAP）](#id44)


- CoAP .well-known/core响应的资源元数据，现在通过专用的[coap_resource.metadata](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__resource.html#a6c1fe25539ecbe4ec2ed7446fff84861)指针配置，不再使用应由应用独占的[coap_resource.user_data](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__resource.html#a202a83a5aa024a62bd25cc40f42e8d65)。实现.well-known/core处理的应用应改用新指针。
- <a id="index-0"></a>

  COAP_RESPONSE_CODE_OK，即2.00响应码定义已移除，因为它不是有效响应码：[RFC 7252](https://datatracker.ietf.org/doc/html/rfc7252.html)未定义它，IANA注册表也未分配该值，见[https://www.iana.org/assignments/core-parameters/core-parameters.xhtml#response-codes](https://www.iana.org/assignments/core-parameters/core-parameters.xhtml#response-codes)。

<a id="modem"></a>

## [调制解调器（Modem）](#id45)

<a id="modem-hl78xx"></a>

### [HL78XX调制解调器（Modem）](#id46)


- HL78XX启动时序相关的CONFIG_MODEM_HL78XX_DEV_*选项改名如下：


  - MODEM_HL78XX_DEV_POWER_PULSE_DURATION改名为MODEM_HL78XX_DEV_POWER_PULSE_DURATION_MS。
  - MODEM_HL78XX_DEV_RESET_PULSE_DURATION改名为MODEM_HL78XX_DEV_RESET_PULSE_DURATION_MS。
  - MODEM_HL78XX_DEV_STARTUP_TIME改名为MODEM_HL78XX_DEV_STARTUP_TIME_MS。
  - MODEM_HL78XX_DEV_SHUTDOWN_TIME改名为MODEM_HL78XX_DEV_SHUTDOWN_TIME_MS。
- 默认启动时序从1000 ms改为120 ms，以提高所有受支持开发板上的初始化可靠性。

  依赖旧默认值的应用必须更新配置。

<a id="lorawan"></a>

## [LoRa广域网（LoRaWAN）](#id47)


- LoRaWAN区域选项从LORAMAC_REGION_*改名为LORAWAN_REGION_*，使名称与具体后端无关。使用以下任一符号的应用必须更新配置文件：


  - CONFIG_LORAMAC_REGION_AS923改名为[CONFIG_LORAWAN_REGION_AS923](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_AS923)。
  - CONFIG_LORAMAC_REGION_AU915改名为[CONFIG_LORAWAN_REGION_AU915](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_AU915)。
  - CONFIG_LORAMAC_REGION_CN470改名为[CONFIG_LORAWAN_REGION_CN470](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_CN470)。
  - CONFIG_LORAMAC_REGION_CN779改名为[CONFIG_LORAWAN_REGION_CN779](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_CN779)。
  - CONFIG_LORAMAC_REGION_EU433改名为[CONFIG_LORAWAN_REGION_EU433](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_EU433)。
  - CONFIG_LORAMAC_REGION_EU868改名为[CONFIG_LORAWAN_REGION_EU868](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_EU868)。
  - CONFIG_LORAMAC_REGION_KR920改名为[CONFIG_LORAWAN_REGION_KR920](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_KR920)。
  - CONFIG_LORAMAC_REGION_IN865改名为[CONFIG_LORAWAN_REGION_IN865](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_IN865)。
  - CONFIG_LORAMAC_REGION_US915改名为[CONFIG_LORAWAN_REGION_US915](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_US915)。
  - CONFIG_LORAMAC_REGION_RU864改名为[CONFIG_LORAWAN_REGION_RU864](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_REGION_RU864)。

<a id="other-subsystems"></a>

## [其他子系统（Other Subsystems）](#id48)

<a id="cfb"></a>

### [字符帧缓冲区（CFB）](#id49)


- 坐标改为使用有符号值表示，因此[cfb_print()](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga029d0f320157e6b2936bb9f0794024d6)、[cfb_invert_area()](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga02dbf9751af0ee01e20a293b94fcfb7a)及[cfb_position](../hardware/P186_字符帧缓冲坐标结构.md)定义已变化。
- DAP子系统的初始化及配置已变化。如何使用USB后端初始化Zephyr DAP Link，请参考[CMSIS-DAP](../observability/P073_CMSIS-DAP调试探针示例.md#cmsis-dap)示例。
- 高速缓存（Cache）


  - 使用[CONFIG_CACHE_HAS_MIRRORED_MEMORY_REGIONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_MIRRORED_MEMORY_REGIONS)替代[CONFIG_CACHE_DOUBLEMAP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_DOUBLEMAP)，新名称更准确地描述镜像内存区域功能。

<a id="flash"></a>

### [闪存（Flash）](#id50)


- 此前已弃用的CONFIG_FLASH_AREA_CHECK_INTEGRITY_MBEDTLS现已移除。
- CONFIG_FLASH_AREA_CHECK_INTEGRITY_PSA也已移除，因为密码库后端已没有其他选项。
- Flash Shell命令flash erase及flash write现在要求明确提供设备参数，以避免意外破坏设备程序Flash。

<a id="flash-map"></a>

### [Flash映射（Flash Map）](#id51)


- [include/zephyr/storage/flash_map.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/storage/flash_map.h)中的以下宏已弃用并替换：

  <table>
  <tr>
  <th>已弃用的宏（Deprecated Macro）</th>
  <th>替代宏（Replacement Macro）</th>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gabb94759e5717302724f08f90f941a945"><code>FIXED_PARTITION_EXISTS</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga4e63c3b898a43a210bc0298dc7b49c1e"><code>PARTITION_EXISTS</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga60d5298007e2ee261b915a110389e76a"><code>FIXED_PARTITION_ID</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gafbc907db76aec2702eff9e5265323560"><code>PARTITION_ID</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga9229bc06458c19baf093ced063a9494b"><code>FIXED_PARTITION_OFFSET</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaee5fe6581a477b83157d00155e150980"><code>PARTITION_OFFSET</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5ac2848ccfcc1425939d76f499756551"><code>FIXED_PARTITION_ADDRESS</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gadfe30156a3a50c69e268075d07ef050b"><code>PARTITION_ADDRESS</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaf6121895f4fdd50533762c6aa57cb319"><code>FIXED_PARTITION_NODE_ADDRESS</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8c68c5fa266dcc128ee9520c3c57807d"><code>PARTITION_NODE_ADDRESS</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga79092c8d0f32aeec69c6a79021d1ab38"><code>FIXED_PARTITION_NODE_OFFSET</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga28906b4cc8b00f8e055a1d9a082dbb5e"><code>PARTITION_NODE_OFFSET</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga2dbc50d9f80d7f7c597c75cbd536cd50"><code>FIXED_PARTITION_SIZE</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab5234434a7f106e4b3f2b79f2087279a"><code>PARTITION_SIZE</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga526459438c6de09abb727585d22b7004"><code>FIXED_PARTITION_NODE_SIZE</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gabaa4ff45d7ec2c57616b9fb721c0c45c"><code>PARTITION_NODE_SIZE</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga3c92b6797feb183da38b8b57e77f2d17"><code>FIXED_PARTITION_DEVICE</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga565f24a138c217bdbe8f42afe8b664e0"><code>PARTITION_DEVICE</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gad64fb220f82870acce62661bfa94991a"><code>FIXED_PARTITION_NODE_DEVICE</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8986be787a0c4d7c35ef835ce91290de"><code>PARTITION_NODE_DEVICE</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaf933ac3bd33006357c8dc0c3b3f5878f"><code>FIXED_PARTITION_MTD</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga583ab6d0092ce23df436e42c1eeeb6e2"><code>PARTITION_MTD</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga891d6e60a927f4b5660bcb2966e9bd2b"><code>FIXED_PARTITION_NODE_MTD</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gac6c6b41211ee9bdb154cefdb46214615"><code>PARTITION_NODE_MTD</code></a></td>
  </tr>
  <tr>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab51fb05a2cd0666b892d90ccbc9de342"><code>FIXED_PARTITION_BY_NODE</code></a></td>
  <td><a href="https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga8f3f3ac80d3858626f05c60aaaec48f7"><code>PARTITION_BY_NODE</code></a></td>
  </tr>
  </table>

  这些新宏还支持[zephyr,mapped-partition](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)绑定。

<a id="jwt"></a>

### [JSON Web令牌（JWT）](#id52)


- 此前已弃用的CONFIG_JWT_SIGN_RSA_LEGACY现已移除。此次未遵循通常的两个版本弃用期，因为项目已就Mbed TLS属于外部模块达成一致，该情形不适用常规弃用规则，见[GitHub #97660](https://github.com/zephyrproject-rtos/zephyr/issues/97660)。

<a id="libsbc"></a>

### [子带编码库（Libsbc）](#id53)


- Libsbc，即sbc.c及sbc.h，移到蓝牙子系统下；sbc.h现在位于include/zephyr/bluetooth。

<a id="management"></a>

### [管理（Management）](#id54)


- 设备更新服务（hawkBit）


  - 已弃用的CONFIG_HAWKBIT_DDI_NO_SECURITY选项已移除。（[GitHub #105150](https://github.com/zephyrproject-rtos/zephyr/issues/105150)）
- 微控制器管理（MCUmgr）


  - 使用[CONFIG_MCUMGR_TRANSPORT_UART](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UART)时，现在还必须选择[CONFIG_UART_MCUMGR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUMGR)；二者关系从select改为depends on。

<a id="random"></a>

### [随机数（Random）](#id55)


- CONFIG_CSPRNG_AVAILABLE改名为[CONFIG_ENTROPY_NODE_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_NODE_ENABLED)。

<a id="tracing"></a>

### [跟踪（Tracing）](#id56)


- 通用跟踪格式（Common Trace Format，CTF）：元数据事件头中的uint8_t id改为uint16_t id。事件ID占用空间加倍，但可表示的事件数从255增至65,535。

  此变化使现有使用8位ID的CTF跟踪数据不再兼容。

<a id="serial"></a>

### [串行接口（Serial）](#id57)


- pl011 UART驱动：从pl011_poll_in()移除读取状态寄存器（Read Status Register，RSR）的错误处理。pl011_err_check()已实现RSR处理，检测及报告接收错误应在该函数中完成。（[GitHub #101715](https://github.com/zephyrproject-rtos/zephyr/issues/101715)）

<a id="settings"></a>

### [设置（Settings）](#id58)


- CONFIG_SETTINGS_TFM_ITS改名为[CONFIG_SETTINGS_TFM_PSA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_TFM_PSA)。

<a id="modules"></a>

## [模块（Modules）](#id59)

<a id="hostap"></a>

### [接入点软件（HostAP）](#id60)


- [CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)现在默认启用。

<a id="mbed-tls"></a>

### [Mbed TLS密码与TLS库](#id61)


- Mbed TLS升级到4.1.0。从此该仓库仅包含TLS及X.509，密码功能移到TF-PSA-Crypto。为后者新增west模块，基于上游1.1.0版本。TF-M仍使用Mbed TLS 3.6.5构建。此调整引入许多密码相关变化，官方强烈建议查阅Mbed TLS 3.x到TF-PSA-Crypto 1.x的迁移指南。（[Mbed TLS 3.x到TF-PSA-Crypto 1.x迁移指南](https://github.com/Mbed-TLS/TF-PSA-Crypto/blob/development/docs/1.0-migration-guide.md)）
- CONFIG_MBEDTLS_ENTROPY_POLL_ZEPHYR改名为[CONFIG_MBEDTLS_PSA_DRIVER_GET_ENTROPY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_DRIVER_GET_ENTROPY)。
- CONFIG_MBEDTLS_PEM_CERTIFICATE_FORMAT替换为它以前启用的底层选项：[CONFIG_MBEDTLS_PEM_PARSE_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_PARSE_C)、[CONFIG_MBEDTLS_PEM_WRITE_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_WRITE_C)及[CONFIG_MBEDTLS_BASE64_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_BASE64_C)。
- CONFIG_MBEDTLS_SERVER_NAME_INDICATION改名为[CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION)。
- CONFIG_MBEDTLS_TEST改名为[CONFIG_MBEDTLS_DEBUG_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_DEBUG_C)。
- 以下PSA相关Kconfig符号已移除，因为TF-PSA-Crypto不再支持它们：


  - `CONFIG_PSA_WANT_KEY_TYPE_DES`
  - `CONFIG_PSA_WANT_ECC_SECP_R1_192`
  - `CONFIG_PSA_WANT_ECC_SECP_K1_192`
  - `CONFIG_PSA_WANT_ECC_SECP_R1_224`
- 以下Mbed TLS Kconfig符号已移除：


  - `CONFIG_CUSTOM_MBEDTLS_CFG_FILE`
  - `CONFIG_MBEDTLS_CHACHAPOLY_AEAD_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_AES_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_CAMELLIA_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_CCM_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_CHACHA20_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_DES_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_GCM_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_MODE_CBC_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_MODE_CTR_ENABLED`
  - `CONFIG_MBEDTLS_CIPHER_MODE_XTS_ENABLED`
  - `CONFIG_MBEDTLS_CMAC`
  - `CONFIG_MBEDTLS_DHM_C`
  - `CONFIG_MBEDTLS_ECDH_C`
  - `CONFIG_MBEDTLS_ECDSA_C`
  - `CONFIG_MBEDTLS_ECDSA_DETERMINISTIC`
  - `CONFIG_MBEDTLS_ECJPAKE_C`
  - `CONFIG_MBEDTLS_ECP_ALL_ENABLED`
  - `CONFIG_MBEDTLS_ECP_C`
  - `CONFIG_MBEDTLS_ECP_DP_BP256R1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_BP384R1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_BP512R1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_CURVE25519_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_CURVE448_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP192K1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP192R1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP224K1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP224R1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP256K1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP256R1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP384R1_ENABLED`
  - `CONFIG_MBEDTLS_ECP_DP_SECP521R1_ENABLED`
  - `CONFIG_MBEDTLS_GENPRIME_ENABLED`
  - `CONFIG_MBEDTLS_HKDF_C`
  - `CONFIG_MBEDTLS_KEY_EXCHANGE_DHE_PSK_ENABLED`
  - `CONFIG_MBEDTLS_KEY_EXCHANGE_DHE_RSA_ENABLED`
  - `CONFIG_MBEDTLS_KEY_EXCHANGE_RSA_ENABLED`
  - `CONFIG_MBEDTLS_KEY_EXCHANGE_RSA_PSK_ENABLED`
  - `CONFIG_MBEDTLS_MD5`
  - `CONFIG_MBEDTLS_PKCS1_V15`
  - `CONFIG_MBEDTLS_PKCS1_V21`
  - `CONFIG_MBEDTLS_POLY1305`
  - `CONFIG_MBEDTLS_RSA_C`
  - `CONFIG_MBEDTLS_SHA1`
  - `CONFIG_MBEDTLS_SHA224`
  - `CONFIG_MBEDTLS_SHA256`
  - `CONFIG_MBEDTLS_SHA384`
  - `CONFIG_MBEDTLS_SHA512`
  - `CONFIG_MBEDTLS_USE_PSA_CRYPTO`

<a id="openthread"></a>

### [OpenThread协议栈](#id62)


- 以下Kconfig选项已改名：


  - CONFIG_OPENTHREAD_MBEDTLS_CHOICE改名为[CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG)。
  - CONFIG_CUSTOM_OPENTHREAD_SECURITY改名为[CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG)。
- [CONFIG_OPENTHREAD_CRYPTO_PSA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA)不再依赖[CONFIG_PSA_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)_CLIENT，而改为选择CONFIG_PSA_CRYPTO。
- 未使用TF-M的构建中，若设置[CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG)及[CONFIG_OPENTHREAD_CRYPTO_PSA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA)，现在会自动隐含启用（Imply）[CONFIG_SECURE_STORAGE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE)，以保证PSA内部可信存储（ITS）实现可用。必须为安全存储（Secure Storage）配置后端，可选择Settings、ZMS或自定义后端。
- [CONFIG_OPENTHREAD_CRYPTO_PSA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CRYPTO_PSA)现在默认启用。
- Mbed TLS升级到4.1.0后，Zephyr不再提供旧式密码支持，因此CONFIG_OPENTHREAD_CRYPTO_LEGACY_MBEDTLS_CONFIG已移除。CONFIG_OPENTHREAD_CRYPTO_PSA_CONFIG原本就是默认密码选项，现在成为唯一受支持选项。

<a id="trusted-firmware-m"></a>

### [可信固件M（Trusted Firmware-M）](#id63)


- TF-M定义SECURE_UART1现在由Zephyr的[CONFIG_TFM_SECURE_UART](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_SECURE_UART)控制，该选项覆盖此前在TF-M仓库中指定的任何平台值。

<a id="architectures"></a>

## [架构（Architectures）](#id64)


- CONFIG_ARCH_HAS_COHERENCE改名为[CONFIG_CACHE_CAN_SAY_MEM_COHERENCE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_CAN_SAY_MEM_COHERENCE)。由于该功能与缓存有关，现归入缓存配置。


  - 使用[sys_cache_is_mem_coherent()](../cache_reference/P001_公共缓存接口.md#ga17071b17b61be7a8c00064a69d107b19)替代arch_mem_coherent()。
- [CONFIG_RISCV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)现在要求设备树中存在[riscv](../cpu_vendor_multiarc_binding_reference/P034_riscv.md#std-dtcompatible-riscv)节点。
- [riscv](../cpu_vendor_multiarc_binding_reference/P034_riscv.md#std-dtcompatible-riscv)节点的riscv,isa-base及riscv,isa-extensions属性，现在用于设置基本整数指令集（Base Integer Instruction Set）及RISC-V扩展，不再由SoC设置。riscv,isa属性已弃用，改用上述两个新属性。（[GitHub #97540](https://github.com/zephyrproject-rtos/zephyr/issues/97540)）


  - 由于RISC-V扩展现在由设备树设置，[CONFIG_SOC_CV64A6](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_CV64A6)_IMAFDC及CONFIG_SOC_CV64A6_IMAC合并为CONFIG_SOC_CV64A6。
  - [CONFIG_SOC_SERIES_AE350](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AE350)的以下选项已移除，因为现在可通过设备树设置：


    - `CONFIG_RV32I_CPU`
    - `CONFIG_RV32E_CPU`
    - `CONFIG_RV64I_CPU`
    - `CONFIG_NO_FPU`
    - `CONFIG_SINGLE_PRECISION_FPU`
    - `CONFIG_DOUBLE_PRECISION_FPU`

## 译注

本页用于4.3到4.4迁移。SDK、Python及C标准要求按官方原文保留。定时器模式、像素格式、看门狗和默认配置变化不应只按名称替换理解。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [?p=PartA2_SD%20Host_Controller_Simplified_Specification_Ver4.20.jpg](https://www.sdcard.org/downloads/pls/pdf/?p=PartA2_SD%20Host_Controller_Simplified_Specification_Ver4.20.jpg)：HTTP Error 403: Forbidden。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：迁移到Zephyr 4.3](P005_迁移到Zephyr_4.3.md) · [本模块主线目录](../reading/releases_guides.md) · [全部主线](../reading/README.md) · [下一篇：迁移到Zephyr 4.5 工作草案](P007_迁移到Zephyr_4.5_工作草案.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P005_迁移到Zephyr_4.3.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_迁移到Zephyr_4.5_工作草案.md)

</details>

<!-- reading-navigation:end -->
