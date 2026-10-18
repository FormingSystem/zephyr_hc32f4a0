---
id: learning.zephyr-docs.releases-guides.page-7
title: 迁移到Zephyr 4.5 工作草案
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/migration-guide-4.5.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="migration-guide-to-zephyr-v4-5-0-working-draft"></a>

<a id="migration-4-5"></a>

# 第7章\_迁移到Zephyr v4.5.0的指南，工作草案（Working Draft）

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/migration-guide-4.5.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

本文说明将应用从Zephyr v4.4.0迁移到Zephyr v4.5.0所需的更改。

其他与应用迁移没有直接关系的变化，见发行说明。（[发行说明（Release Notes）](https://docs.zephyrproject.org/latest/releases/release-notes-4.5.html#zephyr-4-5)）

<a id="contents"></a>


- <a id="id5"></a>

  [通用部分（Common）](#common)
- <a id="id6"></a>

  [构建系统（Build System）](#build-system)
- <a id="id7"></a>

  [内核（Kernel）](#kernel)
- <a id="id8"></a>

  [开发板（Boards）](#boards)
- <a id="id9"></a>

  [设备驱动与设备树（Device Drivers and Devicetree）](#device-drivers-and-devicetree)


  - <a id="id10"></a>

    [模数转换器（ADC）](#adc)
  - <a id="id11"></a>

    [亚德诺半导体（Analog Devices）](#analog-devices)
  - <a id="id12"></a>

    [音频编解码器（Audio Codec）](#audio-codec)
  - <a id="id13"></a>

    [时钟控制（Clock Control）](#clock-control)
  - <a id="id14"></a>

    [比较器（Comparator）](#comparator)
  - <a id="id15"></a>

    [控制器局域网（Controller Area Network，CAN）](#controller-area-network-can)
  - <a id="id16"></a>

    [计数器（Counter）](#counter)
  - <a id="id17"></a>

    [设备树（Devicetree）](#devicetree)
  - <a id="id18"></a>

    [数字麦克风（Digital Microphone）](#digital-microphone)
  - <a id="id19"></a>

    [磁盘（Disk）](#disk)
  - <a id="id20"></a>

    [显示（Display）](#display)
  - <a id="id21"></a>

    [直接存储器访问（DMA）](#dma)
  - <a id="id22"></a>

    [增强型串行外设接口（ESPI）](#espi)
  - <a id="id23"></a>

    [以太网（Ethernet）](#ethernet)
  - <a id="id24"></a>

    [闪存（Flash）](#flash)
  - <a id="id25"></a>

    [电量计（Fuel Gauge）](#fuel-gauge)
  - <a id="id26"></a>

    [通用输入输出（GPIO）](#gpio)
  - <a id="id27"></a>

    [触觉反馈（Haptics）](#haptics)
  - <a id="id28"></a>

    [硬件自旋锁（HWSPINLOCK）](#hwspinlock)
  - <a id="id29"></a>

    [集成电路间总线（I2C）](#i2c)
  - <a id="id30"></a>

    [集成电路间音频总线（I2S）](#i2s)
  - <a id="id31"></a>

    [低速率无线个域网（IEEE 802.15.4）](#ieee-802-15-4)
  - <a id="id32"></a>

    [输入（Input）](#input)
  - <a id="id33"></a>

    [中断控制器（Interrupt Controllers）](#interrupt-controllers)
  - <a id="id34"></a>

    [邮箱（MBOX）](#mbox)
  - <a id="id35"></a>

    [多线串行外设接口（MSPI）](#mspi)
  - <a id="id36"></a>

    [Nordic半导体](#nordic)
  - <a id="id37"></a>

    [恩智浦（NXP）](#nxp)
  - <a id="id38"></a>

    [脉宽调制（PWM）](#pwm)
  - <a id="id39"></a>

    [实时时钟（RTC）](#rtc)
  - <a id="id40"></a>

    [SD主机控制器（SD Host Controller）](#sd-host-controller)
  - <a id="id41"></a>

    [传感器（Sensor）](#sensor)
  - <a id="id42"></a>

    [串行接口（Serial）](#serial)
  - <a id="id43"></a>

    [串行外设接口（SPI）](#spi)
  - <a id="id44"></a>

    [步进电机（Stepper）](#stepper)
  - <a id="id45"></a>

    [STM32](#stm32)
  - <a id="id46"></a>

    [存储（Storage）](#storage)
  - <a id="id47"></a>

    [系统控制器（Syscon）](#syscon)
  - <a id="id48"></a>

    [德州仪器（Texas Instruments）](#texas-instruments)
  - <a id="id49"></a>

    [定时器（Timer）](#timer)
  - <a id="id50"></a>

    [通用串行总线（USB）](#usb)
  - <a id="id51"></a>

    [视频（Video）](#video)
  - <a id="id52"></a>

    [无线局域网（Wi-Fi）](#wifi)
  - <a id="id53"></a>

    [Xen 虚拟机监控器（Xen）](#xen)
- <a id="id54"></a>

  [蓝牙（Bluetooth）](#bluetooth)


  - <a id="id55"></a>

    [蓝牙音频（Bluetooth Audio）](#bluetooth-audio)
  - <a id="id56"></a>

    [经典蓝牙（Bluetooth Classic）](#bluetooth-classic)
  - <a id="id57"></a>

    [蓝牙主机控制器接口（Bluetooth HCI）](#bluetooth-hci)
  - <a id="id58"></a>

    [蓝牙主机（Bluetooth Host）](#bluetooth-host)
  - <a id="id59"></a>

    [蓝牙网状网络（Bluetooth Mesh）](#bluetooth-mesh)
  - <a id="id60"></a>

    [蓝牙服务（Bluetooth Services）](#bluetooth-services)
- <a id="id61"></a>

  [网络（Networking）](#networking)


  - <a id="id62"></a>

    [以太网（Ethernet）](#id1)
  - <a id="id63"></a>

    [调制解调器（Modem）](#modem)
  - <a id="id64"></a>

    [精确时间协议（PTP）](#ptp)
  - <a id="id65"></a>

    [广义精确时间协议（gPTP）](#gptp)
- <a id="id66"></a>

  [调制解调器（Modem）](#id2)


  - <a id="id67"></a>

    [芯讯通SIM7080（SIMCOM SIM7080）](#simcom-sim7080)
- <a id="id68"></a>

  [LoRa广域网（LoRaWAN）](#lorawan)
- <a id="id69"></a>

  [库（Libraries）](#libraries)


  - <a id="id70"></a>

    [环形缓冲区（Ring Buffer）](#ring-buffer)
- <a id="id71"></a>

  [其他子系统（Other Subsystems）](#other-subsystems)


  - <a id="id72"></a>

    [FIDO2身份认证](#fido2)
  - <a id="id73"></a>

    [设备更新服务（hawkBit）](#hawkbit)
  - <a id="id74"></a>

    [日志（Logging）](#logging)
  - <a id="id75"></a>

    [MCU启动加载器（MCUboot）](#mcuboot)
  - <a id="id76"></a>

    [微控制器管理（MCUmgr）](#mcumgr)
  - <a id="id77"></a>

    [网络缓冲区（Network Buffers）](#network-buffers)
  - <a id="id78"></a>

    [可移植操作系统接口（POSIX）](#posix)
  - <a id="id79"></a>

    [电源管理（Power Management）](#power-management)
  - <a id="id80"></a>

    [随机数（Random）](#random)
  - <a id="id81"></a>

    [实时输入输出（RTIO）](#rtio)
  - <a id="id82"></a>

    [安全存储（Secure Storage）](#secure-storage)
  - <a id="id83"></a>

    [命令行（Shell）](#shell)
  - <a id="id84"></a>

    [流式Flash（Stream Flash）](#stream-flash)
- <a id="id85"></a>

  [工具（Tools）](#tools)
- <a id="id86"></a>

  [模块（Modules）](#modules)


  - <a id="id87"></a>

    [轻量图形库（LVGL）](#lvgl)
  - <a id="id88"></a>

    [`hal_nxp`](#hal-nxp)
  - <a id="id89"></a>

    [Mbed TLS密码与TLS库](#mbed-tls)
  - <a id="id90"></a>

    [可信固件M（Trusted Firmware-M，TF-M）](#trusted-firmware-m-tf-m)
- <a id="id91"></a>

  [配置片段（Snippets）](#snippets)
- <a id="id92"></a>

  [架构（Architectures）](#architectures)


  - <a id="id93"></a>

    [视频（Video）](#id4)
  - <a id="id94"></a>

    [测试运行器（Twister）](#twister)

<a id="common"></a>

## [通用部分（Common）](#id5)


- 头文件include/zephyr/sys_clock.h已弃用，将在未来版本移除。应改为包含include/zephyr/sys/clock.h。

<a id="build-system"></a>

## [构建系统（Build System）](#id6)


- 最低要求的CMake版本现在为3.28.0。Ubuntu 24.04 LTS软件仓库提供CMake 3.28.3；Ubuntu 22.04 LTS等提供较旧版本的发行版用户，可从[Kitware APT仓库](https://apt.kitware.com/)获取新版本，或运行pip install cmake。
- 低于C17的C语言标准支持在弃用后已移除。CONFIG_STD_C11、CONFIG_STD_C99及CONFIG_STD_C90选项已删除，编译Zephyr时须使用C17或更高标准。
- [CONFIG_LEGACY_GENERATED_INCLUDE_PATH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LEGACY_GENERATED_INCLUDE_PATH)已弃用，且默认禁用。包含Zephyr文件时，路径现在必须带zephyr/前缀。
- CMake变量SOC_NAME、SOC_SERIES、SOC_FAMILY及SOC_V2_DIR因与已有变量重复而弃用，分别改用[CONFIG_SOC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC)、[CONFIG_SOC_SERIES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES)、[CONFIG_SOC_FAMILY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY)及SOC_FULL_DIR。
- CONFIG_BUILD_NO_GAP_FILL已移除。间隙填充（Gap Filling）由[CONFIG_BUILD_OUTPUT_HEX_GAP_FILL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_OUTPUT_HEX_GAP_FILL)及[CONFIG_BUILD_OUTPUT_S19_GAP_FILL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_OUTPUT_S19_GAP_FILL)明确启用，因此只需删除旧选项。
- cmake/app/boilerplate.cmake已移除。仍直接包含它的应用，必须改为在CMakeLists.txt开头使用find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})。
- 不再读取名为<board>_<revision>.conf的开发板修订版本Kconfig片段，应改名为<board>_<revision>_defconfig。
- zephyr_code_relocate(FILES ...)不再展开通配模式，遇到通配模式现在会失败。应先用file(GLOB ...)展开，再传入得到的文件名。
- 自Zephyr 3.1起已弃用的ZephyrUnittest CMake包现已移除，west zephyr-export也不再注册它。使用find_package(Zephyr COMPONENTS unittest)替代find_package(ZephyrUnittest)。
- west spdx --init已弃用，将在Zephyr 5.0移除。启用[CONFIG_BUILD_OUTPUT_META](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_OUTPUT_META)的构建现在会向CMake请求west spdx读取的基于文件API对象模型，因此生成软件物料清单（SBOM）无需预先准备构建目录：正常构建后运行west spdx即可。
- CMake的flash、debug、debugserver、attach及rtt目标已移除，分别改用west flash、west debug、west debugserver、west attach及west rtt。仿真用的run及debugserver目标不受影响。
- 构建系统不再使用WEST_DIR变量。
- [CONFIG_DEPRECATION_TEST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEPRECATION_TEST)已弃用，因为可改用[CONFIG_WARN_DEPRECATED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WARN_DEPRECATED)。将CONFIG_DEPRECATION_TEST=y替换为CONFIG_WARN_DEPRECATED=n即可。
- [加固工具（Hardening Tool）](../security/P005_安全加固工具.md#hardening)的数据文件scripts/kconfig/hardened.csv已替换为YAML数据库：配置档案位于scripts/kconfig/hardening.yaml，各子系统的hardening.yaml片段位于对应Kconfig文件旁。曾修改CSV的下游分支应将条目迁移到新格式，见加固工具文档；树外建议无需再修改树内文件，可通过-DHARDENCONFIG_EXTRA_SOURCES=提供。旧CSV中的CONFIG_DEBUG_COREDUMP存在语法错误，会被静默跳过；现在会实际检查，因此hardenconfig可能将其报告为新发现。三个CSV条目被删除而未迁移：CONFIG_STACK_USAGE仅生成构建时.su文件，不影响镜像；CONFIG_MPU_STACK_GUARD与CONFIG_BUILTIN_STACK_GUARD则由[CONFIG_HW_STACK_PROTECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HW_STACK_PROTECTION)仲裁，为互斥机制，同时推荐二者会在具有栈指针限值寄存器的内核上错误报告不适用的那个选项。仍推荐启用[CONFIG_HW_STACK_PROTECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HW_STACK_PROTECTION)，让架构选择相应机制。

<a id="kernel"></a>

## [内核（Kernel）](#id7)


- errno从内核移到lib/libc/common，因此_k_neg_eagain改名为_errno_neg_egain。译注：新名称按原网页拼写保留。
- [k_sem_reset()](../synchronization_reference/P008_信号量公共接口.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)不再唤醒等待该信号量的轮询等待者（Poll Waiter）。这些等待者会继续挂起，直到信号量可用或轮询超时。依赖reset唤醒轮询等待者的应用必须改用明确的同步机制。
- CONFIG_SMP_BOOT_DELAY已移除。将辅助CPU的启动推迟到运行时，现在通过设备树按CPU表达：在/cpus下对应cpu节点中添加zephyr,deferred-start标志，通常放在开发板覆盖文件中，之后仍通过[k_smp_cpu_start()](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html#a33eb24503679583d853db1c4dc7e3812)或[k_smp_cpu_resume()](https://docs.zephyrproject.org/latest/doxygen/html/kernel_2smp_8h.html#a39b4f48857baef688ee646bac36c882d)启动。旧选项会跳过所有辅助CPU，新方式可逐CPU选择。注意：该标志仅对绑定包含cpu.yaml的cpu节点生效，没有此类绑定的节点无法延迟启动。
- 启用[CONFIG_SCHED_CPU_MASK_PIN_ONLY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_CPU_MASK_PIN_ONLY)时，调用[k_thread_cpu_mask_clear()](../thread_core_reference/P001_线程公共接口.md#ga80b9c58df6600c7e79f16756c128f44c)、[k_thread_cpu_mask_enable_all()](../thread_core_reference/P001_线程公共接口.md#gaedcfeb0964ae72611791241580b2119d)或[k_thread_cpu_mask_disable()](../thread_core_reference/P001_线程公共接口.md#ga89e6c07ac112da75b2ef115d1a557d44)现在会触发断言，而非静默产生无效状态。在PIN_ONLY模式使用这些函数的应用必须改用[k_thread_cpu_pin()](../thread_core_reference/P001_线程公共接口.md#gae9ebd9845e14ed02944ab9282a185c03)。
- [CONFIG_SCHED_CPU_MASK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_CPU_MASK)不再局限于[CONFIG_SCHED_SIMPLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_SIMPLE)。原本选择SCHED_SCALABLE或SCHED_MULTIQ、但为CPU亲和性（Affinity）而不得不保留SCHED_SIMPLE的项目，现在可直接使用所需后端。
- [k_sleep()](../thread_core_reference/P001_线程公共接口.md#ga093ac91db17ec33696168801d01efe75)及[k_usleep()](../thread_core_reference/P001_线程公共接口.md#gab761f90082335d57e3c6cd4013c819e6)不再各自作为系统调用，而是新系统调用[k_sleep_ticks()](../thread_core_reference/P001_线程公共接口.md#ga5ad6bcbcf89f9a9fbf6929388e2a7842)的内联包装，使编译器可折叠或消除单位换算。其原型、语义及返回值不变，声明从include/zephyr/kernel.h移到新头文件include/zephyr/sleep.h，由kernel.h包含。调用它们的代码无需修改；取其地址或依赖K_SYSCALL_K_SLEEP、K_SYSCALL_K_USLEEP的树外代码，必须改用[k_sleep_ticks()](../thread_core_reference/P001_线程公共接口.md#ga5ad6bcbcf89f9a9fbf6929388e2a7842)。注意：从K_FOREVER提前唤醒时，k_sleep_ticks()报告K_TICKS_FOREVER，而[k_sleep()](../thread_core_reference/P001_线程公共接口.md#ga093ac91db17ec33696168801d01efe75)返回-1。
- sys_port_trace_k_thread_sleep_*()、sys_port_trace_k_thread_msleep_*()及sys_port_trace_k_thread_usleep_*()钩子，替换为sys_port_trace_k_thread_sleep_ticks_enter()及sys_port_trace_k_thread_sleep_ticks_exit()，因为这四个休眠函数中现在仅[k_sleep_ticks()](../thread_core_reference/P001_线程公共接口.md#ga5ad6bcbcf89f9a9fbf6929388e2a7842)不是内联函数。退出钩子以节拍（Tick）报告剩余休眠时间；原来以毫秒展示的后端应转换单位，例如使用[k_ticks_to_ms_ceil64()](../timeutil_reference/P007_时间单位辅助接口.md#gabee58122304820b36d601268eb4598e2)。定义旧钩子的树外跟踪后端必须更新。
- [k_futex](../userspace_sync_reference/P002_Futex结构.md)不再是内核对象，对应K_OBJ_FUTEX类型已移除。任意用户可访问的内存均可用作futex地址，futex操作不再产生-EINVAL错误。
- [对象核心框架（Object Core Framework）](../kernel/P048_内核对象核心.md#object-cores-api)不再通过对象内的节点将对象链接到按类型划分的链表。静态对象直接原位枚举；运行时初始化的对象由容量为[CONFIG_OBJ_CORE_MAX_DYNAMIC_OBJECTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OBJ_CORE_MAX_DYNAMIC_OBJECTS)的有界注册表引用。[k_obj_core](../object_core_reference/P005_对象核心结构.md)的node成员及[k_obj_type](../object_core_reference/P007_对象类型结构.md)的list成员已移除，遍历这些链表的工具须改用[k_obj_type_walk_locked()](../object_core_reference/P001_对象核心公共接口.md#ga51b320f0e50bda2352ad3b5c4874385e)或[k_obj_type_walk_unlocked()](../object_core_reference/P001_对象核心公共接口.md#ga539bed22f047bff5786599bd16187414)。K_OBJ_TYPE_DEFINE现在直接定义[k_obj_type](../object_core_reference/P007_对象类型结构.md)变量，必须删除该变量的单独声明。线程栈或中断栈中的对象不再注册；[CONFIG_OBJ_CORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OBJ_CORE)会选择[CONFIG_THREAD_STACK_INFO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_THREAD_STACK_INFO)，因此每个[k_thread](../thread_core_reference/P004_线程对象结构.md)都增加栈信息字段。新选项[CONFIG_OBJ_CORE_QUEUE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OBJ_CORE_QUEUE)默认启用，会为每个[k_queue](../queue_reference/P002_内核队列结构.md)添加对象核心；FIFO及LIFO内部嵌入队列，因此会同时以自身类型及队列类型报告。
- 对象跟踪（[CONFIG_TRACING_OBJECT_TRACKING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING_OBJECT_TRACKING)）现在由对象核心框架提供，并自动选择该框架。_track_list_k_*链表头、SYS_PORT_TRACK_NEXT()宏、sys_track_*_init()钩子及include/zephyr/tracing/tracking.h已移除。遍历跟踪链表的代码必须先用[k_obj_type_find()](../object_core_reference/P001_对象核心公共接口.md#ga325c21774af7d3f092dcab17d8f260fd)找到对象类型，再使用[k_obj_type_walk_locked()](../object_core_reference/P001_对象核心公共接口.md#ga51b320f0e50bda2352ad3b5c4874385e)或[k_obj_type_walk_unlocked()](../object_core_reference/P001_对象核心公共接口.md#ga539bed22f047bff5786599bd16187414)。

<a id="boards"></a>

## [开发板（Boards）](#id8)


- NXP LPC54xxx的CONFIG_LPC54XXX_SRAM2_CLOCK替换为CONFIG_SOC_SERIES_LPC54XXX_SRAM_CLOCKS。当系列中仅支持LPC54114时，CMSIS SystemInit()只启用SRAM2，旧名称合适；LPC546xx会同时启用SRAM2及SRAM3，因此选项现在涵盖多个存储体。新旧选项均默认y。配置若曾给旧符号赋值，必须更新，否则无法构建。
- RP2040及RP2350的vreg节点，即[raspberrypi,core-supply-regulator](../hardware/P654_RaspberryPi内核供电稳压器绑定.md#dtbinding-raspberrypi-core-supply-regulator)，现在默认禁用，不再是okay。需要此稳压器的树外开发板必须将&vreg节点设置为status = "okay"。

  RP2040的SoC DTSI现在默认设置regulator-always-on及regulator-allowed-modes = <REGULATOR_RPI_PICO_MODE_NORMAL>。此前明确设置它们的开发板可删除这些行。（[GitHub #114751](https://github.com/zephyrproject-rtos/zephyr/issues/114751)）
- RP2350，即rpi_pico系列的cpucluster限定符hazard3及m33已弃用，改为hazard3_0及m33_0，明确标识CPU0，为双核支持做准备。所有树内RP2350开发板已迁移，例如rpi_pico2/rp2350a/m33改为rpi_pico2/rp2350a/m33_0。使用旧限定符的树外开发板应重命名开发板文件，更新board.yml的cpucluster:条目，并将Kconfig select语句改为SOC_RP2350[AB]_HAZARD3_0或SOC_RP2350[AB]_M33_0。soc.yml中旧hazard3/m33条目及对应SOC_RP2350[AB]_HAZARD3/_M33符号已弃用，均将在未来版本移除。
- RAK4631 WisBlock核心模块现在支持WisBlock生态。要暴露传感器及IO插槽，需要配合WisBlock底板扩展板，例如RAK19007 WisBlock第二代底板：（[RAK4631 WisBlock核心模块（Core Module）](../boards_rak_raspberry_raytac/P006_RAK4631_WisBlock_Core_Module.md#rak4631)；[RAK19007第二代WisBlock基板（Base Board 2nd Gen）](../boards_shields/P147_RAK19007_WisBlock_Base_Board_2nd_Gen.md#rakwireless-rak19007)）

  ```text
  west build -b rak4631/nrf52840 --shield rakwireless_rak19007
  ```
- [CONFIG_SRAM_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SRAM_SIZE)及[CONFIG_SRAM_BASE_ADDRESS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SRAM_BASE_ADDRESS)已弃用。开发板应通过设备树zephyr.sram chosen节点指定使用的RAM节点，其值此前用于填充这两个Kconfig值。若手动调整任一选项，将设置[CONFIG_SRAM_DEPRECATED_KCONFIG_SET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SRAM_DEPRECATED_KCONFIG_SET)以标识弃用用法。译注：原文将chosen名称写为zephyr.sram；此处保留原文，常见设备树属性名为zephyr,sram。
- Nordic内部SoC平台符号NRF_PLATFORM_HALTIUM及NRF_PLATFORM_LUMOS不再被树内代码使用，改为明确检查[CONFIG_SOC_SERIES_NRF54H](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54H)、[CONFIG_SOC_SERIES_NRF92](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)、[CONFIG_SOC_SERIES_NRF54L](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)及[CONFIG_SOC_SERIES_NRF71](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)。两个旧符号作为弃用兼容占位保留：选中对应系列且启用[CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_PLATFORM_DEPRECATED_SYMBOLS)时默认y，因此现有CONFIG_NRF_PLATFORM_*=y及depends on NRF_PLATFORM_*仍可构建，但产生弃用警告。使用它们的树外Kconfig、CMake及代码应更新：


  - CONFIG_NRF_PLATFORM_HALTIUM替换为[CONFIG_SOC_SERIES_NRF54H](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54H)或[CONFIG_SOC_SERIES_NRF92](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)。
  - CONFIG_NRF_PLATFORM_LUMOS替换为[CONFIG_SOC_SERIES_NRF54L](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)或[CONFIG_SOC_SERIES_NRF71](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)。
- Aesc Silicon的elemrv开发板改名为elemrv_flask_n。
- STMicroelectronics的stm32mp157c_dk2改名为stm32mp157x_dk2，现在同时引用两个SoC变体。STM32MP157C-DK2使用-b stm32mp157x_dk2/stm32mp157cxx构建；STM32MP157F-DK2使用-b stm32mp157x_dk2/stm32mp157fxx。旧-b stm32mp157c_dk2已弃用，现在映射到stm32mp157x_dk2/stm32mp157cxx。
- Infineon的kit_psc3m6_evk改名为kit_psc3m6_eval。旧-b kit_psc3m6_evk及-b kit_psc3m6_evk/psc3m6ges3ahq1已弃用，分别映射到kit_psc3m6_eval及kit_psc3m6_eval/psc3m6ges3ahq1。
- Nordic sysbuild选项SB_CONFIG_NRF_HALTIUM_GENERATE_UICR改名为SB_CONFIG_NRF_GENERATE_UICR，需更新sysbuild配置。
- Nordic SoC头文件<haltium_power.h>及<haltium_pm_s2ram.h>，分别改名为<soc_power.h>及<soc_pm_s2ram.h>。旧名称的转发头文件仍可用，但会通过#warning提示新包含路径。使用旧路径的树外代码应更新：


  - #include <haltium_power.h>改为#include <soc_power.h>。
  - #include <haltium_pm_s2ram.h>改为#include <soc_pm_s2ram.h>。
- STM32H7RS开发板stm32h7s78_dk及nucleo_h7s3l8的系统时钟提高到600 MHz，通过将PLL1频率提高到300 MHz实现；这也影响总线及内核时钟，使其频率略有提高。
- 大多数STM32开发板不再默认启用[CONFIG_GPIO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。使用GPIO占用节点（GPIO Hogs）的开发板仍启用，因为这些节点需要GPIO。依赖默认CONFIG_GPIO=y的应用必须明确启用该选项。（[GitHub #109468](https://github.com/zephyrproject-rtos/zephyr/issues/109468)）
- 使用UF2镜像的开发板迁移到[zephyr,mapped-partition](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)时，应在默认配置中启用[CONFIG_BUILD_OUTPUT_HEX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_OUTPUT_HEX)，因为UF2生成无法再通过[CONFIG_FLASH_LOAD_OFFSET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_LOAD_OFFSET)确定BIN输出的代码地址。现在默认从HEX而非BIN生成UF2。（[GitHub #107944](https://github.com/zephyrproject-rtos/zephyr/issues/107944)）
- Ezurio的bl54l15u_dvk已移除。bl54l15_dvk仍可用，同时支持bl54l15及bl54l15u模块变体，功能相同。原目标的用户应按需迁移到bl54l15_dvk/nrf54l15/cpuapp或bl54l15_dvk/nrf54l15/cpuflpr。
- stm32h573i_dk及b_u585i_iot02a的默认MCUboot签名类型从RSA-3072改为EC-P256，影响在TF-M中启用MCUboot，即[CONFIG_TFM_BL2](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_BL2)的构建。若继续使用RSA-3072，须将[CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE)设为"RSA-3072"；否则请确保拥有与当前签名类型匹配的自有签名密钥。
- modules/hal_silabs/gecko下全部SOC_GECKO_*选项改名为SILABS_GECKO_*，请相应调整开发板。
- 所有Silabs Series 0及Series 1开发板现在必须在设备树中指定时钟配置。CONFIG_SOC_GECKO_HAS_HFRCO_FREQRANGE及CONFIG_CMU_*已移除，适配示例见[GitHub #111754](https://github.com/zephyrproject-rtos/zephyr/issues/111754)。
- nRF54LM20 DK上的nrf7002eb2扩展板及其nrf7002eb2_nrf7001、nrf7002eb2_nrf7000变体，不再重定向应用控制台。此前为绕过仅在预生产套件存在、量产nRF54LM20 DK不存在的引脚冲突，会禁用UART20，将Shell、mcumgr及蓝牙监控器控制台改接UART30。现在控制台留在UART20，即VCOM1，与标准开发板行为一致，也不再删除button3/sw3。已有用户必须将串口终端从VCOM0改回VCOM1。nRF54L15 DK不受影响：其扩展排针确实与UART20冲突，因此仍重定向到UART30。
- mimxrt1180_evk的NXP_BOARD_SPECIFIC_MPU_SETTINGS选项改名为CONFIG_BOARD_NXP_SPECIFIC_MPU_SETTINGS，与其他NXP开发板选项及frdm_imxrt1186采用的BOARD_NXP_*命名一致。设置CONFIG_NXP_BOARD_SPECIFIC_MPU_SETTINGS的配置必须更新为新名称。
- 支持通过TF-M更新固件的开发板，现在必须选择[CONFIG_TFM_PARTITION_FIRMWARE_UPDATE_SUPPORTED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_PARTITION_FIRMWARE_UPDATE_SUPPORTED)。
- 原本默认启用[CONFIG_SPI_STM32_INTERRUPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_STM32_INTERRUPT)的STM32开发板现已取消此默认值。SPI使用中断还是轮询传输由应用决定。在受影响开发板上依赖中断驱动SPI的应用，例如不使用DMA而调用[spi_transceive_signal()](../hardware/P318_SPI公共接口.md#ga41b8a541257c0d45575fdc4593417edc)或[spi_transceive_cb()](../hardware/P318_SPI公共接口.md#ga6114e63ca23b82f9be0ac70e372b878b)，现在必须在自己的配置中明确启用[CONFIG_SPI_STM32_INTERRUPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_STM32_INTERRUPT)。（[GitHub #116218](https://github.com/zephyrproject-rtos/zephyr/issues/116218)）
- 以下在v4.3或更早版本弃用的开发板名称别名已移除（[GitHub #116657](https://github.com/zephyrproject-rtos/zephyr/issues/116657)、[GitHub #116750](https://github.com/zephyrproject-rtos/zephyr/issues/116750)）。应直接为别名此前重定向的开发板目标构建：


  - arduino_uno_r4_minima改用arduino_uno_r4@minima。
  - arduino_uno_r4_wifi改用arduino_uno_r4@wifi。
  - esp32c6_devkitc改用esp32c6_devkitc/esp32c6/hpcore。
  - esp32_devkitc_wroom/esp32/procpu及esp32_devkitc_wrover/esp32/procpu改用esp32_devkitc/esp32/procpu。
  - esp32_devkitc_wroom/esp32/appcpu及esp32_devkitc_wrover/esp32/appcpu改用esp32_devkitc/esp32/appcpu。
  - neorv32改用neorv32/neorv32/up5kdemo。
  - panb511evb改用panb611evb。
  - raytac_an54l15q_db/nrf54l15/cpuapp改用raytac_an54lq_db_15/nrf54l15/cpuapp。
  - scobc_module1改用scobc_a1。
  - xiao_esp32c6改用xiao_esp32c6/esp32c6/hpcore。
- Nordic nRF52选项CONFIG_GPIO_AS_PINRESET已移除，改为在&uicr设备树节点设置gpio-as-nreset属性。
- Nordic选项CONFIG_SOC_DCDC_NRF52X、CONFIG_SOC_DCDC_NRF52X_HV、CONFIG_SOC_DCDC_NRF53X_APP、CONFIG_SOC_DCDC_NRF53X_NET及CONFIG_SOC_DCDC_NRF53X_HV已移除。改为在设备树中配置稳压器：在&reg1、&vregmain或&vregradio上设置regulator-initial-mode = <NRF5X_REG_MODE_DCDC>，在&reg0或&vregh上设置status = "okay"。
- Nordic nRF53选项CONFIG_BOARD_ENABLE_CPUNET已移除，改用[CONFIG_SOC_NRF53_CPUNET_ENABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_CPUNET_ENABLE)。
- esp_threadbr_ethernet扩展板已移除。已有用户应为esp_threadbr/esp32s3/procpu/ethernet构建，替代esp_threadbr/esp32s3/procpu与SHIELD=esp_threadbr_ethernet的组合。esp_threadbr子板连接器描述也一并移除，因此espressif,esp-threadbr-header绑定、esp_threadbr_header GPIO连接映射节点（Nexus Node）、esp_threadbr_spi及esp_threadbr_i2c设备树标签均已删除。树外覆盖文件必须直接引用SoC节点&spi2、&i2c0、&gpio0或&gpio1。（[GitHub #116956](https://github.com/zephyrproject-rtos/zephyr/issues/116956)）
- STM32MP15 Cortex-M4 SoC符号SOC_STM32MP15_M4改名为CONFIG_SOC_STM32MP157CXX_M4。此前选择旧符号的树外STM32MP15开发板必须改选新符号。（[GitHub #118151](https://github.com/zephyrproject-rtos/zephyr/issues/118151)）
- Arduino UNO R4 WiFi的zephyr,console及zephyr,shell-uart现在默认使用SCI9，而非D0/D1排针上的SCI2。板载ESP32-S3将SCI9以USB CDC ACM端口形式桥接到USB-C，因此无需外部USB转串口适配器，即可在烧录所用端口看到控制台输出。依赖D0/D1控制台的应用可通过设备树覆盖文件重新选择：

  ```text
  / {
      chosen {
          zephyr,console = &uart2;
          zephyr,shell-uart = &uart2;
      };
  };
  ```

  Arduino UNO R4 Minima不受影响。（[GitHub #118433](https://github.com/zephyrproject-rtos/zephyr/issues/118433)）
- Espressif按模块划分的设备树包含文件及对应SoC Kconfig符号已移除。模块或系统级封装（SiP）料号描述开发板搭载多少Flash及PSRAM，属于开发板而非SoC属性，因此现在均由开发板自身声明。

  每个espressif/<soc>/<soc>_<module>.dtsi文件，替换为该SoC共用的espressif/<soc>/<soc>.dtsi。SOC_ESP32S3_WROOM_N8及SOC_ESP32_WROVER_E_N16R8等对应隐藏符号，替换为[CONFIG_SOC_ESP32S3](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32S3)等普通SoC符号。SOC_PART_NUMBER现在报告SoC而非模块。

  树外Espressif开发板必须完成以下更新，否则无法构建：


  - 包含普通SoC DTSI，替代模块DTSI。
  - 在Kconfig.<board>中选择普通SoC符号。
  - 在开发板DTS中描述Flash，同时提供reg及匹配的ranges，因为SoC DTSI不再设置二者。

    ```text
    &flash0 {
        reg = <0x0 DT_SIZE_M(8)>;
        ranges = <0x0 0x0 DT_SIZE_M(8)>;
    };
    ```
  - 若开发板搭载PSRAM，以同样方式描述：

    ```text
    &psram0 {
        size = <DT_SIZE_M(2)>;
    };
    ```

  双核ESP32的espressif/esp32/esp32_appcpu.dtsi也不再设置Flash，因此APPCPU开发板DTS必须声明与对应PROCPU相同的Flash。
- NXP S32K148的ENET节点enet（[nxp,enet](../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet)）、enet_mac（[nxp,enet-mac](../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac)）、enet_mdio（[nxp,enet-mdio](../ethernet_mdio_microchip_binding_reference/P002_nxp_enet-mdio.md#std-dtcompatible-nxp-enet-mdio)）及enet_ptp_clock（[nxp,enet-ptp-clock](../ethernet_nxp_phy_binding_reference/P002_nxp_enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock)）现在默认禁用，不再是okay。使用以太网的树外开发板必须将这些节点设为status = "okay"。
- mimxrt1170_evk及mimxrt1160_evk的cm7目标，以及frdm_imxrt1152，现在提供静态Arm内存保护单元（MPU）区域表，并默认启用[CONFIG_ARM_MPU_CM7_UNMAPPED_REGION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU_CM7_UNMAPPED_REGION)。因此MPU不再回退到PRIVDEFENA背景映射，表外地址不再可访问。该表覆盖ITCM、DTCM、双核板上与CM4共享的OCRAM镜像区域、zephyr,sram chosen节点对应RAM、FlexSPI NOR窗口及外设地址窗口，但不覆盖其余片上存储体：mimxrt1170_evk及frdm_imxrt1152的ocram1、ocram2，以及mimxrt1160_evk的ocram_combined。

  在这些存储体中放置数据的应用，必须通过带zephyr,memory-attr的节点明确声明，随后会为其分配独立MPU区域；树内samples/subsys/ipc示例对与CM4共享的内存即采用这种方式。将[CONFIG_ARM_MPU_CM7_UNMAPPED_REGION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU_CM7_UNMAPPED_REGION)设为n可恢复旧行为。
- Silabs选项CONFIG_SOC_SILABS_IMAGE_PROPERTIES改名为[CONFIG_SOC_VENDOR_SILABS_IMAGE_PROPERTIES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_IMAGE_PROPERTIES)。
- Silabs选项CONFIG_SOC_SILABS_PM_LOW_INTERRUPT_LATENCY改名为[CONFIG_SOC_VENDOR_SILABS_PM_LOW_INTERRUPT_LATENCY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_PM_LOW_INTERRUPT_LATENCY)。
- stm32h573i_dk及stm32h5f5j_dk探索套件现在采用MSPI控制器模型，这是STM32迁移到MSPI支持的下一步。两块板均应将xspi节点声明为st,stm32-xspi-controller兼容项。
- stm32l562e及stm32h735g_disco套件现在采用MSPI控制器模型，这是STM32迁移到MSPI支持的下一步。应将ospi节点声明为st,stm32-ospi-controller兼容项。待所有目标开发板更新后，再更新stm32l5及stm32h735器件DTS。

<a id="device-drivers-and-devicetree"></a>

## [设备驱动与设备树（Device Drivers and Devicetree）](#id9)


- 声明任何上游驱动类别的设备驱动API实例时，现在必须使用[DEVICE_API](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)宏，树外驱动也不例外。[DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)现在断言API属于请求的类别，因此实例必须位于该类别的可迭代段（Iterable Section）。树外驱动类别若将上游API嵌入为首个成员，还必须通过[DEVICE_API_EXTENDS](../device_reference/P007_设备模型头文件参考.md#a2b0530c13706c66229d35977c6553db9)声明继承关系，使针对父类别的[DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)可用于实现子API的设备。详见[驱动API（Driver APIs）](https://docs.zephyrproject.org/latest/kernel/drivers/index.html#device-driver-api)。

<a id="adc"></a>

### [模数转换器（ADC）](#id10)


- [microchip,xec-adc](../hardware/P860_MicrochipXEC模数转换器绑定.md#dtbinding-microchip-xec-adc)原来为数组类型的girqs及pcrs属性，替换为编码后的girqs及整数类型pcr-scr。girqs使用MCHP_XEC_ECIA_GIRQ_ENC宏，pcr-scr编码PCR寄存器索引及位位置。（[GitHub #105658](https://github.com/zephyrproject-rtos/zephyr/issues/105658)）
- [CONFIG_LPADC_DO_OFFSET_CALIBRATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LPADC_DO_OFFSET_CALIBRATION)现在仅在启用[CONFIG_ADC_MCUX_LPADC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_MCUX_LPADC)时有意义，默认y也仅在该条件下生效。树内开发板不再在默认配置中明确启用，因为默认值已涵盖它们。
- CONFIG_LPADC_CHANNEL_COUNT已移除。NXP LPADC驱动现在将硬件命令槽视为逻辑ADC通道，并根据每个实例在设备树中声明的通道子节点推导逻辑通道数量，使未使用的命令槽不再占用RAM。此前通过调低该选项节省RAM的应用只需删除它。未声明任何通道节点的实例仍提供全部硬件容量，因此只在运行时通过[adc_channel_setup()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7bc0488b2d08ae2ee4996c0eed11f0bf)配置通道的应用不受影响；混合使用两种方式的应用，必须在设备树中声明运行时设置的最高通道编号。通道编号超过SoC实现的CMD寄存器数量时，现在产生构建错误，而非运行时HAL断言；[adc_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7567ce3b03ebb294620b4e32b7561ab3)对空通道掩码或选择越界通道的掩码，现在返回-EINVAL，不再静默忽略。（[GitHub #116995](https://github.com/zephyrproject-rtos/zephyr/issues/116995)）

<a id="analog-devices"></a>

### [亚德诺半导体（Analog Devices）](#id11)


- 所有MAX32 SoC的[CONFIG_NUM_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)现在使用Kconfig预处理函数dt_highest_controller_irq_number，根据设备树中已启用，即status = "okay";的设备自动计算。原先按SoC硬编码的值已移除，生成的IRQ表通常显著缩小。通过[IRQ_CONNECT()](../fatal_irq_reference/P007_中断服务接口.md#ga131739d1faf501a15590053817aba984)注册自定义ISR的应用，可能因[CONFIG_NUM_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)变小而遇到如下构建错误：

  ```text
  gen_isr_tables.py: error: IRQ 88 (offset=0) exceeds the maximum of 54
  ```

  明确将[CONFIG_NUM_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NUM_IRQS)设置为适当值即可解决；[以下文档页](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#setting-configuration-values)说明具体方法。

  通过[irq_connect_dynamic()](../fatal_irq_reference/P007_中断服务接口.md#ga4e9915b92b09df49b99bc449f0cc31a1)在运行时安装ISR的应用，不在该构建时检查覆盖范围内，必须人工核查。

<a id="audio-codec"></a>

### [音频编解码器（Audio Codec）](#id12)


- 音频编解码器（Audio Codec）驱动后端API现在使用[audio_codec_driver_api](https://docs.zephyrproject.org/latest/doxygen/html/structaudio__codec__driver__api.html)，替代struct audio_codec_api。

  树外音频编解码器驱动必须重命名后端API结构体定义，并将API实例改为DEVICE_API(audio_codec, ...)。树内驱动更新示例见[GitHub #110631](https://github.com/zephyrproject-rtos/zephyr/issues/110631)。使用audio_codec_... API的应用代码不受影响。

<a id="clock-control"></a>

### [时钟控制（Clock Control）](#id13)


- Nordic选项CONFIG_NRFS_LOCAL_DOMAIN_DVFS_SCALE_DOWN_AFTER_INIT已移除，改用[CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_REQ_LOW_FREQ](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_REQ_LOW_FREQ)。
- [nxp,imxrt11xx-arm-pll](../clock_nxp_pico_realtek_renesas_binding_reference/P001_nxp_imxrt11xx-arm-pll.md#std-dtcompatible-nxp-imxrt11xx-arm-pll)绑定现在使用loop-div及post-div配置ARM PLL。旧clock-mult及clock-div仍支持，但已弃用。现有RT11xx覆盖文件应按loop-div = clock-mult * 2、post-div = clock-div更新。
- SiWx91x时钟控制拆为三个管理器：[silabs,siwx91x-cmu-aon](../clock_silabs_ti_xilinx_binding_reference/P012_silabs_siwx91x-cmu-aon.md#std-dtcompatible-silabs-siwx91x-cmu-aon)、[silabs,siwx91x-cmu-ulp](../clock_silabs_ti_xilinx_binding_reference/P014_silabs_siwx91x-cmu-ulp.md#std-dtcompatible-silabs-siwx91x-cmu-ulp)及[silabs,siwx91x-cmu-hp](../clock_silabs_ti_xilinx_binding_reference/P013_silabs_siwx91x-cmu-hp.md#std-dtcompatible-silabs-siwx91x-cmu-hp)。旧silabs,siwx91x-clock绑定及clock0节点已移除。树外开发板及覆盖文件必须将clocks的phandle更新到对应时钟管理单元（CMU），并采用siwx91x-clock.h中的新SIWX91X_CLK_*标识。例如clocks = <&clock0 SIWX91X_CLK_UART0>;改为clocks = <&cmu_hp SIWX91X_CLK_UART0>;。

<a id="clock-control-nrf-deprecation"></a>

#### nRF时钟控制弃用说明（Clock Control nRF Deprecation）

时钟控制驱动已针对nRF52、nRF53、nRF91及nRF54L系列的以下时钟更新：（[时钟控制（Clock Control）](https://docs.zephyrproject.org/latest/hardware/peripherals/clock_control.html#clock-control-api)）


- 高频时钟（HFCLK）
- 低频时钟（LFCLK）
- 晶体振荡器（XO）
- 24 MHz晶体振荡器（XO24M）
- 192 MHz高频时钟（HFCLK192M）
- 音频高频时钟（HFCLKAUDIO）

若要恢复旧驱动实现，将[CONFIG_CLOCK_CONTROL_NRF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF)设为y。

将代码从Zephyr v4.4.0迁移到v4.5.0时，完成以下步骤：


1. 在应用或开发板专用设备树覆盖文件中，启用由应用控制的每个时钟。

  这会启用对应时钟驱动，例如：

  ```text
  /* if nRF54L XO is to be controlled */
  &xo {
      status = "okay";
  };

  /* if nRF52, nRF53 HFCLK is to be controlled */
  &hfclk {
      status = "okay";
  };

  /* if nRF52, nRF53, nRF91 or nRF54L LFCLK is to be controlled */
  &lfclk {
      status = "okay";
  };

  /* if HFCLK192M is to be controlled */
  &hfclk192m {
      status = "okay";
  };

  /* if XO24M is to be controlled */
  &xo24m {
      status = "okay";
  };

  /* if HFCLKAUDIO is to be controlled */
  &hfclkaudio {
      status = "okay";
  };
  ```
2. 重命名以下Kconfig选项：


  - CONFIG_NRFX_CLOCK_USE_LFRC_CALIBRATION替换为CONFIG_NRFX_CLOCK_LFCLK_USE_LFRC_CALIBRATION。
  - [CONFIG_NRFX_CLOCK_LF_CAL_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_CAL_ENABLED)替换为[CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC_CALIBRATION)。
3. 将以下Kconfig选项迁移到nordic,nrf-clock-lfclk设备树节点：


  - [CONFIG_CLOCK_CONTROL_NRF_K32SRC_FREQUENCY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_K32SRC_FREQUENCY)替换为k32src-frequency属性。
  - [CONFIG_CLOCK_CONTROL_NRF_SOURCE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_SOURCE)选择项替换为k32src枚举属性。
  - CLOCK_CONTROL_NRF_K32SRC_RC及NRFX_CLOCK_LF_SRC_RC替换为k32src = "rc"。
  - CLOCK_CONTROL_NRF_K32SRC_XTAL及NRFX_CLOCK_LF_SRC_XTAL替换为k32src = "xtal"。
  - CLOCK_CONTROL_NRF_K32SRC_SYNTH及NRFX_CLOCK_LF_SRC_SYNTH替换为k32src = "synth"。
  - CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING及NRFX_CLOCK_LF_SRC_LOW_SWING替换为k32src = "ext_low_swing"。
  - CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING及NRFX_CLOCK_LF_SRC_FULL_SWING替换为k32src = "ext_full_swing"。
  - [CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_ACCURACY_PPM)选择项替换为k32src-accuracy-ppm枚举属性。
  - CLOCK_CONTROL_NRF_K32SRC_500PPM替换为k32src-accuracy-ppm = <500>。
  - CLOCK_CONTROL_NRF_K32SRC_250PPM替换为k32src-accuracy-ppm = <250>。
  - CLOCK_CONTROL_NRF_K32SRC_150PPM替换为k32src-accuracy-ppm = <150>。
  - CLOCK_CONTROL_NRF_K32SRC_100PPM替换为k32src-accuracy-ppm = <100>。
  - CLOCK_CONTROL_NRF_K32SRC_75PPM替换为k32src-accuracy-ppm = <75>。
  - CLOCK_CONTROL_NRF_K32SRC_50PPM替换为k32src-accuracy-ppm = <50>。
  - CLOCK_CONTROL_NRF_K32SRC_30PPM替换为k32src-accuracy-ppm = <30>。
  - CLOCK_CONTROL_NRF_K32SRC_20PPM替换为k32src-accuracy-ppm = <20>。
  - [CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED)替换为k32src = "xtal"、k32src = "ext_low_swing"或k32src = "ext_full_swing"。
4. 更新应用，使用新的时钟控制API。

  更新API调用时，使用以下对应关系：


  - mgr是为nordic,nrf-clock创建、通过z_nrf_clock_control_get_onoff取得的开关管理器（On-off Manager）。
  - dev是兼容nordic,nrf-clock的设备。
  - sys是nordic,nrf-clock的子系统。

    新的时钟实现不使用它。
  - new_dev是对应此前sys值的设备，必须与以下节点之一兼容：


    - `nordic,nrf-clock-lfclk`
    - `nordic,nrf-clock-hfclk`
    - `nordic,nrf-clock-xo`
    - `nordic,nrf-clock-hfclk192m`
    - `nordic,nrf-clock-xo24m`
    - `nordic,nrf-clock-hfclkaudio`

  以下示例展示已弃用的API用法及对应的新API用法：

  ```text
  // Old API usage (deprecated)
  z_nrf_clock_calibration_init(&mgrs);    //1
  onoff_release(mgr)                      //2
  onoff_request(mgr, &cli);               //3
  onoff_cancel_or_release(mgr, &cli);     //4
  clock_control_on(dev,sys)               //5
  clock_control_off(dev,sys)              //6
  clock_control_async_on(dev,sys)         //7
  clock_control_get_status(dev,sys)       //8
  z_nrf_clock_control_get_onoff(sys)      //9

  // New API usage
  z_nrf_clock_calibration_init();                             //1
  nrf_clock_control_release(new_dev, NULL);                   //2
  nrf_clock_control_request(new_dev, NULL, &cli);             //3
  nrf_clock_control_cancel_or_release(new_dev, NULL, &cli);   //4
  clock_control_on(new_dev, NULL)                             //5
  clock_control_off(new_dev, NULL)                            //6
  clock_control_async_on(new_dev, NULL)                       //7
  clock_control_get_status(new_dev, NULL)                     //8
  // Remove all uses of z_nrf_clock_control_get_onoff         //9
  ```

<a id="comparator"></a>

### [比较器（Comparator）](#id14)


- [nxp,kinetis-acmp](../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp)中已弃用的nxp,前缀属性已移除。请改用enable-pin-out、use-unfiltered-output、enable-high-speed-mode、filter-enable-sample、filter-count、filter-period及enable-window-mode。

<a id="controller-area-network-can"></a>

### [控制器局域网（Controller Area Network，CAN）](#id15)


- NXP SJA1000及Bosch M_CAN控制器驱动后端的头文件can_sja1000.h及can_mcan.h，已改为库专用包含路径。基于这些后端的树外驱动需要相应更新#include指令。
- Bosch M_CAN驱动现在只通过RX FIFO0处理收到的CAN帧，保证按总线接收顺序处理。树外用户可考虑更新bosch,mram-cfg设备树覆盖属性，将全部FIFO元素分配给RX FIFO0。
- 已弃用的CAN控制器属性bus-speed及bus-speed-data已移除，分别改用bitrate及bitrate-data。
- CAN控制器驱动操作表不再包含can_set_state_change_callback_t函数指针，因为回调添加及移除现在由通用API [can_add_state_change_callback()](../hardware/P362_CAN控制器接口.md#gace0dd2797a133bd293d34a9ac5348e2a)和[can_remove_state_change_callback()](../hardware/P362_CAN控制器接口.md#ga5c1c7633e020aec2936a6ce3ba68b256)处理。树外驱动可删除原操作，或按需替换为can_state_change_callbacks_enabled_t。驱动现在必须通过[can_fire_state_change_callbacks()](../hardware/P369_CAN控制器后端接口.md#gaba24cc4eb2fa759ff8394dd096021982)触发CAN控制器状态变化回调。（[GitHub #117889](https://github.com/zephyrproject-rtos/zephyr/issues/117889)）
- CAN总线网络驱动[CONFIG_NET_CANBUS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CANBUS)现在为每个由[CAN_DEVICE_DT_DEFINE](../hardware/P362_CAN控制器接口.md#ga599d0695abe481411660d7af2893f4a5)或[CAN_DEVICE_DT_INST_DEFINE](../hardware/P362_CAN控制器接口.md#ga20266dc5e962922144e078b85ccb8351)定义的CAN控制器设备创建网络接口，替代只为zephyr,canbus chosen节点创建一个接口。

<a id="counter"></a>

### [计数器（Counter）](#id16)


- [nxp,lpc-ctimer](../nxp_nuvoton_counter_binding_reference/P009_nxp_lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer)现在通过通用多路复用（Mux）子系统路由输入捕获信号。input[mux](https://docs.zephyrproject.org/latest/hardware/peripherals/mux.html#mux-api)-connections已移除；应使用INPUTMUX控制器节点[nxp,inputmux](../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux)描述路由，再通过定时器节点的mux-states引用。描述单元布局不变，例如inputmux-connections = <&inputmux0 0 0x06000024>;改为mux-states = <&inputmux0 0 0x06000024>;。（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
- [nxp,lptmr](../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr)的prescaler已移除，改用prescale-glitch-filter及prescale-glitch-filter-bypass。新属性是指数而非除数：预分频器的实际除数为2^(prescale-glitch-filter + 1)。
- [adi,max32-rtc-counter](../counter_binding_reference/P002_adi_max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter)及[adi,max32-wut](../counter_binding_reference/P003_adi_max32-wut.md#std-dtcompatible-adi-max32-wut)现在使用共享clk_32k节点选择32 kHz时钟源，通过clk_32k的clocks属性配置，替代各外设节点的clock-source属性。（[GitHub #117709](https://github.com/zephyrproject-rtos/zephyr/issues/117709)）
- NXP RTC计数器驱动[nxp,rtc](../soc_rtc_binding_reference/P002_nxp_rtc.md#std-dtcompatible-nxp-rtc)、[nxp,lpc-rtc](../microchip_microcrystal_nxp_rtc_binding_reference/P013_nxp_lpc-rtc.md#std-dtcompatible-nxp-lpc-rtc)及[nxp,imx-snvs-rtc](../nxp_nuvoton_counter_binding_reference/P006_nxp_imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc)，现在在绝对闹钟设置过晚时，从[counter_set_channel_alarm()](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__interface.html#ga00a2857d993a84a56e8e222727f3d85e)返回-ETIME而非-EINVAL，以符合计数器API约定。原来在此路径检查-EINVAL的应用应改查-ETIME。绝对目标等于当前计数值时，现在也报告过晚，即-ETIME；相对闹钟不再执行此检查。

<a id="devicetree"></a>

### [设备树（Devicetree）](#id17)


- int及array类型的设备树属性，若DTS源码使用负数字面量，例如<(-1)>，现在展开为负值，不再是以前的二进制补码无符号值。依赖旧无符号表示的代码，例如无符号比较或BUILD_ASSERT(DT_PROP(node, foo) > 0, ...)检查，必须改用有符号类型或能正确处理符号的检查。（[GitHub #107271](https://github.com/zephyrproject-rtos/zephyr/issues/107271)）
- zephyr,memory-region-mpu属性已移除，改用zephyr,memory-attr；新属性接受整数位掩码，而非字符串：

  ```text
  "RAM"         -> <DT_MEM_ARM_MPU_RAM>
  "RAM_NOCACHE" -> <DT_MEM_ARM_MPU_RAM_NOCACHE>
  "FLASH"       -> <DT_MEM_ARM_MPU_FLASH>
  "PPB"         -> <DT_MEM_ARM_MPU_PPB>
  "IO"          -> <DT_MEM_ARM_MPU_IO>
  "EXTMEM"      -> <DT_MEM_ARM_MPU_EXTMEM>
  ```

<a id="digital-microphone"></a>

### [数字麦克风（Digital Microphone）](#id18)


- 数字麦克风（DMIC）驱动后端API现在使用[dmic_driver_api](https://docs.zephyrproject.org/latest/doxygen/html/structdmic__driver__api.html)，替代struct _dmic_ops。

  树外DMIC驱动必须重命名后端API结构体定义，并将API实例改为DEVICE_API(dmic, ...)。树内更新示例见[GitHub #107695](https://github.com/zephyrproject-rtos/zephyr/issues/107695)。使用[dmic_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga09fc7074323c2f3115b06c5212d21fc7)、[dmic_trigger()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga051e82f30b76f0fca789ba0147054184)及[dmic_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga74b51bddaa175c518d45211f936d08e6)的应用代码不受影响。

<a id="disk"></a>

### [磁盘（Disk）](#id19)


- [CONFIG_NVME_REQUEST_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVME_REQUEST_TIMEOUT)的文档及取值范围以秒为单位，但NVMe请求超时路径以前未换算就与[k_uptime_get_32()](../timer_reference/P086_系统时钟公共接口.md#ga9253cfb7b46af4d8994349323ce9872b)的毫秒值比较，使默认值5约在5 ms而非5秒后超时。驱动现在在安排任务及检查到期前，通过MSEC_PER_SEC换算。若应用依赖旧的短超时行为，应复核所有非默认设置。（[GitHub #117809](https://github.com/zephyrproject-rtos/zephyr/issues/117809)）

<a id="display"></a>

### [显示（Display）](#id20)


- 用于选择SDL显示像素格式的CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_*选项已移除。改为在设备树SDL伪设备节点直接设置pixel-format，使用[include/zephyr/dt-bindings/display/panel.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/display/panel.h)中的PANEL_PIXEL_FORMAT_*宏。（[GitHub #104099](https://github.com/zephyrproject-rtos/zephyr/issues/104099)）
- LVGL选项CONFIG_LV_Z_COLOR_24_BGR_TO_RGB已移除。LVGL的RGB888在内存中按蓝、绿、红字节顺序存放，与[PIXEL_FORMAT_RGB_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)的内存布局一致，因此对报告该格式的显示器不再交换通道。若显示帧缓冲区要求红、绿、蓝顺序，必须报告[PIXEL_FORMAT_BGR_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4625a834a26894db2da3547635a6e172)，LVGL适配层会自动交换红蓝通道。
- 对报告[PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca0d12a0b6fd3df29b0a607eedf7671809)的显示器，LVGL现在直接使用RGB565_SWAPPED格式渲染，因此不再需要[CONFIG_LV_COLOR_16_SWAP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_COLOR_16_SWAP)，且不得同时启用，否则缓冲区会被交换字节两次。t_deck、m5stack_core2及wio_terminal不再默认启用此选项。
- ST7305及ST7306显示器的CONFIG_ST730X_POWERMODE_LOW选项已移除，改为切换设备节点的low-power-mode属性。
- ST7567驱动的set_contrast现在接受0～255对比度值，替代0～63；驱动会将其缩放到控制器要求的6位范围。CONFIG_ST7567_DEFAULT_CONTRAST也已更新以反映新范围。（[GitHub #112528](https://github.com/zephyrproject-rtos/zephyr/issues/112528)）
- [raspberrypi,bcm2711-framebuffer](../display_panel_renesas_sharp_binding_reference/P006_raspberrypi_bcm2711-framebuffer.md#std-dtcompatible-raspberrypi-bcm2711-framebuffer)现在要求pixel-format属性，并新增可选布尔属性red-blue-swap，表示面板要求BGR通道顺序。原来依靠固件协商像素顺序修正通道颠倒的开发板，也必须设置red-blue-swap。（[GitHub #115633](https://github.com/zephyrproject-rtos/zephyr/issues/115633)）
- [chipone,co5300](../compatible_binding_reference/P023_chipone_co5300.md#std-dtcompatible-chipone-co5300) MIPI DSI显示驱动不再维护内部影子帧缓冲区（Shadow Framebuffer），绑定中的pitch-align、addr-align及ext-ram已移除。原来依赖这些属性满足显示控制器对齐要求的开发板，应改为启用LVGL的[CONFIG_LV_Z_AREA_X_ALIGNMENT_WIDTH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_AREA_X_ALIGNMENT_WIDTH)及[CONFIG_LV_Z_AREA_Y_ALIGNMENT_WIDTH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_AREA_Y_ALIGNMENT_WIDTH)，使待重绘区域在传给驱动前按所需边界取整。（[GitHub #117765](https://github.com/zephyrproject-rtos/zephyr/issues/117765)）
- ssd16xx驱动现在报告[PIXEL_FORMAT_MONO01](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)而非[PIXEL_FORMAT_MONO10](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)，以匹配控制器RAM中置位表示白色像素的规则。LVGL及字符帧缓冲区无需更改即可按预期颜色绘制。若应用向[display_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3a5114b4537039fc4d3258678b82cd18)传入自有缓冲区，且曾为补偿旧格式而反相，现在必须移除反相操作。

<a id="dma"></a>

### [直接存储器访问（DMA）](#id21)


- silabs,siwx91x-dma改名为[silabs,udma](../stm32_ti_xilinx_dma_binding_reference/P003_silabs_udma.md#std-dtcompatible-silabs-udma)。Kconfig名称也相应更新：DMA_SILABS_SIWX91X改为DMA_SILABS_SIWX91X_UDMA，DMA_SILABS_SIWX91X_SG_BUFFER_COUNT改为DMA_SILABS_SIWX91X_UDMA_DESCR_COUNT。
- 为与其他驱动一致，GPDMA_SILABS_SIWX91X_DESCRIPTOR_COUNT改名为DMA_SILABS_SIWX91X_GPDMA_DESCR_COUNT。

<a id="espi"></a>

### [增强型串行外设接口（ESPI）](#id22)


- ECUSTOM_HOST_SUBS_INTERRUPT_EN已弃用，改用能逐个启用或禁用eSPI硬件中断的新API。旧方式只能全部启用或全部禁用，并在所有eSPI驱动中与CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE及单个eSPI ACPI硬件块实例紧密耦合。为留出迁移时间，旧接口将在下一个Zephyr版本彻底移除。
- Microchip XEC eSPI v2驱动[microchip,xec-espi-v2](../espi_binding_reference/P006_microchip_xec-espi-v2.md#std-dtcompatible-microchip-xec-espi-v2)已从MEC172x扩展到支持MEC174x、MEC175x及MEC165xB，因此带来若干设备树变化，影响使用该绑定的树外开发板（[GitHub #109519](https://github.com/zephyrproject-rtos/zephyr/issues/109519)）：


  - pcrs替换为pcr-scr，值由<reg bit>单元对改为MCHP_XEC_SCR_ENCODE(reg, bit)编码的单个整数。现有覆盖文件应将pcrs = <2 19>;改为pcr-scr = <MCHP_XEC_SCR_ENCODE(2, 19)>;。
  - 仅在MEC174x、MEC175x及MEC165xB上，girqs的每个条目改为由MCHP_XEC_ECIA_GIRQ_ENC(reg, bit)生成的单个整数，替代<reg bit>单元对。MEC172x继续使用原MCHP_XEC_ECIA(...)形式。
  - 对地址空间超过32位的主机，eSPI控制器节点新增两个可选属性：host-memmap-addr-high表示内存映射逻辑设备的主机地址位[47:32]；sram-bar-addr-high表示两个SRAM基址寄存器（BAR）的主机地址位[47:32]。
  - 为保持一致，eSPI控制器及其host-device子节点的interrupt-names已改名，覆盖文件需相应更新：


    - 控制器：rst改为erst；vwct_0_6及vwct_7_10分别改为ht_vw_bank0及ht_vw_bank1。还必须在interrupts数组中添加对应的ht_vw_bank0及ht_vw_bank1中断。
    - 键盘控制器（KBC）子节点：kbc_obe及kbc_ibf分别改为obe及ibf。
    - ACPI嵌入式控制器（EC）子节点：acpi_ibf及acpi_obe分别改为ibf及obe。
  - MEC5 SoC DTSI，即MEC174x、MEC175x及MEC165xB中，eSPI控制器的每个host-device子节点，包括邮箱、KBC、ACPI EC、ACPI PM1、port92、glue、EMI、BIOS调试端口等，现在都声明[microchip,xec-espi-host-dev](../espi_binding_reference/P003_microchip_xec-espi-host-dev.md#std-dtcompatible-microchip-xec-espi-host-dev)要求的ldn，即逻辑设备号（Logical Device Number）。树外开发板覆盖或新增这些子节点时，必须逐个设置ldn。
- 增强串行外设接口（Enhanced Serial Peripheral Interface，eSPI）示例的开发板电源节点兼容项从intel-rvp,board-power改为intel,rvp-board-power。该示例的树外开发板覆盖文件必须采用新名称。（[增强型串行外设接口（Enhanced SPI，eSPI）](../driver_samples/P053_eSPI接口示例.md#espi)）

<a id="ethernet"></a>

### [以太网（Ethernet）](#id23)


- WIZnet以太网驱动现在共用一组Kconfig选项。将CONFIG_ETH_W5500_*、CONFIG_ETH_W6100_*及CONFIG_ETH_W6300_*替换为对应CONFIG_ETH_WIZNET_*选项。
- ETHERNET_CONFIG_TYPE_T1S_PARAM及相关NET_REQUEST_ETHERNET_SET_T1S_PARAM已移除，应结合[phy_set_plca_cfg()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga260e528dee1c967ccc9f4d9cb2aadad5)及[net_eth_get_phy()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga7225d06fbaa12d4668fa165d9e8f0845)设置这些参数。（[GitHub #108136](https://github.com/zephyrproject-rtos/zephyr/issues/108136)）
- [ethernet_api](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)实现的函数新增[net_if](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if.html)指针参数。该API不直接暴露给应用，因此仅树外驱动需要更新。（[GitHub #106086](https://github.com/zephyrproject-rtos/zephyr/issues/106086)）
- [nxp,enet-mac](../ethernet_nxp_phy_binding_reference/P001_nxp_enet-mac.md#std-dtcompatible-nxp-enet-mac)的pinctrl-0及pinctrl-names属性，必须从MAC节点移到父以太网控制器节点。（[GitHub #107352](https://github.com/zephyrproject-rtos/zephyr/issues/107352)）
- NuMaker以太网驱动及CONFIG_ETH_NUMAKER已移除。NuMaker EMAC现在由[CONFIG_ETH_NUMAKER_DWC_ETHER_1000](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NUMAKER_DWC_ETHER_1000)，即通用Synopsys DesignWare MAC驱动驱动，需要在设备树中描述MDIO控制器及PHY。树外开发板必须启用mdio节点，在其引脚控制状态中设置MDC及MDIO引脚，添加PHY子节点，并通过emac的phy-handle指向它。[nuvoton,numaker-ethernet](../ethernet_mdio_microchip_binding_reference/P020_nuvoton_numaker-ethernet.md#std-dtcompatible-nuvoton-numaker-ethernet)的phy-addr属性已移除。
- [dsa_api](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__api.html)的port_generate_random_mac已移除。[dsa_port_config](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__port__config.html)现在使用[net_eth_mac_config](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html)设置MAC地址，其mac_addr及use_random_mac_addr成员已删除。树外DSA驱动必须更新端口配置代码，采用新API及结构体。（[GitHub #108952](https://github.com/zephyrproject-rtos/zephyr/issues/108952)）（[`dsa_port_config`](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__port__config.html)）
- CONFIG_ETH_NATIVE_TAP_PTP_CLOCK替换为[CONFIG_PTP_CLOCK_NATIVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK_NATIVE)。native_sim PTP时钟驱动新增[zephyr,native-ptp-clock](../ethernet_synopsys_st_xilinx_binding_reference/P025_zephyr_native-ptp-clock.md#std-dtcompatible-zephyr-native-ptp-clock)兼容项；存在该兼容项时，默认启用[CONFIG_PTP_CLOCK_NATIVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_CLOCK_NATIVE)。（[`zephyr,native-ptp-clock`](../ethernet_synopsys_st_xilinx_binding_reference/P025_zephyr_native-ptp-clock.md#std-dtcompatible-zephyr-native-ptp-clock)）
- native_sim TAP以太网驱动现在通过设备树[zephyr,native-tap](../ethernet_synopsys_st_xilinx_binding_reference/P026_zephyr_native-tap.md#std-dtcompatible-zephyr-native-tap)节点实例化。每个接口由设备树节点定义，替代已移除的CONFIG_ETH_NATIVE_TAP_INTERFACE_COUNT；添加多个节点即可创建多个接口。以下Kconfig选项已移除，改用设备树属性：


  - CONFIG_ETH_NATIVE_TAP_DRV_NAME替换为host-interface属性。
  - CONFIG_ETH_NATIVE_TAP_MAC_ADDR替换为local-mac-address属性。
  - CONFIG_ETH_NATIVE_TAP_RANDOM_MAC替换为zephyr,random-mac-address属性。

  命令行选项--eth-if、--mac-addr、--ipv4-addr、--ipv4-gw及--ipv4-nm仍受支持，应用于第一个接口。其他接口新增<node>_eth-if、<node>_mac-addr等按接口命名的选项。
- [dsa_api](https://docs.zephyrproject.org/latest/doxygen/html/structdsa__api.html)的port_phylink_change现在可选。PHY链路变化时，DSA驱动不再需要调用[net_eth_carrier_on()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga62b33344256bbe228689e2cb541a0874)或[net_eth_carrier_off()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga97ef5a8ad9157e2db12e9caf6faef5e7)，由DSA核心处理。port_phylink_change的void *user_data参数改为const struct device *dev，无需再强制转换以取得设备指针。树外DSA驱动必须更新回调签名，并可移除其中对上述载波状态函数的调用。（[GitHub #109671](https://github.com/zephyrproject-rtos/zephyr/issues/109671)）（[`net_eth_carrier_on()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga62b33344256bbe228689e2cb541a0874)；[`net_eth_carrier_off()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga97ef5a8ad9157e2db12e9caf6faef5e7)）
- 通过[net_if_up()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02644cc623fc7a8878c17d54984e4210)启用以太网接口时，现在会在调用[ethernet_api](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)的start前检查MAC地址有效性。地址无效则接口无法启用，并记录错误。原生Wi-Fi驱动同样适用。（[GitHub #110435](https://github.com/zephyrproject-rtos/zephyr/issues/110435)）
- Xilinx GEM驱动[xlnx,gem](../ethernet_synopsys_st_xilinx_binding_reference/P022_xlnx_gem.md#std-dtcompatible-xlnx-gem)改用现有MDIO及PHY框架，实现拆为独立MDIO及以太网MAC驱动，移除了自定义PHY管理代码。旧代码支持的Marvell Alaska千兆PHY系列及TI TLK105/DP83822百兆PHY，均由标准[ethernet-phy](../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy)驱动覆盖。模拟Xilinx GEM的QEMU目标，以及Zynq-7000、ZynqMP／UltraScale+ SoC设备树，都已相应更新。（[GitHub #87313](https://github.com/zephyrproject-rtos/zephyr/issues/87313)）
- 通过ETHERNET_CONFIG_TYPE_EXTRA_TX_PKT_HEADROOM要求额外发送分组头部预留空间（Headroom）的以太网及Wi-Fi驱动，现在必须选择[CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM)。（[GitHub #112924](https://github.com/zephyrproject-rtos/zephyr/issues/112924)）
- [ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)中的ETHERNET_PTP标志已移除。应使用[net_eth_get_ptp_clock()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga37ff48434c56bbb24422dd805449b6f3)检查接口是否有PTP时钟。树外驱动必须从[ethernet_api](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)的get_capabilities实现中删除对该标志的引用。（[GitHub #112788](https://github.com/zephyrproject-rtos/zephyr/issues/112788)）
- 支持链路层发现协议（LLDP）的以太网驱动不再需要在初始化时调用[net_lldp_set_lldpdu()](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html#ga961bc59567ffa2d5a4d21290d1d78407)，该操作现在由ethernet_init()完成。（[GitHub #114087](https://github.com/zephyrproject-rtos/zephyr/issues/114087)）
- [infineon,xmc4xxx-ethernet](../ethernet_mac_mdio_binding_reference/P009_infineon_xmc4xxx-ethernet.md#std-dtcompatible-infineon-xmc4xxx-ethernet)及[wch,ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P016_wch_ethernet.md#std-dtcompatible-wch-ethernet)节点已与各自父节点合并。同级MDIO节点位置不变，因此成为这些以太网节点的子节点。（[GitHub #114899](https://github.com/zephyrproject-rtos/zephyr/issues/114899)）
- infineon,xmc4xxx-mdio的mdi-port-ctrl属性移到父节点[infineon,xmc4xxx-ethernet](../ethernet_mac_mdio_binding_reference/P009_infineon_xmc4xxx-ethernet.md#std-dtcompatible-infineon-xmc4xxx-ethernet)。（[GitHub #114899](https://github.com/zephyrproject-rtos/zephyr/issues/114899)）
- espressif,esp32-mdio、infineon,xmc4xxx-mdio、nxp,enet-qos-mdio、nxp,s32-gmac-mdio、st,stm32-mdio及wch,mdio兼容项，均替换为[snps,dwmac-mdio](../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio)。（[GitHub #114899](https://github.com/zephyrproject-rtos/zephyr/issues/114899)）
- NXP ENET-QOS控制器[nxp,enet-qos](../ethernet_nxp_phy_binding_reference/P003_nxp_enet-qos.md#std-dtcompatible-nxp-enet-qos)的设备树结构已扁平化，以匹配类似控制器。clocks、interrupts、pinctrl-0、pinctrl-names、phy-handle及MAC地址属性，现在直接位于父nxp,enet-qos节点，不再位于独立MAC子节点。nxp,enet-qos-mac及enet_mac节点已移除。树外开发板必须将旧enet_mac属性移到enet节点。（[GitHub #115952](https://github.com/zephyrproject-rtos/zephyr/issues/115952)）
- CONFIG_ETH_NXP_ENET_QOS_MAC_UNIQUE_MAC_ADDRESS改名为[CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS)，使用旧名称的配置必须更新。（[GitHub #115952](https://github.com/zephyrproject-rtos/zephyr/issues/115952)）
- Synopsys DesignWare MAC驱动现在默认通过[CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER)过滤组播，只接收网络栈已加入地址的组播报文。禁用该选项可恢复接收全部组播的旧行为。（[GitHub #113235](https://github.com/zephyrproject-rtos/zephyr/issues/113235)）
- 具有以太网接口的开发板现在应默认启用[CONFIG_ETH_DRIVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DRIVER)，而非[CONFIG_NET_L2_ETHERNET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)；前者启用时，后者现在默认启用。（[GitHub #117121](https://github.com/zephyrproject-rtos/zephyr/issues/117121)）

<a id="flash"></a>

### [闪存（Flash）](#id24)


- [jedec,spi-nand](../mtd_microchip_nordic_nxp_binding_reference/P001_jedec_spi-nand.md#std-dtcompatible-jedec-spi-nand)现在要求plane-bytes属性，表示Flash设备中每个平面（Plane）的大小。单平面设备应将其设为与size-bytes相同。
- [st,stm32-nv-flash](../mtd_nxp_st_ti_partition_binding_reference/P016_st_stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash)的bank2-flash-size已弃用，改为通过reg的大小单元确定Flash存储体大小。设备树只需删除旧属性，无需其他修改。（[GitHub #114971](https://github.com/zephyrproject-rtos/zephyr/issues/114971)）

<a id="fuel-gauge"></a>

### [电量计（Fuel Gauge）](#id25)


- 多个电量计属性枚举及联合体字段已弃用，改用带明确单位后缀的新名称。应用及驱动应迁移，例如FUEL_GAUGE_CURRENT及val.current替换为FUEL_GAUGE_CURRENT_UA及val.current_ua。
- 以前各驱动对FUEL_GAUGE_CYCLE_COUNT的报告不一致，有的表示完整充放电周期，有的以百分之一周期为单位。现在统一报告完整周期；此前报告小数周期的ADP5360及BQ27Z746驱动已更新。依赖旧行为的应用应修改。（[GitHub #112276](https://github.com/zephyrproject-rtos/zephyr/issues/112276)）

<a id="gpio"></a>

### [通用输入输出（GPIO）](#id26)


- 通过[gpio_pin_configure()](../hardware/P266_GPIO公共接口.md#gaed4a2051d76db7eead8ed1719ce2ba33)为禁用状态的GPIO引脚配置上拉或下拉电阻时，STM32 GPIO驱动现在返回-EINVAL。以前返回0，但实际忽略这些标志，未启用电阻。遇到该错误的应用应从传入标志中删除[GPIO_PULL_UP](../hardware/P266_GPIO公共接口.md#gaaa7921da231fd2b96575fa522e2c1970)或[GPIO_PULL_DOWN](../hardware/P266_GPIO公共接口.md#gadec1802e074f3021d464da09cd66c7cf)；由于旧实现本就忽略它们，这将保持原有行为。（[GitHub #104690](https://github.com/zephyrproject-rtos/zephyr/issues/104690)）（[`gpio_pin_configure()`](../hardware/P266_GPIO公共接口.md#gaed4a2051d76db7eead8ed1719ce2ba33)）
- STM32F1系列的GPIO输出引脚现在使用50 MHz最大速度，替代10 MHz。（[GitHub #104690](https://github.com/zephyrproject-rtos/zephyr/issues/104690)）
- [awinic,aw9523b-gpio](../gpio_connectors_bflb_esp_binding_reference/P004_awinic_aw9523b-gpio.md#std-dtcompatible-awinic-aw9523b-gpio)不再提供reset-gpios，该属性移到父[awinic,aw9523b](../hardware/P698_AW9523B多功能设备绑定.md#dtbinding-awinic-aw9523b)多功能设备（MFD）。

<a id="haptics"></a>

### [触觉反馈（Haptics）](#id27)


- cirrus,cs40l5x兼容项替换为按型号区分的[cirrus,cs40l50](../compatible_binding_reference/P031_cirrus_cs40l50.md#std-dtcompatible-cirrus-cs40l50)、[cirrus,cs40l51](../compatible_binding_reference/P032_cirrus_cs40l51.md#std-dtcompatible-cirrus-cs40l51)、[cirrus,cs40l52](../compatible_binding_reference/P033_cirrus_cs40l52.md#std-dtcompatible-cirrus-cs40l52)及[cirrus,cs40l53](../compatible_binding_reference/P034_cirrus_cs40l53.md#std-dtcompatible-cirrus-cs40l53)。使用旧兼容项的应用必须相应更新设备树。
- [ti,drv2605](../sound_haptic_binding_reference/P017_ti_drv2605.md#std-dtcompatible-ti-drv2605)的vib-rated-mv及vib-overdrive-mv现在分别默认采用设备复位值1362 mV及3075 mV，而非3200 mV。需要原驱动电压的开发板必须明确设置。

<a id="hwspinlock"></a>

### [硬件自旋锁（HWSPINLOCK）](#id28)


- num-locks现在是硬件自旋锁（Hardware Spinlock）控制器绑定的标准必需属性，每个控制器节点必须设置。树外绑定必须删除自行定义的num-locks类型及required声明。
- [hw_spin_lock()](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gabad9432edb1105d44856ea982f2573e2)、[hw_spin_trylock()](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#ga455ef07f8dd4e6ed22017275cc11f9d2)及[hw_spin_unlock()](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gaa53fa67f0d60f59b877995d0709bf9cf)不再接受hwspinlock_ctx_t *参数；每把锁对应的Zephyr自旋锁现在位于驱动配置中。struct hwspinlock_context、hwspinlock_ctx_t、[hwspinlock_dt_spec](../intercore_reference/P005_硬件自旋锁设备树规格结构.md)的ctx成员及HWSPINLOCK_CTX_INITIALIZER已移除。[hw_spin_lock_dt()](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#ga8efc4a8a6b5e5fa7e7b2b0ea0c51c80b)、[hw_spin_trylock_dt()](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gaf0abcbcffe72ca2f18cc63187471ddfd)及[hw_spin_unlock_dt()](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#ga7ebca1a434a848ece68bd1eb1bb5ddea)辅助函数不变。因此，所有引用同一硬件自旋锁的[HWSPINLOCK_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gae5ca6ed464f267e12a0123fe2492867d)实例现在共用一把Zephyr自旋锁，不再各有一把。
- 硬件自旋锁驱动必须将[hwspinlock_driver_config](../intercore_reference/P004_硬件自旋锁驱动配置结构.md)作为配置结构体首个成员，用[HWSPINLOCK_COMMON_CONFIG_FROM_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#ga407261f758074c18d96cdf23b5df776f)或[HWSPINLOCK_COMMON_CONFIG_FROM_DT_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gaee1e3139a76d606f3e06de3e8396fc0e)初始化，并通过[HWSPINLOCK_SPINLOCK_ARRAY_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#ga5e8973a8983aec78817f51e3dd2ca96f)或[HWSPINLOCK_SPINLOCK_ARRAY_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gacca85debd57e9b20ed7c31725dd378ed)声明底层自旋锁数组。get_max_id驱动操作现在可选；未实现时，[hw_spinlock_get_max_id()](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gaf0975005e88f92b0cfc8d9dff4f0464f)默认返回设备树num-locks减1。

<a id="i2c"></a>

### [集成电路间总线（I2C）](#id29)


- 基于[CONFIG_I2C_DW](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_DW)的控制器中，CONFIG_I2C_DW_RW_TIMEOUT_MS替换为[CONFIG_I2C_TRANSFER_TIMEOUT_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_TRANSFER_TIMEOUT_MS)，默认500 ms。
- ITE I2C控制器[ite,enhance-i2c](../i2c_infineon_ite_nordic_binding_reference/P006_ite_enhance-i2c.md#std-dtcompatible-ite-enhance-i2c)、[ite,it51xxx-i2c](../i2c_infineon_ite_nordic_binding_reference/P007_ite_it51xxx-i2c.md#std-dtcompatible-ite-it51xxx-i2c)及[ite,it8xxx2-i2c](../i2c_infineon_ite_nordic_binding_reference/P008_ite_it8xxx2-i2c.md#std-dtcompatible-ite-it8xxx2-i2c)的传输超时，现在使用通用zephyr,transfer-timeout-ms属性替代transfer-timeout-ms，默认500 ms。
- [nxp,sc18im704-i2c](../i2c_nxp_pico_renesas_binding_reference/P006_nxp_sc18im704-i2c.md#std-dtcompatible-nxp-sc18im704-i2c)桥接驱动不再将未移位的目标地址发给SC18IM704。Zephyr I2C API向控制器transfer()回调传入7位地址，驱动现在左移一位，构造桥接器要求的地址字节。总线上若有设备树节点曾以预移位reg补偿旧问题，例如地址0x50的设备写为reg = <0xa0>，现在必须改为真实7位地址reg = <0x50>。（[`nxp,sc18im704-i2c`](../i2c_nxp_pico_renesas_binding_reference/P006_nxp_sc18im704-i2c.md#std-dtcompatible-nxp-sc18im704-i2c)）

<a id="i2s"></a>

### [集成电路间音频总线（I2S）](#id30)


- [i2s_buf_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga98cbfe351a8dd5db361f4667959d0b58)分配发送块时现在遵循流配置的timeout。以前无限等待，使文档中的-EAGAIN不可到达，多线程构建中的-ENOMEM也不可到达。依赖无限等待的调用者可将timeout设为SYS_FOREVER_MS，但该字段也限制驱动入队等待，因此没有单个值能重现“分配无限等待、入队有界等待”的旧组合。

<a id="ieee-802-15-4"></a>

### [低速率无线个域网（IEEE 802.15.4）](#id31)


- 自Zephyr 3.6起弃用的IEEE802154_HW_SLEEP_TO_TX无线电能力已移除，其后的能力位重新编号。所有树内驱动均支持直接从低功耗状态发送，因此该标志未提供区分信息。OpenThread平台现在始终通告OT_RADIO_CAPS_SLEEP_TO_TX，并允许从休眠状态发送。树外驱动只需删除对旧能力的声明。

<a id="input"></a>

### [输入（Input）](#id32)


- [gpio-keys](../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys)的no-disconnect替换为枚举属性zephyr,suspend-action。新属性目前有三个取值，其中两个直接对应旧行为：

  > - zephyr,suspend-action = "none";对应原来存在no-disconnect时的行为。使用no-disconnect的用户应替换为此设置。
  > - zephyr,suspend-action = "disconnect-with-pupd";对应原来不存在no-disconnect时的行为。为向后兼容，此值默认选中。
  > - zephyr,suspend-action = "full-disconnect";为新值，详见绑定说明。（[`the binding`](../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys)）

  官方建议使用默认配置的用户重新评估是否适合，并推荐迁移到zephyr,suspend-action = "full-disconnect";。（[GitHub #108294](https://github.com/zephyrproject-rtos/zephyr/issues/108294)）
- ft6146、ft5336及cst8xx输入驱动的Kconfig名称已调整，以与其他输入驱动一致。使用以下选项的应用必须更新配置：


  - CONFIG_INPUT_FT5336_PERIOD改名为[CONFIG_INPUT_FT5336_PERIOD_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_FT5336_PERIOD_MS)。
  - CONFIG_INPUT_CST8XX_PERIOD改名为[CONFIG_INPUT_CST8XX_PERIOD_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_CST8XX_PERIOD_MS)。
  - CONFIG_INPUT_FT6146_PERIOD改名为[CONFIG_INPUT_FT6146_PERIOD_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_FT6146_PERIOD_MS)。
  - Nunchuk驱动以前在按钮事件中错误报告INPUT_KEY_Z及INPUT_KEY_C，现已修正为INPUT_BTN_Z及INPUT_BTN_C。

<a id="interrupt-controllers"></a>

### [中断控制器（Interrupt Controllers）](#id33)


- 所有中断控制器绑定现在使用flags而非sense作为中断描述单元名称。以下绑定已更新：


  - [`intel,ioapic`](../multiarch_interrupt_binding_reference/P001_intel_ioapic.md#std-dtcompatible-intel-ioapic)
  - [`intel,loapic`](../multiarch_interrupt_binding_reference/P002_intel_loapic.md#std-dtcompatible-intel-loapic)
  - [`cdns,xtensa-core-intc`](../multiarch_interrupt_binding_reference/P007_cdns_xtensa-core-intc.md#std-dtcompatible-cdns-xtensa-core-intc)
  - [`intel,ace-intc`](../soc_interrupt_binding_reference/P007_intel_ace-intc.md#std-dtcompatible-intel-ace-intc)
  - [`intel,cavs-intc`](../soc_interrupt_binding_reference/P008_intel_cavs-intc.md#std-dtcompatible-intel-cavs-intc)
  - [`snps,designware-intc`](../multiarch_interrupt_binding_reference/P006_snps_designware-intc.md#std-dtcompatible-snps-designware-intc)
  - [`mediatek,adsp_intc`](../soc_interrupt_binding_reference/P010_mediatek_adsp_intc.md#std-dtcompatible-mediatek-adsp_intc)

  使用这些中断控制器的驱动已改用flags。但树外驱动若通过DT_INST_IRQ(n, sense)或DT_IRQ(node, sense)直接访问中断属性，必须将sense改为flags。
- GIC头文件gic.h中的GIC_NUM_CPU_IF已弃用，应改用CONFIG_MP_MAX_NUM_CPUS。译注：原网页此处包含未正常渲染的Kconfig引用标记。

<a id="mbox"></a>

### [邮箱（MBOX）](#id34)


- [renesas,rz-mhu-mbox](../intercore_reference/P053_RenesasRZ邮箱绑定.md#dtbinding-renesas-rz-mhu-mbox)驱动已重构：单个消息处理单元（MHU）现在在一个邮箱（MBOX）通道上同时处理发送及接收，不再每通道只对应一个方向；单个驱动实例可拥有多个通道。使用该兼容项的设备树必须更新：


  - channel改名为unit，因为它索引底层MHU硬件单元，而非MBOX通道；两种编号体系相互独立。
  - tx-mask及rx-mask替换为单个channel-mask，它是有效MBOX通道的位掩码，位n启用通道n。
  - channels-count必须与节点的interrupt-names条目数一致，现在在构建时强制检查。
  - shared-memory现在可选，多数情况下应不设置。共享内存改由名为mhu_shmem的单个zephyr,memory-region节点提供，替代每个单元的mmio-sram节点，并使链接器为FSP MHU驱动生成__mhu_shmem_start。缺少此内存区域的开发板，会因该符号未定义而链接失败。

  例如：

  ```text
  /* Before */
  mhu3_shm: memory@62f01018 {
          compatible = "mmio-sram";
          reg = <0x62f01018 0x8>;
  };

  mbox3: mhu@40400060 {
          channel = <3>;
          tx-mask = <0x00000002>;
          rx-mask = <0x00000001>;
          shared-memory = <&mhu3_shm>;
  };

  /* After */
  mhu_shmem: memory-region@62f01000 {
          compatible = "zephyr,memory-region";
          reg = <0x62f01000 0x1000>;
          zephyr,memory-region = "mhu_shmem";
  };

  mbox3: mhu@40400060 {
          unit = <3>;
          channel-mask = <0x1>;
  };
  ```

<a id="mspi"></a>

### [多线串行外设接口（MSPI）](#id35)


- MSPI专用设备绑定文件现在采用(vendor,)device-mspi.yaml名称，而设备树兼容字符串描述设备本身，不再编码MSPI总线。官方建议开发板、扩展板、示例、测试及树外覆盖文件按以下关系更新MSPI子节点兼容项：


  - jedec,mspi-nor改为jedec,nor。
  - mspi-atxp032改为atxp032。
  - mspi-is25xX0xx改为is25xX0xx。
  - mspi-aps6404l改为aps6404l。
  - mspi-aps-z8改为aps-z8。
  - zephyr,mspi-emul-device改为zephyr,emul-device-mspi。
  - zephyr,mspi-emul-flash改为zephyr,emul-flash。

  树外MSPI设备驱动也建议将DT_DRV_COMPAT及生成的设备树Kconfig符号引用更新为新兼容项。若驱动、示例或测试必须保证某通用兼容项在MSPI总线上实例化，应增加明确的MSPI总线检查，例如Kconfig中的dt_compat_on_bus，或测试元数据中的dt_compat_on_bus筛选条件。
- MSPI内存映射功能从XIP改名为MEMMAP。Zephyr中的就地执行（XIP，[CONFIG_XIP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)）属于软件配置概念，而该MSPI功能只是映射设备内存，既可访问数据，也可执行代码。（[GitHub #104657](https://github.com/zephyrproject-rtos/zephyr/issues/104657)）MSPI API处于实验阶段，因此不提供弃用别名。树外用户必须更新：


  - CONFIG_MSPI_XIP改为[CONFIG_MSPI_MEMMAP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_MEMMAP)。
  - CONFIG_FLASH_MSPI_XIP_READ改为[CONFIG_FLASH_MSPI_MEMMAP_READ](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MSPI_MEMMAP_READ)。
  - struct mspi_xip_cfg改为struct mspi_memmap_cfg。
  - enum mspi_xip_permit改为enum mspi_memmap_permit；枚举值MSPI_XIP_READ_WRITE及MSPI_XIP_READ_ONLY，分别改为MSPI_MEMMAP_READ_WRITE及MSPI_MEMMAP_READ_ONLY。
  - mspi_xip_config改为[mspi_memmap_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gac025129882f814b59d5726c01f0138ce)；驱动API项xip_config改为memmap_config。
  - MSPI_XIP_CONFIG_DT、MSPI_XIP_CONFIG_DT_INST及MSPI_XIP_CONFIG_DT_NO_CHECK，分别改为MSPI_MEMMAP_CONFIG_DT、MSPI_MEMMAP_CONFIG_DT_INST及MSPI_MEMMAP_CONFIG_DT_NO_CHECK。
  - MSPI_XIP_CFG_STRUCT_DECLARE、MSPI_XIP_BASE_ADDR_DECLARE及MSPI_XIP_BASE_ADDR_INIT，分别改为MSPI_MEMMAP_CFG_STRUCT_DECLARE、MSPI_MEMMAP_BASE_ADDR_DECLARE及MSPI_MEMMAP_BASE_ADDR_INIT。
  - MSPI设备节点的xip-config属性改为memmap-config。

<a id="nordic"></a>

### [Nordic半导体](#id36)


- [nordic,owned-memory](../memory_protection_binding_reference/P010_nordic_owned-memory.md#std-dtcompatible-nordic-owned-memory)及[nordic,owned-partitions](../mtd_microchip_nordic_nxp_binding_reference/P011_nordic_owned-partitions.md#std-dtcompatible-nordic-owned-partitions)的owner-id、perm-read、perm-write、perm-execute、perm-secure及non-secure-callable已移除。改用nordic,access，例如<NRF_OWNER_ID_APPLICATION NRF_PERM_RW>。所有者不再隐式确定：以前省略owner-id表示当前编译的域，现在必须明确指定。

<a id="nxp"></a>

### [恩智浦（NXP）](#id37)


- [CONFIG_MCUX_LPTMR_TIMER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_LPTMR_TIMER)不再因/chosen/zephyr,system-timer与[nxp,lptmr](../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr)兼容就默认y。依赖LPTMR作为系统定时器的树外SoC及开发板，现在必须在Kconfig.defconfig中明确设置默认值，例如default y if PM。
- Kinetis KE1xF在启用[CONFIG_PM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)时，不再需要开发板覆盖文件指定系统定时器。SoC DTSI现在设置zephyr,system-timer chosen属性，因此可删除按Zephyr 4.4迁移指南添加的覆盖配置。
- NXP LPC DTSI文件已从平铺的dts/arm/nxp/lpc/目录重新组织到各系列子目录。直接包含这些文件的树外开发板必须更新路径。

  新的子目录布局如下：

  <table>
  <tr>
  <th>LPC系列（LPC Series）</th>
  <th>新位置（New Location）</th>
  </tr>
  <tr>
  <td>LPC11U6x</td>
  <td><code>dts/arm/nxp/lpc/lpc11u6x/</code></td>
  </tr>
  <tr>
  <td>LPC51U68</td>
  <td><code>dts/arm/nxp/lpc/lpc51u68/</code></td>
  </tr>
  <tr>
  <td>LPC54xxx</td>
  <td><code>dts/arm/nxp/lpc/lpc54xxx/</code></td>
  </tr>
  <tr>
  <td>LPC55xxx</td>
  <td><code>dts/arm/nxp/lpc/lpc55xxx/</code></td>
  </tr>
  <tr>
  <td>LPC84x</td>
  <td><code>dts/arm/nxp/lpc/lpc84x/</code></td>
  </tr>
  </table>

  示例（Example）：

  ```text
  /* Before */
  #include <nxp/lpc/nxp_lpc55S6x.dtsi>

  /* After */
  #include <nxp/lpc/lpc55xxx/nxp_lpc55S6x.dtsi>
  ```
- NXP Kinetis DTSI文件已从平铺的dts/arm/nxp/kinetis/目录重新组织到各系列子目录。直接包含这些文件的树外开发板必须更新路径。

  新的子目录布局如下：

  <table>
  <tr>
  <th>Kinetis系列（Kinetis Series）</th>
  <th>新位置（New Location）</th>
  </tr>
  <tr>
  <td>K2X</td>
  <td><code>dts/arm/nxp/kinetis/k2x/</code></td>
  </tr>
  <tr>
  <td>K32Lx</td>
  <td><code>dts/arm/nxp/kinetis/k32lx/</code></td>
  </tr>
  <tr>
  <td>K6X</td>
  <td><code>dts/arm/nxp/kinetis/k6x/</code></td>
  </tr>
  <tr>
  <td>K8X</td>
  <td><code>dts/arm/nxp/kinetis/k8x/</code></td>
  </tr>
  <tr>
  <td>KE1xF</td>
  <td><code>dts/arm/nxp/kinetis/ke1xf/</code></td>
  </tr>
  <tr>
  <td>KE1xZ</td>
  <td><code>dts/arm/nxp/kinetis/ke1xz/</code></td>
  </tr>
  <tr>
  <td>KL2X</td>
  <td><code>dts/arm/nxp/kinetis/kl2x/</code></td>
  </tr>
  <tr>
  <td>KV5X</td>
  <td><code>dts/arm/nxp/kinetis/kv5x/</code></td>
  </tr>
  <tr>
  <td>KWX</td>
  <td><code>dts/arm/nxp/kinetis/kwx/</code></td>
  </tr>
  </table>

  示例（Example）：

  ```text
  /* Before */
  #include <nxp/kinetis/nxp_k66.dtsi>

  /* After */
  #include <nxp/kinetis/k6x/nxp_k66.dtsi>
  ```
- NXP MCX DTSI文件已从平铺的dts/arm/nxp/mcx/目录重新组织到各系列子目录。直接包含这些文件的树外开发板必须更新路径。

  新的子目录布局如下：

  <table>
  <tr>
  <th>MCX系列（MCX Series）</th>
  <th>新位置（New Location）</th>
  </tr>
  <tr>
  <td>MCXA</td>
  <td><code>dts/arm/nxp/mcx/mcxa/</code></td>
  </tr>
  <tr>
  <td>MCXC</td>
  <td><code>dts/arm/nxp/mcx/mcxc/</code></td>
  </tr>
  <tr>
  <td>MCXE</td>
  <td><code>dts/arm/nxp/mcx/mcxe/</code></td>
  </tr>
  <tr>
  <td>MCXL</td>
  <td><code>dts/arm/nxp/mcx/mcxl/</code></td>
  </tr>
  <tr>
  <td>MCXN</td>
  <td><code>dts/arm/nxp/mcx/mcxn/</code></td>
  </tr>
  <tr>
  <td>MCXW</td>
  <td><code>dts/arm/nxp/mcx/mcxw/</code></td>
  </tr>
  </table>

  示例（Example）：

  ```text
  /* Before */
  #include <nxp/mcx/nxp_mcxc242.dtsi>

  /* After */
  #include <nxp/mcx/mcxc/nxp_mcxc242.dtsi>
  ```
- NXP MCXN系列为mcxn547、mcxn947及mcxn236新增按具体型号组合的DTSI文件nxp_mcxn547.dtsi、nxp_mcxn947.dtsi及nxp_mcxn236.dtsi，同时加入本版本新增的mcxn546、mcxn946及mcxn235占位型号（Phantom Parts）。这些文件仅分别包含已有nxp_mcxn54x.dtsi、nxp_mcxn94x.dtsi及nxp_mcxn23x.dtsi，不覆盖任何内容；相应树内开发板现已改为包含新型号文件。系列文件本身不变，直接包含仍可工作，因此并非必须迁移，但这三个型号的树外开发板可考虑更新，以与系列其余部分一致。

  示例（Example）：

  ```text
  /* Before */
  #include <nxp/mcx/mcxn/nxp_mcxn94x.dtsi>

  /* After */
  #include <nxp/mcx/mcxn/nxp_mcxn947.dtsi>
  ```
- NXP i.MX RT DTSI文件已从平铺的dts/arm/nxp/imxrt/目录重新组织到各系列子目录。直接包含这些文件的树外开发板必须更新路径。

  新的子目录布局如下：

  <table>
  <tr>
  <th>i.MX RT系列（i.MX RT Series）</th>
  <th>新位置（New Location）</th>
  </tr>
  <tr>
  <td>RT10xx</td>
  <td><code>dts/arm/nxp/imxrt/imxrt10xx/</code></td>
  </tr>
  <tr>
  <td>RT11xx</td>
  <td><code>dts/arm/nxp/imxrt/imxrt11xx/</code></td>
  </tr>
  <tr>
  <td>RT5xx</td>
  <td><code>dts/arm/nxp/imxrt/imxrt5xx/</code></td>
  </tr>
  <tr>
  <td>RT6xx</td>
  <td><code>dts/arm/nxp/imxrt/imxrt6xx/</code></td>
  </tr>
  <tr>
  <td>RT7xx</td>
  <td><code>dts/arm/nxp/imxrt/imxrt7xx/</code></td>
  </tr>
  <tr>
  <td>RT118x</td>
  <td><code>dts/arm/nxp/imxrt/imxrt118x/</code></td>
  </tr>
  </table>

  示例（Example）：

  ```text
  /* Before */
  #include <nxp/imxrt/nxp_rt1060.dtsi>

  /* After */
  #include <nxp/imxrt/imxrt10xx/nxp_rt1060.dtsi>
  ```
- i.MX RT118x开发板现在包含单个型号／内核组合文件nxp_rt118<part>_cm<core>.dtsi，替代系列／内核文件加单独型号覆盖文件。树外开发板必须相应更新包含路径。（[GitHub #110228](https://github.com/zephyrproject-rtos/zephyr/issues/110228)）

  原来需要系列文件及型号覆盖文件的型号，其迁移示例如下：

  ```text
  /* Before */
  #include <nxp/imxrt/nxp_rt118x_cm7.dtsi>
  #include <nxp/imxrt/nxp_rt1186.dtsi>

  /* After */
  #include <nxp/imxrt/imxrt118x/nxp_rt1186_cm7.dtsi>
  ```
- i.MX RT7xx开发板现在包含单个型号／内核组合文件nxp_<part>_<core>.dtsi，替代系列／内核文件。树外开发板必须相应更新包含路径。

  原来需要系列文件的型号，其迁移示例如下：

  ```text
  /* Before */
  #include <nxp/imxrt/imxrt7xx/nxp_rt7xx_cm33_cpu0.dtsi>

  /* After */
  #include <nxp/imxrt/imxrt7xx/nxp_rt798s_cm33_cpu0.dtsi>
  ```
- hal_nxp的dts/nxp/树下NXP SoC引脚控制头文件，已重组以对应dts/arm/nxp/<family>/<series>/布局：每个SoC的*-pinctrl.h及*-pinctrl.dtsi移入pinctrl/子目录。直接包含这些文件的树外开发板必须更新路径。

  按系列组织的家族i.MX RT、Kinetis、LPC及MCX，将头文件放在<family>/<series>/pinctrl/；平铺组织的i.MX、S32及RW放在家族级<family>/pinctrl/。Kinetis还为此前未分类的型号新增k0x、km3x及kv3x目录。此外，原nxp_imx已拆分：nxp_imx/rt/变为imxrt/家族，其余i.MX应用处理器归入平铺的imx/家族。

  示例（Examples）：

  ```text
  /* Before */
  #include <nxp/nxp_imx/rt/mimxrt1151dvm8b-pinctrl.dtsi>
  #include <nxp/nxp_imx/mimx8ml8dvnlz-pinctrl.dtsi>
  #include <nxp/kinetis/MK64FN1M0VLL12-pinctrl.h>

  /* After */
  #include <nxp/imxrt/imxrt11xx/pinctrl/mimxrt1151dvm8b-pinctrl.dtsi>
  #include <nxp/imx/pinctrl/mimx8ml8dvnlz-pinctrl.dtsi>
  #include <nxp/kinetis/k6x/pinctrl/MK64FN1M0VLL12-pinctrl.h>
  ```

<a id="pwm"></a>

### [脉宽调制（PWM）](#id38)


- [microchip,xec-pwm](../pwm_intel_microchip_nxp_binding_reference/P012_microchip_xec-pwm.md#std-dtcompatible-microchip-xec-pwm)的数组属性pcrs替换为整数属性pcr-scr，使用编码PCR寄存器索引及位位置的宏。（[GitHub #104570](https://github.com/zephyrproject-rtos/zephyr/issues/104570)）
- 自Zephyr v3.3.0起弃用的STM32 PWM设备树绑定宏PWM_STM32_COMPLEMENTARY不再定义，应改用STM32_PWM_COMPLEMENTARY。
- [nxp,ctimer-pwm](../pwm_intel_microchip_nxp_binding_reference/P019_nxp_ctimer-pwm.md#std-dtcompatible-nxp-ctimer-pwm)现在通过通用Mux子系统路由输入捕获信号。input[mux](https://docs.zephyrproject.org/latest/hardware/peripherals/mux.html#mux-api)-connections已移除；应使用[nxp,inputmux](../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux)控制器节点描述路由，再由定时器节点的mux-states引用。（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
- [nxp,sctimer-pwm](../pwm_nxp_renesas_binding_reference/P012_nxp_sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm)现在通过通用Mux子系统路由输入捕获信号。input-channels已移除；应使用nxp,input[mux](https://docs.zephyrproject.org/latest/hardware/peripherals/mux.html#mux-api)控制器节点描述路由，再由定时器节点的mux-states引用。（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）（[`nxp,inputmux`](../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux)）

<a id="rtc"></a>

### [实时时钟（RTC）](#id39)


- 基于计数器的旧DS3231驱动已移除，完成[GitHub #95221](https://github.com/zephyrproject-rtos/zephyr/issues/95221)开始的弃用过程。使用maxim,ds3231、CONFIG_COUNTER_MAXIM_DS3231或<zephyr/drivers/rtc/maxim_ds3231.h>的应用，必须迁移到实时时钟（RTC）子系统驱动。

  将原单个I2C节点替换为[maxim,ds3231-mfd](../hardware/P709_DS3231多功能设备绑定.md#dtbinding-maxim-ds3231-mfd)父节点及[maxim,ds3231-rtc](../rtc_binding_reference/P013_maxim_ds3231-rtc.md#std-dtcompatible-maxim-ds3231-rtc)子节点。将isw-gpios移到RTC子节点，旧32k-gpios改为freq-32khz-gpios，并用通用RTC API替代maxim_ds3231_*辅助API。
- [microcrystal,rv3032](../microchip_microcrystal_nxp_rtc_binding_reference/P007_microcrystal_rv3032.md#std-dtcompatible-microcrystal-rv3032)的trickle-resistor-ohms及trickle-charger-mode移到父[microcrystal,rv3032-mfd](../hardware/P712_RV3032多功能设备绑定.md#dtbinding-microcrystal-rv3032-mfd)设备。父MFD现在为所有子设备配置备用供电模式。

<a id="sd-host-controller"></a>

### [SD主机控制器（SD Host Controller）](#id40)


- CONFIG_SDHC_STM32_POLLING_SUPPORT改名为[CONFIG_SDHC_STM32_DMA_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_STM32_DMA_MODE)。新符号启用DMA，默认y；设为n使用轮询模式。（[GitHub #101617](https://github.com/zephyrproject-rtos/zephyr/issues/101617)）
- CONFIG_SDHC_STM32_SDIO改名为[CONFIG_SDHC_STM32_SDMMC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_STM32_SDMMC)。（[GitHub #101617](https://github.com/zephyrproject-rtos/zephyr/issues/101617)）
- st,stm32-sdio兼容项已改名，改用[st,stm32-sdmmc](../sdhc_binding_reference/P019_st_stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc)。通过该兼容项，旧磁盘驱动及SDHC驱动可针对同一节点。要迁移到SDHC STM32 SDMMC驱动，应禁用旧磁盘驱动：

  ```text
  CONFIG_SDMMC_STM32=n
  ```

  参见[GitHub #101617](https://github.com/zephyrproject-rtos/zephyr/issues/101617)。
- [st,stm32-sdmmc](../sdhc_binding_reference/P019_st_stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc)的sdhi-on-gpios合并到已有pwr-gpios属性。树外节点必须将sdhi-on-gpios替换为pwr-gpios。
- 旧SDMMC_STM32磁盘驱动现在默认启用[CONFIG_SDMMC_STM32_HWFC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDMMC_STM32_HWFC)，以防止磁盘访问时发生FIFO欠载或溢出。原来设置CONFIG_SDMMC_STM32_HWFC=y的应用应从开发板配置删除该行，因为现在已是默认值。
- [litex,mmc](../sdhc_binding_reference/P010_litex_mmc.md#std-dtcompatible-litex-mmc)现在使用dma-coherent属性表示控制器DMA访问与CPU保持一致性。[CONFIG_SDHC_LITEX_LITESDCARD_NO_COHERENT_DMA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDHC_LITEX_LITESDCARD_NO_COHERENT_DMA)根据该属性自动设置，不再由用户配置。（[GitHub #108411](https://github.com/zephyrproject-rtos/zephyr/issues/108411)）

<a id="sensor"></a>

### [传感器（Sensor）](#id41)


- [pixart,paa3905](../sensor_nxp_qdec_optical_binding_reference/P024_pixart_paa3905.md#std-dtcompatible-pixart-paa3905)驱动现在强制遵循数据手册的SPI约定：驱动设置模式3，设备树spi-max-frequency高于2 MHz会导致构建失败。曾对总线超频的树外开发板必须将该值降至2000000或以下。
- [microchip,xec-tach](../auxdisplay_iio_tach_binding_reference/P017_microchip_xec-tach.md#std-dtcompatible-microchip-xec-tach)原数组属性girqs及pcrs的配置已调整，PCR改用整数属性pcr-scr及编码寄存器索引、位位置的宏；GIRQ配置现在通过包含microchip,dmec-ecia-girq绑定处理。（[GitHub #104808](https://github.com/zephyrproject-rtos/zephyr/issues/104808)）
- [st,lps22hh](../compatible_binding_reference/P087_st_lps22hh.md#std-dtcompatible-st-lps22hh)现在忽略odr属性，采用单次采样（One-shot Sampling）；只有启用CONFIG_LPS22HH_TRIGGER使用周期采样时，才采用odr。
- tdk,ntcg163jf103ft1改名为[tdk,ntcgxx3jx103x](../sensor_st_ti_power_capacitance_binding_reference/P010_tdk_ntcgxx3jx103x.md#std-dtcompatible-tdk-ntcgxx3jx103x)，以反映命名方案中具有相同电阻R25及Beta值B25/85的TDK NTCG热敏电阻型号，使用相同补偿值。（[GitHub #110123](https://github.com/zephyrproject-rtos/zephyr/issues/110123)）
- [nxp,mcux-qdc](../sensor_nxp_qdec_optical_binding_reference/P007_nxp_mcux-qdc.md#std-dtcompatible-nxp-mcux-qdc)现在通过通用Mux子系统路由输入信号。input-channels及input[mux](https://docs.zephyrproject.org/latest/hardware/peripherals/mux.html#mux-api)-connections已移除；应使用[nxp,inputmux](../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux)等Mux控制器节点描述路由，再由解码器节点的mux-states引用。（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
- [ti,tmag5273](../sensor_ti_vishay_wurth_sensing_binding_reference/P003_ti_tmag5273.md#std-dtcompatible-ti-tmag5273)现在以高斯（Gauss）而非毫特斯拉（Millitesla）解释SENSOR_ATTR_FULL_SCALE，与SENSOR_CHAN_MAGN_*通道单位一致。使用TMAG5273_DT_AXIS_RANGE_RUNTIME的应用，传给[sensor_attr_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafbf65226a227e9f8824908bc38e336f5)及从[sensor_attr_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaedfdfc71dce702dc1fb1c6e60ff0f73a)读取的数值都必须按原值的10倍处理，例如80 mT对应800 G。
- [nxp,mcux-qdec](../sensor_nxp_qdec_optical_binding_reference/P008_nxp_mcux-qdec.md#std-dtcompatible-nxp-mcux-qdec)现在通过通用Mux子系统路由输入信号。xbar属性已移除；应使用[nxp,mcux-xbar](../arm_nordic_nxp_control_binding_reference/P016_nxp_mcux-xbar.md#std-dtcompatible-nxp-mcux-xbar)等Mux控制器节点描述路由，再由解码器节点的[mux](https://docs.zephyrproject.org/latest/hardware/peripherals/mux.html#mux-api)-states引用。（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
- [avago,apds9960](../sensor_ams_aosong_bosch_binding_reference/P021_avago_apds9960.md#std-dtcompatible-avago-apds9960)的pgain、again、ppulse-length及pled-boost，以前用十六进制0x00/0x01/0x10/0x11表示所选2位寄存器字段，现在改用实际物理值：pgain为增益倍数1/2/4/8，again为1/4/16/64，ppulse-length为4/8/16/32微秒，pled-boost为100/150/200/300百分比。多数旧值会被新枚举拒绝，但pgain = <0x01>及again = <0x01>仍可构建，且现在选中1倍，而非原2倍及4倍，因此必须明确更新。未设置这些属性的节点不受影响。（[GitHub #116079](https://github.com/zephyrproject-rtos/zephyr/issues/116079)）

<a id="serial"></a>

### [串行接口（Serial）](#id42)


- [uart_irq_update()](../hardware/P333_UART中断驱动接口.md#ga20cf50f53fb9e09e760c6499fd156ff2)返回类型从int改为void。（[GitHub #105231](https://github.com/zephyrproject-rtos/zephyr/issues/105231)）
- brcm,bcm2711-aux-uart绑定已移除，改用[brcm,bcm283x-aux-uart](../uart_adi_arm_atmel_binding_reference/P014_brcm_bcm283x-aux-uart.md#std-dtcompatible-brcm-bcm283x-aux-uart)。节点必须增加[ns16550](../uart_microchip_nordic_nxp_binding_reference/P005_ns16550.md#std-dtcompatible-ns16550)兼容项，将clocks替换为clock-frequency，并指定reg-shift = <2>。BCM2711专用辅助UART驱动已移除，改用通用NS16550驱动，后者通过厂商扩展支持Broadcom BCM283x辅助UART。（[GitHub #115112](https://github.com/zephyrproject-rtos/zephyr/issues/115112)）
- [CONFIG_UART_NS16550_DW8250_DW_APB](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NS16550_DW8250_DW_APB)现在由设备树决定：存在[snps,dw-apb-uart](../uart_silabs_stm32_ti_binding_reference/P011_snps_dw-apb-uart.md#std-dtcompatible-snps-dw-apb-uart)节点时启用，其他情况下不可设置。应为UART节点添加该兼容项，替代在Kconfig中设置选项。（[GitHub #120368](https://github.com/zephyrproject-rtos/zephyr/issues/120368)）

<a id="spi"></a>

### [串行外设接口（SPI）](#id43)


- SPI API已迁移到规则A.2“包容性语言”（Inclusive Language）选定的术语：控制器／外设（Controller/Peripheral）角色，以及SDO/SDI信号名。旧名称已弃用，将在Zephyr v5.0移除：（[规则A.2：包容性语言（Inclusive Language）](../contributing/P009_编码准则.md#coding-guideline-inclusive-language)）


  - [SPI_OP_MODE_CONTROLLER](../hardware/P318_SPI公共接口.md#gace0f0d954c2bd7d603c4003289c11102)及[SPI_OP_MODE_PERIPHERAL](../hardware/P318_SPI公共接口.md#gaa1f42ffeac36380f4d1d8f84bda2990b)，分别替换SPI_OP_MODE_MASTER及SPI_OP_MODE_SLAVE。
  - [spi_config](../hardware/P320_SPI控制器配置结构.md)的slave成员改名为peripheral。
  - [SPI_SDO_OVERRUN_UNKNOWN](../hardware/P318_SPI公共接口.md#ga1dbef324b98a8921507de0da1c4e4fa6)、[SPI_SDO_OVERRUN_DT](../hardware/P318_SPI公共接口.md#gaf66331d56f20e0c37f2a3cff998c6bce)及[SPI_SDO_OVERRUN_DT_INST](../hardware/P318_SPI公共接口.md#ga0e05910cd0be7211389514b7b4edc0cc)，替换对应SPI_MOSI_OVERRUN_*宏。
  - [CONFIG_SPI_PERIPHERAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_PERIPHERAL)替换CONFIG_SPI_SLAVE。
  - 面向驱动的spi_context.h辅助函数中，spi_context_is_peripheral()替换spi_context_is_slave()。
  - [zephyr,spi-bitbang](../spi_stm32_ti_xilinx_binding_reference/P022_zephyr_spi-bitbang.md#std-dtcompatible-zephyr-spi-bitbang)及[raspberrypi,pico-spi-pio](../spi_flexspi_nxp_renesas_binding_reference/P009_raspberrypi_pico-spi-pio.md#std-dtcompatible-raspberrypi-pico-spi-pio)的sdo-gpios/sdi-gpios，[brcm,afbr-s50](../sensor_bosch_broadcom_espressif_binding_reference/P026_brcm_afbr-s50.md#std-dtcompatible-brcm-afbr-s50)的spi-sdi-gpios/spi-sdo-gpios，[nxp,s32-spi](../spi_flexspi_nxp_renesas_binding_reference/P005_nxp_s32-spi.md#std-dtcompatible-nxp-s32-spi)的peripheral，以及[realtek,bee-spi](../spi_flexspi_nxp_renesas_binding_reference/P012_realtek_bee-spi.md#std-dtcompatible-realtek-bee-spi)的is-peripheral，分别替换原来含mosi、miso或slave的属性名。旧名称仍接受，但在绑定中标为弃用。
  - 设备树兼容项[zephyr,bt-hci-spi-peripheral](../bluetooth_st_transport_binding_reference/P010_zephyr_bt-hci-spi-peripheral.md#std-dtcompatible-zephyr-bt-hci-spi-peripheral)替换zephyr,bt-hci-spi-slave。
- SPI_SILABS_SIWX91X_GSPI_DMA及SPI_SILABS_SIWX91X_GSPI_DMA_MAX_BLOCKS已移除，替换为SPI_SILABS_SIWX91X_GSPI_DMA_DESCR_COUNT，用于启用DMA并配置描述符数量。
- [st,stm32h7-spi](../spi_stm32_ti_xilinx_binding_reference/P013_st_stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi)的fifo-enable已移除。轮询及中断模式现在始终使用FIFO以提高性能。新增st,fifo-threshold可配置FIFO阈值，默认1。（[GitHub #110265](https://github.com/zephyrproject-rtos/zephyr/issues/110265)）
- [SPI_CONFIG_DT](../hardware/P318_SPI公共接口.md#gaf7d4888063e5b739f2a3bee295962bfe)、[SPI_CONFIG_DT_INST](../hardware/P318_SPI公共接口.md#ga67837cbae6f29c5f8ad9a05dbc9b05f8)、[SPI_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga43857c934651c4bfb3823a5080a4a294)、[SPI_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#gac9537325ca3188121d0f8c382c798ca1)、[SPI_DT_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga1eec8a77be8a512e8b0fa74d270877e5)、[SPI_DT_INST_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga4e5633f6e8da22f4c00a723a669b2d9a)及[SPI_CS_CONTROL_INIT](../hardware/P318_SPI公共接口.md#ga81308d27cd78e65f0a3ddaa918f2a74a)的可选delay参数已移除，每处调用都需删除该参数。改用spi-cs-setup-delay-ns及spi-cs-hold-delay-ns设备树属性；注意单位为纳秒，而非微秒。

<a id="stepper"></a>

### [步进电机（Stepper）](#id44)


- [adi,tmc50xx-stepper-ctrl](../stepper_binding_reference/P002_adi_tmc50xx-stepper-ctrl.md#std-dtcompatible-adi-tmc50xx-stepper-ctrl)及[adi,tmc51xx-stepper-ctrl](../stepper_binding_reference/P006_adi_tmc51xx-stepper-ctrl.md#std-dtcompatible-adi-tmc51xx-stepper-ctrl)的activate-stallguard2、stallguard-threshold-velocity及stallguard-velocity-check-interval-ms已移除。StallGuard配置现在通过[tmc50xx_stepper_ctrl_configure_stallguard()](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga7ef8f93f0301b2437b98eceac43407c7)、[tmc51xx_stepper_ctrl_configure_stallguard()](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga08b0b69ad4db741165d128cb2b2c3188)及[tmc_stallguard_settings](../hardware/P242_Trinamic堵转检测设置.md)在运行时完成。使用旧属性的树外驱动必须更新并移除这些属性。（[GitHub #110062](https://github.com/zephyrproject-rtos/zephyr/issues/110062)）

<a id="stm32"></a>

### [STM32](#id45)


- [gpio-keys](../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys)设备只有在设备树提供zephyr,suspend-action且值为"none"或"full-disconnect"时才能挂起，否则失败。详见本迁移指南关于该绑定的条目。（[GitHub #104690](https://github.com/zephyrproject-rtos/zephyr/issues/104690)、[GitHub #108294](https://github.com/zephyrproject-rtos/zephyr/issues/108294)）
- STM32MP13 SoC DTSI已按具体料号拆分，使密码外设hash节点只在具有该功能的变体上描述。开发板必须包含与准确SoC料号对应的DTSI，替代通用stm32mp135.dtsi。例如stm32mp135f_dk现在包含<st/mp13/stm32mp135f.dtsi>，替代<st/mp13/stm32mp135.dtsi>。树外STM32MP13开发板必须相应更新#include。（[GitHub #120085](https://github.com/zephyrproject-rtos/zephyr/issues/120085)）
- SoC DTSI现在将所有外设中断优先级统一设为0。依赖旧SoC DTSI优先级的应用，现在必须通过设备树明确配置。（[GitHub #106188](https://github.com/zephyrproject-rtos/zephyr/issues/106188)）
- [st,stm32-sai](../i2s_binding_reference/P017_st_stm32-sai.md#std-dtcompatible-st-stm32-sai)绑定已重构以反映SAI硬件拓扑：父节点表示SAI块控制器，新子绑定表示SAI子块实例。以下属性必须从父SAI节点移到子块节点：dmas、dma-names、pinctrl-0、pinctrl-names、mclk-enable、mclk-divider、synchronous及fifo-threshold。其中dma-names现在按枚举[tx, rx]验证。（[GitHub #104423](https://github.com/zephyrproject-rtos/zephyr/issues/104423)）
- [st,stm32-adc](../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc)绑定已重构以反映ADC硬件拓扑。父节点表示ADC公共块，保存时钟及所有连接到它的ADC实例共享的设置；新子绑定表示各ADC实例本身。

  现有&adcN标签仍表示ADC实例，但现在是&adcN_common公共块节点的子节点；N列出共享该块的实例，如&adc1_common、&adc12_common或&adc123_common。除了实例节点，还必须启用公共块节点。

  clocks、clock-names、st,adc-clock-source、st,adc-prescaler及vref-mv必须从&adcN实例移到父&adcN_common节点。现在每个公共块只描述一次时钟，因此共享该块的实例不能再设置相互冲突的时钟参数。

  <a id="tab-0-QmVmb3Jl"></a>

  <a id="tab-0-QWZ0ZXI="></a>

  <a id="panel-0-QmVmb3Jl"></a>

  **修改前（Before）**

  ```text
  &adc1 {
    clocks = <&rcc STM32_CLOCK(AHB2, 13)>,
             <&rcc STM32_SRC_SYSCLK ADC_SEL(3)>;
    clock-names = "adcx", "adc_ker";
    st,adc-clock-source = "ASYNC";
    st,adc-prescaler = <4>;
    vref-mv = <3000>;
    pinctrl-0 = <&adc1_in1_pa0>;
    pinctrl-names = "default";
    status = "okay";
  };
  ```

  <a id="panel-0-QWZ0ZXI="></a>

  **修改后（After）**

  ```text
  &adc12_common {
    clocks = <&rcc STM32_CLOCK(AHB2, 13)>,
             <&rcc STM32_SRC_SYSCLK ADC_SEL(3)>;
    clock-names = "adcx", "adc_ker";
    st,adc-clock-source = "ASYNC";
    st,adc-prescaler = <4>;
    vref-mv = <3000>;
    status = "okay";
  };

  &adc1 {
    pinctrl-0 = <&adc1_in1_pa0>;
    pinctrl-names = "default";
    status = "okay";
  };
  ```

  仅当vref-mv不同于默认3300时，才需要设置该属性。

  对[st,stm32f1-adc](../hardware/P840_STM32F1模数转换器绑定.md#dtbinding-st-stm32f1-adc)及[st,stm32f4-adc](../hardware/P841_STM32F4模数转换器绑定.md#dtbinding-st-stm32f4-adc)，各实例保留独立寄存器时钟，因此clocks及clock-names仍放在&adcN节点。（[GitHub #117309](https://github.com/zephyrproject-rtos/zephyr/issues/117309)）
- STM32 ADC，即[st,stm32-adc](../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc)：启用[CONFIG_ADC_STM32_VREFINT_CALIBRATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_STM32_VREFINT_CALIBRATE)时，[adc_ref_internal()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gad11845f5621d0b0d03da4b6484d79aa4)及采用INTERNAL参考的[adc_raw_to_millivolts_dt()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga11cf9c8f345a83f66704af83a2a26911)结果，可能不再与设备树vref-mv或3300完全一致。存在okay的[st,stm32-vref](../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref)节点时，此选项默认启用。禁用它可保留此前仅根据静态设备树值进行换算的行为。

  adc_ref_internal()不再为每个STM32 ADC子节点都报告第一个公共块的vref-mv，而是采用各自父公共块的值；该属性可选，默认3300。只影响包含多个公共块、为其设置不同vref-mv且依赖旧共享DEVICE_API的设备树。

  VREFINT测量不再绑定第一个okay的[st,stm32-vref](../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref)节点。任一vref节点，包括禁用节点，其io-channels引用的已启用ADC子节点均可刷新共享电源轨缓存。（[GitHub #117114](https://github.com/zephyrproject-rtos/zephyr/issues/117114)）
- [st,hci-stm32wba](../bluetooth_st_transport_binding_reference/P005_st_hci-stm32wba.md#std-dtcompatible-st-hci-stm32wba)及[st,stm32wba-ieee802154](../lora_ieee802154_binding_reference/P010_st_stm32wba-ieee802154.md#std-dtcompatible-st-stm32wba-ieee802154)节点，标签分别为bt_hci_wba及ieee802154，现在成为顶层[st,stm32wba-radio](../network_radio_frontend_binding_reference/P016_st_stm32wba-radio.md#std-dtcompatible-st-stm32wba-radio)节点的子节点，父节点标签为radio。interrupts现在设置在&radio上，不再在两个子节点重复。树外开发板若修改了任一子节点的interrupts，必须改为设置顶层&radio的属性。（[GitHub #110546](https://github.com/zephyrproject-rtos/zephyr/issues/110546)）
- ST摄像头及显示连接器的GPIO连接映射（GPIO Nexus）兼容项改名如下：st,dsi-lcd-qsh-030改为[st,dsi-lcd-qsh-030-connector](../gpio_silabs_st_connectors_binding_reference/P025_st_dsi-lcd-qsh-030-connector.md#std-dtcompatible-st-dsi-lcd-qsh-030-connector)；st,stm32-dcmi-camera-fpu-330zh改为[st,dvp-cam-zif-30-connector](../gpio_silabs_st_connectors_binding_reference/P026_st_dvp-cam-zif-30-connector.md#std-dtcompatible-st-dvp-cam-zif-30-connector)。
- STM32H5及STM32H7RS系列现在也通过[st,stm32-xspim](../qspi_ospi_xspi_binding_reference/P017_st_stm32-xspim.md#std-dtcompatible-st-stm32-xspim)声明并配置XSPI管理器。使用XSPI的开发板除了启用所需控制器，还必须启用&xspim。（[GitHub #109903](https://github.com/zephyrproject-rtos/zephyr/issues/109903)）
- STM32MP13 SoC DTSI中的以太网标签mac:及mdio:分别改为mac0:及mdio0:，以区分两个可用以太网控制器。（[GitHub #108574](https://github.com/zephyrproject-rtos/zephyr/issues/108574)）
- CONFIG_STM32_MEMMAP改名为[CONFIG_FLASH_STM32_NOR_MEMMAP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_STM32_NOR_MEMMAP)。
- 不再支持通过stm32_lp_tick_source标签选择LPTIM作为系统定时器，这种用法将触发构建错误。应改用通用chosen属性zephyr,system-timer。（[GitHub #112999](https://github.com/zephyrproject-rtos/zephyr/issues/112999)）（[通用chosen节点](../devicetree_api_index/P001_设备树API.md#devicetree-zephyr-chosen-nodes)）
- [st,stm32-pwr](../stm32_soc_power_binding_reference/P010_st_stm32-pwr.md#std-dtcompatible-st-stm32-pwr)中与唤醒引脚有关的wkup-pins-nb、wkup-pins-srcs、wkup-pins-pol、wkup-pins-pupd及子绑定均已移除。替代方式是在所有现有[st,stm32-pwr](../stm32_soc_power_binding_reference/P010_st_stm32-pwr.md#std-dtcompatible-st-stm32-pwr)节点下新增名为wakeup-controller的子节点，兼容项为[st,stm32-pwr-wkupctrl](../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl)。

  对多数树外用户，只需将status = "okay";及开发板DTS中可能声明的唤醒引脚节点，从&pwr移到新wakeup-controller子节点。以下设备树片段展示如何在开发板DTS中增加两行完成迁移：

  <a id="tab-1-QmVmb3Jl"></a>

  <a id="tab-1-QWZ0ZXI="></a>

  <a id="panel-1-QmVmb3Jl"></a>

  **修改前（Before）**

  ```text
  &pwr {
    wkup-pin@1 {
      /* ... */
    };

    status = "okay";
  };
  ```

  <a id="panel-1-QWZ0ZXI="></a>

  **修改后（After）**

  ```text
    &pwr {
      wakeup-controller {
        wkup-pin@1 {
          /* ... */
        };

        status = "okay";
      };
    };
  ```

  树内唤醒引脚节点现在名为wkup@N，替代wkup-pin@N；这只是名称调整，不影响功能。（[GitHub #114092](https://github.com/zephyrproject-rtos/zephyr/issues/114092)）
- SoC DTSI移除了[st,stm32-pwr](../stm32_soc_power_binding_reference/P010_st_stm32-pwr.md#std-dtcompatible-st-stm32-pwr)的status = "disabled";，因此节点现在默认启用。预计无影响，因为此前只有唤醒引脚功能使用该状态，而现在该功能由[st,stm32-pwr-wkupctrl](../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl)处理。（[GitHub #114092](https://github.com/zephyrproject-rtos/zephyr/issues/114092)）
- STM32H5系列除eth_mdc_px0、eth_mdio_px0及eth_pps_out_px0外，所有以太网引脚控制节点均已改名，以匹配数据手册名称。（[GitHub #118318](https://github.com/zephyrproject-rtos/zephyr/issues/118318)）

  下表列出新旧名称对应关系，可用于迁移：

  <table>
  <tr>
  <th>旧名称（Old Name）</th>
  <th>新名称，MII PHY</th>
  <th>新名称，RMII PHY</th>
  </tr>
  <tr>
  <td><code>eth_crs_dv_px0</code></td>
  <td>不适用于MII</td>
  <td><code>eth_rmii_crs_dv_px0</code></td>
  </tr>
  <tr>
  <td><code>eth_ref_clk_px0</code></td>
  <td>不适用于MII</td>
  <td><code>eth_rmii_ref_clk_px0</code></td>
  </tr>
  <tr>
  <td><code>eth_col_px0</code></td>
  <td><code>eth_mii_col_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_crs_px0</code></td>
  <td><code>eth_mii_crs_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_rx_clk_px0</code></td>
  <td><code>eth_mii_rx_clk_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_rx_dv_px0</code></td>
  <td><code>eth_mii_rx_dv_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_rx_er_px0</code></td>
  <td><code>eth_mii_rx_er_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_rxd0_px0</code></td>
  <td><code>eth_mii_rxd0_px0</code></td>
  <td><code>eth_rmii_rxd0_px0</code></td>
  </tr>
  <tr>
  <td><code>eth_rxd1_px0</code></td>
  <td><code>eth_mii_rxd1_px0</code></td>
  <td><code>eth_rmii_rxd1_px0</code></td>
  </tr>
  <tr>
  <td><code>eth_rxd2_px0</code></td>
  <td><code>eth_mii_rxd2_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_rxd3_px0</code></td>
  <td><code>eth_mii_rxd3_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_tx_clk_px0</code></td>
  <td><code>eth_mii_tx_clk_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_tx_en_px0</code></td>
  <td><code>eth_mii_tx_en_px0</code></td>
  <td><code>eth_rmii_tx_en_px0</code></td>
  </tr>
  <tr>
  <td><code>eth_txd0_px0</code></td>
  <td><code>eth_mii_txd0_px0</code></td>
  <td><code>eth_rmii_txd0_px0</code></td>
  </tr>
  <tr>
  <td><code>eth_txd1_px0</code></td>
  <td><code>eth_mii_txd1_px0</code></td>
  <td><code>eth_rmii_txd1_px0</code></td>
  </tr>
  <tr>
  <td><code>eth_txd2_px0</code></td>
  <td><code>eth_mii_txd2_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  <tr>
  <td><code>eth_txd3_px0</code></td>
  <td><code>eth_mii_txd3_px0</code></td>
  <td>不适用于RMII</td>
  </tr>
  </table>

  注意（Note）

  引脚名称现在随采用MII或RMII PHY而变化，由设备树以太网节点的phy-connection-type属性指定为mii或rmii。

  px0是占位符，应替换为实际引脚名称，例如pa1。

  STM32H5Ex及STM32H5Fx系列SoC不受影响，因为它们加入Zephyr时就一直使用新名称。

<a id="storage"></a>

### [存储（Storage）](#id46)


- [flash_sector](https://docs.zephyrproject.org/latest/doxygen/html/structflash__sector.html)的fs_off从off_t改为ptrdiff_t，使各平台及工具链统一使用本机寄存器宽度，而不随C库继承的POSIX off_t变化。Picolibc 1.8.12即便在32位平台也将off_t定义为64位整数，此变化可使使用该库时结构体恢复原布局。旧版Picolibc及其他受支持C库中，ptrdiff_t与off_t底层C类型相同；此变更旨在Picolibc升级前后保持fs_off底层类型一致。

<a id="syscon"></a>

### [系统控制器（Syscon）](#id47)


- 系统控制器（Syscon）API [syscon_read_reg()](../syscon_reference/P001_系统控制器公共接口.md#gad78bc0dbf923ab100c38b9f78c4fd596)及[syscon_write_reg()](../syscon_reference/P001_系统控制器公共接口.md#gad63c5c7a571214c6a4ce0c0f3bc7c53c)的寄存器偏移参数由uint16_t改为uint32_t，以支持更大偏移。明确用uint16_t声明该参数变量，或实现Syscon驱动API的代码，可能需要更新。

<a id="texas-instruments"></a>

### [德州仪器（Texas Instruments）](#id48)


- 将[ti,am654-timer](../stm32_ti_silabs_timer_binding_reference/P012_ti_am654-timer.md#std-dtcompatible-ti-am654-timer)实例作为系统定时器时，现在必须通过通用chosen属性zephyr,system-timer明确选择。使用它的所有SoC均已提供该选择。下游开发板或应用若需不同于SoC默认实例的定时器，必须覆盖此属性。（[GitHub #115068](https://github.com/zephyrproject-rtos/zephyr/issues/115068)）（[通用chosen节点](../devicetree_api_index/P001_设备树API.md#devicetree-zephyr-chosen-nodes)）

<a id="timer"></a>

### [定时器（Timer）](#id49)


- [sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)、[sys_clock_announce()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga9a90b75ed61618b3ccf0122a19f2f661)及[sys_clock_announce_locked()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga1ddcdf65784a84d6623805ae3c8dbd45)的节拍数参数，现在由有符号int32_t改为无符号uint32_t。树外系统定时器驱动必须更新[sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)定义，否则构建报类型冲突。内核现在还将请求超时限制为SYS_CLOCK_MAX_WAIT，不再向驱动传K_TICKS_FOREVER，因此驱动无需再按[sys_clock_announce()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga9a90b75ed61618b3ccf0122a19f2f661)范围限幅或专门处理K_TICKS_FOREVER，只需遵守自身硬件周期计数限制。（[GitHub #111022](https://github.com/zephyrproject-rtos/zephyr/issues/111022)）
- [sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)的bool idle参数已弃用。内核现在调用新钩子[sys_clock_idle_enter()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaab6df10ce3054ee84921aa90a1bc53d1)，替代以idle=true调用[sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)。为向后兼容，新钩子默认仍以idle=true调用旧函数，因此检查idle的驱动暂可不变；但应实现[sys_clock_idle_enter()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaab6df10ce3054ee84921aa90a1bc53d1)并将空闲专用处理移入。idle参数将在未来版本移除。（[GitHub #115844](https://github.com/zephyrproject-rtos/zephyr/issues/115844)）（[`sys_clock_set_timeout()`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)；[`sys_clock_idle_enter()`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaab6df10ce3054ee84921aa90a1bc53d1)）
- 启用[CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE)时，若无待处理超时，内核现在调用[sys_clock_no_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gacb9fad0efce687f8701dd90408a2ec7c)，替代以ticks=K_TICKS_FOREVER调用[sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)。为向后兼容，新钩子默认以ticks=UINT32_MAX调用旧函数，数值相同，因此把它视为“无截止时间”信号、用于停止时钟或设置最大等待的驱动仍可工作。但这些驱动应改为实现[sys_clock_no_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gacb9fad0efce687f8701dd90408a2ec7c)。（[`sys_clock_set_timeout()`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)；[`sys_clock_no_timeout()`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gacb9fad0efce687f8701dd90408a2ec7c)）

  注意两个新钩子的职责：CPU仍运行时屏蔽唤醒属于[sys_clock_no_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gacb9fad0efce687f8701dd90408a2ec7c)，必须保证[sys_clock_cycle_get_32()](../timer_reference/P086_系统时钟公共接口.md#ga42dcd1878309a82246dbfa26510f868a)继续工作；停止时间基准应在[sys_clock_idle_enter()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaab6df10ce3054ee84921aa90a1bc53d1)收到SYS_CLOCK_IDLE_FOREVER时执行。准确语义见[系统定时器驱动文档](https://docs.zephyrproject.org/latest/kernel/services/timing/system_timer_drivers.html#system-timer-drivers)。（[GitHub #115844](https://github.com/zephyrproject-rtos/zephyr/issues/115844)）
- 无周期节拍（Tickless）系统定时器驱动不应再自行处理节拍。实现头文件drivers/timer/system_timer_generic.h统一负责各驱动原先手工重复实现且容易出细微错误的计数逻辑：周期到节拍转换、上报基准、节拍对齐截止时间计算、计数器范围限幅及窄计数器回绕处理。驱动只需少量周期域原语，即读取周期计数器及设置绝对比较值，再包含该头文件一次，即可生成[sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)、[sys_clock_elapsed()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaa9b6d8eebc69d2808beb0580d974bb84)、[sys_clock_cycle_get_32()](../timer_reference/P086_系统时钟公共接口.md#ga42dcd1878309a82246dbfa26510f868a)及[sys_clock_cycle_get_64()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga25328a181bd0229ef5110c15e8452fc1)。（[GitHub #115844](https://github.com/zephyrproject-rtos/zephyr/issues/115844)）
- 启用SYSTEM_TIMER_LPM_COMPANION_COUNTER时，会在构建期检查通用chosen属性zephyr,system-timer-companion选中的低功耗辅助计数器（Low-Power Companion Counter），它必须可作为唤醒源。若节点尚无wakeup-source属性，应添加以声明该能力。（[GitHub #117274](https://github.com/zephyrproject-rtos/zephyr/issues/117274)）（[通用chosen节点](../devicetree_api_index/P001_设备树API.md#devicetree-zephyr-chosen-nodes)）

  注意（Note）

  此前Zephyr版本也预期这种行为，但从未强制断言检查。

<a id="usb"></a>

### [通用串行总线（USB）](#id50)


- STM32N6的SoC DTSI中，用于配置USBPHYC时钟多路复用器的clocks描述单元，已从usbotg_hsN移到usbphycN。采用自定义时钟选择配置的开发板，现在必须设置usbphycN而非usbotg_hsN的clocks。（[GitHub #107813](https://github.com/zephyrproject-rtos/zephyr/issues/107813)）
- 控制传输处理程序通过errno表示协议错误的方式已弃用，应直接返回错误码。（[GitHub #108118](https://github.com/zephyrproject-rtos/zephyr/issues/108118)）
- 主机发起具有主机到设备数据阶段的控制传输时，[usbd_class_api](../usb/P027_USB类回调接口.md)的control_to_dev及[usbd_vreq_node](../usb/P019_USB厂商请求节点.md)的to_dev回调，现在会在接收数据阶段之前以buf=NULL调用，使协议栈可在数据阶段返回STALL。树外类处理程序及厂商处理程序需要更新。（[GitHub #108840](https://github.com/zephyrproject-rtos/zephyr/issues/108840)）
- [usbd_class_api](../usb/P027_USB类回调接口.md)的control_to_host及[usbd_vreq_node](../usb/P019_USB厂商请求节点.md)的to_host回调，现在应自行分配数据阶段缓冲区，只分配实际需要的内存，使最坏内存占用由处理程序实现决定，而非来自主机的不可信wLength。树外类处理程序及厂商处理程序需要更新。（[GitHub #102491](https://github.com/zephyrproject-rtos/zephyr/issues/102491)）
- Espressif USB-OTG全速控制器兼容项espressif,esp32-usb-otg改名为[espressif,esp32-usb-otg-fs](../usb_controller_binding_reference/P010_espressif_esp32-usb-otg-fs.md#std-dtcompatible-espressif-esp32-usb-otg-fs)。内部PHY的D+/D-焊盘编号现在通过phy-dp-pin及phy-dm-pin提供。使用旧兼容项的树外设备树必须更新名称，并添加两个引脚属性。
- [st,stm32-usbphyc](../phy_binding_reference/P004_st_stm32-usbphyc.md#std-dtcompatible-st-stm32-usbphyc)现在要求clock-names。SoC DTSI提供默认值，但开发板DTS可能需要覆盖。（[GitHub #112477](https://github.com/zephyrproject-rtos/zephyr/issues/112477)）
- USB主机控制器API结构体uhc_api改名为uhc_driver_api，并采用[DEVICE_API](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。树外主机控制器驱动必须重命名结构体，将API实例改为DEVICE_API(uhc, ...)。（[GitHub #108414](https://github.com/zephyrproject-rtos/zephyr/issues/108414)）
- [st,stm32u5-otghs-phy](../phy_binding_reference/P007_st_stm32u5-otghs-phy.md#std-dtcompatible-st-stm32u5-otghs-phy)的clock-reference已弃用，应从DTS删除。未提供该属性时驱动自动计算正确值，仍提供时则遵循其值。（[GitHub #117882](https://github.com/zephyrproject-rtos/zephyr/issues/117882)）
- [usbd_class_api](../usb/P027_USB类回调接口.md)的get_desc回调现在返回const void *而非void *，使USB类可将描述符指针数组放在ROM。树外USB类必须更新处理函数返回类型。（[GitHub #118251](https://github.com/zephyrproject-rtos/zephyr/issues/118251)）
- CONFIG_USBD_CDC_ACM_BUF_POOL已移除。CDC ACM现在从每实例独立的池分配批量IN及OUT传输缓冲区，由tx-fifo-size及rx-fifo-size设备树属性决定池大小。

<a id="video"></a>

### [视频（Video）](#id51)


- [ovti,ov7670](../video_camera_endpoint_binding_reference/P016_ovti_ov7670.md#std-dtcompatible-ovti-ov7670)及[ovti,ov7675](../video_camera_endpoint_binding_reference/P017_ovti_ov7675.md#std-dtcompatible-ovti-ov7675)摄像头驱动现在假定XCLK输入为24 MHz，替代6 MHz，以匹配OV7670数据手册的典型频率。开发板必须相应更新XCLK。例如frdm_mcxn236从kFRO12M_to_CLKOUT二分频得到6 MHz，改为kFRO_HF_to_CLKOUT二分频得到24 MHz；frdm_mcxn947保留kMAIN_CLK_to_CLKOUT，但CLKOUT分频数从25改为6，得到24 MHz。（[GitHub #109393](https://github.com/zephyrproject-rtos/zephyr/issues/109393)）
- <zephyr/drivers/video.h>中的API现在位于<zephyr/video/video.h>。（[GitHub #112420](https://github.com/zephyrproject-rtos/zephyr/issues/112420)）

<a id="wifi"></a>

### [无线局域网（Wi-Fi）](#id52)


- [net_wifi_mgmt_offload](https://docs.zephyrproject.org/latest/doxygen/html/structnet__wifi__mgmt__offload.html)及其内部[ethernet_api](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)、[wifi_mgmt_ops](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__mgmt__ops.html)实现的函数，新增[net_if](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if.html)指针参数。该API不直接暴露给应用，因此仅树外驱动需要更新。（[GitHub #106086](https://github.com/zephyrproject-rtos/zephyr/issues/106086)）
- Espressif Wi-Fi选项CONFIG_ESP32_WIFI_STA_AUTO_DHCPV4已移除，改用通用[CONFIG_WIFI_STA_AUTO_DHCPV4](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_STA_AUTO_DHCPV4)。此前禁用厂商专用选项的应用，现在必须禁用通用选项，才能在STA连接后保留手动DHCPv4或静态IP行为。
- [wifi_status](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__status.html)新增status_code及reason_code，携带原始IEEE 802.11代码，因此结构体大于旧的int。发出或接收NET_EVENT_WIFI_SCAN_DONE、NET_EVENT_WIFI_CONNECT_RESULT、NET_EVENT_WIFI_DISCONNECT_RESULT、NET_EVENT_WIFI_DISCONNECT_COMPLETE、NET_EVENT_WIFI_AP_ENABLE_RESULT及NET_EVENT_WIFI_AP_DISABLE_RESULT的代码，必须将事件载荷长度从sizeof(int)改为sizeof(struct wifi_status)。只读取status值的处理程序不受影响，因为它仍是首个成员。（[GitHub #116704](https://github.com/zephyrproject-rtos/zephyr/issues/116704)）
- Wi-Fi连接请求超时后，现在通过NET_EVENT_WIFI_CONNECT_RESULT报告[WIFI_STATUS_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)，替代原始-ETIMEDOUT。只影响由认证请求方（Supplicant）处理的连接。原来匹配errno值的应用必须改为匹配状态值。（[GitHub #116704](https://github.com/zephyrproject-rtos/zephyr/issues/116704)）

<a id="xen"></a>

### [Xen 虚拟机监控器（Xen）](#id53)


- 引入zephyr-xenlib后，Xen公共头文件路径已变化，请使用xen/public/...替代zephyr/xen/public/...。

<a id="bluetooth"></a>

## [蓝牙（Bluetooth）](#id54)

<a id="bluetooth-audio"></a>

### [蓝牙音频（Bluetooth Audio）](#id55)


- 基本音频配置文件（BAP）


  - [bt_bap_stream.codec_cfg](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream.html#a286b95d990433995a7ee74b7c3ec2f59)现在为const，以体现其只读性质。非读取用法必须改用相应操作，例如[bt_bap_stream_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaaecbb590e5d073829d4c150e4fd2d8aa)、[bt_bap_stream_reconfig()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa7df3f6b906241ad5291295a6ddcf1e4)、[bt_bap_stream_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga13a859b31b0310ec22339ec7ed0754f8)或[bt_bap_stream_metadata()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0afe6c927729697e2f984cefcbc7c0f1)。（[GitHub #104219](https://github.com/zephyrproject-rtos/zephyr/issues/104219)）
  - [bt_bap_stream.qos](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream.html#a503bd9d7e7f594d090bcbe7fc5e313fc)现在为const，以体现只读性质。非读取用法必须通过[bt_bap_unicast_group_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaafd53b5f45d998b44e94a1b58e93ba21)、[bt_bap_unicast_group_reconfig()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gacd684504c8127ff4f8d038cc06718e5e)、[bt_bap_broadcast_source_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gacdebfc435eebd47cf9cd05099a5f78e0)或[bt_bap_broadcast_source_reconfig()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#gabecaa9db7be5cb03ed997ba478878d40)等相应操作设置。（[GitHub #104887](https://github.com/zephyrproject-rtos/zephyr/issues/104887)）
  - API中几乎所有struct bt_bap_qos_cfg *现在均带const。因此qos一旦存入[bt_bap_broadcast_source_param](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__param.html)或[bt_bap_unicast_group_stream_param](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__stream__param.html)等参数结构体，就不能通过其中的指针修改，而应修改原结构体对象。（[GitHub #104219](https://github.com/zephyrproject-rtos/zephyr/issues/104219)）
  - [bt_bap_unicast_group_info.sink_pd](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a74730a75337b985b7260297b1ecf8a21)及source_pd现在反映组中定义的本地值，而非任何远端音频流端点（ASE）的配置值。（[GitHub #104887](https://github.com/zephyrproject-rtos/zephyr/issues/104887)）（[`bt_bap_unicast_group_info.source_pd`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a05ecedc6350f6961d9794f854bf5be37)）
  - [bt_bap_unicast_client_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gacef9c88f66762e8de19303d20dafa0bb)及[bt_bap_broadcast_assistant_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gab59c5ebc4fef28da34d8a54b1244c33b)现在要求连接在发现前已完成配对，并满足BAP安全要求。新设备通常需要调用[bt_conn_set_security()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae001f1268e1ff42c3c974c95dcb6735d)；已绑定设备重连通常无需额外操作。
  - API中几乎所有struct bt_audio_codec_cfg *现在均带const。因此codec_cfg一旦存入[bt_bap_stream](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream.html)或[bt_bap_broadcast_source_subgroup_param](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__broadcast__source__subgroup__param.html)等结构体，就不能通过参数中的指针修改，而应修改原结构体对象。（[GitHub #104219](https://github.com/zephyrproject-rtos/zephyr/issues/104219)）
  - 按照BAP规范，所有BAP角色现在要求[CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)至少为19个八位字节（Octet）。使用BAP且配置值更小时，应用必须提高到至少19。受影响选项如下：（[`CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUDIO_CODEC_CFG_MAX_DATA_SIZE)）


    - [`CONFIG_BT_ASCS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ASCS)
    - [`CONFIG_BT_BAP_UNICAST_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_SERVER)
    - [`CONFIG_BT_BAP_UNICAST_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_UNICAST_CLIENT)
    - [`CONFIG_BT_BAP_BROADCAST_SOURCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SOURCE)
    - [`CONFIG_BT_BAP_BROADCAST_SINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_SINK)
    - [`CONFIG_BT_BAP_SCAN_DELEGATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_SCAN_DELEGATOR)
    - [`CONFIG_BT_BAP_BROADCAST_ASSISTANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_ASSISTANT)

    参见[GitHub #107989](https://github.com/zephyrproject-rtos/zephyr/issues/107989)。
  - 基本音频配置文件（BAP）的广播音频助手（Broadcast Audio Assistant）、广播接收端（Broadcast Audio Sink）、广播源（Broadcast Audio Source）、单播音频客户端（Unicast Audio Client）及单播音频服务器（Unicast Audio Server）示例，从[samples/bluetooth/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/)移到[samples/bluetooth/audio](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/audio)。（[基本音频配置文件（BAP）广播音频助手（Broadcast Audio Assistant）](../bluetooth_samples/P065_BAP广播音频助手.md#bluetooth_bap_broadcast_assistant)；[基本音频配置文件（BAP）广播音频接收端（Broadcast Audio Sink）](../bluetooth_samples/P066_BAP广播音频接收端.md#bluetooth_bap_broadcast_sink)；[基本音频配置文件（BAP）广播音频源（Broadcast Audio Source）](../bluetooth_samples/P067_BAP广播音频源.md#bluetooth_bap_broadcast_source)；[基本音频配置文件（BAP）单播音频客户端（Unicast Audio Client）](../bluetooth_samples/P068_BAP单播音频客户端.md#bluetooth_bap_unicast_client)；[基本音频配置文件（BAP）单播音频服务器（Unicast Audio Server）](../bluetooth_samples/P069_BAP单播音频服务端.md#bluetooth_bap_unicast_server)）
  - bt_bap_stream_ops.configured改名为codec_configured，qos_set改名为qos_configured，以匹配音频流控制服务（ASCS）规范定义的ASE状态。回调签名及调用条件不变，应用只需在回调赋值位置将configured替换为codec_configured，将qos_set替换为qos_configured。（[GitHub #114835](https://github.com/zephyrproject-rtos/zephyr/issues/114835)）（[`bt_bap_stream_ops.codec_configured`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream__ops.html#afa90da66b69835c9df73068aa6373778)；[`bt_bap_stream_ops.qos_configured`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream__ops.html#a23616f17ef90a03db2f78df180887897)）
  - [bt_bap_scan_delegator_mod_src()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac022f38269742f16ff6887840ef5ba9a)不再将metadata_len = 0解释为保留现有内容，而会将子组元数据长度设为0。若要保留现有数据，必须将metadata_len设为原长度，并复制现有元数据。
- 通用音频配置文件（CAP）


  - [bt_cap_commander_broadcast_reception_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga25be83bb53c8e2ab76f311eaf4f615b9)现在等待CAP接收方同步到广播后才完成。因此广播源必须处于活动状态，启用周期广播并配置BASE；即使原先离线，或是[bt_cap_handover_unicast_to_broadcast()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaae56deae3792740bc3e8074882c87837)创建的同位置广播源，也需满足这些条件。对后者，可用新增[bt_cap_handover_cb.unicast_to_broadcast_created](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__cb.html#a46892bfd9ac055ae73634520b385fa51)配置BASE。应用此前为等待接收状态更新、确认同步成功而实现的检查可以移除，因为调用[bt_cap_commander_cb.broadcast_reception_start](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__cb.html#a14f6a51db5a76aac015a5de617712af3)时，启动函数已保证这一点。[bt_cap_commander_broadcast_reception_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gac5b2b6d617a092fb98b23c41b2f52d15)也作了类似调整。（[GitHub #101070](https://github.com/zephyrproject-rtos/zephyr/issues/101070)）（[`bt_cap_handover_unicast_to_broadcast()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gaae56deae3792740bc3e8074882c87837)；[`bt_cap_commander_broadcast_reception_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga25be83bb53c8e2ab76f311eaf4f615b9)）
  - 通用音频配置文件（Common Audio Profile，CAP）的接收方（Acceptor）、切换（Handover）及发起方（Initiator）示例，从samples/bluetooth/移到samples/bluetooth/audio。（[通用音频配置文件（CAP）接收方（Acceptor）](../bluetooth_samples/P070_CAP接受端.md#bluetooth_cap_acceptor)；[通用音频配置文件（CAP）切换（Handover）](../bluetooth_samples/P071_CAP切换.md#bluetooth_cap_handover)；[通用音频配置文件（CAP）发起方（Initiator）](../bluetooth_samples/P072_CAP发起端.md#bluetooth_cap_initiator)）
  - 若调用不会改变任何状态，即参数元数据与服务器已报告给本端的内容一致，[bt_cap_initiator_unicast_audio_update()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga92e4e2c12720ec25c4050cde307cd639)现在拒绝调用并返回-EALREADY。
- 呼叫控制配置文件（CCP）


  - [bt_tbs_client_cb.technology](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__client__cb.html#a596b31583975c416aa9cb6d64301c55f)的value参数由uint32_t改为enum bt_bearer_tech。使用该回调的应用应更新类型。（[GitHub #102430](https://github.com/zephyrproject-rtos/zephyr/issues/102430)）
  - 全部BT_TBS_TECHNOLOGY_*值改名为BT_BEARER_TECH_*，如BT_TBS_TECHNOLOGY_3G改为BT_BEARER_TECH_3G。应用可查找替换前缀。此外，定义从[include/zephyr/bluetooth/audio/tbs.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/audio/tbs.h)移到[include/zephyr/bluetooth/assigned_numbers.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/assigned_numbers.h)。（[GitHub #102430](https://github.com/zephyrproject-rtos/zephyr/issues/102430)）
  - bt_tbs_register_param.supported_features改名为optional_opcodes，应用可直接替换成员名。BT_TBS_FEATURE_*宏也改为BT_TBS_OPTIONAL_OPCODE_*，可按前缀替换。（[GitHub #103350](https://github.com/zephyrproject-rtos/zephyr/issues/103350)）（[`bt_tbs_register_param.optional_opcodes`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__register__param.html#a004fc8f70cff59acf0122135bdd27065)）
  - 呼叫控制配置文件（Call Control Profile，CCP）的呼叫控制服务器（Call Control Server）示例，从samples/bluetooth/移到samples/bluetooth/audio。译注：原文将Call Control Server重复列出两次，此处不推断另一项名称。（[呼叫控制配置文件（CCP）呼叫控制服务器（Call Control Server）](../bluetooth_samples/P073_CCP呼叫控制客户端.md#bluetooth_ccp_call_control_client)；[呼叫控制配置文件（CCP）呼叫控制服务器（Call Control Server）](../bluetooth_samples/P074_CCP呼叫控制服务端.md#bluetooth_ccp_call_control_server)）
- 协调集合识别配置文件（CSIP）


  - 协调集合标识服务（Coordinated Set Identification Service，CSIS）的可选特征，现在可通过Kconfig配置，必须明确启用：


    - 协调集合大小（Coordinated Set Size）：[CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_SIZE_SUPPORT)。
    - 集合成员锁（Set Member Lock）：[CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_LOCK_SUPPORT)。
    - 集合成员序号（Set Member Rank）：[CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_MEMBER_RANK_SUPPORT)。
- 听力访问配置文件（HAP）


  - 听力访问配置文件（Hearing Access Profile，HAP）的助听器（Hearing Aid，HA）示例，从samples/bluetooth/移到samples/bluetooth/audio。（[听力访问配置文件（HAP）助听器（Hearing Aid，HA）](../bluetooth_samples/P075_HAP助听器.md#bluetooth_hap_ha)）
- 公共广播配置文件（PBP）


  - 公共广播配置文件（Public Broadcast Profile，PBP）的公共广播接收端（Public Broadcast Sink）及公共广播源（Public Broadcast Source）示例，从samples/bluetooth/移到samples/bluetooth/audio。（[公共广播配置文件（PBP）公共广播接收端（Public Broadcast Sink）](../bluetooth_samples/P076_PBP公共广播接收端.md#bluetooth_public_broadcast_sink)；[公共广播配置文件（PBP）公共广播源（Public Broadcast Source）](../bluetooth_samples/P077_PBP公共广播源.md#bluetooth_public_broadcast_source)）
- 电话与媒体音频配置文件（TMAP）


  - 电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）的广播媒体接收方（BMR）、广播媒体发送方（BMS）、中心设备（Central）及外围设备（Peripheral）示例，从samples/bluetooth/移到samples/bluetooth/audio。（[电话与媒体音频配置文件（TMAP）广播媒体接收方（BMR）](../bluetooth_samples/P078_TMAP广播媒体接收器.md#ble_peripheral_tmap_bmr)；[电话与媒体音频配置文件（TMAP）广播媒体发送方（BMS）](../bluetooth_samples/P079_TMAP广播媒体发送器.md#ble_peripheral_tmap_bms)；[电话与媒体音频配置文件（TMAP）中心设备（Central）](../bluetooth_samples/P080_TMAP中心设备.md#ble_peripheral_tmap_central)；[电话与媒体音频配置文件（TMAP）外围设备（Peripheral）](../bluetooth_samples/P081_TMAP外设.md#ble_peripheral_tmap_peripheral)）
- 音量偏移控制服务（VOCS）


  - 音量偏移控制服务（VOCS）客户端现在要求自动发现客户端特征配置（CCC）。[CONFIG_BT_VOCS_CLIENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_VOCS_CLIENT)依赖[CONFIG_BT_GATT_AUTO_DISCOVER_CCC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)，使用该客户端的应用必须确保启用CCC自动发现。（[GitHub #110607](https://github.com/zephyrproject-rtos/zephyr/issues/110607)）

<a id="bluetooth-classic"></a>

### [经典蓝牙（Bluetooth Classic）](#id56)


- [bt_conn_cb](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__cb.html)中BR/EDR专用回调role_changed及br_mode_changed，移入新子结构体[bt_conn_br_cb](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__br__cb.html)，通过br成员访问。应用必须更新指定初始化器：


  - .role_changed改为.br.role_changed。
  - .br_mode_changed改为.br.mode_changed。

  参见[GitHub #108022](https://github.com/zephyrproject-rtos/zephyr/issues/108022)。
- CONFIG_BT_DEVICE_VEDNOR_ID改名为[CONFIG_BT_DEVICE_VENDOR_ID](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_VENDOR_ID)，以修正拼写错误。
- [bt_rfcomm_dlc_ops.recv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__dlc__ops.html#ab8ef2f8c1d27eee20d0b5e7fce6f7354)回调返回类型从void改为int。现有实现须返回0以保留原同步行为，或返回-EINPROGRESS以采用新的异步完成路径。

<a id="bluetooth-hci"></a>

### [蓝牙主机控制器接口（Bluetooth HCI）](#id57)


- bflb,bl70x-bt-hci改名为[bflb,bt-hci](../bluetooth_vendor_hci_binding_reference/P002_bflb_bt-hci.md#std-dtcompatible-bflb-bt-hci)，因为单一绑定现在覆盖博流（Bouffalo Lab）所有BL60x、BL70x及BL70XL片上BLE控制器。树外开发板及扩展板必须更新设备树。
- 蓝牙HCI驱动现在必须将公共结构体作为自身data及config结构体的首个字段，分别为[bt_hci_driver_data](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__data.html)及[bt_hci_driver_config](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__config.html)。
- HCI驱动setup()操作、[bt_hci_setup()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)、[bt_hci_setup_params](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__setup__params.html)、[CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)及H:4驱动的bt_h4_vnd_setup()钩子已弃用，将在两个版本后移除。实现setup()的驱动应将工作移到[bt_hci_driver_api.open](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__api.html#a889d9a3553c4dd04595198dcfaf61d23)：


  - 使用[bt_hci_lockstep_cmd_send_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)通过驱动自身传输发送厂商专用命令，替代主机HCI命令API，并将每个收到的包交给[bt_hci_lockstep_feed()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gacb84fdafc6376483e12a8b7ec391fa7c)。include/zephyr/bluetooth/hci_pkt.h提供命令封装辅助函数。若通过HCI命令以外的方法复位控制器，之后调用[bt_hci_lockstep_reset()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga1d2d42b2db398cf4449b337588897f56)。
  - 通过[bt_hci_get_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)读取公共地址，替代[bt_hci_setup_params.public_addr](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__setup__params.html#a6aea62826eeab39e6af40f9005548f3f)。与原行为相同，未设置公共地址时得到BT_ADDR_ANY，而非BT_ADDR_NONE。
  - 从驱动Kconfig移除select BT_HCI_SETUP。

  这样，无主机（Host）构建中也会执行初始化，以前这类构建从不调用setup()。存在主机时，初始化在调用[bt_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac45d16bfe21c3c38e834c293e5ebc42b)的线程中、该函数返回前完成，即使传入ready回调也一样；旧setup()在这种情况下由系统工作队列执行。所有原先实现setup()的树内驱动均已转换。
- [bt_hci_driver_api.open](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__api.html#a889d9a3553c4dd04595198dcfaf61d23)回调不再接受recv参数，由公共HCI驱动层通过公共数据结构管理。驱动使用新[bt_hci_recv()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga407beb20238b8fe6fdbd4ef199eb1f6c)将数据交给蓝牙主机栈等上层。少数需要取得recv()错误的驱动可用[bt_hci_recv_err()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaad2dc7f911913468a1440fad91cb3d62)，但出错时调用者负责释放缓冲区引用。
- [CONFIG_BT_HCI_SET_PUBLIC_ADDR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SET_PUBLIC_ADDR)不再选择[CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)。仍在setup()中应用公共地址的树外驱动，必须自行选择[CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)，否则[bt_hci_driver_api](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__api.html)不存在setup成员，回调也不会调用。地址现在从传输打开时即可通过[bt_hci_get_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)取得，因此可改在open()中应用。
- HCI驱动API现已明确生命周期约定。调用方对同一设备不能并发调用[bt_hci_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gac744c98801cea5afd13d6774154e71c8)、[bt_hci_close()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gad187f0aff959a4756b281aa33d1b4394)及[bt_hci_send()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga64079b6f03479561c1c7d09b3af81ede)；发送仅能用于已打开的传输，也不能从接收回调调用关闭。驱动方面：open()失败后传输保持关闭，不会随后调用close()；close()失败则保持打开；关闭成功后不再调用接收回调；除setup()外，驱动操作不得使用主机HCI命令API。树外HCI驱动及直接调用驱动API的树外代码可能需调整以遵循这些规则。（[HCI驱动API（HCI Driver API）](../bluetooth/P013_HCI驱动.md#bt-hci-drivers)；[`bt_hci_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga64079b6f03479561c1c7d09b3af81ede)；[`bt_hci_close()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gad187f0aff959a4756b281aa33d1b4394)）
- H:4厂商扩展现在从[include/zephyr/drivers/bluetooth/h4.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/bluetooth/h4.h)声明的[bt_h4_vnd_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html#ga4ac11c5a18b0891a04bb791e2f7c15bd)配置控制器，替代bt_h4_vnd_setup()及setup()操作。H:4驱动在open()末尾调用该钩子，并提供用于扩展命令的锁步辅助器（Lockstep Helper）。扩展选择[CONFIG_BT_H4_VND_OPEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_H4_VND_OPEN)而非[CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)，并用[bt_hci_get_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)读取公共地址，不再从setup参数取值。若扩展仍选择[CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)，bt_h4_vnd_setup()仍通过setup()调用。

<a id="bluetooth-host"></a>

### [蓝牙主机（Bluetooth Host）](#id58)


- 连接参数更新失败，即LE Connection Update Complete事件状态非零时，不再调用[bt_conn_cb](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__cb.html).le_param_updated。以前总会调用，报告未改变的参数却不提供错误信息，无法与成功更新区分。若应用需要获知由应用发起的参数更新被拒绝，应启用[CONFIG_BT_USER_CONN_PARAM_REJECTED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_USER_CONN_PARAM_REJECTED)并实现新le_param_update_rejected回调。
- CONFIG_BT_RECV_CONTEXT选择项及CONFIG_BT_RECV_WORKQ_SYS、CONFIG_BT_RECV_WORKQ_BT已移除。主机现在始终在专用蓝牙RX工作队列处理低优先级HCI包，即旧BT_RECV_WORKQ_BT行为。曾为节省RAM而选择系统工作队列的应用，例如nRF51应用，必须删除旧选项；现在始终创建专用RX线程。应根据主机功能调整[CONFIG_BT_RX_STACK_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RX_STACK_SIZE)。低优先级接收不再占用系统工作队列后，可能可以减小[CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE)，但两个栈大小均取决于应用，必须通过栈使用测量验证。
- 启用[CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES)时，主机会在建立绑定时读取对端的中心设备地址解析（Central Address Resolution）特征一次；条件允许时该选项默认启用。若对已知不支持地址解析的对端使用[BT_LE_ADV_OPT_DIR_ADDR_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f)，[bt_le_adv_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad2e3caef88d52d720e8e4d21df767b02)、[bt_le_ext_adv_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad02b855dd7a26e3910b247fa73f19297)及[bt_le_ext_adv_update_param()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1aabdb81cb1a1841ff0fb91d849123fc)现在返回-ENOTSUP，因为对端无法解析目标地址，永远不会响应这种广播。应用可提前通过[bt_le_bond_addr_res_support()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5b5e51f79896d674bf6b70b2251e79d4)查询，并改为针对其身份地址做定向广播。禁用该选项可恢复旧行为。
- 部分蓝牙主机工作项现在在专用蓝牙RX工作队列而非系统工作队列执行，因此其应用回调运行于蓝牙RX线程。包括连接拆除、延迟连接工作，如disconnected()及SMP配对超时，以及ATT/GATT、L2CAP、AVDTP及HFP AG的超时和完成路径。依赖回调运行于系统工作队列的应用，应复核同步及回调栈需求，详见[GitHub #93033](https://github.com/zephyrproject-rtos/zephyr/issues/93033)。
- CONFIG_BT_AUTO_PHY_UPDATE已移除，改用按角色划分的BT_AUTO_PHY_CENTRAL及BT_AUTO_PHY_PERIPHERAL。旧值=n不能简单通过删除选项迁移，因为中心角色默认[CONFIG_BT_AUTO_PHY_CENTRAL_2M](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_CENTRAL_2M)；必须将两个角色都明确设为_NONE。
- 自Zephyr 4.2起弃用的CONFIG_BT_CONN_TX_MAX已移除。带回调的待处理TX缓冲区数量始终由[CONFIG_BT_BUF_ACL_TX_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BUF_ACL_TX_COUNT)决定。
- 传统广播集的[bt_le_ext_adv_info.sid](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__info.html#a19877c440137814ec0e4aa1a1270f6fe)现在设为BT_GAP_SID_INVALID，因为SID仅对扩展广播集有效。应用不应期待[bt_le_adv_param.sid](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__adv__param.html#a6e2f0e1b76495afe7fe661e8698d0909)应用于传统广播集。
- [bt_le_ext_adv_info.sid](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__info.html#a19877c440137814ec0e4aa1a1270f6fe)现在反映传给[bt_le_ext_adv_update_param()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1aabdb81cb1a1841ff0fb91d849123fc)的SID；以前即使控制器已采用新值，此字段仍保留[bt_le_ext_adv_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad02b855dd7a26e3910b247fa73f19297)时的值。
- [bt_addr_le_to_str()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga74a644cd3de081a353a281d80b32b91e)现在在LE地址前加单字符类型前缀：P:表示公共地址，R:表示随机地址，后面直接接地址，例如R:11:22:33:44:55:66。不再输出11:22:33:44:55:66 (random)。含额外HCI级标志位的类型，如BT_ADDR_LE_RANDOM_ID，也按基础类型格式化，不再显示(random-id)或原始十六进制值。解析Zephyr日志或Shell输出以提取地址的代码必须更新。[BT_ADDR_LE_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gae0df0067c55eb4388625bb62f3d7e235)随之从30减为20。
- [bt_addr_le_from_str()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga24752df467449d7cb0dc25e3c4330862)不再接受单独的地址类型字符串，只接受[bt_addr_le_to_str()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga74a644cd3de081a353a281d80b32b91e)生成的P:/R:前缀格式；旧"XX:XX:XX:XX:XX:XX"加"public"或"random"格式不再支持。因此，bt connect、bt disconnect、bt clear、bt fal-add、bt per-adv-sync-create、gatt resubscribe及bap_broadcast_assistant add_src等接受LE地址的命令，均改为单个P:XX:XX:XX:XX:XX:XX或R:XX:XX:XX:XX:XX:XX参数。

<a id="bluetooth-mesh"></a>

### [蓝牙网状网络（Bluetooth Mesh）](#id59)


- 已弃用的CONFIG_BT_MESH_BLOB_IO_FLASH_WITH_ERASE及CONFIG_BT_MESH_BLOB_IO_FLASH_WITHOUT_ERASE已移除，无替代选项。自Zephyr 4.3起，BLOB IO Flash模块在运行时查询擦除能力，这两个选项从当时起已弃用且不再生效。

<a id="bluetooth-services"></a>

### [蓝牙服务（Bluetooth Services）](#id60)


- [CONFIG_BT_OTS_MAX_OBJ_CNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS_MAX_OBJ_CNT)从hex改为更直观的int。将0x30等十六进制值转换为48等十进制值即可。

<a id="networking"></a>

## [网络（Networking）](#id61)


- HTTP客户端响应回调[http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)现在可能针对同一个接收缓冲区调用多次，每个正文片段一次，例如分块响应的每个块一次。原先假定每次接收只调用一次的应用，必须逐一追加收到的所有片段。
- CONFIG_NET_TEST_PROTOCOL及其唯一被测系统示例samples/net/sockets/tcp已移除。该选项提供JSON控制通道，让树外TTCN-3套件驱动TCP栈并读取内部状态，但树内没有启用它，其代码已多年无法编译，使用它的测试套件也被作者归档。

  该选项还会禁用初始序列号随机化，使net_tcp_connect()不等待连接就返回，因此启用与未启用该选项的构建行为不同。

  没有替代配置选项。替代方案是[tests/net/conformance](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/conformance)中的一致性测试，直接通过网络驱动未改动的构建，其中TCP套件覆盖相同范围。详见[使用TTCN-3进行协议一致性测试](../networking/P155_TTCN3协议一致性测试.md#ttcn3-testing)（Protocol Conformance Testing with TTCN-3）。
- [dns_resolve_context](https://docs.zephyrproject.org/latest/doxygen/html/structdns__resolve__context.html)内部的struct dns_server改名为struct dns_server_info。C++类成员不能与所在类同名，旧类型标签导致C++无法包含<zephyr/net/dns_resolve.h>。字段名均未更改，因此ctx->servers[i].dns_server_addr等访问不受影响；仅明确引用该类型的代码，例如CONTAINER_OF()用法，需要更新。
- 多个IP路由相关选项现在增加IPV6前缀，以便为IPv4提供相同功能且可独立控制的符号。
- IPv4及IPv6单播路由表支持，现在分别通过[CONFIG_NET_IPV4_ROUTE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTE)及[CONFIG_NET_IPV6_ROUTE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ROUTE)提供。

  这些选项控制各地址族的单播路由表，用于静态路由管理、网络Shell路由命令，以及本机发起流量的主机侧路由选择，例如发往VPN的分组。它们本身不启用接口间分组转发。
- [CONFIG_NET_IPV4_ROUTING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTING)及[CONFIG_NET_IPV6_ROUTING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ROUTING)，分别改名为[CONFIG_NET_IPV4_FORWARDING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_FORWARDING)及[CONFIG_NET_IPV6_FORWARDING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_FORWARDING)。

  新名称明确描述接口间IP转发。只需路由表查询或静态路由的应用，应启用对应ROUTE选项，保持转发禁用；作为路由器的应用应同时启用路由表及对应FORWARDING选项。（[`CONFIG_NET_IPV4_ROUTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTE)；[`CONFIG_NET_IPV6_ROUTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ROUTE)）
- 树外IPv6配置还应停止使用已弃用别名[CONFIG_NET_ROUTE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE)、[CONFIG_NET_ROUTING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTING)、[CONFIG_NET_MAX_ROUTES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MAX_ROUTES)及[CONFIG_NET_MAX_NEXTHOPS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MAX_NEXTHOPS)，直接采用CONFIG_NET_IPV6_*符号。
- <a id="index-0"></a>

  samples/net/wifi/test_certs/rsa2k中的企业网络测试证书已移除，因为TF-PSA-Crypto无法解密其采用DES加密的PKCS#8私钥。改用samples/net/wifi/test_certs/rsa2k_no_des，或将WIFI_TEST_CERTS_DIR设为其他使用AES加密的证书目录。
- [CONFIG_OPENTHREAD_JOINER_PSKD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_JOINER_PSKD)不再默认使用公开文档中的"J01NME"，现在没有默认值。启用[CONFIG_OPENTHREAD_JOINER_AUTOSTART](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_JOINER_AUTOSTART)的构建，必须配置6～32个大写字母数字字符的PSKd才能成功；允许0～9及A～Z，但排除I、O、Q、Z。

  通过Kconfig设置的PSKd会编译进镜像，因此所有运行同一固件的设备都使用同一值，使范围内任意配置管理者（Commissioner）可将尚未配网的设备加入自己的网络。该选项应作为开发辅助；产品固件应从工厂数据读取每设备独有的PSKd，并由应用调用otJoinerStart()。
- net_if_config_get因与[net_if_get_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae271e0e4dcb031a83d9908e597a45048)重复而移除。（[GitHub #110930](https://github.com/zephyrproject-rtos/zephyr/issues/110930)）
- ZVFS事件文件描述符（Eventfd）数量现在由ZVFS_EVENTFD_SIZE定义决定，不再直接使用[CONFIG_ZVFS_EVENTFD_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_EVENTFD_MAX)。子系统可通过CONFIG_ZVFS_EVENTFD_ADD_SIZE_前缀选项声明需求，将需求求和后与MAX比较，取较大值。若要强制使用MAX，即使它小于需求总和，可启用新增且默认禁用的[CONFIG_ZVFS_EVENTFD_IGNORE_MIN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_EVENTFD_IGNORE_MIN)。因此，为HTTP服务器、CoAP服务器、LwM2M、PTP、SSH、套接字服务及WPA认证请求方等分配eventfd的网络子系统，应用无需再手动增加MAX。（[GitHub #111201](https://github.com/zephyrproject-rtos/zephyr/issues/111201)）（[`CONFIG_ZVFS_EVENTFD_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_EVENTFD_MAX)；[`CONFIG_ZVFS_EVENTFD_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_EVENTFD_MAX)；[`CONFIG_ZVFS_EVENTFD_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_EVENTFD_MAX)）
- [CONFIG_NET_L2_PTP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP)已弃用，替换为更准确描述时间戳功能的[CONFIG_NET_L2_PTP_TIMESTAMPING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。明确启用旧选项的应用或开发板配置应更新。（[`CONFIG_NET_L2_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP)；[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)）
- WPA认证请求方的默认网络选择准则从吞吐量改为基于信噪比（SNR）的可靠性，[CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL)默认值由_THROUGHPUT改为_RELIABILITY。以前认为SNR高于25 dBm就足够，选择接入点时基本不再考虑；现在始终考虑SNR，以改善嵌入式Wi-Fi稳定性。启用[CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT)可恢复旧行为。译注：原文将SNR阈值单位写为dBm，此处保留，不自行改写数值或单位。（[`CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_RELIABILITY)；[`CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_NW_SEL_THROUGHPUT)）
- 链路本地组播名称解析（LLMNR）已弃用，[CONFIG_LLMNR_RESOLVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLMNR_RESOLVER)及[CONFIG_LLMNR_RESPONDER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLMNR_RESPONDER)将在未来版本移除，最早4.7。官方说明微软正在淘汰RFC 4795定义的LLMNR，现代Windows默认禁用。依赖本地名称解析的应用应迁移到组播DNS（mDNS），使用[CONFIG_MDNS_RESOLVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESOLVER)或[CONFIG_MDNS_RESPONDER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER)。
- 以下MQTT-SN传输函数现在接受[mqtt_sn_transport](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__transport.html)，替代[mqtt_sn_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__client.html)：


  - [`mqtt_sn_transport.recvfrom`](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__transport.html#a1a94f8c7facf9997d1bff237ef2f2503)
  - [`mqtt_sn_transport.poll`](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__transport.html#af6f8c4904857664d14a578a9ead178e4)
  - [`mqtt_sn_transport.sendto`](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__sn__transport.html#a700e8b1f1d541b90da76f050d492fb7a)
- [net_if_down()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2187650062d6139b9f4b81745a206803)不再清除接口组播地址。仍发送离开消息，但地址保留在接口组播列表中，接口重新启用时自动重新加入，使应用关闭再启用接口时不丢失组播地址。（[GitHub #115307](https://github.com/zephyrproject-rtos/zephyr/issues/115307)）
- DHCPv4客户端现在在放弃租约前触发NET_EVENT_IPV4_DHCP_STOP，旧行为是最后触发。若应用停止客户端并在此处理程序中检查接口，现在仍能看到租用地址及租约DNS服务器；处理程序返回后才删除，最后删除地址。应将此类工作移到NET_EVENT_IPV4_ADDR_DEL处理程序，该事件现在是拆除流程的最后事件。

<a id="id1"></a>

### [以太网（Ethernet）](#id62)


- [CONFIG_NET_DEFAULT_IF_ETHERNET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DEFAULT_IF_ETHERNET)现在选择第一个以太网接口，而非以太网及Wi-Fi中的第一个。
- [CONFIG_ETH_QEMU_EXTRA_ARGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_QEMU_EXTRA_ARGS)及[CONFIG_NET_QEMU_USER_EXTRA_ARGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_USER_EXTRA_ARGS)不再用于指定QEMU以太网MAC地址，应改用[CONFIG_NET_QEMU_DEVICE_EXTRA_ARGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_DEVICE_EXTRA_ARGS)。原因是QEMU参数由-nic改为-netdev及-device。（[GitHub #107326](https://github.com/zephyrproject-rtos/zephyr/issues/107326)）
- 提供接收时间戳的以太网驱动，在将有效时间戳写入接收包后，现在必须调用net_pkt_set_rx_timestamping()。AF_PACKET套接字仅通过net_pkt_is_rx_timestamping()判断SO_TIMESTAMPING控制数据是否有效。只填充pkt->timestamp的树外驱动必须更新，否则时间戳无法传给套接字应用。（[GitHub #110582](https://github.com/zephyrproject-rtos/zephyr/issues/110582)）

<a id="modem"></a>

### [调制解调器（Modem）](#id63)


- 蜂窝调制解调器聊天（Chat）的分隔符及过滤器，现在在[modem_cellular_vendor_config](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__vendor__config.html)中指定，而非[modem_cellular_data](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__data.html)。
- 蜂窝调制解调器实例的PPP指针现在自动填入modem_cellular_config，应删除对[modem_cellular_data](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__data.html)的赋值。
- 聊天脚本回调参数类型已更新，在user_data之前新增[modem_chat_script_completion_info](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__chat__script__completion__info.html)指针。

<a id="ptp"></a>

### [精确时间协议（PTP）](#id64)


- PTP UDP协议选项已改名，以统一大小写：


  - CONFIG_PTP_UDP_IPv4_PROTOCOL改为[CONFIG_PTP_UDP_IPV4_PROTOCOL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV4_PROTOCOL)。
  - CONFIG_PTP_UDP_IPv6_PROTOCOL改为[CONFIG_PTP_UDP_IPV6_PROTOCOL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_UDP_IPV6_PROTOCOL)。

<a id="gptp"></a>

### [广义精确时间协议（gPTP）](#id65)


- ethernet_context中的int port改为uint16_t gptp_port，明确该字段仅供gPTP栈保存端口号。
- 依据IEEE 1588标准，gptp_default_ds中的nb_ports改用uint16_t。
- net_eth_get_ptp_port及net_eth_set_ptp_port已移除，可改用[gptp_get_port_number()](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaf4366741c39144e244d7555582b3b62c)及[gptp_set_port_number()](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga4af3bf8e0ef4e3833260b6365b2b1e2f)。
- [CONFIG_NET_GPTP_CLOCK_ACCURACY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_CLOCK_ACCURACY)_*已移除，用户须在CONFIG_NET_GPTP_CLOCK_ACCURACY中配置正确的gPTP时钟精度值。

<a id="id2"></a>

## [调制解调器（Modem）](#id66)

<a id="simcom-sim7080"></a>

### [芯讯通SIM7080（SIMCOM SIM7080）](#id67)


- CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS拆为[CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_M1](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_M1)及[CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_NB1](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS_NB1)，因为NB-IoT及CAT-M可用频段略有差异。新配置为所选频段的十六进制位图，默认选择8、20及28频段。

  设置CONFIG_MODEM_SIMCOM_SIM7080_LTE_BANDS的应用必须更新配置。

<a id="lorawan"></a>

## [LoRa广域网（LoRaWAN）](#id68)


- 原生LoRaWAN后端[CONFIG_LORA_MODULE_BACKEND_NATIVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_MODULE_BACKEND_NATIVE)，现在要求先调用[lorawan_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga640d93930e09327ee87563597f919725)，再使用以下运行时配置API：


  - 启动前调用[lorawan_set_datarate()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaaa70ba5aa545b59233bc906948a4030d)或[lorawan_set_conf_msg_tries()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga14f9cb6a11c585f9ac4e9986735a82c3)，返回-EPERM。
  - 启动前调用返回void的[lorawan_enable_adr()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga432929bd5911e04e57ef178b65e1beaa)，会记录警告并忽略调用。

  这些API此前可在[lorawan_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga640d93930e09327ee87563597f919725)前暂存的配置值，现在不再保留。初始化期间调用它们的应用必须将调用移到start之后；仍可在[lorawan_join()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5b2c7543c45801c9d0d7f46546771f17)成功之前或之后调用。

  [lorawan_set_channels_mask()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga243c3200693ae9c81dea238068afc7dd)不受影响，仍可在[lorawan_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga640d93930e09327ee87563597f919725)后的任意时刻调用，因为通道掩码也影响Join-Request自身的通道选择。

  这些顺序要求不适用于LoRaMac-node后端[CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)。

<a id="libraries"></a>

## [库（Libraries）](#id69)

<a id="ring-buffer"></a>

### [环形缓冲区（Ring Buffer）](#id70)

环形缓冲区API已重构，以减小[ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)并提高内部记账效率。零拷贝（Zero-copy）的认领／完成API ring_buf_put_claim()/ring_buf_put_finish()及对应get函数，替换为不累计认领状态的[ring_buf_put_ptr()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga7877a84b56da9077422dd732e25654d9)及[ring_buf_get_ptr()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#gad3990b5a2ae63166b76c6d1db179a215)。

旧claim/finish API仍可用，但仅在启用[CONFIG_RING_BUFFER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RING_BUFFER)时提供。新代码应直接使用_ptr API。

启用[CONFIG_RING_BUFFER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RING_BUFFER)会选择旧环形缓冲区头文件，也恢复默认头文件中已删除的其他弃用符号：全部条目（Item）API，包括ring_buf_item_init()、ring_buf_item_put()、ring_buf_item_get()、ring_buf_item_space_get()、RING_BUF_ITEM_DECLARE*、RING_BUF_ITEM_SIZEOF及ring_buf_internal_reset()。仍使用这些符号的树外代码会编译失败且无其他提示；迁移到[sys_ringq](../ringq_reference/P002_环形队列结构.md)及_ptr API期间，可启用该选项恢复旧符号。

默认精简构建中，[ring_buf_get()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga615c20bd465b1a9c2b34424b608da851)不再接受NULL目标以丢弃数据；仅启用[CONFIG_RING_BUFFER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RING_BUFFER)时仍容许NULL。若要丢弃数据而不提供目标缓冲区，直接通过[ring_buf_consume()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga8afdb493f570b9a70af35012b427f1bd)前移读索引，例如ring_buf_consume(rb, MIN(count, ring_buf_size_get(rb)))。

试写后取消、提交前回填已写头部等高级场景，现在依赖[ring_buf_put_ptr()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga7877a84b56da9077422dd732e25654d9)及[ring_buf_get_ptr()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#gad3990b5a2ae63166b76c6d1db179a215)末尾的offset参数。它表示调用者已在当前写或读索引之后暂时预留的字节数，回绕由内部处理。通过递增offset安排连续区域，实际环形缓冲区保持不变；最后只通过[ring_buf_commit()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga50e1cb774f39d3cda234b55a3102cf2f)或[ring_buf_consume()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga8afdb493f570b9a70af35012b427f1bd)推进。任一步失败时直接返回而不提交，即等价于旧ring_buf_put_finish(rb, 0)取消操作。

例如，以下claim/finish代码：

```text
int write_pkg(struct ring_buf *rb, const uint8_t *payload, size_t payload_size)
{
        struct hdr *h;
        uint8_t *ptr;
        uint32_t claim_size;

        claim_size = ring_buf_put_claim(rb, (uint8_t **)&h, sizeof(*h));
        if (claim_size < sizeof(*h)) {
                ring_buf_put_finish(rb, 0);
                return -ENOMEM;
        }

        claim_size = ring_buf_put_claim(rb, &ptr, payload_size);
        if (claim_size == 0) {
                ring_buf_put_finish(rb, 0);
                return -ENOMEM;
        }
        h->len = claim_size;
        /* ... write payload through ptr ... */
        ring_buf_put_finish(rb, sizeof(*h) + h->len);
        return h->len;
}
```

大致可转换为：

```text
int write_pkg(struct ring_buf *rb, const uint8_t *payload, size_t payload_size)
{
        struct hdr *h;
        uint8_t *ptr;
        uint32_t claim_size;

        /* Reserve the header region without committing it. */
        if (ring_buf_put_ptr(rb, (uint8_t **)&h, 0) < sizeof(*h)) {
                return -ENOMEM;
        }

        /* Expose the region right after the header via a trailing offset. */
        claim_size = ring_buf_put_ptr(rb, &ptr, sizeof(*h));
        if (claim_size == 0) {
                /* Nothing was committed to rb, so the write is cancelled. */
                return -ENOMEM;
        }
        h->len = MIN(claim_size, payload_size);
        /* ... write payload through ptr ... */

        /* Publish header and payload atomically to the real buffer. */
        ring_buf_commit(rb, sizeof(*h) + h->len);
        return h->len;
}
```

<a id="other-subsystems"></a>

## [其他子系统（Other Subsystems）](#id71)


- 按需分页（Demand Paging）从subsys/demand_paging移到内存管理下的subsys/mem_mgmt/demand_paging。自定义后备存储（Backing Store）及换出算法代码也需要移到那里。
- <zephyr/sys/ring_buffer.h>中的环形缓冲区Item API已弃用，改用<zephyr/sys/ringq.h>中新的固定大小队列API。

  存储固定大小条目的代码应迁移到[sys_ringq](../ringq_reference/P002_环形队列结构.md)，见sys_ringq数据结构。仅按字节使用Item API的代码，应在同一[ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)上改用字节模式函数[ring_buf_put()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#gafd112c33f0ff2520f5fa1421ecf8da5c)及[ring_buf_get()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga615c20bd465b1a9c2b34424b608da851)。（[GitHub #98255](https://github.com/zephyrproject-rtos/zephyr/issues/98255)）（[sys_ringq数据结构（Data Structure）](https://docs.zephyrproject.org/latest/kernel/data_structures/ringq.html#fixed-size-ringq-api)）
- ZTEST_BENCHMARK_SETUP_TEARDOWN()及ZTEST_BENCHMARK_TIMED_SETUP_TEARDOWN()已移除。其准备／清理（Setup/Teardown）签名合并到[ZTEST_BENCHMARK()](../hardware/P501_ZTest基准测试接口.md#gaf5f904c376be7111cfaf1e21a5a99bd4)及[ZTEST_BENCHMARK_TIMED()](../hardware/P501_ZTest基准测试接口.md#ga0f1d1daa73aa6db26ac91f9f17a19646)，现在每处调用都要求明确传setup_fn及teardown_fn。基准测试确实不需要它们时传NULL。

  按以下方式更新现有调用：

  ```text
  /* Before */
  ZTEST_BENCHMARK(suite, my_bench, 100) { /* ... */ }
  ZTEST_BENCHMARK_TIMED(suite, my_bench, 1000) { /* ... */ }
  ZTEST_BENCHMARK_SETUP_TEARDOWN(suite, my_bench, 100, setup, teardown) { /* ... */ }
  ZTEST_BENCHMARK_TIMED_SETUP_TEARDOWN(suite, my_bench, 1000, setup, teardown) { /* ... */ }

  /* After */
  ZTEST_BENCHMARK(suite, my_bench, 100, NULL, NULL) { /* ... */ }
  ZTEST_BENCHMARK_TIMED(suite, my_bench, 1000, NULL, NULL) { /* ... */ }
  ZTEST_BENCHMARK(suite, my_bench, 100, setup, teardown) { /* ... */ }
  ZTEST_BENCHMARK_TIMED(suite, my_bench, 1000, setup, teardown) { /* ... */ }
  ```
- 自Zephyr 4.0起弃用的[CONFIG_ZTEST_SHUFFLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SHUFFLE)_SUITE_REPEAT_COUNT及CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT已移除。单独启用CONFIG_ZTEST_SHUFFLE时，每次执行中套件及测试仅以打乱顺序各运行一次。若需重复，应启用[CONFIG_ZTEST_REPEAT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_REPEAT)，并设置[CONFIG_ZTEST_SUITE_REPEAT_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SUITE_REPEAT_COUNT)及[CONFIG_ZTEST_TEST_REPEAT_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_TEST_REPEAT_COUNT)。
- CPU负载指标模块并入统一CPU负载模块。[CONFIG_CPU_LOAD_METRIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_METRIC)已弃用，改为启用[CONFIG_CPU_LOAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD)及[CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS)后端。<zephyr/sys/cpu_load_metric.h>现在只包含<zephyr/sys/cpu_load.h>，[cpu_load_metric_get()](../observability/P049_CPU负载接口.md#ga3333539cf7d8a6916cbbec9cd1f5bf59)成为[cpu_load_get_cpu()](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)的弃用包装。注意：新函数返回千分比0～1000，而非百分比；可用[CPU_LOAD_PERMILLE_TO_PERCENT](../observability/P049_CPU负载接口.md#ga21c1e9efe2f4ba8f40a3e9dd1f32b52e)转换。（[CPU负载（CPU Load）](../observability/P007_CPU负载.md#cpu-load)；[`cpu_load_get_cpu()`](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)）
- 内部定义__ASSERT_ON已移除。树外代码应直接调用__ASSERT()或__ASSERT_NO_MSG()，因为禁用断言时这些宏本身就不会生成代码。仅供断言使用的值应按需标为__maybe_unused或使用ARG_UNUSED()。
- 若干旧断言选项已弃用，改用按模块设置的ZASSERT级别CONFIG_ASSERT_MODULE_<module>_LEVEL，默认通过DEFAULT模块确定：


  - [CONFIG_ASSERT_VERBOSE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_VERBOSE)对应[CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_VERBOSE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_VERBOSE)。
  - [CONFIG_ASSERT_NO_COND_INFO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_NO_COND_INFO)、[CONFIG_ASSERT_NO_MSG_INFO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_NO_MSG_INFO)及[CONFIG_ASSERT_NO_FILE_INFO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_NO_FILE_INFO)对应[CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_TERSE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_TERSE)。
  - CONFIG_FORCE_NO_ASSERT替换为将[CONFIG_ASSERT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT)设为n。
  - CONFIG_ASSERT_LEVEL替换为DEFAULT模块级别；原级别0对应[CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_OFF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_MODULE_DEFAULT_LEVEL_OFF)。
- 断言钩子assert_post_action及assert_print已移除，改用zassert_post_action及zassert_vprint实现等效功能。注意：zassert_post_action是终止函数，不支持返回调用者。若应用需要返回，可启用[CONFIG_ASSERT_TEST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_TEST)，将该钩子声明为非终止函数，允许运行后继续执行。
- [CONFIG_ASSERT_NO_FILE_INFO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_NO_FILE_INFO)不会改变zassert_post_action签名，不同于旧assert_post_action的行为。
- 替代assert_print的zassert_vprint现在接受va_list参数，而非可变数量的参数。实现该钩子的树外代码必须更新。

<a id="fido2"></a>

### [FIDO2身份认证](#id72)


- FIDO2传输回调API已变化。[fido2_transport_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#af8365317181d301d3f44fd3eb9416475)现在返回int，表示FIDO2核心是否接受收到的消息；[fido2_transport_cancel_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a081a49ee568a0939254bc640b509c3f8)现在接受收到取消命令的[fido2_transport](https://docs.zephyrproject.org/latest/doxygen/html/structfido2__transport.html)实例。树外传输实现必须处理接收回调返回值，并在调用取消回调时传入传输实例。（[GitHub #116552](https://github.com/zephyrproject-rtos/zephyr/issues/116552)）
- 通过[CONFIG_FIDO2_UP_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_UP_CUSTOM)选择、由应用提供的用户在场（User Presence）后端，现在必须实现[fido2_up_reset()](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7fb0da6d327ef0be220d32558ea6be2)，为每个新请求清理状态。（[GitHub #116552](https://github.com/zephyrproject-rtos/zephyr/issues/116552)）

<a id="hawkbit"></a>

### [设备更新服务（hawkBit）](#id73)


- 自Zephyr 4.0弃用的旧头文件<zephyr/mgmt/hawkbit.h>已移除。改为包含<zephyr/mgmt/hawkbit/hawkbit.h>、<zephyr/mgmt/hawkbit/config.h>及<zephyr/mgmt/hawkbit/autohandler.h>。

<a id="logging"></a>

### [日志（Logging）](#id74)


- UART字典日志解析脚本scripts/logging/dictionary/log_parser_uart.py已移除，改用[scripts/logging/dictionary/live_log_parser.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/logging/dictionary/live_log_parser.py)，在serial子命令后指定端口及波特率。

<a id="mcuboot"></a>

### [MCU启动加载器（MCUboot）](#id75)


- CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_WITHOUT_SCRATCH已移除，改用[CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE)。
- Sysbuild不再为Espressif SoC强制选择MCUboot仅覆盖模式及无签名镜像，改用通用默认值：偏移交换保留旧镜像以便回退，并使用MCUboot开发密钥进行RSA-2048签名。使用自有密钥的项目必须设置[SB_CONFIG_BOOT_SIGNATURE_KEY_FILE](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOOT_SIGNATURE_KEY_FILE)；依赖旧行为的项目可明确选择[SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY)及[SB_CONFIG_BOOT_SIGNATURE_TYPE_NONE](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOOT_SIGNATURE_TYPE_NONE)。新默认值下构建的启动加载器会拒绝无签名镜像，因此设备切换到新默认值时，必须一起重新烧录启动加载器及应用。
- Espressif共享分区表不再定义scratch_partition，因此使用这些表的开发板不再提供[SB_CONFIG_MCUBOOT_MODE_SWAP_SCRATCH](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_MODE_SWAP_SCRATCH)。其他分区偏移不变；需要暂存分区的项目可通过开发板覆盖文件重新添加。

<a id="mcumgr"></a>

### [微控制器管理（MCUmgr）](#id76)


- CONFIG_MCUMGR_GRP_OS_INFO_HARDWARE_INFO_SHORT_HARDWARE_PLATFORM已移除。[OS/Application Info](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_groups/smp_group_0.html#mcumgr-os-application-info)现在始终以开发板目标作为硬件平台，无法再采用4.3之前的开发板名称加修订版本输出。
- [CONFIG_MCUMGR_TRANSPORT_UART_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UART_MTU)及[CONFIG_MCUMGR_TRANSPORT_SHELL_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SHELL_MTU)已弃用。它们只设置已弃用get_mtu回调的返回值，SMP层并不使用：串行帧限制为127字节，最大SMP包大小由[CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE)决定。应从配置中删除它们；设置非默认值时产生弃用警告。
- [smp_transport_api_t](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport__api__t.html)的get_mtu成员及[smp_transport_get_mtu_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga2085e89b99428a61596d90e084d7c5e2)类型已弃用，因为SMP层从不调用。树外代码应停止设置或调用get_mtu。传输实现仍负责在output函数中拆分发送包，见[smp_transport_out_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga4da3579b031ba6a90448ad9248f52155)。
- 镜像管理客户端[CONFIG_MCUMGR_GRP_IMG_CLIENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_IMG_CLIENT)除了SHA-256，现在还支持SHA-512镜像摘要：


  - [img_mgmt_client_state_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#gab98286b3baac7330c7f42539d38663cd)新增hash_len参数。hash非NULL时传入其字节长度，例如SHA-256为32；否则传0。
  - [mcumgr_image_data](https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__data.html)现在保存可变长度摘要：hash缓冲区为[IMG_MGMT_CLIENT_HASH_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt__client.html#ga96a605c7a4f46851eced1d538f3134b6)，即64字节，新增hash_len保存实际长度。读取hash的代码必须使用hash_len，不能再假定[IMG_MGMT_DATA_SHA_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga70168b0d707c15658fd09b02c361a64c)。
- [CONFIG_MCUMGR_TRANSPORT_UDP_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UDP_MTU)不得超过[CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE)，超过时配置阶段失败。缓冲区小于1500字节时，MTU默认取缓冲区大小，不再默认1500。
- [smp_client_single_response()](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7818782c9eefcc78911c589078ece26)新增首参数，表示接收响应的SMP传输；res_hdr必须采用主机字节序。响应现在只会完成经同一传输发送、组及命令ID都匹配的待处理命令。若服务器未回显组及命令ID，响应被忽略，命令持续重试直至超时。

<a id="network-buffers"></a>

### [网络缓冲区（Network Buffers）](#id77)


- [net_buf_max_len()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga65924b8234c91dfc09069ba06242a6b7)及[net_buf_simple_max_len()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7476ec7222d074e7dc9783e7ed9cd800)已弃用。它们返回data指针之后的缓冲区容量，既不是总存储大小，也不是剩余可添加空间。应使用[net_buf_tailroom()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaecbc6adf16469e3366c88445ea7a553a)或[net_buf_simple_tailroom()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga73e2c42fc23e857a46553084b747c996)查询尾部可追加量，用[net_buf_headroom()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac9a09897f44e708f920064826aa2f703)或[net_buf_simple_headroom()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadc6ae86245c2a2607c671a524227b026)查询头部可压入量。若代码将旧值用作从data开始的临时工作区大小，可通过buf->len + net_buf_tailroom(buf)计算。

<a id="posix"></a>

### [可移植操作系统接口（POSIX）](#id78)


- CONFIG_POSIX_READER_WRITER_LOCKS已移除，改用[CONFIG_POSIX_RW_LOCKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RW_LOCKS)。

<a id="power-management"></a>

### [电源管理（Power Management）](#id79)


- 新增实验选项[CONFIG_PM_EARLY_SYSTEM_TIMER_RESUME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_EARLY_SYSTEM_TIMER_RESUME)，默认关闭，启用[GitHub #118977](https://github.com/zephyrproject-rtos/zephyr/issues/118977)引入的恢复顺序：SoC后处理、系统定时器退出空闲、设备恢复、PM退出通知。必须验证平台依赖及超时回调后才能启用。SoC后处理在设备恢复前执行；定时器退出空闲可能在设备仍挂起时调用[k_timer](https://docs.zephyrproject.org/latest/doxygen/html/structk__timer.html)到期函数。不启用该选项时，若低功耗状态停止了定时器，设备恢复回调中的基于定时器的[k_busy_wait()](../thread_core_reference/P001_线程公共接口.md#ga550b642e071480323e589866abb99c22)仍不受支持。

  参见[GitHub #120960](https://github.com/zephyrproject-rtos/zephyr/issues/120960)。

<a id="random"></a>

### [随机数（Random）](#id80)


- CONFIG_CTR_DRBG_CSPRNG_GENERATOR已移除，改用[CONFIG_PSA_CSPRNG_GENERATOR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CSPRNG_GENERATOR)。
- CONFIG_CS_CTR_DRBG_PERSONALIZATION已移除，因为它不产生任何效果。

<a id="rtio"></a>

### [实时输入输出（RTIO）](#id81)


- 取消句柄由struct rtio_sqe *改为[rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47)，包含池索引及代际编号（Generation）。与裸指针不同，句柄可检查范围及代际。取消一个已完成且池槽已复用的提交，现在安全地不执行任何操作，而非产生未定义行为。
- [rtio_sqe_cancel()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga9e04f43dc23a142ce3ec18e8b8552d69)除句柄外，现在还接受所属RTIO上下文，以便依据该上下文的提交队列条目（SQE）池解析句柄：

  ```text
  /* Before */
  int rtio_sqe_cancel(struct rtio_sqe *sqe);
  ```

  ```text
  /* After */
  int rtio_sqe_cancel(struct rtio *r, rtio_sqe_handle_t handle);
  ```
- [rtio_sqe_copy_in_get_handles()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga77506a320d6e31c6aeb2951312890295)、[sensor_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga58bb95758fc4bd2927c93671727e6080)及[adc_stream()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga92bc0474999b93f4fdfbcfec65199d79)的句柄输出参数从struct rtio_sqe **改为[rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47) *。保存句柄的变量，包括sensing_sensor.stream_sqe，必须改为rtio_sqe_handle_t。原来以NULL判断无提交的位置，应改用[RTIO_SQE_HANDLE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#gabc777d715f939d6e3585b00ea1410ace)。
- [rtio_sqe_copy_in_get_handles()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga77506a320d6e31c6aeb2951312890295)现在为每个复制的SQE输出一个句柄，不再只输出第一个，因此输出参数为sqe_count长度的句柄数组。仅复制一个SQE的调用不受影响；复制链或事务且原来只传单变量地址的调用，必须改传足够大的数组。
- [rtio_sqe_cancel()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga9e04f43dc23a142ce3ec18e8b8552d69)只标记句柄指定的提交，不影响链或事务其他部分。因此取消整个链或事务时，必须取消其返回的每个句柄。取消仍是尽力而为：在成员派发前标记可以阻止执行，因为执行器交给iodev前会逐个检查状态；但若其前驱在标记之前或过程中完成，该成员可能已开始运行，此时会执行到完成。（[`rtio_sqe_copy_in_get_handles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga77506a320d6e31c6aeb2951312890295)）
- RTIO_SQE_CANCELED标志已弃用。取消状态从sqe.flags移到所属[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)的原子状态字，以原子方式设置及检查。读取旧标志的代码，通常为处理流式提交的驱动，必须改用[rtio_iodev_sqe_is_canceled()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga8c497b13ca1b4f3c1988b1091244e7bc)。读取旧标志仍能编译并警告，但不再反映[rtio_sqe_cancel()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga9e04f43dc23a142ce3ec18e8b8552d69)在运行时提出的取消请求。旧标志存在期间，提交前设置它仍会取消提交，但新代码应通过句柄取消。
- 提交后由子系统或驱动修改的运行时状态，从[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)移到所属[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)，包括内存池缓冲区绑定、await信号状态及delay到期时间。内存池绑定以前会写回sqe->rx.buf及buf_len；iodev后续完成步骤不能再重新读取sqe->rx.buf取得绑定缓冲区，应再次调用[rtio_sqe_rx_buf()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga6c2bde1de4e98b7db4cd2043da0cb5f6)，它会返回已绑定的缓冲区。内存池提交的该字段运行时保持NULL，编译时不会提示；调用者提供的RX缓冲区不受影响。

  可用Coccinelle语义补丁重写两组字段移动：sqe.await.{ok,callback,userdata}变为rt.await.{ok,callback,userdata}，sqe.delay.expiry变为rt.delay_expiry：

  ```text
  spatch --sp-file scripts/coccinelle/rtio_sqe_runtime_state.cocci \
         --macro-file scripts/coccinelle/macros.h --dir . --in-place
  ```

  内存池缓冲区无法机械替换，因为将sqe.rx读取改为[rtio_sqe_rx_buf()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga6c2bde1de4e98b7db4cd2043da0cb5f6)调用，需要知道驱动所需长度，并提供分配失败路径。MODE=report会在自行绑定内存池缓冲区的文件中报告这些读取。通过裸struct rtio_sqe *访问已移动的await或delay成员将无法编译，必须通过[CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)取得包装对象，或使用操作收到的[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。
- 多数应用可用第二份Coccinelle语义补丁自动迁移：更新句柄变量类型，将rtio_sqe_cancel(handle)改为rtio_sqe_cancel(ctx, handle)，ctx从生成句柄的rtio_sqe_copy_in_get_handles、sensor_stream或adc_stream调用绑定，并将RTIO_SQE_CANCELED读取改为[rtio_iodev_sqe_is_canceled()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga8c497b13ca1b4f3c1988b1091244e7bc)：

  ```text
  spatch --sp-file scripts/coccinelle/rtio_sqe_handle.cocci \
         --macro-file scripts/coccinelle/macros.h --dir . --in-place
  ```

  也可通过包装脚本运行MODE=patch scripts/coccicheck。保存在结构体字段中、在不同函数产生及取消的句柄，例如传感子系统，以及保存在数组中的句柄，超出补丁可绑定范围，必须人工修改。MODE=report报告剩余rtio_sqe_cancel()调用及RTIO_SQE_CANCELED用法，包括无法机械替换的写操作。

<a id="secure-storage"></a>

### [安全存储（Secure Storage）](#id82)


- 以下文件已改名：


  - zephyr/secure_storage/its/store/settings_get.h改为zephyr/secure_storage/its/store/settings.h。
  - zephyr/secure_storage/its/transform/aead_get.h改为zephyr/secure_storage/its/transform/aead.h。
- ZMS后端分区的chosen名称从secure_storage_its_partition改为zephyr,secure-storage-its-partition。（[GitHub #118501](https://github.com/zephyrproject-rtos/zephyr/issues/118501)）
- psa_its_get*()现在可能返回PSA_ERROR_INVALID_SIGNATURE及PSA_ERROR_DATA_CORRUPT，原来统一报告为PSA_ERROR_GENERIC_ERROR。（[GitHub #118718](https://github.com/zephyrproject-rtos/zephyr/issues/118718)）
- data_size为0时调用psa_its_get()，现在也执行正常检索流程，因此可能返回PSA_ERROR_DOES_NOT_EXIST等错误，不再总是PSA_SUCCESS。（[GitHub #118718](https://github.com/zephyrproject-rtos/zephyr/issues/118718)）

<a id="shell"></a>

### [命令行（Shell）](#id83)


- 自Zephyr v4.1.0弃用的Shell命令kernel log_level <module> <severity>已移除。改用log enable <severity> <module>：参数顺序相反，严重程度使用none、err、wrn、inf或dbg名称，而非数字。

<a id="stream-flash"></a>

### [流式Flash（Stream Flash）](#id84)


- stream_flash_erase_page()已移除，改用[flash_area_erase()](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gacc5cbff19d23773115f3334f862814d2)或[flash_erase()](../flash_reference/P001_Flash公共接口.md#ga05f9c8b0c1ff7273f71797e7ff799c95)；Stream Flash没有等效API。

<a id="tools"></a>

## [工具（Tools）](#id85)


- 调用运行器的west命令，包括flash、debug、debugserver、attach、rtt、reset、robot及simulate，已移除--skip-rebuild，改用--no-rebuild。
- pyocd运行器不再读取PYOCD_DAPARG环境变量，改为向west flash或west debug传--daparg。
- openocd运行器现在通过标准-i/--dev-id按序列号选择调试适配器，与其他运行器一致。旧--serial已弃用但保留为别名，映射到同一机制，值仍以_ZEPHYR_BOARD_SERIAL传给OpenOCD配置。脚本应更新为west flash -i <serial>。

<a id="modules"></a>

## [模块（Modules）](#id86)


- [CHRE](https://github.com/zephyrproject-rtos/chre)框架不再是Zephyr清单中的可选模块，示例也移出源码树。现在作为外部模块提供，要继续使用，需将其加入应用清单。（[外部模块（External Module）](../external_modules/P014_上下文中心运行时CHRE.md#external-module-chre)）
- [CANopenNode](https://github.com/CANopenNode/CANopenNode)协议栈支持移到外部模块。（[外部模块（External Module）](../external_modules/P002_CANopenNode协议栈.md#external-module-canopennode)）

<a id="lvgl"></a>

### [轻量图形库（LVGL）](#id87)


- LVGL从v9.5升级到v9.6，其自身变化见LVGL迁移指南。（[LVGL迁移指南（Migration Guide）](https://lvgl.io/docs/open/changelog/migration-v9-6)）
- LVGL v9.6弃用LV_COLOR_DEPTH选择项，改用LV_COLOR_FORMAT_DEFAULT。CONFIG_LV_COLOR_DEPTH_*不再在Zephyr中选择颜色格式，应替换为CONFIG_LV_COLOR_FORMAT_*，例如CONFIG_LV_COLOR_DEPTH_16=y改为CONFIG_LV_COLOR_FORMAT_RGB565=y。
- CONFIG_LV_ATTRIBUTE_MEM_ALIGN_SIZE替换为[CONFIG_LV_Z_ATTRIBUTE_MEM_ALIGN_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_ATTRIBUTE_MEM_ALIGN_SIZE)。
- 开发板、扩展板及SoC不再在Kconfig.defconfig设置LVGL选项，因为缺少LVGL模块时这些选项未定义。现在设置Zephyr选项，由其提供LVGL默认值。树外配置必须替换以下选项：


  - LV_COLOR_DEPTH选择项改为LV_Z_COLOR_FORMAT，例如LV_COLOR_DEPTH_16改为LV_Z_COLOR_FORMAT_RGB565。
  - LV_DPI_DEF及LV_DRAW_BUF_ALIGN，分别改为[CONFIG_LV_Z_DPI_DEF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_DPI_DEF)及[CONFIG_LV_Z_DRAW_BUF_ALIGN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_DRAW_BUF_ALIGN)。
  - LV_USE_DRAW_DMA2D改为[CONFIG_LV_Z_DRAW_DMA2D_DEFAULT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_DRAW_DMA2D_DEFAULT)。
  - LV_USE_DRAW_DMA2D_INTERRUPT及LV_DRAW_DMA2D_HAL_INCLUDE，分别改为[CONFIG_LV_Z_DRAW_DMA2D_INTERRUPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_DRAW_DMA2D_INTERRUPT)及[CONFIG_LV_Z_DRAW_DMA2D_HAL_INCLUDE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_DRAW_DMA2D_HAL_INCLUDE)。
  - LV_NEMA_USE_CACHE及LV_NEMA_CACHE_HAL_INCLUDE，分别改为[CONFIG_LV_Z_NEMA_USE_CACHE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_NEMA_USE_CACHE)及[CONFIG_LV_Z_NEMA_CACHE_HAL_INCLUDE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_NEMA_CACHE_HAL_INCLUDE)。
  - LV_USE_NEMA_LIB选择项改为某个LV_Z_NEMA_LIB_*选项，例如[CONFIG_LV_Z_NEMA_LIB_M7](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_NEMA_LIB_M7)。

  LV_USE_NEMA_HAL无需替代，因为Zephyr使用的自定义HAL就是LVGL默认值。应用在.conf中设置LVGL选项的用法不受影响。
- Zephyr LVGL适配层日志级别不再跟随LVGL本身，现在使用标准CONFIG_LV_Z_LOG_LEVEL选择项，如CONFIG_LV_Z_LOG_LEVEL_DBG，默认[CONFIG_LOG_DEFAULT_LEVEL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_DEFAULT_LEVEL)。LVGL自身日志仍由CONFIG_LV_USE_LOG及CONFIG_LV_LOG_LEVEL_*配置。转发到Zephyr日志子系统的LVGL消息同时受两级过滤，因此查看LVGL跟踪消息需设置CONFIG_LV_Z_LOG_LEVEL_DBG=y。
- CONFIG_LV_USE_SYSMON不再隐含启用[CONFIG_CPU_LOAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD)。要让系统监视器报告CPU使用率，应启用[CONFIG_CPU_LOAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD)。
- zephyr,lvgl-pointer-input绑定的swap-xy、invert-x及invert-y已标为弃用。应在底层触摸输入控制器节点添加对应触摸屏属性swapped-x-y、inverted-x及inverted-y；这些坐标变换现在统一在该处定义。
- [CONFIG_LV_Z_FULL_REFRESH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_FULL_REFRESH)现在属于LV_Z_RENDERING_MODE选择项，与默认[CONFIG_LV_Z_PARTIAL_REFRESH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_PARTIAL_REFRESH)及[CONFIG_LV_Z_DIRECT_RENDERING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_DIRECT_RENDERING)并列。在.conf中设置=y仍有效，但=n会被静默忽略，因为无法这样取消选择项成员。原来通过=n退出默认全刷新模式的树外开发板或扩展板，必须在Kconfig.defconfig或.defconfig中覆盖选择项默认值：

  ```text
  choice LV_Z_RENDERING_MODE
    default LV_Z_PARTIAL_REFRESH
  endchoice
  ```

<a id="hal-nxp"></a>

### [`hal_nxp`](#id88)


- CONFIG_LV_USE_GPU_NXP_PXP已移除。它只启用NXP PXP HAL组件，而[CONFIG_MCUX_PXP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_PXP)已经提供该功能；当[nxp,pxp](../nxp_realtek_renesas_dma_binding_reference/P005_nxp_pxp.md#std-dtcompatible-nxp-pxp)节点启用且设置[CONFIG_DISPLAY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISPLAY)时，后者默认y。不使用显示子系统而使用PXP组件的应用必须明确启用[CONFIG_MCUX_PXP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_PXP)。
- S32K344的引脚复用头文件从S32K344-172MQFP-pinctrl.h改名为S32K344_K324_K314_172HDQFP-pinctrl.h。树外开发板必须相应更新包含指令：

  ```text
  #include <nxp/s32/S32K344_K324_K314_172HDQFP-pinctrl.h>
  ```

<a id="mbed-tls"></a>

### [Mbed TLS密码与TLS库](#id89)


- 以下已弃用Kconfig选项已移除：


  - CONFIG_MBEDTLS_MD改名为[CONFIG_MBEDTLS_MD_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_MD_C)。
  - CONFIG_MBEDTLS_LMS改名为[CONFIG_MBEDTLS_LMS_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_LMS_C)。
  - CONFIG_MBEDTLS_TLS_VERSION_1_2改名为[CONFIG_MBEDTLS_SSL_PROTO_TLS1_2](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)。
  - CONFIG_MBEDTLS_DTLS改名为[CONFIG_MBEDTLS_SSL_PROTO_DTLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_DTLS)。
  - CONFIG_MBEDTLS_TLS_VERSION_1_3改名为[CONFIG_MBEDTLS_SSL_PROTO_TLS1_3](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)。
  - CONFIG_MBEDTLS_TLS_SESSION_TICKETS改名为[CONFIG_MBEDTLS_SSL_SESSION_TICKETS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_SESSION_TICKETS)。
  - CONFIG_MBEDTLS_CTR_DRBG_ENABLED改名为[CONFIG_MBEDTLS_CTR_DRBG_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CTR_DRBG_C)。
  - CONFIG_MBEDTLS_HMAC_DRBG_ENABLED改名为[CONFIG_MBEDTLS_HMAC_DRBG_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_HMAC_DRBG_C)。

  新选项与已移除选项不同，不会自动启用依赖项。
- [CONFIG_MBEDTLS_SSL_EARLY_DATA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_EARLY_DATA)现在必须明确启用，不再由[CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_TLS1_3_KEY_EXCHANGE_MODE_PSK_ENABLED)隐含启用。依赖TLS 1.3预共享密钥早期数据（PSK Early Data，0-RTT）的树外应用或开发板配置，必须明确启用该选项。（[`CONFIG_MBEDTLS_SSL_EARLY_DATA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_EARLY_DATA)）
- [CONFIG_PSA_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)_CLIENT因与[CONFIG_PSA_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)重复而移除。原使用者应改用CONFIG_PSA_CRYPTO。（[GitHub #108960](https://github.com/zephyrproject-rtos/zephyr/issues/108960)）
- CMake接口库mbedTLS改名为mbedtls_iface。为向后兼容，前者暂作为后者别名保留，但将在未来版本移除。
- Mbed TLS更新到4.1.1，发行说明见此链接。（[此处](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-4.1.1)）
- TF-PSA-Crypto更新到1.1.1，发行说明见此链接。（[此处](https://github.com/Mbed-TLS/TF-PSA-Crypto/releases/tag/tf-psa-crypto-1.1.1)）

<a id="trusted-firmware-m-tf-m"></a>

### [可信固件M（Trusted Firmware-M，TF-M）](#id90)


- [CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY)已弃用，改用[CONFIG_TFM_ZEPHYR_4_2_COMPATIBILITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_ZEPHYR_4_2_COMPATIBILITY)，新名称更准确描述需要设置该符号的情形。
- [CONFIG_BUILD_WITH_TFM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)不再启用[CONFIG_MBEDTLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS)及[CONFIG_PSA_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)，构建时必须按需明确启用。（[GitHub #114762](https://github.com/zephyrproject-rtos/zephyr/issues/114762)）
- [CONFIG_TFM_PARTITION_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_PARTITION_CRYPTO)现在依赖[CONFIG_PSA_CRYPTO_PROVIDER_TFM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO_PROVIDER_TFM)，因此要启用TF-M密码分区，必须先启用[CONFIG_PSA_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)。（[GitHub #116318](https://github.com/zephyrproject-rtos/zephyr/issues/116318)）

<a id="snippets"></a>

## [配置片段（Snippets）](#id91)


- xen_dom0改名为xen-dom0。

<a id="architectures"></a>

## [架构（Architectures）](#id92)


- 新增架构原语arch_cpu_irqs_are_enabled()，在不修改状态的情况下返回调用CPU当前的中断使能状态，补充用于检查已保存密钥的arch_irq_unlocked()。树外架构移植必须提供实现。
- CONFIG_XTENSA_MPU_ONLY_SOC_RANGES已移除。SoC或开发板若要覆盖默认MPU区域表，应在对应层覆盖xtensa_mpu_ranges。
- xtensa_soc_mpu_ranges[]及xtensa_soc_mpu_ranges_num已移除。SoC或开发板若启动时需要自定义内存区域，改为覆盖xtensa_mpu_ranges。
- CONFIG_XTENSA_MPU_DEFAULT_MEM_TYPE已移除，因为内存类型现在通过xtensa_mpu_mem_type_ranges[]定义。
- CONFIG_XTENSA_BACKTRACE_[EXCEPTION_DUMP](https://docs.zephyrproject.org/latest/doxygen/html/exception_8h.html#a39da57c6e073d8a2ea07b49b0c51aa3e)_HOOK已移除，因为回溯（Backtrace）现在始终通过EXCEPTION_DUMP输出。
- 使用CONFIG_XTENSA_BACKTRACE的SoC现在应实现xtensa_soc_stack_ptr_is_sane()及xtensa_soc_ptr_executable()。
- ARMv7-M MPU的设备类型区域属性REGION_PPB_ATTR、REGION_IO_ATTR及REGION_EXTMEM_ATTR，现在在所有ARMv7-M内核设置禁止执行（Execute-Never，XN=1）。在设备或强顺序内存执行代码，按ARMv7-M架构定义属于不可预测（UNPREDICTABLE），因此合法用例不受影响。对Cortex-M7，XN还可阻止对这些区域的推测取指（Speculative Instruction Fetch），避免总线挂起或外设读取副作用；仅靠内存类型无法阻止，参见Arm Cortex-M7技术参考手册的推测访问及系统设计注意事项。树外开发板若仍从这类属性映射区域执行，必须自行定义属性。
- 新选项[CONFIG_ARM_MPU_CM7_UNMAPPED_REGION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU_CM7_UNMAPPED_REGION)使Arm MPU驱动将最低优先级区域0设置为覆盖4 GB的强顺序、禁止访问、禁止执行兜底区域，实现Cortex-M7勘误1013783（SDEN-1068427）的规避措施，防止对未映射地址的推测访问。静态MPU表已明确覆盖固件所用全部内存的Cortex-M7开发板或SoC可启用；静态区域随后从区域1开始配置。mimxrt1180_evk及frdm_imxrt1186的cm7目标默认启用，替代原手工UNMAPPED表项，运行时行为相同。
- CONFIG_SSE及CONFIG_SSE_FP_MATH已移除，分别改用[CONFIG_X86_SSE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_SSE)及[CONFIG_X86_SSE_FP_MATH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_SSE_FP_MATH)。
- CONFIG_PLATFORM_SPECIFIC_INIT及z_arm_platform_init()钩子已移除。应启用[CONFIG_SOC_RESET_HOOK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RESET_HOOK)，并将钩子改名为[soc_reset_hook()](https://docs.zephyrproject.org/latest/doxygen/html/hooks_8h.html#ad6e8df1eefd1add03ad8379802bd989e)。新钩子在复位路径中更晚执行，位于栈指针设置之后；从挂起到RAM恢复时跳过。
- RISC-V专用CONFIG_EXTRA_EXCEPTION_INFO已移除，改用[CONFIG_EXCEPTION_DEBUG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXCEPTION_DEBUG)。Arm及SPARC上的选项不变。
- [arch_mem_map()](../arch_core_reference/P003_架构内存映射接口.md#gab716b971ebbc382e397b6a464d534e69)及[arch_mem_unmap()](../arch_core_reference/P003_架构内存映射接口.md#gad78289a6d8810c30c7fa3052bcac9c23)返回类型从void改为int，使关闭断言时调用者也可处理错误码。启用断言时，目前基本保留原来的系统停止行为。

<a id="id4"></a>

### [视频（Video）](#id93)


- [video_import_buffer()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaa65b69cdc4271a07ad26c4850ff96e45)不再通过uint16_t *idx输出参数返回导入缓冲区索引，而是返回导入的[video_buffer](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__buffer.html)指针，失败返回NULL。这样可对应用隐藏索引细节，并使应用直接访问缓冲区。

<a id="twister"></a>

### [测试运行器（Twister）](#id94)


- 测试通过后发生的故障现在会被明确检测，并使整个测试套件失败。故意产生故障的测试，必须标记ignore_faults: true。（[GitHub #116359](https://github.com/zephyrproject-rtos/zephyr/issues/116359)）

## 译注

本页为4.4到4.5迁移工作草案（Working Draft），内容可能继续变化。兼容项、API及符号的原文拼写疑点均在对应段落注明；迁移建议仅针对官方文档范围。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：迁移到Zephyr 4.4](P006_迁移到Zephyr_4.4.md) · [本模块主线目录](../reading/releases_guides.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P006_迁移到Zephyr_4.4.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)

</details>

<!-- reading-navigation:end -->
