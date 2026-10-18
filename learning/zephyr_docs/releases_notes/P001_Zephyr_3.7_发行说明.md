---
id: learning.zephyr-docs.releases-notes.page-1
title: Zephyr 3.7 发行说明
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/release-notes-3.7.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zephyr-3-7-0"></a>

<a id="zephyr-3-7"></a>

# 第1章\_Zephyr 3.7.0版本

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/release-notes-3.7.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Zephyr项目宣布发布3.7.0版本。

这是3.x系列最后一个非维护版本，因此也将成为下一个长期支持版本（LTS）。（[长期支持（Long Term Support，LTS）版本](../project_governance/P008_发布流程.md#release-process-lts)）

本版本的主要增强包括：


- 引入全面重构的新硬件模型（Hardware Model），改变Zephyr中SoC及开发板的命名、定义和组织方式。更多信息见[开发板移植指南（Board Porting Guide）](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html#board-porting-guide)。（[重构后的硬件模型（Hardware Model）](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html#hw-model-v2)）
- 新增期待已久的HTTP服务器库及配套服务API，可便捷实现HTTP/1.1及HTTP/2服务器。资源支持静态或动态注册，并支持WebSocket。（[HTTP服务器（HTTP Server）](../networking/P055_HTTP服务器库.md#http-server-interface)）
- 扩展[POSIX支持](../portability/P010_POSIX文档入口.md#posix-support)，覆盖IEEE 1003-2017系统接口的大多数选项，以及[PSE51](../portability/P013_POSIX应用环境规范.md#posix-aep-pse51)、[PSE52](../portability/P013_POSIX应用环境规范.md#posix-aep-pse52)及[PSE53](../portability/P013_POSIX应用环境规范.md#posix-aep-pse53)要求的大多数选项和选项组。（[系统接口（System Interfaces）](../portability/P012_POSIX符合性.md#posix-system-interfaces-required)）
- 蓝牙主机新增Nordic UART服务（NUS）、免提音频网关（Hands-free Audio Gateway，AG）、高级音频分发配置文件（A2DP）及音视频分发传输协议（AVDTP）支持。
- 传感器抽象模型已重构，采用先读取再解码（Read-then-decode）的方式，较原fetch/get API支持更多传感器类型及数据流。（[先读取再解码（Read-then-decode）方式](../sensors/P006_读取与解码.md#sensor-read-and-decode)）
- 新增LLEXT扩展开发工具包（Extension Developer Kit，EDK），方便开发并集成自定义Zephyr扩展，也支持在Zephyr源码树外开发。（[可装载链接扩展开发工具包（LLEXT Extension Developer Kit，EDK）](../llext/P002_构建扩展.md#llext-build-edk)）
- [原生模拟器（Native Simulator）](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)现在可使用主机原生网络栈，无需复杂配置主机环境。
- 集成Trusted Firmware-M（TF-M）2.1.0及Mbed TLS 3.6.0，两者均为长期支持版。此外，采用[PSA Crypto](../crypto/P003_PSA密码学.md#psa-crypto)替代TinyCrypt，增强安全性及性能。
- 新增实验性精确时间协议（[Precision Time Protocol](../networking/P128_PTP精确时间协议.md#ptp-interface)，PTP，IEEE 1588）实现，可在设备间以亚微秒精度同步时间。
- 新增文档页，帮助开发者配置[Visual Studio Code](../developer_tools/P002_Visual_Studio_Code.md#vscode-ide)及[CLion](../developer_tools/P005_CLion.md#clion-ide)本地开发环境。

从Zephyr v3.6.0迁移到v3.7.0所需或推荐修改的概览，见单独的迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P003_迁移到Zephyr_3.7.md#migration-3-7)）

完整变更记录可查阅此前3.x版本发行说明。与上一个长期支持版Zephyr 2.7.0相比，其他主要增强和变化包括：


- 新增Picolibc支持，并将其作为新的默认C库。
- 新增以下硬件外设类型支持：


  - 单线总线（1-Wire）
  - 电池充电器（Battery Charger）
  - 蜂窝调制解调器（Cellular Modem）
  - 电量计（Fuel Gauge）
  - 全球导航卫星系统（GNSS）
  - 硬件自旋锁（Hardware Spinlock）
  - 改进型集成电路间总线（I3C）
  - 实时时钟（Real Time Clock，RTC）
  - 系统管理总线（SMBus）
- 新增配置片段（Snippet）支持，用于跨平台复用通用配置设置。
- 新增可链接可加载扩展（Linkable Loadable Extensions，LLEXT）支持。
- 破坏兼容性的变化概览如下，详见此前版本的发行说明及迁移指南：


  - 全部Zephyr公共头文件移到include/zephyr，因此包含时必须使用<zephyr/...>前缀。
  - 引脚复用（Pinmux）API已移除，应使用[引脚控制（Pin Control）](https://docs.zephyrproject.org/latest/hardware/pinctrl/index.html#pinctrl-guide)替代，详见对应文档。
  - 以下已弃用或实验性功能已移除：


    - 6LoCAN网络协议
    - civetweb模块，可使用Zephyr 3.7新增HTTP服务器替代。（[HTTP服务器（HTTP Server）](../networking/P055_HTTP服务器库.md#http-server-interface)）
    - tinycbor模块，可使用zcbor替代。

以下各节按组件提供详细变更列表。

<a id="security-vulnerability-related"></a>

## 安全漏洞相关变更（Security Vulnerability Related）

本版本修复以下通用漏洞披露（CVE）项：

更多详细信息见：[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](../security/P020_安全漏洞总览.md)。


- CVE-2024-3077，Zephyr项目问题跟踪：GHSA-gmfv-4vfh-2mh8。（[Zephyr项目问题跟踪条目 GHSA-gmfv-4vfh-2mh8](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-gmfv-4vfh-2mh8)）
- CVE-2024-3332，Zephyr项目问题跟踪：GHSA-jmr9-xw2v-5vf4。（[Zephyr项目问题跟踪条目 GHSA-jmr9-xw2v-5vf4](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-jmr9-xw2v-5vf4)）
- CVE-2024-4785：原发行说明记载，披露保密期截至2024-08-07。
- CVE-2024-5754：原发行说明记载，披露保密期截至2024-09-04。
- CVE-2024-5931：原发行说明记载，披露保密期截至2024-09-10。
- CVE-2024-6135：原发行说明记载，披露保密期截至2024-09-11。
- CVE-2024-6137：原发行说明记载，披露保密期截至2024-09-11。
- CVE-2024-6258：原发行说明记载，披露保密期截至2024-09-05。
- CVE-2024-6259：原发行说明记载，披露保密期截至2024-09-12。
- CVE-2024-6442：原发行说明记载，披露保密期截至2024-09-22。
- CVE-2024-6443：原发行说明记载，披露保密期截至2024-09-22。
- CVE-2024-6444：原发行说明记载，披露保密期截至2024-09-22。

<a id="api-changes"></a>

## API变更（API Changes）

<a id="removed-apis-in-this-release"></a>

### 本版本移除的API（Removed APIs）

> - 蓝牙子系统专用调试符号已移除，替换为Zephyr日志符号。
> - PCIe API移除已弃用的pcie_probe及pcie_bdf_lookup函数。
> - 移除已弃用的CONFIG_EMUL_EEPROM_AT2X选项。
> - 设备电源管理（Device PM）API移除pm_device_state_lock、pm_device_state_is_locked及pm_device_state_unlock。
> - 移除已弃用MCUmgr传输API：zephyr_smp_rx_req、zephyr_smp_alloc_rsp及zephyr_smp_free_buf。

<a id="deprecated-in-this-release"></a>

### 本版本弃用的功能（Deprecated）

> - 蓝牙广播选项BT_LE_ADV_OPT_USE_NAME及BT_LE_ADV_OPT_FORCE_NAME_IN_AD现已弃用，因此以下宏也弃用：
>
>   > - `BT_LE_ADV_CONN_NAME`
>   > - `BT_LE_ADV_CONN_NAME_AD`
>   > - `BT_LE_ADV_NCONN_NAME`
>   > - `BT_LE_EXT_ADV_CONN_NAME`
>   > - `BT_LE_EXT_ADV_SCAN_NAME`
>   > - `BT_LE_EXT_ADV_NCONN_NAME`
>   > - `BT_LE_EXT_ADV_CODED_NCONN_NAME`
>
>   应用开发者现在必须通过更新广播数据或扫描响应数据，自行设置广播名称。


- 控制器局域网（CAN）


  - can_calc_prescaler()已弃用，因为它容许比特率误差。同一网络节点间的比特率误差，会使节点在帧起始（Start-of-frame，SOF）同步后逐渐偏离，导致总线错误。
  - can_get_min_bitrate()及can_get_max_bitrate()已弃用，分别改用[can_get_bitrate_min()](../hardware/P362_CAN控制器接口.md#ga343456749eec6144a91bacae0d94b114)及[can_get_bitrate_max()](../hardware/P362_CAN控制器接口.md#ga1e6dc8026e4d922bce4d398d9f32a457)。
  - CAN_MAX_STD_ID及CAN_MAX_EXT_ID已弃用，分别改用[CAN_STD_ID_MASK](../hardware/P362_CAN控制器接口.md#ga4cd8ce34887b90baeeaa6a4aa048b398)及[CAN_EXT_ID_MASK](../hardware/P362_CAN控制器接口.md#ga15ee71e8abcf51008925585049125986)。
- `PM`


  - CONFIG_PM_DEVICE_RUNTIME_EXCLUSIVE已弃用，可通过[CONFIG_PM_DEVICE_SYSTEM_MANAGED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_SYSTEM_MANAGED)实现类似行为。

<a id="zephyr-3-7-posix-api-deprecations"></a>


- POSIX应用编程接口（POSIX API）


  - 已弃用的PTHREAD_BARRIER_DEFINE已移除。
  - 已弃用的EFD_IN_USE及EFD_FLAGS_SET已移除。
  - 为使Kconfig选项直接对应IEEE 1003.1-2017的选项及选项组，以下配置已弃用，括号内为替代项：


    - CONFIG_EVENTFD_MAX，替代项为[CONFIG_ZVFS_EVENTFD_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_EVENTFD_MAX)。
    - CONFIG_FNMATCH，替代项为[CONFIG_POSIX_C_LIB_EXT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LIB_EXT)。
    - [CONFIG_GETOPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GETOPT)，替代项为[CONFIG_POSIX_C_LIB_EXT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LIB_EXT)。
    - CONFIG_MAX_PTHREAD_COUNT，替代项为[CONFIG_POSIX_THREAD_THREADS_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_THREADS_MAX)。
    - CONFIG_MAX_PTHREAD_KEY_COUNT，替代项为[CONFIG_POSIX_THREAD_KEYS_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_KEYS_MAX)。
    - CONFIG_MAX_TIMER_COUNT，替代项为[CONFIG_POSIX_TIMER_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMER_MAX)。
    - CONFIG_POSIX_LIMITS_RTSIG_MAX，替代项为[CONFIG_POSIX_RTSIG_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RTSIG_MAX)。
    - CONFIG_POSIX_CLOCK，替代项为[CONFIG_POSIX_CLOCK_SELECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_CLOCK_SELECTION)、[CONFIG_POSIX_CPUTIME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_CPUTIME)、[CONFIG_POSIX_MONOTONIC_CLOCK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MONOTONIC_CLOCK)、[CONFIG_POSIX_TIMERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS)及[CONFIG_POSIX_TIMEOUTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMEOUTS)。
    - CONFIG_POSIX_FS，替代项为[CONFIG_POSIX_FILE_SYSTEM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FILE_SYSTEM)。
    - CONFIG_POSIX_MAX_FDS，替代项为[CONFIG_POSIX_OPEN_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_OPEN_MAX)及[CONFIG_ZVFS_OPEN_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_OPEN_MAX)。
    - CONFIG_POSIX_MAX_OPEN_FILES，替代项为[CONFIG_POSIX_OPEN_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_OPEN_MAX)及[CONFIG_ZVFS_OPEN_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS_OPEN_MAX)。
    - CONFIG_POSIX_MQUEUE，替代项为[CONFIG_POSIX_MESSAGE_PASSING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MESSAGE_PASSING)。
    - CONFIG_POSIX_PUTMSG，替代项为[CONFIG_XOPEN_STREAMS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XOPEN_STREAMS)。
    - CONFIG_POSIX_SIGNAL，替代项为[CONFIG_POSIX_SIGNALS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SIGNALS)。
    - CONFIG_POSIX_SYSCONF，替代项为[CONFIG_POSIX_SINGLE_PROCESS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SINGLE_PROCESS)。
    - CONFIG_POSIX_UNAME，替代项为[CONFIG_POSIX_SINGLE_PROCESS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SINGLE_PROCESS)。
    - CONFIG_PTHREAD，替代项为[CONFIG_POSIX_THREADS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)。
    - CONFIG_PTHREAD_BARRIER，替代项为[CONFIG_POSIX_BARRIERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_BARRIERS)。
    - CONFIG_PTHREAD_COND，替代项为[CONFIG_POSIX_THREADS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)。
    - CONFIG_PTHREAD_IPC，替代项为[CONFIG_POSIX_THREADS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)。
    - CONFIG_PTHREAD_KEY，替代项为[CONFIG_POSIX_THREADS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)。
    - CONFIG_PTHREAD_MUTEX，替代项为[CONFIG_POSIX_THREADS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS)。
    - CONFIG_PTHREAD_RWLOCK，替代项为CONFIG_POSIX_READER_WRITER_LOCKS。
    - CONFIG_PTHREAD_SPINLOCK，替代项为[CONFIG_POSIX_SPIN_LOCKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SPIN_LOCKS)。
    - CONFIG_SEM_NAMELEN_MAX，替代项为[CONFIG_POSIX_SEM_NAMELEN_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEM_NAMELEN_MAX)。
    - CONFIG_SEM_VALUE_MAX，替代项为[CONFIG_POSIX_SEM_VALUE_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEM_VALUE_MAX)。
    - CONFIG_TIMER，替代项为[CONFIG_POSIX_TIMERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS)。
    - CONFIG_TIMER_DELAYTIMER_MAX，替代项为[CONFIG_POSIX_DELAYTIMER_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_DELAYTIMER_MAX)。

    参见POSIX API迁移指南。（[POSIX API迁移指南（Migration Guide）](../releases_guides/P003_迁移到Zephyr_3.7.md#zephyr-3-7-posix-api-migration)）

> - 串行外设接口（SPI）
>
> > - 已弃用的spi_is_ready()已移除。
> > - 已弃用的spi_transceive_async()已移除。
> > - 已弃用的spi_read_async()已移除。
> > - 已弃用的spi_write_async()已移除。

<a id="architectures"></a>

## 架构（Architectures）


- ARC架构


  - 为ARC-V目标新增ARC MWDT工具链支持。
  - 为多核目标新增硬件内存屏障（Hardware Memory Barrier）API支持。
  - 使用ARC MWDT工具链及C++时，默认启用线程局部存储（Thread-local Storage，TLS）。
  - 修复ARC MWDT工具链配合最小C库（Minimal LibC）时，因错误标记C库边界检查接口扩展支持的宏定义，导致mbedtls构建失败的问题。
  - 修复ARC MWDT工具链下设备延迟初始化的问题。
- ARM架构


  - 新增Cortex-M85内核初步支持。
- ARM64架构


  - 在回溯（Backtrace）中实现符号名称显示，通过[CONFIG_SYMTAB](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYMTAB)启用。
  - 新增面向Cortex-R82的编译器调优。
- RISC-V架构


  - 故障触发的致命错误消息现在包含被调用者保存寄存器（Callee-saved Registers）的状态。
  - 实现栈展开（Stack Unwinding）。


    - 可选择使用帧指针（Frame Pointer）获得精确栈跟踪，代价是体积略增及速度略降。
    - 通过CONFIG_EXCEPTION_STACK_TRACE_SYMTAB可启用符号名称显示。
- Xtensa架构


  - 新增保存及恢复HiFi AudioEngine寄存器的支持。
  - 新增内存保护单元（MPU）支持。
  - 新增自动生成中断处理程序的支持。
  - 新增构建时生成向量表并包含到链接脚本的支持。
  - 新增[CONFIG_XTENSA_BREAK_ON_UNRECOVERABLE_EXCEPTIONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_BREAK_ON_UNRECOVERABLE_EXCEPTIONS)，控制是否对不可恢复异常使用break指令。启用可能产生无限中断风暴，妨碍调试。
  - 修复通过系统调用传递第7个参数时处理错误的问题。
  - 修复[arch_user_string_nlen()](../arch_core_reference/P004_架构用户空间接口.md#ga174c4f356fe315c523cefbf513858c9c)访问未映射内存时产生不可恢复异常的问题。

<a id="kernel"></a>

## 内核（Kernel）

> - 新增[k_uptime_seconds()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gae082928ea608a8b180b4cb3a79d21a24)，简化k_uptime_get() / 1000用法。
> - 新增[k_realloc()](../heap_reference/P001_内核堆公共接口.md#ga852a7a60dce5853b6925897b24a54e02)，使用内核堆实现传统[realloc()](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html#ad28fed1039f35d754710633141b4edf0)语义。
> - 通过[CONFIG_DEVICE_DT_METADATA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_DT_METADATA)，设备现在可保存节点标签（Nodelabel）等设备树元数据。在Shell等场景可通过device_get_by_dt_nodelabel()等API，以易读名称获取设备。
> - 设备对应节点若设置特殊属性zephyr,deferred-init，即可推迟初始化，之后通过[device_init()](../device_reference/P001_设备模型公共接口.md#gaeea4f9c9f14ab12d224378ab90231c09)完成。
> - 静态分配线程栈的声明已更新，单栈及栈数组均使用[K_THREAD_STACK_LEN](../thread_stack_reference/P001_线程栈接口.md#ga72fa31a9d8e28ccabd6e5e908a24ec00)，以保证全部线程栈正确对齐。对用户线程，视架构对齐要求，静态栈对象大小可能增加。
> - 修复[k_thread_abort()](../thread_core_reference/P001_线程公共接口.md#ga1f44bb0307bea7a97227764ecd7bf963)及join的边界死锁：SMP系统中竞争的ISR可能因互相向被中断线程发送信号而持续自旋。
> - 修复[CONFIG_SCHED_SCALABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_SCALABLE)与[CONFIG_SCHED_DEADLINE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_DEADLINE)一起使用时损坏调度队列的问题。

<a id="bluetooth"></a>

## 蓝牙（Bluetooth）


- 音频（Audio）


  - 移除bt_bap_broadcast_assistant_cb.recv_state_removed中冗余的err参数。
  - 示例改名如下：broadcast_audio_assistant改为bap_broadcast_assistant；broadcast_audio_sink改为bap_broadcast_sink；broadcast_audio_source改为bap_broadcast_source；unicast_audio_client改为bap_unicast_client；unicast_audio_server改为bap_unicast_server；public_broadcast_sink改为pbp_public_broadcast_sink；public_broadcast_source改为pbp_public_broadcast_source。
  - 对BT_CAP_SET_TYPE_AD_HOC集合，CAP指挥方（Commander）及发起方（Initiator）不再要求先发现通用音频服务（CAS），使应用可对未实现CAP接收方角色的BAP单播服务器等设备使用这些API。
- 主机（Host）


  - 新增Nordic UART服务（NUS），通过[CONFIG_BT_ZEPHYR_NUS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ZEPHYR_NUS)启用。支持声明多个GATT服务实例，以便将多个串行端点用于不同用途。
  - 实现免提音频网关（Hands-free Audio Gateway，AG），通过[CONFIG_BT_HFP_AG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG)启用。典型网关为手机，负责控制作为远端音频输入及输出机制的免提单元（Hands-free Unit）。
  - 实现高级音频分发配置文件（A2DP）及音视频分发传输协议（AVDTP），分别通过[CONFIG_BT_A2DP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_A2DP)及[CONFIG_BT_AVDTP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVDTP)启用，提供分发单声道、立体声或多声道高质量音频的协议和流程。典型用途为从立体声播放器向耳机或扬声器传输音乐；音频采用合适格式压缩，以有效利用有限带宽。
  - 重构数据及命令发送路径，移除BT TX线程，以及HCI片段、L2CAP分段缓冲池。与控制器的全部通信现在仅在系统工作队列上下文执行。
  - [CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER)及[CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER)现在依赖[CONFIG_BT_CONN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN)，因为它们无法在无连接条件下工作。
  - 改进[bt_foreach_bond()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad380b7f8984f8522c1b79f9bdc04905)，支持遍历经典蓝牙（Bluetooth Classic）密钥。
- HCI驱动（HCI Drivers）


  - 全面重新设计HCI驱动接口。详见Zephyr v3.7.0迁移指南的蓝牙HCI部分。（[迁移到Zephyr v3.7.0的指南](../releases_guides/P003_迁移到Zephyr_3.7.md#migration-3-7)）
  - 新增Ambiq Apollo3 Blue系列支持。
  - 新增NXP RW61x支持。
  - 新增Infineon CYW208XX支持。
  - 新增Renesas SmartBond DA1469x支持。
  - 移除无人维护的B91驱动。
  - 在mimxrt1170_evkb及mimxrt1040_evk上新增NXP IW612支持，可通过[CONFIG_BT_NXP_NW612](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_NXP_NW612)启用。译注：该配置名按原文保留。

<a id="boards-soc-support"></a>

## 开发板与SoC支持（Boards & SoC Support）


- 新增以下SoC系列支持：


  - 新增Ambiq Apollo3 Blue及Apollo3 Blue Plus SoC系列支持。
  - 新增Synopsys ARC-V RMX1xx仿真平台支持。
  - 新增STM32H7R/S SoC系列支持。
  - 新增NXP mke15z7、mke17z7、mke17z9、MCXNx4x及RW61x支持。
  - 新增Analog Devices MAX32 SoC系列支持。
  - 新增Infineon Technologies AIROC™ CYW20829低功耗蓝牙SoC系列支持。
  - 新增MediaTek MT8195音频数字信号处理器（DSP）支持。
  - 新增Nuvoton Numaker M2L31X SoC系列支持。
  - 新增Microchip PolarFire ICICLE Kit的对称多处理（SMP）变体支持。
  - 新增Renesas RA8系列SoC支持。
- 其他SoC系列变化如下：


  - Intel ACE音频DSP：使用专用寄存器报告启动状态，替代任意内存位置。
  - ITE：重命名所有ITE SoC变体的Kconfig符号。
  - STM32：在兼容系列启用ART加速器、指令缓存（I-cache）、数据缓存（D-cache）及预取（Prefetch）。
  - STM32H5：新增停止模式（Stop Mode）及[CONFIG_PM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)支持。
  - STM32WL：Sub-GHz SPI频率从12 MHz降低到8 MHz。
  - STM32C0：新增[CONFIG_POWEROFF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWEROFF)支持。
  - STM32U5：新增Stop3模式支持。
  - 新思科技（Synopsys）：


    - nsim：将平台拆为基于ARCv2及ARCv3指令集的arc_classic，以及基于RISC-V指令集的arc_v。
    - nsim/nsim_hs5x/smp：系统时钟频率与其他SMP nSIM配置统一。
  - NXP IMX8M：新增资源域控制器（Resource Domain Controller）支持。
  - NXP s32k146：将RTC时钟源设为内部振荡器。
  - GD32F4XX：修复uart4中断编号错误。
  - Nordic nRF54L：新增快速轻量处理器（Fast Lightweight Processor，FLPR）RISC-V CPU支持。
  - Espressif：从全部ESP32 SoC变体移除idf-bootloader依赖。
  - Espressif：为ESP32 SoC变体新增简易启动（Simple Boot）支持，可用单个二进制镜像加载应用，无需第二阶段启动加载器。
  - Espressif：重构并优化全部SoC内存映射。
  - LiteX平台：


    - 新增sys_arch_reboot()支持。
    - 不再错误地将[CONFIG_RISCV_ISA_EXT_A](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_A)选择为y。
  - rp2040：停用专用UART驱动，改用PL011。
  - Renesas RZ/T2M：为系统时钟控制寄存器添加默认值。
- 新增以下开发板支持：


  - 新增[Ambiq Apollo3 Blue开发板](../boards_alif_ambiq/P009_Apollo3_Blue_EVB.md#apollo3_evb)： apollo3_evb支持。
  - 新增[Ambiq Apollo3 Blue Plus开发板](../boards_alif_ambiq/P010_Apollo3_Blue_Plus_EVB.md#apollo3p_evb)： apollo3p_evb支持。
  - 新增Raspberry Pi 5开发板： rpi_5支持。（[树莓派5开发板（Raspberry Pi 5）](../boards_rak_raspberry_raytac/P010_Raspberry_Pi_5_Cortex-A76.md#rpi_5)）
  - 新增[Seeed Studio XIAO RP2040开发板](../boards_seeed/P021_XIAO_RP2040.md#xiao_rp2040)： xiao_rp2040支持。
  - 新增[Mikroe RA4M1 Clicker开发板](../boards_mikroe_to_mxchip/P002_Clicker_RA4M1.md#mikroe_clicker_ra4m1)： mikroe_clicker_ra4m1支持。
  - 新增[Arduino UNO R4 WiFi开发板](../boards_arduino/P017_Arduino_UNO_R4_Minima_WiFi.md#arduino_uno_r4)： arduino_uno_r4_wifi支持。
  - 新增Renesas EK-RA8M1开发板： ek_ra8m1支持。（[瑞萨EK-RA8M1开发板](../boards_renesas_ra/P022_RA8M1_Evaluation_Kit.md#ek_ra8m1)）
  - 新增[ST Nucleo H533RE](../boards_st_nucleo/P041_Nucleo_H533RE.md#nucleo_h533re)： nucleo_h533re支持。
  - 新增[ST STM32C0116-DK Discovery Kit](../boards_st_discovery_eval/P015_STM32C0116-DK_Discovery_Kit.md#stm32c0116_dk)： stm32c0116_dk支持。
  - 新增[ST STM32H745I Discovery](../boards_st_discovery_eval/P036_STM32H745I_Discovery.md#stm32h745i_disco)： stm32h745i_disco支持。
  - 新增ST STM32H7S78-DK探索板stm32h7s78_dk支持。（[ST STM32H7S78-DK Discovery开发板](../boards_st_discovery_eval/P041_STM32H7S78-DK_Discovery.md#stm32h7s78_dk)）
  - 新增[ST STM32L152CDISCOVERY开发板](../boards_st_discovery_eval/P042_STM32L1_Discovery.md#stm32l1_disco)stm32l152c_disco支持。
  - 新增ST STEVAL STWINBX1开发套件steval_stwinbx1支持。（[ST STEVAL STWINBX1开发套件（Development Kit）](../boards_st_discovery_eval/P011_STEVAL_STWINBX1_Development_kit.md#steval_stwinbx1)）
  - 新增NXP开发板frdm_mcxn947、ke17z512、rd_rw612_bga、frdm_rw612、frdm_ke15z及frdm_ke17z支持。
  - 新增基于nSIM的Synopsys ARC-V RMX1xx仿真平台nsim_arc_v/rmx100支持。（[Synopsys ARC-V RMX1xx基于nSIM的仿真平台](../boards_sipeed_sparkfun/P014_RISC-V_nSIM_and_HAPS_FPGA_boards.md#nsim_arc_v)）
  - 新增[Analog Devices MAX32690EVKIT](../boards_adi_max32_max78_sdp/P017_MAX32690EVKIT.md#max32690evkit)： max32690evkit支持。
  - 新增[Analog Devices MAX32680EVKIT](../boards_adi_max32_max78_sdp/P016_MAX32680EVKIT.md#max32680evkit)： max32680evkit支持。
  - 新增[Analog Devices MAX32672EVKIT](../boards_adi_max32_max78_sdp/P013_MAX32672EVKIT.md#max32672evkit)： max32672evkit支持。
  - 新增[Analog Devices MAX32672FTHR](../boards_adi_max32_max78_sdp/P014_MAX32672FTHR.md#max32672fthr)： max32672fthr支持。
  - 新增[Analog Devices MAX32670EVKIT](../boards_adi_max32_max78_sdp/P012_MAX32670EVKIT.md#max32670evkit)： max32670evkit支持。
  - 新增[Analog Devices MAX32655EVKIT](../boards_adi_max32_max78_sdp/P004_MAX32655EVKIT.md#max32655evkit)： max32655evkit支持。
  - 新增[Analog Devices MAX32655FTHR](../boards_adi_max32_max78_sdp/P005_MAX32655FTHR.md#max32655fthr)： max32655fthr支持。
  - 新增[Analog Devices AD-APARD32690-SL](../boards_adi_ethernet_platforms/P002_AD-APARD32690-SL.md#apard32690)： ad_apard32690_sl支持。
  - 新增[Infineon Technologies CYW920829M2EVK-02](../boards_infineon_innblue/P009_CYW920829M2EVK-02.md#cyw920829m2evk_02)： cyw920829m2evk_02支持。
  - 新增[Nuvoton Numaker M2L31KI开发板](../boards_norik_to_nuvoton/P016_NUMAKER_M2L31KI.md#numaker_m2l31ki)numaker_m2l31ki支持。
  - 新增[Espressif ESP32-S2 DevKit-C](../boards_espressif/P027_ESP32-S2-DevKitC.md#esp32s2_devkitc)： esp32s2_devkitc支持。
  - 新增[Espressif ESP32-S3 DevKit-C](../boards_espressif/P030_ESP32-S3-DevKitC.md#esp32s3_devkitc)： esp32s3_devkitc支持。
  - 新增[Espressif ESP32-C6 DevKit-C](../boards_espressif/P023_ESP32-C6-DevKitC.md#esp32c6_devkitc)： esp32c6_devkitc支持。
  - 新增[Waveshare ESP32-S3-Touch-LCD-1.28](../boards_waveshare_tail/P011_ESP32-S3-Touch-LCD-1.28.md#esp32s3_touch_lcd_1_28)： esp32s3_touch_lcd_1_28支持。
  - 新增[M5Stack ATOM Lite](../boards_lilygo_to_m5stack/P020_ATOM_Lite.md#m5stack_atom_lite)： m5stack_atom_lite支持。
  - 新增[CTHINGS.CO Connectivity Card nRF52840](../boards_cdac_to_cthings/P018_CTHINGS.CO_Connectivity_Card.md#ctcc)： ctcc支持。
- 开发板变化如下：


  - ST STM32H7B3I探索套件stm32h7b3i_dk启用完整缓存管理、Chrom-ART、双帧缓冲及全刷新，以优化LVGL性能。（[ST STM32H7B3I探索套件（Discovery Kit）](../boards_st_discovery_eval/P040_STM32H7B3I_Discovery_kit.md#stm32h7b3i_dk)）
  - STM32开发板的stm32cubeprogrammer运行器现在可通过--extload烧录外部Flash。
  - 为所有NXP开发板的Linkserver新增HEX文件支持。
  - 更新Linkserver west运行器，以适配LinkServer v1.5.xx命令行接口变化。
  - 为NXP mimxrt1010_evk、mimxrt1160_evk、frdm_rw612、rd_rw612_bga及frdm_mcxn947新增LinkServer支持。
  - 引入模拟目标[nrf54l15bsim](../bsim_reference/P004_NRF54L15模拟开发板.md#nrf54l15bsim)。
  - nrf5x bsim目标现在支持蓝牙LE编码物理层（LE Coded PHY）。
  - 重构LLVM模糊测试（Fuzzing）支持，并为native_sim添加该支持。
  - nRF54H20 PDK预发布版转换为[nRF54H20 DK](../boards_nordic/P011_nRF54H20_DK.md#nrf54h20dk)。
  - [nRF54H20 DK](../boards_nordic/P011_nRF54H20_DK.md#nrf54h20dk)的PPR内核目标默认从RAM运行；新增xip变体，从磁阻RAM（MRAM）就地执行。
  - 重构[BeagleConnect Freedom](../boards_beagle/P003_BeagleConnect_Freedom.md#beagleconnect_freedom)外部天线切换处理。
  - 为nRF5340 Audio DK新增Arduino设备树节点标签。
  - nRF54L15 PDK默认修订版本由0.2.1改为0.3.0。
  - nRF5340开发板不再直接访问控制网络核强制关闭（Force-OFF）信号的寄存器，而使用开关管理器（On-off Manager）跟踪网络核使用情况的模块，API位于<nrf53_cpunet_mgmt.h>。
  - Laird Connectivity开发板品牌更名为Ezurio。
- 新增以下扩展板（Shield）支持：


  - [Adafruit 2.8英寸TFT触摸扩展板v2](../boards_shields/P004_Adafruit_2.8_TFT_Touch_Shield_v2.md#adafruit-2-8-tft-touch-v2)（adafruit_2_8_tft_touch_v2）
  - Adafruit 5×5 NeoPixel点阵BFF扩展板（adafruit_neopixel_grid_bff）（[Adafruit 5×5 NeoPixel网格BFF扩展板](../boards_shields/P033_Adafruit_5x5_NeoPixel_Grid_BFF.md#adafruit-neopixel-grid-bff)）
  - Arduino UNO click扩展板（arduino_uno_click）（[Arduino UNO click扩展板（Shield）](../boards_shields/P052_Arduino_UNO_click_shield.md#arduino-uno-click)）
  - [DVP FPC-24 MT9M114摄像头模块](../boards_shields/P062_DVP_FPC-24_MT9M114_Camera_Module.md#dvp-fpc24-mt9m114)（dvp_fpc24_mt9m114）
  - NXP LCD_PAR_S035 TFT液晶模块（lcd_par_s035）（[NXP LCD_PAR_S035 TFT LCD模块](../boards_shields/P078_NXP_LCD_PAR_S035_TFT_LCD_Module.md#lcd-par-s035)）
  - [MikroElektronika Weather Click](../boards_shields/P123_MikroElektronika_Weather_Click.md#mikroe-weather-click)气象模块（mikroe_weather_click）
  - [NXP BTB-44 OV5640摄像头模块](../boards_shields/P135_NXP_BTB-44_OV5640_Camera_Module.md#nxp-btb44-ov5640)（nxp_btb44_ov5640）
  - [Reyax LoRa RYLR896及RYLR915模块](../boards_shields/P151_Reyax_LoRa_RYLR896_and_RYLR915_Modules.md#reyax-lora)（reyax_lora）
  - NXP RK043FN02H-CT并行显示器（rk043fn02h_ct）（[NXP RK043FN02H-CT并行显示屏](../boards_shields/P152_NXP_RK043FN02H-CT_Parallel_Display.md#rk043fn02h-ct)）
  - NXP RK043FN66HS-CTG并行显示器（rk043fn66hs_ctg）（[NXP RK043FN66HS-CTG并行显示屏](../boards_shields/P153_NXP_RK043FN66HS-CTG_Parallel_Display.md#rk043fn66hs-ctg)）
  - Raspberry Pi Pico转UNO FlexyPin适配板（rpi_pico_uno_flexypin）（[树莓派Pico转UNO FlexyPin适配板（Adapter）](../boards_shields/P156_Raspberry_Pi_Pico_to_UNO_FlexyPin_Adapter.md#rpi-pico-uno-flexypin)）
  - Seeed Studio XIAO扩展板（seeed_xiao_expansion_board）（[Seeed Studio XIAO扩展板（Expansion Board）](../boards_shields/P164_Seeed_Studio_XIAO_Expansion_Board.md#seeed-xiao-expansion-board)）
  - Seeed Studio XIAO圆形显示器（seeed_xiao_round_display）（[Seeed Studio XIAO圆形显示屏（Round Display）](../boards_shields/P166_Seeed_Studio_XIAO_Round_Display.md#seeed-xiao-round-display)）
  - SparkFun MicroMod资产跟踪扩展板（sparkfun_carrier_asset_tracker）（[Sparkfun SparkFun MicroMod资产追踪扩展板（Asset Tracker Shield）](../boards_shields/P171_Sparkfun_SparkFun_MicroMod_Asset_Tracker_Shield.md#sparkfun-carrier-asset-tracker)）
  - [ST B-LCD40-DSI1显示扩展板](../boards_shields/P183_ST_B-LCD40-DSI1.md#st-b-lcd40-dsi1-mb1166)（st_b_lcd40_dsi1_mb1166）
  - WAVESHARE电子纸裸面板扩展板（waveshare_epaper）（[WAVESHARE电子纸裸屏扩展板（e-Paper Raw Panel Shield）](../boards_shields/P195_WAVESHARE_e-Paper_Raw_Panel_Shield.md#waveshare-epaper)）
  - X-NUCLEO-BNRG2A1低功耗蓝牙扩展板（x_nucleo_bnrg2a1）（[X-NUCLEO-BNRG2A1：低功耗蓝牙BLE扩展板](../boards_shields/P203_X-NUCLEO-BNRG2A1_BLE_expansion_board.md#x-nucleo-bnrg2a1)）

<a id="build-system-and-infrastructure"></a>

## 构建系统与基础设施（Build System and Infrastructure）

> - 新增可在持续集成（CI）中运行的黑盒测试，验证大多数Twister标志的正确性。
> - 为应用引入socs目录，可保存适用于特定SoC及开发板限定符下所有开发板目标的Kconfig片段与设备树覆盖文件。（[GitHub #70418](https://github.com/zephyrproject-rtos/zephyr/issues/70418)）Sysbuild也新增支持。（[GitHub #71320](https://github.com/zephyrproject-rtos/zephyr/issues/71320)）
> - 新增开发板及SoC烧录配置设置。（[GitHub #69748](https://github.com/zephyrproject-rtos/zephyr/issues/69748)）（[开发板／SoC烧录配置（Flashing Configuration）](https://docs.zephyrproject.org/latest/build/flashing/configuration.html#flashing-soc-board-config)）
> - 全局CMake属性CSTD已弃用，改为通过[CONFIG_STD_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STD_C)选择C标准版本。子系统也可声明最低所需C标准，例如CONFIG_REQUIRES_STD_C11。
> - 修复通过sysbuild向应用传递UTF-8配置的问题。（[GitHub #74152](https://github.com/zephyrproject-rtos/zephyr/issues/74152)）
> - 修复sysbuild配置变化后立即执行west flash时，加载并使用旧域文件信息的问题。（[GitHub #73864](https://github.com/zephyrproject-rtos/zephyr/issues/73864)）
> - 修复未设置Kconfig文件的Zephyr模块未在sysbuild中列出的问题。（[GitHub #72070](https://github.com/zephyrproject-rtos/zephyr/issues/72070)）
> - 新增sysbuild选项SB_CONFIG_COMPILER_WARNINGS_AS_ERRORS，可为所有镜像启用“警告视为错误”的工具链标志。（[GitHub #70217](https://github.com/zephyrproject-rtos/zephyr/issues/70217)）
> - 修复项目所用设备树覆盖文件、Kconfig片段等未被正确监视，修改后CMake不重新配置的问题。（[GitHub #74655](https://github.com/zephyrproject-rtos/zephyr/issues/74655)）
> - 为LinkServer运行器新增Intel Hex文件烧录支持。
> - 新增sysbuild/CMakeLists.txt入口及APPLICATION_CONFIG_DIR支持，可调整sysbuild行为。（[GitHub #72923](https://github.com/zephyrproject-rtos/zephyr/issues/72923)）
> - 修复armfvp查找路径包含冒号分隔列表时的问题。（[GitHub #74868](https://github.com/zephyrproject-rtos/zephyr/issues/74868)）
> - 修复version.cmake未强制限制字段大小的问题。（[GitHub #74357](https://github.com/zephyrproject-rtos/zephyr/issues/74357)）
> - 修复sysbuild处理镜像前未清除EXTRA_CONF_FILE，导致该选项无法传给镜像的问题。（[GitHub #74082](https://github.com/zephyrproject-rtos/zephyr/issues/74082)）
> - 新增sysbuild根路径支持，类似已有root模块，可相对APP_DIR调整路径。（[GitHub #73390](https://github.com/zephyrproject-rtos/zephyr/issues/73390)）
> - 为缺失的二进制块（Blob）增加警告或错误消息。（[GitHub #73051](https://github.com/zephyrproject-rtos/zephyr/issues/73051)）
> - 修复部分系统未正确检测Python可执行程序的问题。（[GitHub #72232](https://github.com/zephyrproject-rtos/zephyr/issues/72232)）
> - 新增对整个应用启用链接时优化（Link-time Optimization，LTO）的支持。（[GitHub #69519](https://github.com/zephyrproject-rtos/zephyr/issues/69519)）
> - 修复FILE_SUFFIX重复应用后缀、sysbuild中未应用后缀，以及CMake函数变量名冲突的问题。（[GitHub #70124](https://github.com/zephyrproject-rtos/zephyr/issues/70124)、[GitHub #71280](https://github.com/zephyrproject-rtos/zephyr/issues/71280)）
> - 通过[CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE)支持GCC及Clang更积极的体积优化标志。（[GitHub #70511](https://github.com/zephyrproject-rtos/zephyr/issues/70511)）
> - 修复BUILD_VERSION为空时的输出问题。（[GitHub #70970](https://github.com/zephyrproject-rtos/zephyr/issues/70970)）
> - 修复sysbuild_cache_set()去重时错误识别部分匹配的问题。（[GitHub #71381](https://github.com/zephyrproject-rtos/zephyr/issues/71381)）
> - 修复检测到错误VERSION文件的问题。（[GitHub #71385](https://github.com/zephyrproject-rtos/zephyr/issues/71385)）
> - 通过[CONFIG_OUTPUT_DISASSEMBLY_WITH_SOURCE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OUTPUT_DISASSEMBLY_WITH_SOURCE)，可禁用在反汇编输出中包含源码。（[GitHub #71535](https://github.com/zephyrproject-rtos/zephyr/issues/71535)）
> - Twister新增--flash-before参数，可在打开串口前烧录被测设备（Device Under Test，DUT）。（[GitHub #47037](https://github.com/zephyrproject-rtos/zephyr/issues/47037)）

<a id="drivers-and-sensors"></a>

## 驱动与传感器（Drivers and Sensors）


- 模数转换器（ADC）


  - 新增ADC_DT_SPEC_*BY_NAME()宏，可按名称从设备树取得ADC IO通道信息。
  - 新增电压偏置（Voltage Biasing）支持：


    - 新增CONFIG_ADC_CONFIGURABLE_VBIAS_PIN，由支持电压偏置的驱动选择。
    - adc-controller基础绑定新增zephyr,vbias-pins，用于描述电压偏置引脚。
    - 在TI ADC114s08驱动中实现。
  - 示例变化（Sample Changes）


    - 原ADC示例改名为adc_dt。
    - 新增[adc_sequence](../hardware/P445_ADC采样序列结构.md)示例，展示更多运行时adc_sequence功能。
  - 新增ADC驱动（New ADC Drivers）


    - 新增ENE KB1200驱动。
    - 新增NXP GAU ADC驱动。
  - ADI AD559x变化


    - 新增ADI ad5593支持。
    - 为ADI ad559x新增I2C总线支持。
    - 为ad559x新增内部参考电压值配置，以支持[adc_raw_to_millivolts()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gaef98dabea3e0dc1cef8add298171a950)调用。
    - 修复ad559x初始化中与[CONFIG_THREAD_NAME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_THREAD_NAME)可用性有关、导致运行异常的问题。
    - 改进ad559x的ADC读取效率及验证。
  - ESP32变化


    - 更新ESP32 ADC驱动，以适配hal_espressif 5.1。
    - 为ESP32S3及ESP32C3新增DMA模式支持。
  - nRF变化


    - nrfx_saadc新增nRF54L15及nRF54H20支持。
    - nRF SAADC驱动禁用未使用通道的突发模式（Burst Mode），避免卡死。
    - 修复adc_nrfx_saadc.c在单端模式允许负ADC读数的问题。注意：由于硬件限制，此修复使nRF54H及nRF54L系列无法进行8位分辨率单端读取。
  - NXP LPADC变化


    - 在NXP LPADC驱动中启用采集时间（Acquisition Time）功能。
    - 新增将稳压器输出作为NXP LPADC参考电压的支持。
    - nxp,lpc-lpadc绑定中，phandle类型的nxp,reference-supply改为phandle-array类型的nxp,references。NXP LPADC驱动现在支持通过nxp,references传递参考电压值。
  - SmartBond变化


    - 为SmartBond SDADC及GPADC驱动新增电源管理支持。
    - 修复SmartBond ADC驱动的[CONFIG_PM_DEVICE_RUNTIME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)支持。
  - STM32变化


    - 修复STM32 ADC驱动DMA支持的多个问题。
    - 新增STM32H7R/S系列支持。
  - 其他驱动变化（Other Driver Changes）


    - numaker ADC驱动新增Nuvoton m2l31x支持。
    - 修复ads1119驱动配置寄存器访问问题。
    - 修复静态分析发现的kb1200驱动未初始化值。
    - 修正tla2021参考电压值，解决[adc_raw_to_millivolts()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gaef98dabea3e0dc1cef8add298171a950)只返回实际电压一半的问题。
  - 新增Nuvoton Numaker M2L31X系列支持。
- 电池（Battery）


  - 电池绑定新增re-charge-voltage-microvolt，可设置自动重新开始充电的阈值。
- 电池备份RAM（Battery-backed RAM）


  - 新增STM32G0及STM32H5系列支持。
- 控制器局域网（CAN）


  - 扩展自动采样点位置支持，使[can_calc_timing()](../hardware/P362_CAN控制器接口.md#gac27fe64142603f0d32d422594356b2d7)及[can_calc_timing_data()](../hardware/P362_CAN控制器接口.md#ga358cd73ed59c2099f4b2c6ceb397ca11)也可使用。
  - CAN收发器新增可选min-bitrate设备树属性。
  - 新增[DT_CAN_TRANSCEIVER_MIN_BITRATE](../hardware/P373_CAN设备树宏.md#ga60cb3dc5c2feb517dddcb5a57cce8a9b)及[DT_INST_CAN_TRANSCEIVER_MIN_BITRATE](../hardware/P373_CAN设备树宏.md#ga5c0b8011b5ec85dd8772f33572ae2b71)宏，用于取得CAN收发器支持的最低比特率。
  - 内部宏CAN_DT_DRIVER_CONFIG_GET及CAN_DT_DRIVER_CONFIG_INST_GET新增指定CAN控制器最低比特率的支持。
  - 新增[can_get_bitrate_min()](../hardware/P362_CAN控制器接口.md#ga343456749eec6144a91bacae0d94b114)及[can_get_bitrate_max()](../hardware/P362_CAN控制器接口.md#ga1e6dc8026e4d922bce4d398d9f32a457)，取得特定CAN控制器与收发器组合支持的最低、最高比特率，体现查询限制不再失败的语义。原can_get_max_bitrate()已弃用。
  - CAN时序函数验证比特率时，现在考虑最低受支持比特率。
  - sample-point及sample-point-data设备树属性改为可选。
  - [can_driver_config](../hardware/P371_CAN驱动公共配置.md)的bus_speed及bus_speed_data，分别改名为bitrate及bitrate_data。
  - 新增[nordic,nrf-can](../can_adi_atmel_nxp_binding_reference/P014_nordic_nrf-can.md#std-dtcompatible-nordic-nrf-can)驱动。
  - [nuvoton,numaker-canfd](../can_adi_atmel_nxp_binding_reference/P015_nuvoton_numaker-canfd.md#std-dtcompatible-nuvoton-numaker-canfd)驱动新增Numaker M2L31X支持。
  - 新增主机通信测试套件。
- 充电器（Charger）


  - maxim,max20335-charger新增chgin-to-sys-current-limit-microamp属性。
  - maxim,max20335-charger新增system-voltage-min-threshold-microvolt属性。
  - maxim,max20335-charger新增re-charge-threshold-microvolt属性。
  - maxim,max20335-charger新增thermistor-monitoring-mode属性。
- 时钟控制（Clock Control）


  - STM32H5新增微控制器时钟输出（Microcontroller Clock Output，MCO）支持。
  - STM32WL新增多速内部（MSI）时钟支持。
  - 新增Analog Devices MAX32 SoC系列驱动。
  - 新增Nuvoton Numaker M2L31X系列支持。
  - 重构ESP32时钟控制驱动，以支持ESP32-C6。
  - LiteX的drivers/clock_control/clock_control_litex.c新增对litex_clk_get_duty_cycle()及litex_clk_get_clkout_divider()返回码的检查。
- 计数器（Counter）


  - 新增Ambiq Apollo3系列支持。
  - 新增STM32H7R/S系列支持。
  - 为NXP MCXN947新增低功耗定时器（LPTMR）驱动。
  - nxp,lptmr绑定新增resolution，表示LPTMR外设计数器使用的最大位宽。
- 数模转换器（DAC）


  - 新增NXP RW SoC系列数模转换器（DAC）支持，兼容项为[nxp,gau-dac](../hardware/P766_NXPGAU数模转换器绑定.md#dtbinding-nxp-gau-dac)。
  - 新增Analog Devices AD5691、AD5692及AD5693 DAC支持，兼容项分别为[adi,ad5691](../hardware/P796_AD5691数模转换器绑定.md#dtbinding-adi-ad5691)、[adi,ad5692](../hardware/P797_AD5692数模转换器绑定.md#dtbinding-adi-ad5692)及[adi,ad5693](../hardware/P798_AD5693数模转换器绑定.md#dtbinding-adi-ad5693)。
  - 新增Texas Instruments DACx0501系列支持，兼容项为[ti,dacx0501](../hardware/P818_DACx0501数模转换器绑定.md#dtbinding-ti-dacx0501)。
- 磁盘（Disk）


  - STM32 SD驱动新增嵌入式多媒体卡（eMMC）支持，可通过[CONFIG_SDMMC_STM32_EMMC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDMMC_STM32_EMMC)启用。
  - 新增回环磁盘（Loopback Disk）驱动，将文件作为底层磁盘设备，可通过[loopback_disk_access_register()](https://docs.zephyrproject.org/latest/doxygen/html/loopback__disk_8h.html#a17a5f2ad1706fd7c3a8dcdbda2753b9c)注册文件。
  - 新增[DISK_IOCTL_CTRL_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#ga9def34b23915a3ce6c9a8a746d3d1372)及[DISK_IOCTL_CTRL_DEINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gaf13b377592baace863070fee450bd5be)，支持运行时初始化及反初始化磁盘，使SD卡等热插拔磁盘可在运行时移除并重新插入。
  - STM32H5系列新增SDMMC支持。
- 显示（Display）


  - 所有能支持[MIPI显示总线接口（Display Bus Interface，DBI）](https://docs.zephyrproject.org/latest/hardware/peripherals/display/index.html#mipi-dbi-api)的树内显示驱动均已转换，包括GC9X01X、UC81XX、SSD16XX、ST7789V及ST7735R。使用这些显示器的开发板必须更新设备树，示例见Zephyr v3.7.0迁移指南显示部分。（[迁移到Zephyr v3.7.0的指南](../releases_guides/P003_迁移到Zephyr_3.7.md#migration-3-7)）
  - 新增ST7796S显示控制器驱动，兼容项[sitronix,st7796s](../display_sinowealth_sitronix_solomon_binding_reference/P012_sitronix_st7796s.md#std-dtcompatible-sitronix-st7796s)。
  - ILI9XXX显示驱动新增[display_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3f497776520b0eac16b8aea80ccbbcfc)支持，通过[CONFIG_ILI9XXX_READ](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ILI9XXX_READ)启用。
  - SSD16XXX显示驱动新增[display_set_orientation()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4e0a4dc2e434144874af014b8e7c4394)支持。
  - 新增NT35510 MIPI-DSI显示控制器驱动，兼容项[frida,nt35510](../display_adi_chipone_eink_binding_reference/P016_frida_nt35510.md#std-dtcompatible-frida-nt35510)。
  - 新增[led-strip-matrix](../display_ilitek_matrix_nxp_binding_reference/P013_led-strip-matrix.md#std-dtcompatible-led-strip-matrix)驱动，将LED灯带抽象为显示器。
  - NXP eLCDIF新增[display_set_pixel_format()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga7ede828663090760c2558a231d9f2150)支持，可使用ARGB8888、RGB888及BGR565。
  - SSD1306新增通过[display_set_pixel_format()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga7ede828663090760c2558a231d9f2150)在运行时反转颜色的支持。
  - ST7789V驱动[sitronix,st7789v](../display_sinowealth_sitronix_solomon_binding_reference/P011_sitronix_st7789v.md#std-dtcompatible-sitronix-st7789v)现在可通过inversion-off禁用反相模式。
  - 新增NXP MCXNx4x支持。
- 直接存储器访问（DMA）


  - 重命名错误回调配置，更清楚地表示启用或禁用状态。
  - 新增NXP MCXN947支持。
- 数字麦克风接口（DMIC）


  - 新增NXP rd_rw612_bga支持。
- 熵（Entropy）


  - 新增STM32H7R/S系列支持。
- 电可擦可编程只读存储器（EEPROM）


  - [zephyr,i2c-target-eeprom](../mtd_nxp_st_ti_partition_binding_reference/P022_zephyr_i2c-target-eeprom.md#std-dtcompatible-zephyr-i2c-target-eeprom)新增address-width属性，用于指定地址宽度。
- eSPI


  - 重命名eSPI虚拟线（Virtual Wire）方向宏、枚举值及Kconfig，以符合eSPI 1.5规范的新术语。
- 以太网（Ethernet）


  - 新增[CONFIG_ETH_DRIVER_RAW_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_DRIVER_RAW_MODE)，允许在不包含Zephyr二层以太网实现的情况下构建以太网驱动。
  - 移除ethernet-fixed-link设备树绑定。
  - 以太网驱动移除虚拟局域网（VLAN）处理，现在由通用以太网二层代码处理。
  - 实现或重构eth_mcux、eth_nxp_enet、eth_nxp_s32_gmac、eth_stm32及eth_nxp_s32_netc中的硬件MAC地址过滤。
  - 新增驱动（New Drivers）


    - 新增eth_nxp_enet_qos，驱动NXP MCXN SoC上的以太网控制器。
    - 新增adin1100 PHY支持。
    - 新增Realtek RTL8211F PHY支持。
  - NXP ENET驱动变化


    - eth_nxp_enet不再标为实验性驱动。
    - 弃用eth_mcux驱动。
    - 所有具有nxp,kinetis-ethernet节点的开发板及SoC，已改用新[nxp,enet](../ethernet_nxp_phy_binding_reference/P004_nxp_enet.md#std-dtcompatible-nxp-enet)绑定。
    - Kinetis平台的nxp_enet驱动新增网络设备电源管理支持。
    - eth_nxp_enet的RX处理改用内核管理的专用工作队列，替代手工无限循环。
    - eth_nxp_enet启用IPv6时禁用硬件校验和加速，因为硬件不支持加速ICMPv6校验和。
    - 新增nxp,enet1g支持。
    - 部分平台的nxp_enet MAC新增使用熔丝保存地址的支持。
    - 修复nxp_enet未设置本地管理地址（Locally Administered Address，LAA）位，以及nxp,unique-mac属性说明含糊的问题。
    - 修复nxp_enet使用不可缓存DMA缓冲区时仍启用缓存维护的问题。
    - 为nxp_enet添加内存映射输入输出（MMIO）映射。
    - 澄清eth_nxp_enet的分布式交换架构（DSA）支持。
  - NXP S32以太网变化


    - eth_nxp_s32_gmac现在隐含启用[CONFIG_MDIO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDIO)。
    - eth_nxp_s32_netc更新为使用新邮箱（MBOX）API。
  - Adin2111驱动变化


    - 修正adin2111中IAMSK1 TX_READY_MASK位域位置。
    - adin2111现在始终在帧末尾追加CRC32。
    - 调整eth_adin2111，使用正确组播过滤掩码。
    - 修复adin2111的无CRC8通用SPI模式。
    - adin2111新增OPEN Alliance SPI协议支持。
    - adin2111新增自定义驱动扩展API。
    - adin2111启用混杂模式（Promiscuous Mode）支持。
    - 将OPEN Alliance缓冲区移出adin2111设备数据，使采用通用SPI协议时节省约32 KB。
    - 修复64位平台上eth_adin2111构建警告。
    - 对adin2111进行若干小幅调整。
  - STM32以太网驱动变化


    - 为兼容的STM32F7、STM32H5及STM32H7系列新增精确时间协议（PTP）支持。
    - eth_stm32改用PHY API访问PHY，避免多任务冲突。
    - 移除STM32 F4、F7及H7的旧STM32Cube HAL API支持。
    - eth_stm32_hal新增接收及发送时间戳支持。
  - ESP32以太网驱动变化


    - ESP32以太网驱动新增运行时设置MAC地址的支持。
    - 更新ESP32以太网驱动，以适配hal_espressif 5.1。
    - 修复启用[CONFIG_NET_STATISTICS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_STATISTICS)时ESP32以太网驱动构建失败。
    - 修复ESP32以太网驱动未通过GPIO正确为外部PHY提供时钟的问题。
  - 其他以太网驱动变化


    - w5500以太网驱动新增链路状态检测，可通过Kconfig配置。
    - eth_liteeth新增运行时设置MAC地址的能力。
    - 修复eth_stellaris未考虑驱动收到的中断数可能少于控制器收到的数据包数的问题。
    - enc28j60新增设置RX过滤器的设备树属性。
    - 修复enc28j60出错时未清除ESTAT TXABRT位的问题。
    - 为native_posix以太网驱动增加条件，在启用PTP子系统时启用ptp_clock驱动实现。
    - 修复KSZ8xxx DSA驱动，使其正确初始化LAN设备。
    - 修复ksz8863启用尾部标签（Tail Tag）时使用错误寄存器地址的问题。
  - 物理层驱动变化（PHY Driver Changes）


    - 修复KSZ8081 PHY驱动在复位、自动协商、链路检测及日志缺失或刷屏方面的多个控制问题。
    - 更改KSZ8081设备树绑定的复位及中断GPIO属性名。
    - 修复phy_mii在固定链路（Fixed-link）模式下的总线故障。
- 闪存（Flash）


  - 新增Ambiq Apollo3系列支持。
  - 为SPI NOR驱动spi_nor.c新增多实例支持。
  - 初步支持无需擦除的设备：向[flash_parameters](../flash_reference/P004_Flash存储参数结构.md)加入设备能力，并新增[flash_params_get_erase_cap()](../flash_reference/P001_Flash公共接口.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c)以取得设备擦除类型。新增[FLASH_ERASE_C_EXPLICIT](../flash_reference/P001_Flash公共接口.md#ga760f7d79cb9f23bc0326abfea85808aa)，目前它是唯一受支持的擦除类型，所有Flash设备均设置它。
  - 新增[flash_flatten()](../flash_reference/P001_Flash公共接口.md#ga11eda0cdc7be12636a90d2e8c7264e4a)，适用于需要或无需擦除的设备，用于原本通过擦除移除或打乱设备数据、而非为随机数据写入做准备的场景。
  - 新增[flash_fill()](../flash_reference/P001_Flash公共接口.md#ga022838332e905b0111d5136dd963889b)辅助函数，可在指定设备的给定范围内写入同一个值。
  - 新增nrf54l15电阻式RAM（RRAM）支持。
  - STM32 OSPI驱动新增非忙等待轮询支持。
  - 新增STM32 XSPI外部NOR Flash驱动[st,stm32-xspi-nor](../flash_renesas_st_ti_binding_reference/P014_st_stm32-xspi-nor.md#std-dtcompatible-st-stm32-xspi-nor)支持。
  - STM32 OSPI、QSPI及XSPI驱动新增在外部NOR Flash上就地执行（XIP）的支持。
  - STM32 OSPI驱动的clk、dqs及ncs端口现在可通过设备树配置，见[st,stm32-ospi](../qspi_ospi_xspi_binding_reference/P002_st_stm32-ospi.md#std-dtcompatible-st-stm32-ospi)。
  - 为NXP MCXN947新增FlexSPI支持。
  - 新增Nuvoton Numaker M2L31X系列支持。
- 电量计（Fuel Gauge）


  - max17048：电压单位从mV修正为µV。
- 全球导航卫星系统（GNSS）


  - 新增全球导航卫星系统（GNSS）设备驱动API测试套件。
  - 新增u-blox UBX协议支持。
  - 新增u-blox M8 GNSS模块驱动，兼容项[u-blox,m8](../gnss_fingerprint_binding_reference/P012_u-blox_m8.md#std-dtcompatible-u-blox-m8)。
  - 新增Luatos Air530z GNSS模块驱动，兼容项[luatos,air530z](../gnss_fingerprint_binding_reference/P006_luatos_air530z.md#std-dtcompatible-luatos-air530z)。
- 通用输入输出（GPIO）


  - 新增Ambiq Apollo3系列支持。
  - 新增Broadcom机顶盒（Set-top Box，brcmstb）SoC GPIO驱动。
  - 新增[STM32_GPIO_WKUP](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__stm32.html#ga9a05f736e9ee915f591a65a7f6d382d3)，可将STM32 L4、U5、WB及WL的特定引脚配置为从关机状态唤醒的来源。
  - 新增Analog Devices MAX32 SoC系列驱动。
  - 新增Nuvoton Numaker M2L31X系列支持。
  - Renesas RZ/T2M GPIO驱动[renesas,rzt2m-gpio](../gpio_raspberrypi_renesas_binding_reference/P029_renesas_rzt2m-gpio.md#std-dtcompatible-renesas-rzt2m-gpio)新增中断支持。
- 硬件信息（Hardware Info）


  - 为STM32WB、STM32WBA及STM32WL新增设备EUI64标识支持及实现。
- 集成电路间总线（I2C）


  - 新增Ambiq Apollo3系列支持。
  - STM32 V2驱动新增[CONFIG_I2C_STM32_V2_TIMING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_STM32_V2_TIMING)，根据实际时钟配置自动计算硬件块所需总线时序。为避免生产应用嵌入这一较重算法，提供专用[I2C V2 timings](../board_samples/P003_STM32的I2C时序.md#stm32_i2c_v2_timings)示例用于取得计算结果。得到总线时序配置后，可禁用该选项，并通过设备树设置时序。（[`CONFIG_I2C_STM32_V2_TIMING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_STM32_V2_TIMING)）
  - 新增STM32H5系列支持。
  - 新增NXP MCXN947支持。
  - 新增Analog Devices MAX32 SoC系列驱动。
  - 新增Nuvoton Numaker M2L31X系列支持。
  - LiteX I2C驱动drivers/i2c/i2c_litex.c：


    - 新增通过设备树设置比特率的支持。
    - 新增i2c_litex_recover_bus()及i2c_litex_get_config()实现。
- 集成电路间音频总线（I2S）


  - 新增STM32H5系列支持。
  - 扩展MCUX Flexcomm驱动，支持更多通道及格式。
  - 新增Nordic nRF54L系列支持。
  - 修复nRF I2S驱动的分频计算。
- 改进型集成电路间总线（I3C）


  - 新增通过Shell查询总线及执行通用命令码（CCC）命令的支持。
  - 新增NPCX I3C控制器驱动。
  - 改进并修复[nxp,mcux-i3c](../i3c_smbus_binding_reference/P007_nxp_mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c)，包括更妥善处理总线忙状态，而非直接返回错误。
- 输入（Input）


  - 新增驱动：[adc-keys](../input_adc_touch_matrix_binding_reference/P002_adc-keys.md#std-dtcompatible-adc-keys)、[chipsemi,chsc6x](../input_adc_touch_matrix_binding_reference/P009_chipsemi_chsc6x.md#std-dtcompatible-chipsemi-chsc6x)、[cirque,pinnacle](../compatible_binding_reference/P026_cirque_pinnacle.md#std-dtcompatible-cirque-pinnacle)、[futaba,sbus](../input_adc_touch_matrix_binding_reference/P016_futaba_sbus.md#std-dtcompatible-futaba-sbus)、[pixart,pat912x](../input_keyboard_optical_ctsu_binding_reference/P013_pixart_pat912x.md#std-dtcompatible-pixart-pat912x)、[pixart,paw32xx](../input_keyboard_optical_ctsu_binding_reference/P014_pixart_paw32xx.md#std-dtcompatible-pixart-paw32xx)、[pixart,pmw3610](../input_keyboard_optical_ctsu_binding_reference/P015_pixart_pmw3610.md#std-dtcompatible-pixart-pmw3610)及[sitronix,cf1133](../input_touch_lvgl_gesture_binding_reference/P006_sitronix_cf1133.md#std-dtcompatible-sitronix-cf1133)。
  - [holtek,ht16k33](../led_issi_nordic_nxp_binding_reference/P004_holtek_ht16k33.md#std-dtcompatible-holtek-ht16k33)及[microchip,xec-kbd](../input_keyboard_optical_ctsu_binding_reference/P007_microchip_xec-kbd.md#std-dtcompatible-microchip-xec-kbd)从键盘扫描（Kscan）迁移到输入（Input）子系统。
- 发光二极管（LED）


  - LED Shell命令新增设备名称补全，get_info现在将颜色显示为字符串。
  - 新增ISSI旗下Lumissil Microsystems的IS31FL3194控制器驱动，兼容项[issi,is31fl3194](../led_issi_nordic_nxp_binding_reference/P006_issi_is31fl3194.md#std-dtcompatible-issi-is31fl3194)。
- LED灯带（LED Strip）


  - 全部LED灯带绑定新增chain-length及color-mapping属性。
  - 更新灯带前现在检查长度；提供的数据过长时返回错误。
  - 新增[led_strip_length()](https://docs.zephyrproject.org/latest/doxygen/html/group__led__strip__interface.html#ga7f94eab0b357a81cccb5f0ea1575714a)，返回LED灯带长度。
  - 更新通道函数现在可选，可以不实现。
  - [worldsemi,ws2812-gpio](../led_strip_binding_reference/P008_worldsemi_ws2812-gpio.md#std-dtcompatible-worldsemi-ws2812-gpio)的in-gpios及[worldsemi,ws2812-rpi_pico-pio](../led_strip_binding_reference/P011_worldsemi_ws2812-rpi_pico-pio.md#std-dtcompatible-worldsemi-ws2812-rpi_pico-pio)的output-pin，均改名为gpios。
  - 移除重构后已无用途的CONFIG_WS2812_STRIP及CONFIG_WS2812_STRIP_DRIVER。
  - 新增Texas Instruments TLC59731 RGB控制器驱动。
- 远距离无线通信（LoRa）


  - 新增Reyax LoRa模块驱动。
- 邮箱（Mailbox）


  - 新增基于硬件信号量（HSEM）的STM32驱动支持。
- 管理数据输入输出（MDIO）


  - bus_enable及bus_disable现在可由驱动选择是否实现，并移除多个驱动中的空实现。
  - 新增NXP ENET QOS MDIO控制器驱动。
  - 修复NXP ENET MDIO驱动阻塞系统工作队列的问题。
  - [CONFIG_MDIO_NXP_ENET_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDIO_NXP_ENET_TIMEOUT)单位改为微秒。
  - 新增STM32 MDIO控制器驱动支持。
- 多功能设备（MFD）


  - 新增[nxp,lp-flexcomm](../hardware/P702_NXP低功耗灵活通信接口绑定.md#dtbinding-nxp-lp-flexcomm)驱动。
  - 新增[rohm,bd8lb600fs](../hardware/P715_BD8LB600FS多功能设备绑定.md#dtbinding-rohm-bd8lb600fs)驱动。
  - 新增[maxim,max31790](../hardware/P710_MAX31790多功能设备绑定.md#dtbinding-maxim-max31790)驱动。
  - 新增[infineon,tle9104](../hardware/P729_TLE9104多功能设备绑定.md#dtbinding-infineon-tle9104)驱动。
  - 新增[adi,ad559x](../compatible_binding_reference/P001_adi_ad559x.md#std-dtcompatible-adi-ad559x)驱动。
  - [x-powers,axp192](../hardware/P691_AXP192多功能设备绑定.md#dtbinding-x-powers-axp192)新增禁用N_VBUSEN的选项。
  - [nordic,npm1300](../hardware/P685_nPM1300多功能设备绑定.md#dtbinding-nordic-npm1300)新增GPIO输入边沿事件。
  - [nordic,npm1300](../hardware/P685_nPM1300多功能设备绑定.md#dtbinding-nordic-npm1300)新增长按复位配置。
  - 修复[nordic,npm6001](../hardware/P688_nPM6001多功能设备绑定.md#dtbinding-nordic-npm6001)的迟滞模式（Hysteretic Mode）初始化。
- 调制解调器（Modem）


  - 移除已弃用GSM_PPP驱动及设备树兼容项zephyr,gsm-ppp。
  - 移除原GSM_PPP使用、现已弃用的UART_MUX及GSM_MUX。
  - MODEM_CELLULAR驱动移除zephyr,gsm-ppp兼容项支持。
  - MODEM_IFACE_UART_INTERRUPT模块移除UART_MUX集成。
  - MODEM_SHELL模块移除UART_MUX集成。
  - MODEM_CELLULAR实现调制解调器管道链接（Modem Pipelink），用于各调制解调器提供的附加数据链路连接标识（DLCI）通道。包括名为user_pipe_<index>的通用AT模式通道，以及为GNSS隧道保留、名为gnss_pipe的通道。
  - 新增一组Shell命令，可通过新管道链接直接向调制解调器发送AT命令。命令既可实际使用，也与MODEM_CELLULAR一起展示如何实现及使用Modem Pipelink模块。
- 高速外设互连（PCIe）


  - pcie_bdf_lookup及pcie_probe自v3.3.0起已弃用，现予移除。
- MIPI 显示总线接口（MIPI-DBI）


  - 新增释放（Release）API。
  - 新增通过设备树选择模式的支持。
- 多线串行外设接口（MSPI）


  - 新增实验性多位SPI（Multi-bit SPI，MSPI）API，支持通常需要命令、地址、数据阶段及可变时延的高级SPI控制器与外设。API支持同步或异步通信，覆盖单线单倍数据率（SDR）至十六线双倍数据率（DDR）。（[多线串行外设接口（Multi-bit SPI，MSPI）](../hardware/P065_多位SPI总线.md#mspi-api)）
  - 在总线仿真器中新增MSPI总线仿真器，展示MSPI API实现。
  - 新增MSPI Flash设备仿真器，展示API使用及与MSPI总线控制器交互。
  - 新增APS6404L四线外围接口（QPI）伪静态RAM驱动。
  - 新增ATXP032八线外围接口（OPI）NOR Flash驱动。
  - 新增Ambiq Apollo3p MSPI控制器驱动。
  - 新增MSPI异步传输及JEDEC MSPI-NOR Flash示例，展示设备驱动使用。（[MSPI异步传输（Asynchronous Transfer）](../driver_samples/P022_MSPI异步传输示例.md#mspi-async)；[JEDEC MSPI-NOR闪存（Flash）](../driver_samples/P023_MSPI_NOR闪存示例.md#mspi-flash)）
  - 新增mspi/api及mspi/flash测试用例，供开发者检查实现。
- 引脚控制（Pin Control）


  - 新增Renesas RA8系列驱动。
  - 新增Infineon PSoC6旧式（Legacy）驱动。
  - 新增Analog Devices MAX32 SoC系列驱动。
  - 新增Ambiq Apollo3驱动。
  - 新增ENE KB1200驱动。
  - 新增NXP RW驱动。
  - Espressif驱动现在支持ESP32C6。
  - STM32驱动现在支持STM32C0重映射（Remap）功能。
  - 新增Nuvoton Numaker M2L31X系列支持。
- 脉宽调制（PWM）


  - 新增STM32H7R/S系列支持。
  - 为NXP imxrt11xx新增四通道定时器（QTMR）PWM驱动。
  - 使NXP MCUX PWM驱动具备线程安全性。
  - 修复[PWM Blinky](../basic_samples/P004_PWM闪烁LED.md#pwm-blinky)示例，展示[BeagleConnect Freedom](../boards_beagle/P003_BeagleConnect_Freedom.md#beagleconnect_freedom)的PWM支持。
  - 新增ENE KB1200驱动。
  - 新增Nordic nRF54H及nRF54L系列SoC支持。
  - 新增Nuvoton Numaker M2L31X系列支持。
- 稳压器（Regulators）


  - 新增[cirrus,cp9314](../hardware/P674_CP9314稳压器绑定.md#dtbinding-cirrus-cp9314)驱动。
  - 通用稳压器驱动新增regulator-boot-off，并更新[adi,adp5360-regulator](../hardware/P671_ADP5360稳压器绑定.md#dtbinding-adi-adp5360-regulator)、[nordic,npm1300-regulator](../hardware/P662_nPM1300稳压器绑定.md#dtbinding-nordic-npm1300-regulator)、[nordic,npm6001-regulator](../hardware/P665_nPM6001稳压器绑定.md#dtbinding-nordic-npm6001-regulator)及[x-powers,axp192-regulator](../hardware/P679_AXP192稳压器绑定.md#dtbinding-x-powers-axp192-regulator)使用该属性。
  - 为[renesas,smartbond-regulator](../hardware/P655_Renesas_SmartBond稳压器绑定.md#dtbinding-renesas-smartbond-regulator)新增电源管理。
  - 新增is_enabled Shell命令。
  - 单线程系统不再使用忙等待（Busy Wait）。
  - 修复[x-powers,axp192-regulator](../hardware/P679_AXP192稳压器绑定.md#dtbinding-x-powers-axp192-regulator)的DCDC2输出控制。
  - 修复[renesas,smartbond-regulator](../hardware/P655_Renesas_SmartBond稳压器绑定.md#dtbinding-renesas-smartbond-regulator)的电流及电压读取函数。
  - 修复NXP VREF的Kconfig配置泄漏问题。
  - 修复Shell中微单位数值的显示。
  - 修复adset Shell命令的strcmp用法错误。
- 复位（Reset）


  - 新增Nuvoton NPCX芯片复位控制器驱动。
  - 新增NXP SYSCON复位控制器驱动。
  - 新增NXP RSTCTL复位控制器驱动。
  - 新增Nuvoton Numaker M2L31X系列支持。
- 实时时钟（RTC）


  - 新增Raspberry Pi Pico RTC驱动。
  - 除STM32F1外，为全部STM32 MCU系列新增[CONFIG_RTC_ALARM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_ALARM)支持。
  - 新增Nuvoton Numaker M2L31X系列支持。
- 实时输入输出（RTIO）


  - 将无锁队列从RTIO移到lib，移除单生产者单消费者（SPSC）及多生产者单消费者（MPSC）队列名称中的rtio_前缀。
  - 新增链式回调请求相关测试，并修复相关问题。
  - 为p4wq创建RTIO工作队列包装，在没有原生异步RTIO功能的情况下，将阻塞行为转换为非阻塞行为。
- SD 主机控制器（SDHC）


  - 新增ESP32 SDHC驱动，兼容项[espressif,esp32-sdhc](../sdhc_binding_reference/P007_espressif_esp32-sdhc.md#std-dtcompatible-espressif-esp32-sdhc)。
  - 新增Renesas MMC控制器SDHC驱动，兼容项[renesas,rcar-mmc](../sdhc_binding_reference/P018_renesas_rcar-mmc.md#std-dtcompatible-renesas-rcar-mmc)。
- 传感器（Sensors）


  - 通用部分（General）


    - 为新读取／解码器（Read/Decoder）API添加通道说明符。
    - 新增阻塞式传感器读取调用[sensor_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gace7f20e29b302e607ba274fe40a2c2bd)。
    - 通过RTIO工作队列服务解耦请求，将sensor_submit_callback()转换为异步请求。
    - 将大多数驱动移到厂商子目录。
  - AMS


    - 新增TSL2591光照传感器驱动，兼容项[ams,tsl2591](../sensor_ams_aosong_bosch_binding_reference/P009_ams_tsl2591.md#std-dtcompatible-ams-tsl2591)。
  - Aosong


    - 新增DHT20数字输出温湿度传感器驱动，兼容项[aosong,dht20](../sensor_ams_aosong_bosch_binding_reference/P014_aosong_dht20.md#std-dtcompatible-aosong-dht20)。
    - dht11驱动新增[CONFIG_DHT_LOCK_IRQS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DHT_LOCK_IRQS)，可在读取传感器期间锁定中断，避免读取问题。
  - Bosch


    - BME280更新为使用新异步API。
  - 英飞凌（Infineon）


    - 新增TLE9104动力系统开关诊断传感器驱动，兼容项[infineon,tle9104-diagnostics](../sensor_espressif_honeywell_invensense_binding_reference/P017_infineon_tle9104-diagnostics.md#std-dtcompatible-infineon-tle9104-diagnostics)。
  - Maxim


    - 新增DS18S20单线（1-Wire）温度传感器驱动，兼容项[maxim,ds18s20](../sensor_liteon_maxim_temperature_binding_reference/P013_maxim_ds18s20.md#std-dtcompatible-maxim-ds18s20)。
    - 新增MAX31790风扇转速及故障传感器，兼容项[maxim,max31790-fan-fault](../sensor_liteon_maxim_temperature_binding_reference/P019_maxim_max31790-fan-fault.md#std-dtcompatible-maxim-max31790-fan-fault)及[maxim,max31790-fan-speed](../sensor_liteon_maxim_temperature_binding_reference/P020_maxim_max31790-fan-speed.md#std-dtcompatible-maxim-max31790-fan-speed)。
  - 恩智浦（NXP）


    - 新增低功耗比较器驱动[nxp,lpcmp](../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp)。
  - Rohm


    - 新增BD8LB600FS诊断传感器驱动[rohm,bd8lb600fs-diagnostics](../sensor_realtek_rohm_sensirion_binding_reference/P009_rohm_bd8lb600fs-diagnostics.md#std-dtcompatible-rohm-bd8lb600fs-diagnostics)。
  - 芯科科技（Silabs）


    - 对SI7006温湿度传感器驱动进行多项修复及增强。
  - ST


    - QDEC驱动现在支持编码器模式配置，见[st,stm32-qdec](../sensor_st_lsm_stm32_binding_reference/P028_st_stm32-qdec.md#std-dtcompatible-st-stm32-qdec)。
    - 新增STM32数字温度传感器支持，兼容项[st,stm32-digi-temp](../sensor_st_lsm_stm32_binding_reference/P027_st_stm32-digi-temp.md#std-dtcompatible-st-stm32-digi-temp)。
    - 新增IIS328DQ I2C/SPI加速度传感器驱动，兼容项[st,iis328dq](../compatible_binding_reference/P074_st_iis328dq.md#std-dtcompatible-st-iis328dq)。
  - TDK


    - MPU6050驱动新增MPU6500三轴加速度计及三轴陀螺仪支持。
  - TI


    - 新增TMP114驱动，兼容项[ti,tmp114](../sensor_ti_vishay_wurth_sensing_binding_reference/P008_ti_tmp114.md#std-dtcompatible-ti-tmp114)。
    - 新增INA226双向电流及功率监测驱动，兼容项[ti,ina226](../sensor_st_ti_power_capacitance_binding_reference/P021_ti_ina226.md#std-dtcompatible-ti-ina226)。
    - 新增LM95234四路远端二极管及本地温度传感器驱动，兼容项[national,lm95234](../sensor_microchip_nordic_nxp_binding_reference/P016_national_lm95234.md#std-dtcompatible-national-lm95234)。
  - 其他厂商（Other Vendors）


    - 新增Angst+Pfister FCX-MLDX5氧气传感器驱动，兼容项[ap,fcx-mldx5](../sensor_ams_aosong_bosch_binding_reference/P015_ap_fcx-mldx5.md#std-dtcompatible-ap-fcx-mldx5)。
    - 新增ENE KB1200转速计传感器驱动，兼容项[ene,kb1200-tach](../auxdisplay_iio_tach_binding_reference/P014_ene_kb1200-tach.md#std-dtcompatible-ene-kb1200-tach)。
    - 新增Festo VEAA-X-3系列比例压力调节器驱动，兼容项[festo,veaa-x-3](../sensor_espressif_honeywell_invensense_binding_reference/P003_festo_veaa-x-3.md#std-dtcompatible-festo-veaa-x-3)。
    - 新增Innovative Sensor Technology TSic xx6温度传感器驱动，兼容项[ist,tsic-xx6](../sensor_liteon_maxim_temperature_binding_reference/P002_ist_tsic-xx6.md#std-dtcompatible-ist-tsic-xx6)。
    - 新增ON Semiconductor NCT75温度传感器驱动，兼容项[onnn,nct75](../sensor_nxp_qdec_optical_binding_reference/P020_onnn_nct75.md#std-dtcompatible-onnn-nct75)。
    - 新增ScioSense ENS160数字金属氧化物多气体传感器驱动，兼容项[sciosense,ens160](../compatible_binding_reference/P055_sciosense_ens160.md#std-dtcompatible-sciosense-ens160)。
    - 对GROW_R502A指纹传感器驱动进行多项修复及增强。
- 串行接口（Serial）


  - 新增通过Nordic UART服务（NUS）在低功耗蓝牙上传输UART的驱动，使控制台、Shell、日志等所有支持UART的子系统都能使用蓝牙作为传输。
  - STM32驱动的异步DMA模式新增[CONFIG_NOCACHE_MEMORY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NOCACHE_MEMORY)支持。只要DMA缓冲区位于不可缓存内存段，STM32 F7及H7现在可在启用[CONFIG_DCACHE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DCACHE)时以DMA模式使用UART。
  - 新增STM32H7R/S系列支持。
  - Renesas RCar平台UART驱动新增带FIFO的高速串行通信接口（HSCIF）支持。
  - 新增ENE KB1200 UART驱动。
  - 新增Analog Devices MAX32微控制器UART驱动。
  - 新增Renesas RA8 UART驱动。
  - UART仿真驱动uart_emul（[zephyr,uart-emul](../hardware/P526_UART仿真设备绑定.md#dtbinding-zephyr-uart-emul)）：


    - UART仿真驱动新增异步API支持。
  - ESP32 UART驱动uart_esp32（[espressif,esp32-uart](../uart_espressif_infineon_microchip_binding_reference/P002_espressif_esp32-uart.md#std-dtcompatible-espressif-esp32-uart)）：


    - 新增反转TX及RX引脚信号的支持。
    - 新增ESP32C6 SoC支持。
  - 原生TTY UART驱动uart_native_tty（[zephyr,native-tty-uart](../uart_ti_wch_virtual_binding_reference/P014_zephyr_native-tty-uart.md#std-dtcompatible-zephyr-native-tty-uart)）：


    - 新增仿真中断驱动UART的支持。
  - MCUX低功耗UART驱动uart_mcux_lpuart（nxp,kinetis-lpuart）：


    - 新增单线半双工（Single-wire Half-duplex）通信支持。
    - 新增反转TX及RX引脚信号的支持。
  - NPCX UART驱动uart_npcx（[nuvoton,npcx-uart](../uart_microchip_nordic_nxp_binding_reference/P007_nuvoton_npcx-uart.md#std-dtcompatible-nuvoton-npcx-uart)）：


    - 新增异步API支持。
    - 新增3 MHz波特率支持。译注：原文单位写作MHz，此处保留。
  - Nordic UARTE驱动uart_nrfx_uarte（[nordic,nrf-uarte](../uart_microchip_nordic_nxp_binding_reference/P004_nordic_nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte)）：


    - 新增UART不活动时将TX及RX引脚置于低功耗模式的支持。
  - Nordic UARTE驱动uart_nrfx_uarte2（[nordic,nrf-uarte](../uart_microchip_nordic_nxp_binding_reference/P004_nordic_nrf-uarte.md#std-dtcompatible-nordic-nrf-uarte)）：


    - 设备挂起时阻止UART发送。
    - 修复部分事件未触发的问题。
  - PL011 UART驱动uart_pl011（[arm,pl011](../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011)）：


    - 新增运行时配置支持。
    - 新增设备复位支持。
    - 新增使用时钟控制确定频率的支持。
    - 新增硬件流控（Hardware Flow Control）支持。
    - 新增Ambiq Apollo3 SoC UART支持。
  - SmartBond UART驱动uart_smartbond（[renesas,smartbond-uart](../uart_raspberrypi_realtek_renesas_binding_reference/P019_renesas_smartbond-uart.md#std-dtcompatible-renesas-smartbond-uart)）：


    - 新增电源管理支持。
    - 新增通过DTR及RX线路唤醒的支持。
  - STM32 UART驱动uart_stm32（[st,stm32-uart](../uart_silabs_stm32_ti_binding_reference/P015_st_stm32-uart.md#std-dtcompatible-st-stm32-uart)）：


    - 新增识别DMA缓冲区位于数据缓存还是不可缓存内存的支持。
  - 新增Nuvoton Numaker M2L31X系列支持。
- 串行外设接口（SPI）


  - 新增NXP MCXN947支持。
  - 新增Ambiq Apollo3系列基于通用IOM的SPI支持。
  - 新增Ambiq Apollo3基于BLEIF的SPI支持，专用于内部HCI。
  - STM32 SPI驱动新增[CONFIG_PM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)及[CONFIG_PM_DEVICE_RUNTIME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)支持。
  - STM32F7x的DMA SPI模式新增[CONFIG_NOCACHE_MEMORY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NOCACHE_MEMORY)支持。
  - 新增STM32H7R/S系列支持。
  - 新增Analog Devices MAX32 SoC系列驱动。
  - 修复GD32 SPI寄存器赋值错误。
- 通用串行总线（USB）


  - 新增NXP EHCI及IP3511 USB控制器的USB设备控制器（UDC）适配层驱动。
  - 对IT82xx2、DWC2、STM32、RP2040及SmartBond USB控制器驱动进行多项修复和改进。
- 视频（Video）


  - 新增STM32数字摄像头接口（Digital Camera Interface，DCMI）驱动支持，兼容项[st,stm32-dcmi](../video_st_sony_emulation_binding_reference/P004_st_stm32-dcmi.md#std-dtcompatible-st-stm32-dcmi)。
  - 启用NXP USB设备控制器。
  - 新增ov7670摄像头支持。
  - 新增ov5640摄像头支持。
  - 为NXP MCUX新增MIPI CSI-2驱动。
  - 新增DVP FPC 24引脚mt9m114摄像头模块扩展板支持。
- 看门狗（Watchdog）


  - 新增[CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS)，以毫秒设置提前警告时间；移除不再使用的CONFIG_WDT_NPCX_DELAY_CYCLES。
  - 新增Ambiq Apollo3系列支持。
  - 新增STM32H7R/S系列支持。
  - 新增Nuvoton Numaker M2L31X系列支持。
  - 为ESP32 SoC变体新增外部32 kHz晶体看门狗。
- 无线局域网（Wi-Fi）


  - 修复esp-at消息解析。
  - 修复esp-at连接失败问题。
  - 为esp-at的UDP套接字实现[bind()](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a05b4e957a092db3e68281988ceb32df8)及[recvfrom()](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a1c41b0d557d19b5031e668b1997dc73a)。
  - 为eswifi新增最大数据大小设置选项。
  - 修复ESP32 Wi-Fi驱动内存泄漏。

<a id="networking"></a>

## 网络（Networking）


- 地址解析协议（ARP）：


  - 新增发送免费ARP（Gratuitous ARP）支持。
  - 修复ARP模块TX及RX线程之间可能发生的死锁。
  - 修复可能发生的ARP条目泄漏。
  - 改进ARP调试日志。
- 受限应用协议（CoAP）：


  - 修复CoAP观察（Observe）时间计数溢出。
  - 提高CoAP重传次数[CONFIG_COAP_MAX_RETRANSMIT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_MAX_RETRANSMIT)的上限。
  - 修复CoAP客户端库的观察功能。
  - 新增[coap_client_cancel_requests()](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3f511d4df22bece05c1ac97ff4d09a80)，可取消正在进行的观察。
  - 修复CoAP服务器示例中响应ID的生成。
- 连接管理器（Connection Manager）：


  - 新增net_mgmt事件，可分别跟踪IPv4及IPv6连接状态：


    - [`NET_EVENT_L4_IPV4_CONNECTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga532fdc2f199e047a5d17e325cee12cf1)
    - [`NET_EVENT_L4_IPV4_DISCONNECTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaa92cc806d93446d548a05edb8e0074c2)
    - [`NET_EVENT_L4_IPV6_CONNECTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf6bb88ed90df5aacb40e42fcc5bfbcf5)
    - [`NET_EVENT_L4_IPV6_DISCONNECTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac81abeab44fbf2b6f29d4e11a1e1bd17)
- IPv4动态主机配置协议（DHCPv4）：


  - 新增封装厂商专用选项支持。启用[CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_OPTION_CALLBACKS_VENDOR_SPECIFIC)后，可通过[net_dhcpv4_init_option_vendor_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gaec0f1c87f5093767a4bb1c43b8e18e72)初始化回调，再用[net_dhcpv4_add_option_vendor_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#gabf3d97139fc4f7122c1bdee52cb003cb)注册以处理这些选项。
  - 新增厂商类别标识符（Vendor Class Identifier）选项，通过[CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER)启用，并用[CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER_STRING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER_STRING)设置内容。
  - DHCPv4选项提供的NTP服务器现在可用于设置系统时间。启用[CONFIG_NET_CONFIG_CLOCK_SNTP_INIT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT)时默认这样处理。
  - Syslog服务器地址现在可通过DHCPv4选项设置，启用[CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION)时默认使用。
  - 修复未向服务器请求已注册回调的选项的问题。
  - 修复未正确应用服务器提供的子网掩码的问题。
  - 重新实现DHCPv4客户端续租及重绑定（RENEW/REBIND）逻辑，以符合RFC 2131。
  - 改进DHCPv4服务器对已拒绝地址的管理，现在可在配置时间后重新使用。
  - 依据RFC 6842，修复DHCPv4服务器响应中的客户端ID选项。
  - 新增[CONFIG_NET_DHCPV4_SERVER_NAK_UNRECOGNIZED_REQUESTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_SERVER_NAK_UNRECOGNIZED_REQUESTS)，可覆盖RFC规定行为，对无法识别客户端的请求回复否定确认（NAK）。
  - 修复DHCPv4服务器客户端ID生成。
  - 对DHCPv4客户端及服务器进行其他小幅修复。
- IPv6动态主机配置协议（DHCPv6）：


  - 修复DHCPv6的net_mgmt事件代码基值错误。
  - 新增[CONFIG_NET_DHCPV6_DUID_MAX_LEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6_DUID_MAX_LEN)，可配置支持的DHCP唯一标识符（DUID）最大长度。
  - 新增DHCPv6文档页。
- DNS／多播DNS（mDNS）／链路本地多播名称解析（LLMNR）：


  - 修复同时启用mDNS解析器（Resolver）时响应器（Responder）不工作的问题；现在二者可同时使用。
  - 重构LLMNR及mDNS响应器、DNS解析器，改用套接字及套接字服务API。
  - 新增ANY查询资源类型。
  - 新增mDNS运行时提供记录的支持。
  - 新增DNS记录缓存支持。
  - 修复创建套接字失败，以及已返回全部结果时的错误码。
  - 修复DNS重传超时计算。
- gPTP/PTP:


  - 新增IEEE 1588-2019精确时间协议（PTP）支持。
  - 新增SO_TIMESTAMPING套接字选项，可从辅助数据（Ancillary Data）取得时间戳信息。
  - 修复时间戳回调竞争条件。
  - 修复本机不是最高主时钟（Grandmaster，GM）时的主时钟同步发送状态机。
- 超文本传输协议（HTTP）：


  - 新增HTTP/2服务器库及示例应用，支持静态、动态及WebSocket资源。
  - 新增HTTP Shell组件。
  - 改进HTTP客户端错误报告。
  - HTTP客户端库不再标为实验性。
  - HTTP客户端发送响应时新增POLLOUT监测。
- 互联网协议支持配置文件（IPSP）：


  - 移除互联网协议支持配置文件（IPSP），CONFIG_NET_L2_BT不再存在。
- 互联网协议第4版（IPv4）：


  - 依据RFC 5227实现IPv4地址冲突检测（Address Conflict Detection）。
  - 新增[net_ipv4_is_private_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gadce220ef01f6f329152e74f2143cbaa3)。
  - IPv4子网掩码现在按地址分别设置，不再针对整个接口设置。
  - 其他小幅修复及改进。
- 互联网协议第6版（IPv6）：


  - 依据RFC 8981实现IPv6隐私扩展（Privacy Extensions）。
  - 新增[net_ipv6_is_private_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga3d471601814ad2f4c2f9e6fb91055067)。
  - 实现IPv6可达性提示（Reachability Hint）。上层可通过[net_if_nbr_reachability_hint()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga655599b1432463455610cff768997e2b)报告邻居可达性，避免不必要的邻居发现请求。
  - 新增[CONFIG_NET_IPV6_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_MTU)，可设置自定义IPv6最大传输单元（MTU）。
  - 新增[CONFIG_NET_MCAST_ROUTE_MAX_IFACES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MCAST_ROUTE_MAX_IFACES)，可为组播转发表项设置多个接口。
  - 新增[CONFIG_NET_MCAST_ROUTE_MLD_REPORTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MCAST_ROUTE_MLD_REPORTS)，可在组播监听发现v2（MLDv2）报告中报告组播路由。
  - 修复组播包的IPv6跳数限制（Hop Limit）处理。
  - 提高IPv6邻居发现（Neighbor Discovery）测试覆盖率。
  - 修复报告重复地址检测（DAD）冲突的邻居通告（Neighbor Advertisement）包被丢弃的问题。
  - 其他小幅修复及改进。
- 轻量级机器到机器协议（LwM2M）：


  - 新增以下API函数：


    - [`lwm2m_set_bulk()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga41b673986e11748b2ded8e1f8f05e0a7)
    - `lwm2m_rd_client_set_ctx()`
  - [lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)新增offset参数，影响写后处理、验证及部分固件回调。
  - 修复分块传输收到编号0的块时未复位块上下文的问题。
  - 修复分块传输中与服务器协商块大小的问题。
  - 新增[CONFIG_LWM2M_ENGINE_ALWAYS_REPORT_OBJ_VERSION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_ENGINE_ALWAYS_REPORT_OBJ_VERSION)，可强制客户端始终报告对象版本。
  - 没有注册回调的资源现在也可进行分块传输。
  - 修复注册回调发出的空ACK未立即发送的问题。
  - 移除已弃用API函数及定义。
  - 其他小幅修复及改进。
- 其他（Misc）：


  - 整体改进网络API的Doxygen文档。
  - TFTP库改用zsock_* API。
  - 新增SNTP函数[sntp_simple_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gadb5603eeaea68e0823f8a3f6a1b8a6c1)，用于已知服务器IP地址时执行查询。
  - 新增[CONFIG_NET_TC_THREAD_PRIO_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TC_THREAD_PRIO_CUSTOM)，可覆盖默认流量类别（Traffic Class）线程优先级。
  - 修复网络配置库的IPv6事件处理程序初始化顺序。
  - Telnet Shell后端重构为使用套接字及套接字服务API。
  - 修复IGMP包被重复解除引用的问题。
  - 多个测试及示例从native_posix迁移到native_sim。
  - 新增复制网络缓冲区用户数据的支持。
  - 修复零大小网络缓冲区的克隆。
  - 新增处理40位数据格式的net_buf API。
  - 为空二层（Dummy L2）新增接收回调，适用于抓包等场景。
  - 实现用于抓包的伪接口（Pseudo Interface），又称any接口。
  - 新增熟化模式（Cooked Mode）抓包支持，允许捕获非IP网络数据。
  - 开始或停止抓包时产生网络事件。
  - 移除过时且未使用的[net_pkt](https://docs.zephyrproject.org/latest/doxygen/html/structnet__pkt.html)标志tcp_first_msg。
  - 新增[安全MQTT传感器／执行器（Secure MQTT Sensor/Actuator）](../networking/P061_安全MQTT传感器与执行器示例.md#secure-mqtt-sensor-actuator)示例。
  - 新增三层（L3）及四层（L4）部分校验和卸载支持。
  - 为[Microsoft Azure IoT Hub MQTT](../networking/P217_Azure物联网MQTT示例.md#mqtt-azure)更新证书颁发机构（CA）证书，因为原证书即将到期。
  - 新增原生模拟器（Native Simulator）卸载套接字（Offloaded Sockets）驱动。
  - 全面重构VLAN支持，改用虚拟网络接口（Virtual Network Interfaces）。
  - 为虚拟网络接口新增统计收集。
  - 修复启用[CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE)时，mgmt_event_work_handler()阻塞系统工作队列的问题。
- 消息队列遥测传输协议（MQTT）：


  - MQTT TLS后端新增应用层协议协商（ALPN）支持。
  - [mqtt_client](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__client.html)上下文结构体新增用户数据字段。
  - 修复MQTT WebSocket传输可能发生的套接字泄漏。
- 网络接口（Network Interface）：


  - 新增以下API函数：


    - [`net_if_ipv4_maddr_foreach()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gae82f53c670f602e9c37b65abb6dfaec7)
    - [`net_if_ipv6_maddr_foreach()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gab677496fb2e27be2df299a346e9c7132)
  - 改进网络接口代码的调试日志。
  - [net_if_addr](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__addr.html)结构体新增引用计数器。
  - 修复接口启用时IPv6 DAD及MLDv2操作。
  - 为OpenThread接口添加唯一默认名称。
  - 其他小幅修复。
- OpenThread协议栈


  - 移除已弃用的openthread_set_state_changed_cb()。
  - 新增低功耗蓝牙（BLE）TCAT广播API实现。
- 点对点协议（PPP）


  - 移除已弃用gsm_modem驱动及示例。
  - 优化PPP驱动内存分配。
  - 对蜂窝调制解调器示例进行多项改进。（[蜂窝调制解调器（Cellular Modem）](../networking/P214_蜂窝调制解调器示例.md#cellular-modem)）
  - 新增PPP底层抓包支持。
- 命令行（Shell）：


  - 新增net ipv4 gateway命令，设置IPv4网关地址。
  - 网络Shell宏新增参数验证。
  - 修复net_mgmt套接字信息输出。
  - 重构VLAN信息输出。
  - net iface set_mac新增设置随机MAC地址的选项。
  - 输出组播地址信息时增加组播加入状态。
- 套接字（Sockets）：


  - 实现以下新网络POSIX API：


    - [`if_nameindex()`](https://docs.zephyrproject.org/latest/doxygen/html/if_8h.html#aadc0427486b1b97fa250760e8ccd4f7f)
    - [`inet_ntoa()`](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html#aeac5d8b00354beb2127ba1468e021ef4)
    - [`inet_addr()`](https://docs.zephyrproject.org/latest/doxygen/html/inet_8h.html#a3e3b8f43e05dc3b87977b6a7a2ed09ca)
  - 新增跟踪套接字API调用的支持。
  - TLS套接字不再是实验性API。
  - 修复AF_PACKET套接字protocol字段的字节序。
  - 修复TCP的[getsockname()](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#abef44fb98f476ef2adba92bbdb362a1b)。
  - 改进DTLS套接字的[sendmsg()](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a8a2ad4261d3978ba299926f45d56ed74)支持。
  - 修复套接字服务线程停止时[net_socket_service_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gaa72bb82aa413b711e61eda092504b091)卡住的问题。
  - 修复注销服务时可能导致套接字服务线程停止的问题。
  - 移除套接字服务库的异步超时支持。
  - 修复文件描述符不足时[zsock_accept()](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#ga1532a65955c402cbb365becb58167f19)可能持续忙循环的问题。
- 系统日志（Syslog）：


  - 新增以下API函数：


    - [log_backend_net_set_ip()](../log_transport_reference/P007_网络日志后端接口.md#ga83ec275408770c4c1a29fabec09168fe)可直接用IP地址初始化Syslog网络后端。
    - [log_backend_net_start()](../log_transport_reference/P007_网络日志后端接口.md#gaab57f963e8a9e88b1e9483872e737466)便于激活Syslog网络后端。
  - 为Syslog网络后端新增结构化日志（Structured Logging）支持。
  - 为Syslog网络后端新增TCP支持。
- 传输控制协议（TCP）：


  - 修复接受新TCP连接时可能发生的死锁。
  - 修复连接拆除过程中的ACK序号验证。
  - 修复FIN包所含数据字节被忽略的问题。
  - 修复首个SYN包发送失败时可能泄漏TCP上下文的问题。
  - CONFIG_NET_TCP_ACK_TIMEOUT因与其他配置重复而弃用。
  - 改进调试日志，使高负载时更易追踪。
  - 初始序列号（ISN）生成从MD5改为SHA-256，哈希计算也改用PSA API，替代旧Mbed TLS函数。
  - 改进没有PSH标志时的ACK回复逻辑，减少冗余ACK。
- WebSocket协议：


  - 新增以下WebSocket API：


    - [`websocket_register()`](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gabc2556e62f001f8109bf6ae9f50f3952)
    - [`websocket_unregister()`](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gaa3131d2599c8c69ab95c55c2e38e28e0)
  - WebSocket库改用zsock_* API。
  - 为WebSocket套接字新增对象核心（Object Core）支持。
  - 发送时新增POLLOUT监测。
- 无线局域网（Wi-Fi）：


  - 减少5 GHz信道列表的内存占用。
  - 接入点（AP）模式新增信道有效性检查。
  - 连接调用新增基本服务集标识符（BSSID）配置支持。
  - 修复Wi-Fi Shell帮助文本及选项解析。
  - 支持WPA自动个人安全模式（WPA Auto Personal）。
  - 收集单播网络包接收及发送统计。
  - 新增请求发送（RTS）阈值配置，可设置阈值或禁用RTS机制。
  - 新增接入点参数配置支持，可在构建时及运行时设置。
  - 新增基本服务集（BSS）的max_inactivity参数，可在构建及运行时设置，控制AP因站点（STA）不活动而将其断开前允许的最大时长。
  - 新增BSS的inactivity_poll参数，仅构建时设置，用于控制AP因STA不活动而丢弃它之前，是否先轮询该STA。
  - 新增BSS的max_num_sta参数，可在构建及运行时设置，控制STA条目最大数量。
- 网络性能测试工具（zperf）：


  - 修复zperf对IP_TOS及IPV6_TCLASS选项的处理。
  - 修复长时间zperf会话的吞吐量计算。
  - 修复使用组播IP地址时TCP上传会话结束报错。
  - 修复IPv6套接字绑定IPv4地址而报错的问题。
  - 新增指定zperf会话所用网络接口的选项。
  - 新增ZPERF_SESSION_PERIODIC_RESULT事件，在TCP上传期间周期更新结果。
  - 修复zperf会话出错时可能发生的套接字泄漏。
  - 改进zperf示例默认配置下的性能。

<a id="usb"></a>

## 通用串行总线（USB）


- 新USB设备栈（USB Device Stack）：


  - 新增人机接口设备（HID）支持。
  - 引入按速率区分的配置，使高速支持符合USB 2.0规范。
  - 新增通知支持及二进制设备对象存储（BOS）初步支持。

<a id="devicetree"></a>

## 设备树（Devicetree）


- 新增[DT_INST_NODE_HAS_COMPAT](../dt_instance_reference/P001_设备树驱动实例宏.md#gaf88c7dc0e935ad7097e317e54c362ba0)，检查节点是否具有某兼容项，对拥有多个兼容项的节点尤其有用。
- 新增[DT_CHILD_NUM](../dt_identity_reference/P001_设备树节点标识宏.md#ga37cf660c2a7a844f70191d21b6543dc1)及其变体，统计节点子节点数。
- 新增[DT_FOREACH_NODELABEL](../dt_foreach_reference/P001_设备树遍历宏.md#gad5585436896efc4c5154a93b5980d3b0)及其变体，可遍历设备树节点的节点标签。
- 新增[DT_NODELABEL_STRING_ARRAY](../dt_identity_reference/P001_设备树节点标识宏.md#ga0114cbfa3a2075558769d4632b7bb1e9)、[DT_NUM_NODELABELS](../dt_irq_reference/P001_设备树中断属性宏.md#ga7b63eb05db40d7b95ccb62a9fd1f4404)及其变体。
- 新增[DT_REG_HAS_NAME](../dt_reg_reference/P001_设备树寄存器属性宏.md#ga2c68672c60d95725b69371c3ab306d24)及其变体。
- 重构[DT_ANY_INST_HAS_PROP_STATUS_OKAY](../dt_instance_reference/P001_设备树驱动实例宏.md#gaf2a45df474090b0403dffe1b7b82b735)，使结果可用于[IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)、IF_ENABLED及COND_CODE_x等宏。
- 重构[DT_NODE_HAS_COMPAT_STATUS](../dt_identity_reference/P002_设备树存在性与状态宏.md#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)，使其可在预处理阶段求值。
- DTS脚本使用的PyYAML更新到6.0，以消除供应链漏洞。

<a id="kconfig"></a>

## Kconfig配置系统


- 新增substring Kconfig预处理函数。
- 新增dt_node_ph_prop_path Kconfig预处理函数。
- 新增dt_compat_any_has_prop Kconfig预处理函数。

<a id="libraries-subsystems"></a>

## 库与子系统（Libraries / Subsystems）


- 调试（Debug）


  - symtab

  > - 启用[CONFIG_SYMTAB](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYMTAB)后，受支持架构会随Zephyr链接阶段可执行文件生成符号表（Symbol Table）。
- 按需分页（Demand Paging）


  - 最近未使用（Not Recently Used，NRU）换出算法更新了选择逻辑，避免总是选择同一页。现在从上次换出的页之后开始线性查找新候选页。
  - 新增最近最少使用（Least Recently Used，LRU）换出算法。
- 格式化输出（Formatted Output）


  - 修复使用ARCMWDT编译cbprintf时的警告。
- 管理（Management）


  - 设备更新服务（hawkBit）


    - hawkBit子系统已重构，使用设置（Settings）子系统保存配置。
    - 启用[CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME)后，可通过[hawkbit_set_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)在运行时配置hawkBit，也可使用hawkBit Shell的hawkbit set命令。
    - 使用hawkBit自动处理器（Autohandler）安装更新时，安装完成后设备现在会自动重启。
    - 启用[CONFIG_HAWKBIT_CUSTOM_DEVICE_ID](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_CUSTOM_DEVICE_ID)后，可通过[hawkbit_set_device_identity_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga4ce085b8f2bb46af2c2e9f3f2879d633)注册设置设备ID的回调。
    - 启用[CONFIG_HAWKBIT_CUSTOM_ATTRIBUTES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_CUSTOM_ATTRIBUTES)后，可通过[hawkbit_set_custom_data_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#gad8e83255a969eb61244b1edfd0b95e5d)注册回调，设置发送给hawkBit服务器的设备属性。
  - 微控制器管理（MCUmgr）


    - 移除已弃用mcumgr Go工具的说明；其他受支持客户端列表见工具与库（[Tools/libraries](https://docs.zephyrproject.org/latest/services/device_mgmt/mcumgr.html#mcumgr-tools-libraries)）。
    - 修复SMP结构体未打包（Packed），导致不支持未对齐内存访问的设备发生故障的问题。
    - 新增[CONFIG_MCUMGR_TRANSPORT_BT_DYNAMIC_SVC_REGISTRATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_BT_DYNAMIC_SVC_REGISTRATION)，可选择MCUmgr蓝牙服务在编译时静态注册，或运行时动态注册。
    - 文件系统管理组（FS Group）中，SHA计算从TinyCrypt改为PSA调用。
- 日志（Logging）


  - 启用[CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_NET_USE_DHCPV4_OPTION)后，日志网络后端的Syslog服务器IP由DHCPv4日志服务器选项7设置。
  - POSIX平台使用实时时钟作为时间戳。
  - 新增Syslog的POSIX支持。
  - 新增[LOG_WRN_ONCE](../log_core_reference/P002_日志公共接口.md#gaa9b22a7d4659030d9a3273f1f1e6786c)，警告消息仅在首次发生时记录。
  - 新增[log_thread_trigger()](../log_core_reference/P005_日志控制接口.md#ga173eff0a07bbd1fc2978a1a705cae1fb)，触发日志消息处理。
  - 修复禁用[CONFIG_MULTITHREADING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MULTITHREADING)时延迟日志（Deferred Logging）无法编译的问题。
  - 修复字典日志与非字典日志混用时，日志字符串可能被从二进制中移除的问题。
  - 修复某些情况下未生成字典数据库的问题。
  - 修复字典日志解析器未正确处理long long参数的问题。
  - 修复[CONFIG_LOG_MSG_APPEND_RO_STRING_LOC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_MSG_APPEND_RO_STRING_LOC)支持。
- 调制解调器模块（Modem Modules）


  - 新增Modem Pipelink模块，可全局共享调制解调器管道，使驱动能够为应用创建并设置管道。
  - 简化Modem Pipe同步机制，仅保护回调及用户数据，与树内实际用法一致。
  - 新增modem_stats，跟踪整个调制解调器子系统的缓冲区使用情况。
- 电源管理（Power Management）


  - 设备现在可声明哪些系统电源状态会导致掉电，按需据此设置及释放电源状态约束。通过[CONFIG_PM_POLICY_DEVICE_CONSTRAINTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_POLICY_DEVICE_CONSTRAINTS)启用，再用[pm_policy_device_power_lock_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#ga708b7d2f8cb5f09738e3c6e5937c475e)及[pm_policy_device_power_lock_put()](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__sys__policy.html#gafb90036c42bce2cc44466427b2907a81)锁定或解锁所有会导致该设备掉电的状态。
  - 新增设备电源管理Shell支持。
  - 设备电源管理与系统电源管理解耦。新选项[CONFIG_PM_DEVICE_SYSTEM_MANAGED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_SYSTEM_MANAGED)控制系统休眠时是否挂起设备。
  - 可通过zephyr,pm-device-disabled按电源状态单独禁用系统管理的设备电源管理，便于目标选择哪些状态应触发设备电源管理。
- 密码功能（Crypto）


  - TinyCrypt仍可用，但正逐步由PSA Crypto替代，以提高安全性及性能。
  - Mbed TLS更新到3.6.0，发行说明见：[https://github.com/Mbed-TLS/mbedtls/releases/tag/v3.6.0](https://github.com/Mbed-TLS/mbedtls/releases/tag/v3.6.0)。
  - 系统存在PSA密码提供方，即启用CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT时，现在必须通过CONFIG_PSA_WANT_xxx明确选择所需PSA功能。
  - 新增[CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG)及[CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG)选择项，指定Mbed TLS PSA密码核心如何生成随机数。默认前者依赖旧熵源及CTR_DRBG/HMAC_DRBG模块；后者依赖密码学安全伪随机数生成器（CSPRNG）驱动。
  - [CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_P256M_DRIVER_ENABLED)启用Mbed TLS p256-m PSA密码驱动，它是针对Cortex-M优化的secp256r1曲线软件实现。
- CMSIS神经网络库（CMSIS-NN）


  - CMSIS-NN从v4.1.0更新到v6.0.0，版本历史见：[https://arm-software.github.io/CMSIS-NN/latest/rev_hist.html](https://arm-software.github.io/CMSIS-NN/latest/rev_hist.html)。
- 现场可编程门阵列（FPGA）


  - 改进对缺少reset、load、get_status及get_info方法的驱动的处理。
  - 新增Agilex及Agilex 5支持。
- 随机数（Random）


  - 除原[sys_rand32_get()](../data_utilities/P007_随机数接口.md#ga62cb24a6049b7aa9d03d66786e4a4db6)外，现在还提供[sys_rand8_get()](../data_utilities/P007_随机数接口.md#ga810eaca8c5f71c9417d87f05c8fa4ebb)、[sys_rand16_get()](../data_utilities/P007_随机数接口.md#ga27581a2b65faa6f1f3978ad6794300ba)及[sys_rand64_get()](../data_utilities/P007_随机数接口.md#ga26da47b7d5a76475b2fc528f5d6eced6)，均基于[sys_rand_get()](../data_utilities/P007_随机数接口.md#gaf4f6792ac29c876d59ace1deae53bbd7)实现。
- 安全数字卡（SD）


  - 重构SDMMC及SDIO频率和时序选择逻辑。以前SDHC设备未报告某模式支持的最高频率时，即使支持该模式也不选择；现在只要主机控制器和卡均支持某时序模式，即使不支持其最高频率，也会选择该模式并配置较低频率。（[GitHub #72705](https://github.com/zephyrproject-rtos/zephyr/issues/72705)）
- 状态机框架（State Machine Framework）


  - [SMF_CREATE_STATE](../smf/P005_状态机API参考.md#ga5760b98a36ed1ac55eba700cf44c7e1e)现在始终接受5个参数。
  - 转换源是已运行状态的父状态时，现在会选择正确的最低共同祖先（Least Common Ancestor），以执行退出及进入动作（Exit/Entry Actions）。
  - 现在禁止向[smf_set_state()](../smf/P005_状态机API参考.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)传入NULL。
- 存储（Storage）


  - FAT文件系统：可通过[CONFIG_FS_FATFS_MKFS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FS_FATFS_MKFS)单独提供格式化功能，无需同时启用挂载失败时自动格式化。设置[CONFIG_FILE_SYSTEM_MKFS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM_MKFS)时，该选项默认启用。
  - 文件系统：现在可向[fs_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__file__system__api.html#ga9c90031ba3e5a10da8e00e81d53ef63b)传入FS_O_TRUNC，在打开文件时截断。
  - Flash映射（Flash Map）：Flash区域完整性检查从TinyCrypt改为PSA Crypto。
  - Flash映射：新增[flash_area_flatten()](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gafd097d05f5bfe91695bc7793e82cabcd)，用于此前通过擦除移除或打乱数据、而非为随机数据写入做准备的场景。
  - Flash映射：新增[FIXED_PARTITION_NODE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga79092c8d0f32aeec69c6a79021d1ab38)、[FIXED_PARTITION_NODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga526459438c6de09abb727585d22b7004)及[FIXED_PARTITION_NODE_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gad64fb220f82870acce62661bfa94991a)，可从设备树节点而非标签取得固定分区信息。
  - 新增[CONFIG_NVS_DATA_CRC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVS_DATA_CRC)，为数据添加循环冗余校验（CRC）保护。注意：启用后，NVS与此前未对数据使用CRC的现有存储不兼容。
  - 修复[nvs_calc_free_space()](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga37e5a55f0b9209c7c0c95db9e1e84715)未扣除预留分配表项（ATE）空间，返回值大于实际可用空间的问题。
  - 修复ext2格式化分区时可用空间计算错误。
  - 修复FAT驱动卸载后仍使磁盘保持已初始化状态的问题。
- 任务看门狗（Task Watchdog）


  - 新增Shell，主要用于开发期间测试。
- POSIX应用编程接口（POSIX API）


  - 改进Kconfig选项，以反映标准POSIX选项及选项组（Options / Option Groups）。
  - 新增以下选项组支持：


    - [POSIX_MAPPED_FILES](../portability/P015_POSIX选项与选项组.md#posix-option-group-mapped-files)
    - [POSIX_MEMORY_PROTECTION](../portability/P015_POSIX选项与选项组.md#posix-option-group-memory-protection)
    - [POSIX_NETWORKING](../portability/P015_POSIX选项与选项组.md#posix-option-group-networking)
    - [POSIX_SINGLE_PROCESS](../portability/P015_POSIX选项与选项组.md#posix-option-group-single-process)
    - [POSIX_TIMERS](../portability/P015_POSIX选项与选项组.md#posix-option-group-timers)
    - [XSI_SYSTEM_LOGGING](../portability/P015_POSIX选项与选项组.md#posix-option-group-xsi-system-logging)
  - 新增以下选项支持：


    - [_POSIX_ASYNCHRONOUS_IO](../portability/P015_POSIX选项与选项组.md#posix-option-asynchronous-io)
    - [_POSIX_CPUTIME](../portability/P015_POSIX选项与选项组.md#posix-option-cputime)
    - [_POSIX_FSYNC](../portability/P015_POSIX选项与选项组.md#posix-option-fsync)
    - [_POSIX_MEMLOCK](../portability/P015_POSIX选项与选项组.md#posix-option-memlock)
    - [_POSIX_MEMLOCK_RANGE](../portability/P015_POSIX选项与选项组.md#posix-option-memlock-range)
    - [_POSIX_READER_WRITER_LOCKS](../portability/P015_POSIX选项与选项组.md#posix-option-reader-writer-locks)
    - [_POSIX_SHARED_MEMORY_OBJECTS](../portability/P015_POSIX选项与选项组.md#posix-shared-memory-objects)
    - [_POSIX_THREAD_CPUTIME](../portability/P015_POSIX选项与选项组.md#posix-option-thread-cputime)
    - [_POSIX_THREAD_PRIO_PROTECT](../portability/P015_POSIX选项与选项组.md#posix-option-thread-prio-protect)
    - [_POSIX_THREAD_PRIORITY_SCHEDULING](../portability/P015_POSIX选项与选项组.md#posix-option-thread-priority-scheduling)
    - [_XOPEN_STREAMS](../portability/P015_POSIX选项与选项组.md#posix-option-xopen-streams)
  - 修复eventfd的F_SETFL处理，避免覆盖内部标志。
  - 修复调试消息中的线程栈地址输出。
  - 修复信号代码中的宏参数用法。
- LoRa无线通信／LoRa广域网（LoRaWAN）


  - 新增分片数据块传输（Fragmented Data Block Transport）服务，通过[CONFIG_LORAWAN_FRAG_TRANSPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_FRAG_TRANSPORT)启用。除默认Semtech分片解码器外，还提供内存占用更低的树内实现。
  - 新增LoRaWAN空中固件升级（Firmware Upgrade Over the Air，FUOTA）示例。
- Zephyr消息总线（ZBus）


  - 优化向消息订阅者发送投递通知时所用克隆的通道引用复制，改进VDED流程。
  - 静态初始化信号量及运行时观察者列表，缩短zbus初始化阶段耗时。
  - 新增通道消息订阅者池隔离方式。部分通道可共享隔离池，以避免投递失败并缩短通信时延。只需启用[CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION)，再用[zbus_chan_set_msg_sub_pool()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga3f90d50f20e7779ef257676ac10da357)更换通道消息池；多个通道可共享同一池。

<a id="hals"></a>

## 硬件抽象层（HALs）


- Nordic半导体


  - nrfx更新到3.5.0。
  - 新增nRF Services（nrfs）库。
- STM32系列


  - STM32F0更新到Cube V1.11.5。
  - STM32F3更新到Cube V1.11.5。
  - STM32F4更新到Cube V1.28.0。
  - STM32F7更新到Cube V1.17.2。
  - STM32G0更新到Cube V1.6.2。
  - STM32G4更新到Cube V1.5.2。
  - STM32H5更新到Cube V1.2.0。
  - STM32H7更新到Cube V1.11.2。
  - STM32L5更新到Cube V1.5.1。
  - STM32U5更新到Cube V1.5.0。
  - STM32WB更新到Cube V1.19.1。
  - STM32WBA更新到Cube V1.3.1。
  - 新增STM32H7R/S，采用Cube V1.0.0。
- ADI


  - 引入hal_adi，它是Maxim软件开发工具包（MSDK）的子集，包含器件头文件及裸机外设驱动。（[GitHub #72391](https://github.com/zephyrproject-rtos/zephyr/issues/72391)）
- 乐鑫（Espressif）


  - HAL更新到v5.1，包含新SoC底层文件。

<a id="mcuboot"></a>

## MCU启动加载器（MCUboot）

> - 修复bootutil中基于HMAC的密钥派生函数（HKDF）实现的内存泄漏。
> - 修复强制要求类型／长度／值（TLV）条目受保护的逻辑。
> - 修复指令及数据缓存禁用操作。
> - 修复镜像额外开销估算。
> - 修复移动交换（Swap-move）算法无法验证多镜像的问题。
> - 修复imgtool中的对齐脚本错误。
> - 修复imgtool对Hex文件格式的镜像验证。
> - 修复读取Flash镜像复位向量的问题。
> - 修复mbedtls过早包含check_config.h的问题。
> - 重构镜像依赖函数，减小代码体积。
> - 为ESP32-C6新增MCUboot支持。
> - 新增可选MCUboot启动横幅（Boot Banner）。
> - 新增受保护区域的TLV查询。
> - bootutil新增使用内置密钥验证的支持。
> - PSA Crypto后端新增内置椭圆曲线数字签名（ECDSA）密钥支持。
> - 为次镜像新增OVERWRITE_ONLY_KEEP_BACKUP选项。
> - 新增SOC_FLASH_0_ID及SPI_FLASH_0_ID定义。
> - 修复mbedtls 3.1及以后版本的抽象语法标记（ASN.1）支持。
> - 修复bootutil的boot_read_enc_key中有符号与无符号比较。
> - 更新imgtool的version.py，使其接受命令行参数。
> - 改进imgtool dumpinfo。
> - 修复imgtool dumpinfo的多个问题。
> - 修复imgtool verify命令验证edcsa-p384签名镜像的问题。译注：原文算法拼写为edcsa-p384，此处保留。
> - 新增NXP MCXN947支持。
> - 本次发布采用MCUboot 2.1.0+0-dev。

<a id="osdp"></a>

## 开放监督设备协议（OSDP）


- 修复控制面板（CP）安全通道握手问题：恶意外围设备（PD）发送乱序安全通道响应，可能将响应消息认证码（R-MAC）回退到旧值，导致重放攻击。

<a id="trusted-firmware-m"></a>

## 可信固件M（Trusted Firmware-M）


- TF-M更新到2.1.0，发行说明见：[https://tf-m-user-guide.trustedfirmware.org/releases/2.1.0.html](https://tf-m-user-guide.trustedfirmware.org/releases/2.1.0.html)。
- 新增RSA-3072以外的MCUboot签名类型，可通过[CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE)选择。新默认EC-P256相较RSA可节省数KB Flash。

<a id="lvgl"></a>

## 轻量图形库（LVGL）

LVGL更新到8.4.0，发行说明见：[https://docs.lvgl.io/8.4/CHANGELOG.html#v8-4-0-19-march-2024](https://docs.lvgl.io/8.4/CHANGELOG.html#v8-4-0-19-march-2024)。

此外，Zephyr进行了以下变化：

> - 启用[CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION)后，可将内存池缓冲区放入.lvgl_heap段。
> - 移除基于键盘扫描（Kscan）的指针输入封装代码。
> - 修正编码器按钮行为，使其正确产生LV_KEY_ENTER事件。
> - 改进invert-x、invert-y及swap-xy配置的处理。
> - 关闭文件时增加LV_MEM_CUSTOM_FREE调用。
> - 补充DMA2D符号缺失的Kconfig占位定义。
> - 集成LVGL坐标取整回调（Rounder Callback）支持。

<a id="tests-and-samples"></a>

## 测试与示例（Tests and Samples）

> - 新增配置片段（Snippet）：在west build时传入-S nus-console，即可启用通过低功耗蓝牙（Bluetooth LE）传输UART数据。该片段设置[CONFIG_BT_ZEPHYR_NUS_AUTO_START_BLUETOOTH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ZEPHYR_NUS_AUTO_START_BLUETOOTH)，使使用UART API的非蓝牙示例无需修改即可运行，例如控制台（Console）及日志（Logging）示例。
> - 移除net/cloud/tagoio及net/mgmt/updatehub示例中GSM_PPP专用的配置覆盖文件。GSM_PPP设备驱动已弃用并移除；替代它的MODEM_CELLULAR驱动使用原生网络协议栈及电源管理（PM）子系统，与以太网类似，建立网络无需应用执行专门操作。
> - 移除net/gsm_modem示例，因为其依赖的GSM_PPP设备驱动已弃用并移除。替代示例为基于MODEM_CELLULAR驱动的net/cellular_modem。
> - 持续集成（CI）现在使用nrf5x的bsim目标，对蓝牙低功耗编码物理层（BT LE Coded PHY）进行运行时测试。
> - tests/net测试中禁用外部以太网网络接口，因为这些测试应使用模拟网络接口。

<a id="issue-related-items"></a>

## 问题相关条目（Issue Related Items）

<a id="known-issues"></a>

### 已知问题（Known Issues）


- [GitHub #74345](https://github.com/zephyrproject-rtos/zephyr/issues/74345)：蓝牙在nRF51上发生故障，无法正常工作。

## 译注

本页按对应版本的官方发行说明翻译；“新增”“弃用”“当前”等描述均以该版本为背景。安全编号、开发板目标、设备树compatible、代码和源码路径保留原始标识；不会将原文中的历史保密期说明作为当前状态承诺。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [2.1.0.html](https://tf-m-user-guide.trustedfirmware.org/releases/2.1.0.html)：HTTP Error 404: Not Found。

---

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/releases_notes.md) · [全部主线](../reading/README.md) · [下一篇：Zephyr 4.2 发行说明](P002_Zephyr_4.2_发行说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_Zephyr_4.2_发行说明.md)

</details>

<!-- reading-navigation:end -->
