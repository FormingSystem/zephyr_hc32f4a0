---
id: learning.zephyr-docs.releases-notes.page-3
title: Zephyr 4.3 发行说明
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/release-notes-4.3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zephyr-4-3-0"></a>

<a id="zephyr-4-3"></a>

# 第3章\_Zephyr 4.3.0版本

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/release-notes-4.3.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Zephyr 4.3.0版本现已发布。

本版本的主要增强包括：

新一代USB设备协议栈（USB Device “Next” Stack）成为默认选项

新USB设备协议栈基于现代USB设备控制器接口（USB Device Controller，UDC），替代旧协议栈，支持多个控制器同时工作、运行时配置，并改进整体架构。旧协议栈现已弃用，计划在Zephyr 4.5中移除。（[USB设备协议栈（USB Device Stack）](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/usb_device.html#usb-device-stack-next)）

CPU负载与动态调频子系统（CPU Load / Dynamic Frequency Scaling）

新增实验性CPU调频子系统，可根据策略动态调整时钟，在功耗与性能之间取得平衡。同时新增CPU负载子系统，根据调度器统计获得CPU使用率指标，用于驱动调频策略。（[CPU频率（CPU Frequency）](https://docs.zephyrproject.org/latest/services/cpu_freq/index.html#cpu-freq)；[CPU负载（CPU Load）](../observability/P007_CPU负载.md#cpu-load)）

插桩子系统（Instrumentation Subsystem）

新增插桩子系统，利用编译器管理的函数插桩，简化Zephyr应用的跟踪（Tracing）与性能分析（Profiling），可在运行时记录调用图轨迹及统计性能数据。（[插桩子系统（Instrumentation Subsystem）](https://docs.zephyrproject.org/latest/services/instrumentation/index.html#instrumentation)）

开放充电桩协议库（OCPP 1.6 Library）

新增[开放充电桩协议（Open Charge Point Protocol，OCPP）](../networking/P179_OCPP充电桩协议.md#ocpp-interface)库，支持使用Zephyr开发电动汽车充电站。该库通过WebSocket实现OCPP 1.6充电点（Charge Point）功能，支持授权、交易管理及电表读数上报等核心配置文件操作，用于与中央系统（Central System）服务器通信。

Twister显示测试框架（Display Harness）

Twister现在可通过USB摄像头采集帧，并与预先记录的视觉“指纹”（Visual Fingerprints）比对，验证目标设备的显示输出。（[验证目标设备显示输出](https://docs.zephyrproject.org/latest/develop/twister/harness/display_capture.html#twister-display-capture-harness)）

开发体验改进（Developer Experience Improvements）

引入多种新工具，辅助常见开发及故障排查任务：


- 设备树诊断（Devicetree Diagnostics）工具dtdoctor，辅助诊断设备树构建错误。（[设备树诊断（Devicetree Diagnostics，dtdoctor）](https://docs.zephyrproject.org/latest/develop/sca/dtdoctor.html#dtdoctor)）
- [traceconfig](https://docs.zephyrproject.org/latest/build/kconfig/tracing.html#kconfig-traceconfig)构建目标，帮助了解Kconfig符号的来源及最终取值。
- 交互式内存占用图（Footprint Charts），可视化应用的RAM/ROM使用情况。（[交互式内存占用图（Interactive Footprint Charts）](https://docs.zephyrproject.org/latest/develop/optimizations/tools.html#footprint-tools-plot)）

扩展开发板支持（Expanded Board Support）

本次发布新增105款开发板及39款扩展板（Shield）支持。（[新增开发板](#boards-added-in-zephyr-4-3)；[新增扩展板](#shields-added-in-zephyr-4-3)）

应用从Zephyr v4.2.0迁移到v4.3.0所需或建议的修改，见单独的[迁移指南（Migration Guide）](../releases_guides/P005_迁移到Zephyr_4.3.md#migration-4-3)。

以下各节按组件提供详细变更列表。

<a id="security-vulnerability-related"></a>

## 安全漏洞相关变更（Security Vulnerability Related）

本版本修复以下通用漏洞披露（CVE）项：


- <a id="index-0"></a>

  [CVE 2025-9408](https://www.cve.org/CVERecord?id=CVE-2025-9408)：Zephyr项目问题跟踪条目GHSA-3r6j-5mp3-75wr。（[Zephyr项目问题跟踪条目 GHSA-3r6j-5mp3-75wr](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-3r6j-5mp3-75wr)）
- <a id="index-1"></a>

  [CVE 2025-9557](https://www.cve.org/CVERecord?id=CVE-2025-9557)：原发行说明记载的保密期截至2025-11-24。
- <a id="index-2"></a>

  [CVE 2025-9558](https://www.cve.org/CVERecord?id=CVE-2025-9558)：原发行说明记载的保密期截至2025-11-24。
- <a id="index-3"></a>

  [CVE 2025-12035](https://www.cve.org/CVERecord?id=CVE-2025-12035)：原发行说明记载的保密期截至2025-12-13。
- <a id="index-4"></a>

  [CVE 2025-12899](https://www.cve.org/CVERecord?id=CVE-2025-12899)：原发行说明记载的保密期截至2026-01-28。
- <a id="index-5"></a>

  [CVE 2025-59438](https://www.cve.org/CVERecord?id=CVE-2025-59438)：密码错误报告的时序可能形成填充预言机（Padding Oracle）。（[密码错误报告时序形成的填充预言机（Padding Oracle）](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-10-invalid-padding-error/)）
- <a id="index-6"></a>

  [CVE 2025-54764](https://www.cve.org/CVERecord?id=CVE-2025-54764)：RSA密钥生成及运算中的侧信道（Side Channel），涉及SSBleed及M-Step。（[RSA密钥生成及运算中的侧信道（SSBleed、M-Step）](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-10-ssbleed-mstep/)）

更多详细信息见：[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](../security/P020_安全漏洞总览.md)。

<a id="api-changes"></a>

## API变更（API Changes）


- 密码功能（Crypto）


  - [hash_pkt](../crypto/P027_散列数据包结构.md)的输入缓冲区现在带const限定。

<a id="removed-apis-and-options"></a>

### 已移除的API与选项（Removed APIs and Options）


- 由于上游版本已不再维护，TinyCrypt库已移除。Zephyr现在推荐使用PSA Crypto API作为密码库接口。
- 移除旧管道对象API，请改用新的管道（Pipe）API。
- `bt_le_set_auto_conn`
- `CONFIG_BT_BUF_ACL_RX_COUNT`
- 从设备树base.yaml绑定的status属性中彻底移除ok枚举值。
- 移除通过Kconfig选择STM32低功耗定时器（LPTIM）时钟源的功能，必须改用设备树。受影响的配置符号为[CONFIG_STM32_LPTIM_CLOCK_LSI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_LPTIM_CLOCK_LSI)及[CONFIG_STM32_LPTIM_CLOCK_LSE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_LPTIM_CLOCK_LSE)。

<a id="deprecated-apis-and-options"></a>

### 已弃用的API与选项（Deprecated APIs and Options）


- 弃用maxim,ds3231，改用[maxim,ds3231-rtc](../rtc_binding_reference/P013_maxim_ds3231-rtc.md#std-dtcompatible-maxim-ds3231-rtc)。
- 弃用[SPI_CONFIG_DT](../hardware/P318_SPI公共接口.md#gaf7d4888063e5b739f2a3bee295962bfe)、[SPI_CONFIG_DT_INST](../hardware/P318_SPI公共接口.md#ga67837cbae6f29c5f8ad9a05dbc9b05f8)、[SPI_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga43857c934651c4bfb3823a5080a4a294)及[SPI_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#gac9537325ca3188121d0f8c382c798ca1)的第三个参数，以及[SPI_CS_CONTROL_INIT](../hardware/P318_SPI公共接口.md#ga81308d27cd78e65f0a3ddaa918f2a74a)的第二个参数。请改用新设备树属性spi-cs-setup-delay-ns及spi-cs-hold-delay-ns指定延迟。
- bt_hci_bus未被使用，现已弃用；请改用[BT_DT_HCI_BUS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga766eaafe5d88d9d1efa0b3f09a334fc8)。
- 弃用CONFIG_BT_AUTO_PHY_UPDATE，替换为按中心设备／外围设备（Central / Peripheral）角色分别设置的选项，以明确指定自动更新时优先选择的物理层（PHY）。
- 弃用CONFIG_POSIX_READER_WRITER_LOCKS，改用[CONFIG_POSIX_RW_LOCKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RW_LOCKS)。
- 弃用CONFIG_JWT_SIGN_RSA_LEGACY，请改用基于PSA Crypto API的替代项[CONFIG_JWT_SIGN_RSA_PSA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT_SIGN_RSA_PSA)。
- 弃用RISC-V的[CONFIG_EXTRA_EXCEPTION_INFO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXTRA_EXCEPTION_INFO)，改用[CONFIG_EXCEPTION_DEBUG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXCEPTION_DEBUG)。

<a id="new-apis-and-options"></a>

### 新增API与选项（New APIs and Options）


- 架构（Architectures）


  - `CONFIG_ARCH_HAS_HW_SHADOW_STACK`
  - [`CONFIG_SRAM_SW_ISR_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SRAM_SW_ISR_TABLE)
  - x86的英特尔控制流强制技术（Intel CET）支持。


    - [`CONFIG_X86_CET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CET)
    - [`CONFIG_X86_CET_IBT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CET_IBT)
    - [`CONFIG_X86_CET_SHADOW_STACK_ALIGNMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CET_SHADOW_STACK_ALIGNMENT)
    - [`CONFIG_X86_CET_SOC_PREPARE_SHADOW_STACK_SWITCH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CET_SOC_PREPARE_SHADOW_STACK_SWITCH)
    - [`CONFIG_X86_CET_VERIFY_KERNEL_SHADOW_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_CET_VERIFY_KERNEL_SHADOW_STACK)
  - ARM Cortex-M系统状态保存／恢复原语（Save/Restore Primitives）。


    - z_arm_save_scb_context() / z_arm_restore_scb_context()。
    - z_arm_save_mpu_context() / z_arm_restore_mpu_context()。
    - 现有z_arm_save_fp_context()及z_arm_save_fp_context()也已更新。译注：原文两次列出同一函数名，此处保留，不推测另一函数。
  - Xtensa架构


    - [`CONFIG_XTENSA_HIFI_SHARING_MODEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI_SHARING_MODEL)
    - [`CONFIG_XTENSA_EAGER_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_EAGER_HIFI_SHARING)
    - [`CONFIG_XTENSA_LAZY_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_LAZY_HIFI_SHARING)
    - [`CONFIG_XTENSA_EXCEPTION_ENTER_GDB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_EXCEPTION_ENTER_GDB)
- 蓝牙（Bluetooth）


  - 音频（Audio）


    - [bt_audio_codec_cfg](https://docs.zephyrproject.org/latest/doxygen/html/structbt__audio__codec__cfg.html)现在包含target_latency及target_phy选项。
    - [`bt_bap_broadcast_source_foreach_stream()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__broadcast__source.html#ga9d543b9282e0dadca3afe3a97e385b15)
    - [`bt_cap_initiator_broadcast_foreach_stream()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga45fa73b787bb4fefc73928acf3592e20)
    - [bt_bap_stream](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__stream.html)现在包含iso字段，用于引用等时（ISO）通道。
    - [`bt_bap_unicast_group_get_info()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#ga4ba0e4c3fa7ec3a36a64a19c80027504)
    - [`bt_cap_unicast_group_get_info()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga86aca9c7f2f8658f4486925c68148850)
    - [`bt_bap_unicast_client_unregister_cb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaee092a4e918a67bb5fd94cb78cc21141)
  - 主机（Host）


    - [bt_iso_unicast_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__unicast__info.html)现在包含cig_id及cis_id字段。
    - [bt_iso_broadcaster_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__broadcaster__info.html)现在包含big_handle及bis_number字段。
    - [bt_iso_sync_receiver_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__sync__receiver__info.html)现在包含big_handle及bis_number字段。
    - [bt_le_ext_adv_info](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__info.html)现在包含sid字段，保存广播集标识（Advertising Set ID）。
    - [`CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_PERIPHERAL_NONE)
    - [`CONFIG_BT_AUTO_PHY_PERIPHERAL_1M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_PERIPHERAL_1M)
    - [`CONFIG_BT_AUTO_PHY_PERIPHERAL_2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_PERIPHERAL_2M)
    - [`CONFIG_BT_AUTO_PHY_PERIPHERAL_CODED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_PERIPHERAL_CODED)
    - [`CONFIG_BT_AUTO_PHY_CENTRAL_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_CENTRAL_NONE)
    - [`CONFIG_BT_AUTO_PHY_CENTRAL_1M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_CENTRAL_1M)
    - [`CONFIG_BT_AUTO_PHY_CENTRAL_2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_CENTRAL_2M)
    - [`CONFIG_BT_AUTO_PHY_CENTRAL_CODED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AUTO_PHY_CENTRAL_CODED)
- CPU调频（CPUFreq）


  - 引入实验性动态CPU调频（Dynamic CPU Frequency Scaling）子系统。


    - [`CONFIG_CPU_FREQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ)
- 蜂窝通信（Cellular）


  - [`CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT`](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910)
- 密码功能（Crypto）


  - [`CONFIG_MBEDTLS_PSA_CRYPTO_BUILTIN_KEYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_BUILTIN_KEYS)
- 显示（Display）


  - [`PIXEL_FORMAT_AL_88`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca92f4901daf73e26c4290e656e7afeb2f)
  - 简单直接媒体层（SDL）


    - `CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_AL_88`
    - [`CONFIG_SDL_DISPLAY_COLOR_TINT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDL_DISPLAY_COLOR_TINT)
- 以太网（Ethernet）

  > - 多数以太网物理层（PHY）新增default-speeds设备树属性，用于在驱动初始化时设置自动协商所通告的速率。
- 触觉反馈（Haptics）


  - [`CONFIG_HAPTICS_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAPTICS_SHELL)
- 插桩子系统（Instrumentation Subsystem）


  - 引入插桩子系统（Instrumentation Subsystem）。


    - [`CONFIG_INSTRUMENTATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION)
    - [`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH)
    - `CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_BUFFER_SIZE`
    - [`CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_BUFFER_OVERWRITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_MODE_CALLGRAPH_BUFFER_OVERWRITE)
    - [`CONFIG_INSTRUMENTATION_MODE_STATISTICAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_MODE_STATISTICAL)
    - [`CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_NUM_FUNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_NUM_FUNC)
    - [`CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_CALL_DEPTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_MODE_STATISTICAL_MAX_CALL_DEPTH)
    - [`CONFIG_INSTRUMENTATION_TRIGGER_FUNCTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_TRIGGER_FUNCTION)
    - [`CONFIG_INSTRUMENTATION_STOPPER_FUNCTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_STOPPER_FUNCTION)
    - [`CONFIG_INSTRUMENTATION_EXCLUDE_FUNCTION_LIST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_EXCLUDE_FUNCTION_LIST)
    - [`CONFIG_INSTRUMENTATION_EXCLUDE_FILE_LIST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INSTRUMENTATION_EXCLUDE_FILE_LIST)
    - [`instr_header`](../observability/P033_插桩事件头.md)
    - [`instr_event_context`](../observability/P034_插桩事件上下文.md)
    - [`instr_record`](../observability/P035_插桩事件记录.md)
    - [`instr_tracing_supported()`](../observability/P025_插桩接口参考.md#ga4644a5ae2a95db35896eb0007dffffac)
    - [`instr_profiling_supported()`](../observability/P025_插桩接口参考.md#gae4d79f7bddd5925282491230dcbdafcd)
    - [`instr_fundamentals_initialized()`](../observability/P025_插桩接口参考.md#gaae69ccca44c9795d520ff88dd16ad270)
    - [`instr_init()`](../observability/P025_插桩接口参考.md#gabfe70f8b42bd46a7670c0caf19ecf9d6)
    - [`instr_initialized()`](../observability/P025_插桩接口参考.md#ga6a50c0f38ce42543ffffe36e8fa66cad)
    - [`instr_enabled()`](../observability/P025_插桩接口参考.md#ga18b2ab24755c20195625fc0c1a940cdf)
    - [`instr_enable()`](../observability/P025_插桩接口参考.md#gab75168585bb4dfa4ad61bc61d6d13139)
    - [`instr_disable()`](../observability/P025_插桩接口参考.md#ga9cbb034bc9515bbe73db65786aee2883)
    - [`instr_turn_on()`](../observability/P025_插桩接口参考.md#ga4b0236b900f4b6ad17f5e76553182c7c)
    - [`instr_turn_off()`](../observability/P025_插桩接口参考.md#ga047f5ae434a533de2c417b283fa4507b)
    - [`instr_turned_on()`](../observability/P025_插桩接口参考.md#gaefe08795d416d7348678554d3a78a72f)
    - [`instr_trace_enabled()`](../observability/P025_插桩接口参考.md#ga6f11997e33209ae444f26c7ccf7448a0)
    - [`instr_profile_enabled()`](../observability/P025_插桩接口参考.md#ga4197c8d96b8679484ff7f03c5ea189fa)
    - [`instr_dump_buffer_uart()`](../observability/P025_插桩接口参考.md#ga1ce7ffd9ef1a74c0f1b17d91bcf85b8f)
    - [`instr_dump_deltas_uart()`](../observability/P025_插桩接口参考.md#ga1881790320b21092700a470b20fd3291)
    - [`instr_event_handler()`](../observability/P025_插桩接口参考.md#ga898bf91eca9e1b79c67533aeb21f6bf5)
    - [`instr_set_trigger_func()`](../observability/P025_插桩接口参考.md#gab2e8c42b53d635c7c5aa256fbf827277)
    - [`instr_set_stop_func()`](../observability/P025_插桩接口参考.md#ga0303b08c48819229833dcce7c19fc55c)
    - [`instr_get_trigger_func()`](../observability/P025_插桩接口参考.md#ga8ba100c1d94dc45b3a6d17f36c2bf583)
    - [`instr_get_stop_func()`](../observability/P025_插桩接口参考.md#ga275febe8ffcca4ee03197e9f3bc2d225)
- 内核（Kernel）


  - [`CONFIG_HW_SHADOW_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HW_SHADOW_STACK)
  - [`CONFIG_HW_SHADOW_STACK_ALLOW_REUSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HW_SHADOW_STACK_ALLOW_REUSE)
  - [`CONFIG_HW_SHADOW_STACK_MIN_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HW_SHADOW_STACK_MIN_SIZE)
  - [`CONFIG_HW_SHADOW_STACK_PERCENTAGE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HW_SHADOW_STACK_PERCENTAGE_SIZE)
  - `K_THREAD_HW_SHADOW_STACK_SIZE`
  - [`K_KERNEL_HW_SHADOW_STACK_DECLARE`](../thread_stack_reference/P001_线程栈接口.md#ga8df21c697e521dab1864065794edb3c7)
  - [`K_KERNEL_HW_SHADOW_STACK_ARRAY_DECLARE`](../thread_stack_reference/P001_线程栈接口.md#ga643f8cf646b57afc5d30979ade7fed09)
  - [`K_THREAD_HW_SHADOW_STACK_DEFINE`](../thread_stack_reference/P001_线程栈接口.md#ga16eed4de8bbcf2132f0947844c3874b8)
  - [`K_THREAD_HW_SHADOW_STACK_ARRAY_DEFINE`](../thread_stack_reference/P001_线程栈接口.md#gaec292361c5f7e59771fff901e1600c9c)
  - `K_THREAD_HW_SHADOW_STACK_ATTACH`
  - `k_thread_hw_shadow_stack_attach`
- 轻量多功能图形库（Light and Versatile Graphics Library，LVGL）


  - [`CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION)
  - [`CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION_NAME)
  - [`CONFIG_LV_Z_VDB_ZEPHYR_REGION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_VDB_ZEPHYR_REGION)
  - [`CONFIG_LV_Z_VDB_ZEPHYR_REGION_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_VDB_ZEPHYR_REGION_NAME)
- 日志（Logging）：


  - [`CONFIG_LOG_BACKEND_SWO_SYNC_PACKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_SWO_SYNC_PACKETS)
  - 新增日志后端省略时间戳及级别的选项。


    - [`CONFIG_LOG_BACKEND_SHOW_TIMESTAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_SHOW_TIMESTAMP)
    - [`CONFIG_LOG_BACKEND_SHOW_LEVEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_SHOW_LEVEL)
  - 新增限速日志宏（Rate-limited Logging Macros），避免高频消息淹没日志。


    - [LOG_ERR_RATELIMIT](../log_core_reference/P002_日志公共接口.md#ga139c2e364fe3b48d6819eabb53d0b3e6)：错误级别的限速日志宏（便捷形式）。
    - [LOG_WRN_RATELIMIT](../log_core_reference/P002_日志公共接口.md#ga35f1b201ad3a64b11ff4c4e5e1261c90)：警告级别的限速日志宏（便捷形式）。
    - [LOG_INF_RATELIMIT](../log_core_reference/P002_日志公共接口.md#gaedb160ea6d8d1cb2995220be20426792)：信息级别的限速日志宏（便捷形式）。
    - [LOG_DBG_RATELIMIT](../log_core_reference/P002_日志公共接口.md#ga5ebcc5529db8c780a410ccffcc1eeb9f)：调试级别的限速日志宏（便捷形式）。
    - [LOG_HEXDUMP_ERR_RATELIMIT](../log_core_reference/P002_日志公共接口.md#ga9142d42415a88d2527a828bae7ee7edf)：错误级别的限速十六进制转储宏（便捷形式）。
    - [LOG_HEXDUMP_WRN_RATELIMIT](../log_core_reference/P002_日志公共接口.md#gaea4da5c62175cc28c77b4fffa22fc0fb)：警告级别的限速十六进制转储宏（便捷形式）。
    - [LOG_HEXDUMP_INF_RATELIMIT](../log_core_reference/P002_日志公共接口.md#ga1de018ec3aceaac1e4e0c15c9bf95bb1)：信息级别的限速十六进制转储宏（便捷形式）。
    - [LOG_HEXDUMP_DBG_RATELIMIT](../log_core_reference/P002_日志公共接口.md#ga5f421b159c9cc2184af9554faaa380a1)：调试级别的限速十六进制转储宏（便捷形式）。
    - [LOG_ERR_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#gad589f7c4ec8993f3233c96e98c5f175c)：错误级别的限速日志宏（显式指定速率）。
    - [LOG_WRN_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#ga0c909fd16984756720ceec09e046db0c)：警告级别的限速日志宏（显式指定速率）。
    - [LOG_INF_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#ga1e825a958f88a242a37cac4476d3086a)：信息级别的限速日志宏（显式指定速率）。
    - [LOG_DBG_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#gad442e443db2bfca5a7c4d995c626c003)：调试级别的限速日志宏（显式指定速率）。
    - [LOG_HEXDUMP_ERR_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#ga172225ddfffaef58f0d75417924ce249)：错误级别的限速十六进制转储宏（显式指定速率）。
    - [LOG_HEXDUMP_WRN_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#gabdf159ae843cc556ce46cc4ca3f2d983)：警告级别的限速十六进制转储宏（显式指定速率）。
    - [LOG_HEXDUMP_INF_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#ga785e466dfd6c6ea167b2034912d323fe)：信息级别的限速十六进制转储宏（显式指定速率）。
    - [LOG_HEXDUMP_DBG_RATELIMIT_RATE](../log_core_reference/P002_日志公共接口.md#gaffa5cfd74b768f464b399050dd091368)：调试级别的限速十六进制转储宏（显式指定速率）。
- 管理（Management）


  - 设备更新服务（hawkBit）


    - [`CONFIG_HAWKBIT_REBOOT_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_REBOOT_NONE)
    - [`CONFIG_HAWKBIT_CONFIRM_IMG_ON_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_CONFIRM_IMG_ON_INIT)
    - [`CONFIG_HAWKBIT_ERASE_SECOND_SLOT_ON_CONFIRM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_ERASE_SECOND_SLOT_ON_CONFIRM)
  - 微控制器管理（MCUmgr）


    - [`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)
    - [`CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_SLOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_SLOT)
- 调制解调器（Modem）


  - [`CONFIG_MODEM_DEDICATED_WORKQUEUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_DEDICATED_WORKQUEUE)
- 非易失存储器（NVMEM）


  - 引入[非易失性存储器（Non-Volatile Memory，NVMEM）](https://docs.zephyrproject.org/latest/services/storage/nvmem/index.html#nvmem)子系统。


    - [`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)
    - [`CONFIG_NVMEM_EEPROM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM_EEPROM)
    - [`nvmem_cell`](../storage/P019_NVMEM数据单元结构.md)
    - [`nvmem_cell_read()`](../storage/P013_NVMEM接口参考.md#ga5db94733cecfd4b46dd87ee07128d58d)
    - [`nvmem_cell_write()`](../storage/P013_NVMEM接口参考.md#gaef749ffc4b49e2e37b489fab2d8fa6b4)
    - [`nvmem_cell_is_ready()`](../storage/P013_NVMEM接口参考.md#ga614cac8acc913cb2f7b62c2f0d625421)
    - [NVMEM_CELL_GET_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga6ba5137ac2ca250c769b32506d2eddae)及其变体。
    - [NVMEM_CELL_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga2d8ded7e090878d8dee0e2a4c3daac7b)及其变体。
- 网络（Networking）


  - 受限应用协议（CoAP）


    - [`coap_client_response_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__response__data.html)
    - [`coap_client_request.payload_cb`](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__client__request.html#a14e1036a45b1bcfa60faaa5b158b535a)
    - [`CONFIG_COAP_CLIENT_MAX_PATH_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MAX_PATH_LENGTH)
    - [`CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS)
  - 连接管理器（Connection Manager）


    - [`NET_EVENT_CONN_IF_IDLE_TIMEOUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#gaaab7f33dcc175b4c9117d6c69a0c84c8)
    - [`conn_mgr_if_set_idle_timeout()`](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga93f333199c87b2d7668e94c92efd31ce)
    - [`conn_mgr_if_get_idle_timeout()`](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga5d22b2a44c3595a5b7b240c8fe7d0db1)
    - [`conn_mgr_if_used()`](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga4079113088236aede697538d79e5272f)
  - 域名系统（DNS）


    - [`DNS_QUERY_TYPE_CNAME`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a128aa925168ae2b096ff879c7648d2e4)
    - [`DNS_QUERY_TYPE_TXT`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a42c3f3d5876b275f764a67e1bf43d850)
    - [`DNS_QUERY_TYPE_SRV`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gga7169c5a920fb1b0d77910a6ab922e3f0a2e976a8ed83e609b4836444d7a95d65d)
    - [`dns_resolve_enable_packet_forwarding()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3326e98da31313d33861565fe0a10bdf)
    - [`dns_resolve_remove_server_addresses()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf491764b213a891f296c9f91c35b1b72)
  - 超文本传输协议（HTTP）


    - [`CONFIG_HTTP_SERVER_STATIC_FS_RESPONSE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_STATIC_FS_RESPONSE_SIZE)
    - [`http_service_config`](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__service__config.html)
  - 互联网协议第6版（IPv6）


    - [`CONFIG_NET_IPV6_NS_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_NS_TIMEOUT)
    - [`net_ipv6_get_addr_mcast_scope()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga7fe843d70cbb04a6f4c022483346ad23)
  - 轻量级机器到机器协议（LwM2M）


    - [`lwm2m_cache_filter_cb_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a0bb9d5652f7f0fd0cc4a1139be6f37)
    - [`lwm2m_set_cache_filter()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e7da0353914601c3ec101415c2e110)
  - 传感器网络消息队列遥测传输协议（MQTT-SN）


    - [`mqtt_sn_predefine_topic()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#gadd0a809d7e451df55540fb7ea227fd50)
    - [`mqtt_sn_update_will_topic()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga90ced79565deb9a92be8cd3a99d808b7)
    - [`mqtt_sn_update_will_message()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga0850d89af7dd6b5d3ec2b1e1abe01d19)
    - [`mqtt_sn_define_short_topic()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mqtt__sn__socket.html#ga1a6b39984ef047f0089cea43f5378d0f)
  - 其他（Misc）


    - [`CONFIG_NET_LATMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON)
    - [`CONFIG_NETMIDI2_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETMIDI2_HOST)
    - [`CONFIG_OCPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OCPP)
    - [`npf_rule.priority`](https://docs.zephyrproject.org/latest/doxygen/html/structnpf__rule.html#a3691e7be04a2948f0c979305f48fbb2c)
    - [`NPF_PRIORITY`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt__filter.html#ga3b740a5ca1ad99aa593bfa30a39c41f2)
    - [`CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC)
    - [`ppp_peer_async_control_character_map()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ppp.html#ga716727874cecc8ee358da6c76adedc0a)
  - OpenThread协议栈


    - [`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)
    - [`CONFIG_OPENTHREAD_BORDER_ROUTING_DHCP6_PD_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_BORDER_ROUTING_DHCP6_PD_CLIENT)
    - [`CONFIG_OPENTHREAD_CHANNEL_MONITOR_AUTO_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_CHANNEL_MONITOR_AUTO_START)
    - [`CONFIG_OPENTHREAD_MAC_BEACON_PAYLOAD_PARSING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MAC_BEACON_PAYLOAD_PARSING)
    - [`CONFIG_OPENTHREAD_MULTIPLE_INSTANCE_NUM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MULTIPLE_INSTANCE_NUM)
    - [`CONFIG_OPENTHREAD_PLATFORM_RADIO_COEX_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_PLATFORM_RADIO_COEX_ENABLE)
    - [`CONFIG_OPENTHREAD_PLATFORM_USEC_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_PLATFORM_USEC_TIMER)
    - [`CONFIG_OPENTHREAD_RCP_RESTORATION_MAX_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_RCP_RESTORATION_MAX_COUNT)
    - [`CONFIG_OPENTHREAD_SRP_SERVER_FAST_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SRP_SERVER_FAST_START)
    - [`CONFIG_OPENTHREAD_TREL_MANAGE_DNSSD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_TREL_MANAGE_DNSSD)
  - 套接字（Sockets）


    - [zsock_listen()](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html#gae8ea59ea82063aa28a9b72da2f08c9fd)现在支持backlog参数，TCP服务器套接字会将等待处理的入站连接数量限制在该值以内。
    - `IP_RECVTTL`
    - `IPV6_PKTINFO`
    - `IPV6_RECVHOPLIMIT`
    - `IPV6_HOPLIMIT`
  - 无线局域网（Wi-Fi）


    - [`CONFIG_WIFI_NM_WPA_SUPPLICANT_DEBUG_SHOW_KEYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_DEBUG_SHOW_KEYS)
    - 由于证书验证被禁用，将企业级密码配置标记为不安全（Insecure）。
    - 若使用模式选项启用接入点（AP），则自动启用AP模式。
    - 为wpa_supplicant新增后台扫描（Background Scanning，bgscan）配置选项。
    - 新增多个虚拟接口（Virtual Interfaces，VIF）支持。
- Newlib C库


  - [`CONFIG_NEWLIB_LIBC_USE_POSIX_LIMITS_H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NEWLIB_LIBC_USE_POSIX_LIMITS_H)
- 运算放大器（Opamp）


  - 引入通过[CONFIG_OPAMP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPAMP)选择的运算放大器（Op-amp）设备驱动API，支持通过设备树初始配置，并通过厂商专用API运行时配置。
  - 新增NXP OPAMP（[nxp,opamp](../hardware/P732_NXP运算放大器绑定.md#dtbinding-nxp-opamp)）支持。
  - 新增NXP OPAMP_FAST（nxp,opamp_fast）支持。
- 电源管理（Power Management）

  > - [`pm_device_driver_deinit()`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gadf145eb83c32eac741ab08fb7b262a55)
  > - [`CONFIG_PM_DEVICE_RUNTIME_DEFAULT_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_DEFAULT_ENABLE)
  > - [CONFIG_PM_S2RAM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_S2RAM)重构为无用户提示（Promptless）的选项。应用现在只需在设备树中启用任意suspend-to-ram电源状态。
  > - PM_S2RAM_CUSTOM_MARKING重命名为HAS_PM_S2RAM_CUSTOM_MARKING，并改为无用户提示的选项。SoC若在挂起到RAM（Suspend-to-RAM）实现中需要该功能，现在由SoC选择此项。
- 设置（Settings）

  > - `CONFIG_SETTINGS_TFM_ITS`
- 命令行（Shell）

  > - MQTT后端（Backend）
  >
  >   > - [`CONFIG_SHELL_MQTT_TOPIC_RX_ID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_MQTT_TOPIC_RX_ID)
  >   > - [`CONFIG_SHELL_MQTT_TOPIC_TX_ID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_MQTT_TOPIC_TX_ID)
  >   > - [`CONFIG_SHELL_MQTT_CONNECT_TIMEOUT_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_MQTT_CONNECT_TIMEOUT_MS)
  >   > - [`CONFIG_SHELL_MQTT_WORK_DELAY_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_MQTT_WORK_DELAY_MS)
  >   > - [`CONFIG_SHELL_MQTT_LISTEN_TIMEOUT_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_MQTT_LISTEN_TIMEOUT_MS)
- 状态机框架（State Machine Framework）


  - [`smf_get_current_leaf_state()`](../smf/P005_状态机API参考.md#gabbb84eb59e5991b1ab51840f08a6a13f)
  - [`smf_get_current_executing_state()`](../smf/P005_状态机API参考.md#gae74fa0c5be2756cee5e1112a5c7b6da8)
- 存储（Storage）

  > - [`CONFIG_FILE_SYSTEM_SHELL_LS_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM_SHELL_LS_SIZE)
- 系统功能（Sys）


  - [`sys_count_bits()`](../util_reference/P001_通用工具公共接口.md#ga20319acca384077a5292543f22881365)
- 任务看门狗（Task Watchdog）


  - [`CONFIG_TASK_WDT_DUMMY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TASK_WDT_DUMMY)
- 工具链（Toolchain）


  - `__deprecated_version`
- 通用串行总线（USB）


  - 视频（Video）


    - `uvc_add_format()`
- 视频（Video）


  - [video_format.size](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__format.html#a42a2dfacc89f692c36c448b3ea297a90)字段。
  - [`video_estimate_fmt_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga774ef89a7321a6842890005ad53c1594)
  - [`video_transfer_buffer()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga4d3c1458b8c30cff9ac5e6a62d6391c9)

<a id="new-boards"></a>

<a id="boards-added-in-zephyr-4-3"></a>

## 新增开发板（New Boards）


- Adafruit Industries, LLC

  > - [Feather RP2040 Adalogger](../boards_adafruit_feather_esp32_rp2040/P001_Feather_RP2040_Adalogger.md#adafruit_feather_adalogger_rp2040)开发板（adafruit_feather_adalogger_rp2040）
  > - Feather RP2040 CAN总线开发板（adafruit_feather_canbus_rp2040）（[Feather RP2040 CAN总线（CAN Bus）](../boards_adafruit_feather_esp32_rp2040/P002_Feather_RP2040_CAN_bus.md#adafruit_feather_canbus_rp2040)）
  > - [Adafruit Feather ESP32](../boards_adafruit_feather_esp32_rp2040/P003_Adafruit_Feather_ESP32.md#adafruit_feather_esp32)开发板（adafruit_feather_esp32）
  > - [Feather RP2040 RFM95 Lora](../boards_adafruit_feather_and_grand_central/P006_Feather_RP2040_RFM95_Lora.md#adafruit_feather_rfm95_rp2040)开发板（adafruit_feather_rfm95_rp2040）
  > - [Feather RP2040](../boards_adafruit_feather_and_grand_central/P007_Feather_RP2040.md#adafruit_feather_rp2040)开发板（adafruit_feather_rp2040）
  > - [Itsybitsy RP2040](../boards_adafruit_itsybitsy_metro_qt_trinkey/P004_Itsybitsy_RP2040.md#adafruit_itsybitsy_rp2040)开发板（adafruit_itsybitsy_rp2040）
  > - [Metro RP2040](../boards_adafruit_itsybitsy_metro_qt_trinkey/P007_Metro_RP2040.md#adafruit_metro_rp2040)开发板（adafruit_metro_rp2040）
  > - [Adafruit Metro RP2350](../boards_adafruit_itsybitsy_metro_qt_trinkey/P008_Adafruit_Metro_RP2350.md#adafruit_metro_rp2350)开发板（adafruit_metro_rp2350）
  > - [Trinkey QT2040](../boards_adafruit_itsybitsy_metro_qt_trinkey/P013_Trinkey_QT2040.md#adafruit_trinkey_qt2040)开发板（adafruit_trinkey_qt2040）
- Advanced Micro Devices（AMD）, Inc.

  > - Versal Net APU 开发板（Development Board）（versalnet_apu）（[Versal Net应用处理单元开发板（APU Development Board）](../boards_amd/P010_Versal_Net_APU_Development_Board.md#versalnet_apu)）
- 安信可（Ai-Thinker Co., Ltd.）

  > - Ai-Thinker M62-12F 开发板（Development Board）（ai_m62_12f_kit）（[安信可Ai-Thinker M62-12F开发板（Development Board）](../boards_aesc_aithinker_alientek/P005_Ai-Thinker_M62-12F_development_board.md#ai_m62_12f_kit)）
  > - [Ai-Thinker ESP32-CAM](../boards_aesc_aithinker_alientek/P009_Ai-Thinker_ESP32-CAM.md#esp32_cam)开发板（esp32_cam）
- Ambiq Micro, Inc.

  > - [Apollo2 EVB](../boards_alif_ambiq/P008_Apollo2_EVB.md#apollo2_evb)开发板（apollo2_evb）
- Analog Devices, Inc.

  > - [MAX32658EVKIT](../boards_adi_max32_max78_sdp/P007_MAX32658EVKIT.md#max32658evkit)开发板（max32658evkit）
- Arduino

  > - [Arduino UNO Q](../boards_arduino/P016_Arduino_UNO_Q.md#arduino_uno_q)开发板（arduino_uno_q）
- Core Devices LLC公司

  > - [Pebble 2 Duo](../boards_cdac_to_cthings/P013_Pebble_2_Duo.md#p2d)开发板（p2d）
  > - [Pebble Time 2](../boards_cdac_to_cthings/P015_Pebble_Time_2.md#pt2)开发板（pt2）
- DFRobot

  > - [DFRobot Beetle RP2040](../boards_cypress_to_dragino/P009_DFRobot_Beetle_RP2040.md#beetle_rp2040)开发板（beetle_rp2040）
- Doctors of Intelligence & Technology

  > - XT-ZB1 Zigbee 3.0 and BLE 5.0 共存模块开发套件（Coexistence Module Development Kit）（dt_xt_zb1_devkit）（[XT-ZB1 Zigbee 3.0与BLE 5.0共存模块开发套件（Coexistence Module Development Kit）](../boards_cypress_to_dragino/P019_XT-ZB1_Zigbee_3.0_and_BLE_5.0_Coexistence_Module_Development_Kit.md#dt_xt_zb1_devkit)）
- Egis Technology Inc公司

  > - ET171 开发板（Development Board）（egis_et171）（[ET171开发板（Development Board）](../boards_ebyte_to_enjoydigital/P007_ET171_Development_Board.md#egis_et171)）
- 乐鑫信息科技（Espressif Systems）

  > - [ESP32-H2-DevKitM](../boards_espressif/P024_ESP32-H2-DevKitM.md#esp32h2_devkitm)开发板（esp32h2_devkitm）
- FANKE Technology Co., Ltd.（反客科技）

  > - [FK723M1-ZGT6](../boards_fanke_to_gardena/P001_FK723M1-ZGT6.md#fk723m1_zgt6)开发板（fk723m1_zgt6）
- Firefly

  > - ROC-RK3588-PC (四核Cortex-A55)开发板（roc_rk3588_pc）（[ROC-RK3588-PC（四核Cortex-A55，标题按原文保留）](../boards_fanke_to_gardena/P008_ROC-RK3588-PC_Quad-core_Cortex-A55.md#roc_rk3588_pc)）
- FoBE Studio

  > - [Quill nRF52840 Mesh](../boards_fanke_to_gardena/P012_Quill_nRF52840_Mesh.md#quill_nrf52840_mesh)开发板（quill_nrf52840_mesh）
- 广东天嵌科技（Guangdong Embedsky Technology Co., Ltd.）

  > - [TQ H503A](../boards_ebyte_to_enjoydigital/P017_TQ_H503A.md#tq_h503a)开发板（tq_h503a）
- 英飞凌科技（Infineon Technologies）

  > - PSOC™ Control C3M5 评估套件（Evaluation Kit）（kit_psc3m5_evk）（[PSOC Control C3M5评估套件（Evaluation Kit）](../boards_infineon_innblue/P012_PSOC_Control_C3M5_Evaluation_Kit.md#kit_psc3m5_evk)）
  > - PSOC™ Edge E84 AI 评估套件（Evaluation Kit）（kit_pse84_ai）（[PSOC Edge E84 AI评估套件（AI Evaluation Kit）](../boards_infineon_innblue/P014_PSOC_Edge_E84_AI_Evaluation_Kit.md#kit_pse84_ai)）
  > - PSOC™ Edge E84 评估套件（Evaluation Kit）（kit_pse84_eval）（[PSOC Edge E84评估套件（Evaluation Kit）](../boards_infineon_innblue/P015_PSOC_Edge_E84_Evaluation_Kit.md#kit_pse84_eval)）
- 英特尔公司（Intel Corporation）

  > - [Panther Lake H CRB](../boards_intel_ite/P016_Panther_Lake_H_CRB.md#intel_ptl_h_crb)开发板（intel_ptl_h_crb）
- 微芯科技（Microchip Technology Inc.）

  > - PIC32CM JH01 Curiosity Nano+ 触摸（Touch） 评估套件（Evaluation Kit）（pic32cm_jh01_cnano）（[PIC32CM JH01 Curiosity Nano+ Touch评估套件](../boards_microchip/P017_PIC32CM_JH01_Curiosity_Nano_Touch_Evaluation_Kit.md#pic32cm_jh01_cnano)）
  > - [PIC32CM JH01 Curiosity Pro](../boards_microchip/P018_PIC32CM_JH01_Curiosity_Pro.md#pic32cm_jh01_cpro)开发板（pic32cm_jh01_cpro）
  > - [PIC32CX SG61 Curiosity Ultra](../boards_microchip/P022_PIC32CX_SG61_Curiosity_Ultra.md#pic32cx_sg61_cult)开发板（pic32cx_sg61_cult）
  > - [PIC32CZ CA80 Curiosity Ultra](../boards_microchip/P023_PIC32CZ_CA80_Curiosity_Ultra.md#pic32cz_ca80_cult)开发板（pic32cz_ca80_cult）
  > - [SAM E54 Xplained Pro](../boards_microchip/P027_SAM_E54_Xplained_Pro.md#sam_e54_xpro)开发板（sam_e54_xpro）
  > - [SAMA7D65 Curiosity Kit](../boards_microchip/P029_SAMA7D65_Curiosity_Kit.md#sama7d65_curiosity)开发板（sama7d65_curiosity）
- 新唐科技（Nuvoton Technology Corporation）

  > - [NUMAKER M3334KI](../boards_norik_to_nuvoton/P017_NUMAKER_M3334KI.md#numaker_m3334ki)开发板（numaker_m3334ki）
  > - [NUMAKER M5531](../boards_norik_to_nuvoton/P019_NUMAKER_M5531.md#numaker_m5531)开发板（numaker_m5531）
- 恩智浦半导体（NXP Semiconductors）

  > - [FRDM-IMX91](../boards_nxp_frdm_imx_kinetis/P001_FRDM-IMX91.md#frdm_imx91)开发板（frdm_imx91）
  > - [FRDM-IMX93](../boards_nxp_frdm_imx_kinetis/P002_FRDM-IMX93.md#frdm_imx93)开发板（frdm_imx93）
  > - [FRDM-K32L2B3](../boards_nxp_frdm_imx_kinetis/P007_FRDM-K32L2B3.md#frdm_k32l2b3)开发板（frdm_k32l2b3）
  > - [FRDM-MCXA344](../boards_nxp_frdm_mcx_rw/P003_FRDM-MCXA344.md#frdm_mcxa344)开发板（frdm_mcxa344）
  > - [FRDM-MCXA266](../boards_nxp_frdm_mcx_rw/P005_FRDM-MCXA266.md#frdm_mcxa266)开发板（frdm_mcxa266）
  > - [FRDM-MCXA346](../boards_nxp_frdm_mcx_rw/P006_FRDM-MCXA346.md#frdm_mcxa346)开发板（frdm_mcxa346）
  > - [FRDM-MCXA366](../boards_nxp_frdm_mcx_rw/P007_FRDM-MCXA366.md#frdm_mcxa366)开发板（frdm_mcxa366）
  > - [FRDM-MCXE247](../boards_nxp_frdm_mcx_rw/P010_FRDM-MCXE247.md#frdm_mcxe247)开发板（frdm_mcxe247）
  > - [FRDM-MCXE31B](../boards_nxp_frdm_mcx_rw/P011_FRDM-MCXE31B.md#frdm_mcxe31b)开发板（frdm_mcxe31b）
  > - [FRDM-MCXW23](../boards_nxp_frdm_mcx_rw/P015_FRDM-MCXW23.md#frdm_mcxw23)开发板（frdm_mcxw23）
  > - [i.MX91 QSB](../boards_nxp_imx_evk/P006_i.MX91_QSB.md#imx91_qsb)开发板（imx91_qsb）
  > - [i.MX95 15x15 EVK](../boards_nxp_imx_evk/P011_i.MX95_15x15_EVK.md#imx95_evk_15x15)开发板（imx95_evk_15x15）
  > - [MCX-N9XX-EVK](../boards_nxp_remaining/P003_MCX-N9XX-EVK.md#mcx_n9xx_evk)开发板（mcx_n9xx_evk）
  > - [MCX-N5XX-EVK](../boards_nxp_remaining/P002_MCX-N5XX-EVK.md#mcx_n5xx_evk)开发板（mcx_n5xx_evk）
  > - [MCXW23-EVK](../boards_nxp_remaining/P004_MCXW23-EVK.md#mcxw23_evk)开发板（mcxw23_evk）
- 松下（Panasonic Corporation）

  > - PAN B611 评估板（Evaluation Board）（panb611evb）（[PAN B611评估板](../boards_panasonic_particle_pcbcupid_peregrine/P007_PAN_B611_Evaluation_Board.md#panb611evb)）
- PCB Cupid

  > - [Glyph-C6](../boards_panasonic_particle_pcbcupid_peregrine/P015_Glyph-C6.md#glyph_c6)开发板（glyph_c6）
- RAKwireless Technology Limited

  > - [RAK3112](../boards_rak_raspberry_raytac/P004_RAK3112.md#rak3112)开发板（rak3112）
- Raspberry Pi基金会（Foundation）

  > - Raspberry Pi 调试探针（Debug Probe）（rpi_debug_probe）（[Raspberry Pi调试探针（Debug Probe）](../boards_rak_raspberry_raytac/P011_Raspberry_Pi_Debug_Probe.md#rpi_debug_probe)）
- 瑞萨电子（Renesas Electronics Corporation）

  > - RA4C1 评估套件（Evaluation Kit）（ek_ra4c1）（[RA4C1评估套件](../boards_renesas_ra/P007_RA4C1_Evaluation_Kit.md#ek_ra4c1)）
  > - RA8D2 评估套件（Evaluation Kit）（ek_ra8d2）（[RA8D2评估套件](../boards_renesas_ra/P021_RA8D2_Evaluation_Kit.md#ek_ra8d2)）
  > - RA8M2 评估套件（Evaluation Kit）（ek_ra8m2）（[RA8M2评估套件](../boards_renesas_ra/P023_RA8M2_Evaluation_Kit.md#ek_ra8m2)）
  > - RX261 评估套件（Evaluation Kit）（ek_rx261）（[RX261评估套件（Evaluation Kit）](../boards_renesas_rx_rz/P001_RX261_Evaluation_Kit.md#ek_rx261)）
  > - RX261 快速原型板（Fast Prototyping Board）（fpb_rx261）（[RX261快速原型板](../boards_renesas_rx_rz/P011_RX261_Fast_Prototyping_Board.md#fpb_rx261)）
  > - RX26T 电机控制板（Motor Control Board）（mcb_rx26t）（[RX26T电机控制板](../boards_renesas_rx_rz/P014_RX26T_Motor_Control_Board.md#mcb_rx26t)）
  > - RA8T2 电机控制套件（Motor Control Kit）（mck_ra8t2）（[RA8T2电机控制套件](../boards_renesas_rx_rz/P017_RA8T2_Motor_Control_Kit.md#mck_ra8t2)）
  > - [RA2L1电容触摸评估系统（Capacitive Touch Evaluation System）](../boards_renesas_rx_rz/P023_Capacitive_Touch_Evaluation_System_for_RA2L1.md#rssk_ra2l1)（rssk_ra2l1）
- Seeed Technology Co., Ltd

  > - Wio-WM1110 开发套件（Dev Kit）（wio_wm1110_dev_kit）（[Wio-WM1110开发套件（Dev Kit）](../boards_seeed/P010_Wio-WM1110_Dev_Kit.md#wio_wm1110_dev_kit)）
  > - [XIAO NRF54L15](../boards_seeed/P017_XIAO_NRF54L15.md#xiao_nrf54l15)开发板（xiao_nrf54l15）
- 上海睿赛德电子科技有限公司（Shanghai Ruiside Electronic Technology Co., Ltd.）

  > - [ART-Pi](../boards_realtek_ruiside_sifive/P010_ART-Pi.md#art_pi)开发板（art_pi）
- Shenzhen Holyiot Technology Co., Ltd.

  > - [YJ-17095](../boards_gd_to_iar/P036_YJ-17095.md#holyiot_yj17095)开发板（holyiot_yj17095）
- 思澈科技（南京）有限公司（SiFli Technologies (Nanjing) Co., Ltd）

  > - [SF32LB52-DevKit-LCD](../boards_retronix_sifli/P026_SF32LB52-DevKit-LCD.md#sf32lb52_devkit_lcd)开发板（sf32lb52_devkit_lcd）
- 芯科科技（Silicon Laboratories）

  > - BGM220 探索套件（Explorer Kit） (BGM220-EK4314A)（bgm220_ek4314a）（[BGM220探索套件，BGM220-EK4314A](../boards_silabs/P016_BGM220_Explorer_Kit_BGM220-EK4314A.md#bgm220_ek4314a)）
  > - EFM32PG23 专业套件（Pro Kit） (PG23-PK2504A)（pg23_pk2504a）（[EFM32PG23专业套件（Pro Kit），PG23-PK2504A](../boards_silabs/P002_EFM32PG23_Pro_Kit_PG23-PK2504A.md#pg23_pk2504a)）
  > - EFM32PG28 专业套件（Pro Kit） (PG28-PK2506A)（pg28_pk2506a）（[EFM32PG28专业套件，PG28-PK2506A](../boards_silabs/P003_EFM32PG28_Pro_Kit_PG28-PK2506A.md#pg28_pk2506a)）
  > - SiWx917 Wi-Fi 6 and 低功耗蓝牙（Bluetooth LE） SoC 开发套件（Dev Kit） (BRD2605A)（siwx917_dk2605a）（[SiWx917 Wi-Fi 6与低功耗蓝牙SoC开发套件，BRD2605A](../boards_silabs/P005_SiWx917_Wi-Fi_6_and_Bluetooth_LE_SoC_Dev_Kit_BRD2605A.md#siwx917_dk2605a)）
  > - EFR32BG22 探索套件（Explorer Kit） (BG22-EK4108A)（bg22_ek4108a）（[EFR32BG22探索套件，BG22-EK4108A](../boards_silabs/P015_EFR32BG22_Explorer_Kit_BG22-EK4108A.md#bg22_ek4108a)）
  > - EFR32xG22E 探索套件（Explorer Kit） (xG22-EK2710A)（xg22_ek2710a）（[EFR32xG22E探索套件，xG22-EK2710A](../boards_silabs/P017_EFR32xG22E_Explorer_Kit_xG22-EK2710A.md#xg22_ek2710a)）
  > - xGM260P 探索套件（Explorer Kit） (MGM260P-EK2713A)（mgm260p_ek2713a）（[xGM260P探索套件，MGM260P-EK2713A](../boards_silabs/P018_xGM260P_Explorer_Kit_MGM260P-EK2713A.md#mgm260p_ek2713a)）
  > - EFM32PG26 探索套件（Explorer Kit） (PG26-EK2711A)（pg26_ek2711a）（[EFM32PG26探索套件，PG26-EK2711A](../boards_silabs/P019_EFM32PG26_Explorer_Kit_PG26-EK2711A.md#pg26_ek2711a)）
  > - EFR32xG26 探索套件（Explorer Kit） (xG26-EK2709A)（xg26_ek2709a）（[EFR32xG26探索套件，xG26-EK2709A](../boards_silabs/P020_EFR32xG26_Explorer_Kit_xG26-EK2709A.md#xg26_ek2709a)）
  > - EFR32BG29 低功耗蓝牙（Bluetooth LE） 4 dBm DCDC升压（Boost） WLCSP (BG29-RB4420A)开发板（bg29_rb4420a）（[EFR32BG29低功耗蓝牙4 dBm升压DC-DC、WLCSP无线电板，BG29-RB4420A](../boards_silabs/P058_EFR32BG29_Bluetooth_LE_4_dBm_DCDC_Boost_WLCSP_BG29-RB4420A.md#bg29_rb4420a)）
  > - EFR32xG22 2.4 GHz +6 dBm 无线电板（Radio Board）（slwrb4182a）（[EFR32xG22 2.4 GHz +6 dBm无线电板](../boards_silabs/P039_EFR32xG22_2.4_GHz_6_dBm_Radio_Board.md#slwrb4182a)）
  > - BGM220P 蓝牙模块（Bluetooth Module） 2.4 GHz +8 dBm 无线电板（Radio Board）（slwrb4311a）（[BGM220P蓝牙模块2.4 GHz +8 dBm无线电板](../boards_silabs/P040_BGM220P_Bluetooth_Module_2.4_GHz_8_dBm_Radio_Board.md#slwrb4311a)）
  > - [EFR32xG24 2.4 GHz 10 dBm (xG24-RB4186C)](../boards_silabs/P043_EFR32xG24_2.4_GHz_10_dBm_xG24-RB4186C.md#xg24_rb4186c)开发板（xg24_rb4186c）
  > - [EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C)](../boards_silabs/P044_EFR32xG24_2.4_GHz_20_dBm_xG24-RB4187C.md#xg24_rb4187c)开发板（xg24_rb4187c）
  > - xGM240P 10 dBm 模块无线电板（Module Radio Board） (xGM240-RB4316A)（xgm240_rb4316a）（[xGM240P 10 dBm模块无线电板，xGM240-RB4316A](../boards_silabs/P046_xGM240P_10_dBm_Module_Radio_Board_xGM240-RB4316A.md#xgm240_rb4316a)）
  > - xGM240P 20 dBm 模块无线电板（Module Radio Board） (xGM240-RB4317A)（xgm240_rb4317a）（[xGM240P 20 dBm模块无线电板，xGM240-RB4317A](../boards_silabs/P047_xGM240P_20_dBm_Module_Radio_Board_xGM240-RB4317A.md#xgm240_rb4317a)）
  > - MGM260P 2.4 GHz +10 dBm 无线电板（Radio Board）（mgm260p_rb4350a）（[MGM260P 2.4 GHz +10 dBm无线电板](../boards_silabs/P049_MGM260P_2.4_GHz_10_dBm_Radio_Board.md#mgm260p_rb4350a)）
  > - EFR32xG26 2.4 GHz +10 dBm BGA136 无线电板（Radio Board）（xg26_rb4118a）（[EFR32xG26 2.4 GHz +10 dBm BGA136无线电板](../boards_silabs/P051_EFR32xG26_2.4_GHz_10_dBm_BGA136_Radio_Board.md#xg26_rb4118a)）
  > - EFR32xG26 2.4 GHz +10 dBm 无线电板（Radio Board）（xg26_rb4120a）（[EFR32xG26 2.4 GHz +10 dBm无线电板](../boards_silabs/P052_EFR32xG26_2.4_GHz_10_dBm_Radio_Board.md#xg26_rb4120a)）
  > - EFR32BG27 2.4 GHz 4 dBm DCDC降压（Buck） CSP (BG27-RB4110B)开发板（bg27_rb4110b）（[EFR32BG27 2.4 GHz 4 dBm降压DC-DC、CSP无线电板，BG27-RB4110B](../boards_silabs/P054_EFR32BG27_2.4_GHz_4_dBm_DCDC_Buck_CSP_BG27-RB4110B.md#bg27_rb4110b)）
  > - EFR32BG27 2.4 GHz 4 dBm DCDC升压（Boost） CSP (BG27-RB4111B)开发板（bg27_rb4111b）（[EFR32BG27 2.4 GHz 4 dBm升压DC-DC、CSP无线电板，BG27-RB4111B](../boards_silabs/P055_EFR32BG27_2.4_GHz_4_dBm_DCDC_Boost_CSP_BG27-RB4111B.md#bg27_rb4111b)）
  > - [EFR32xG27 2.4 GHz 8 dBm (xG27-RB4194A)](../boards_silabs/P056_EFR32xG27_2.4_GHz_8_dBm_xG27-RB4194A.md#xg27_rb4194a)开发板（xg27_rb4194a）
  > - [EFR32xG28 868-915 MHz 20 dBm (xG28-RB4401C)](../boards_silabs/P057_EFR32xG28_868-915_MHz_20_dBm_xG28-RB4401C.md#xg28_rb4401c)开发板（xg28_rb4401c）
- SparkFun Electronics

  > - [Sparkfun SAMD21 Dev Breakout](../boards_sipeed_sparkfun/P023_Sparkfun_SAMD21_Dev_Breakout.md#sparkfun_samd21_breakout)开发板（sparkfun_samd21_breakout）
- SteelSeries

  > - [Apex Pro Mini](../boards_starfive_trenz/P003_Apex_Pro_Mini.md#apex_pro_mini)开发板（apex_pro_mini）
- 意法半导体（STMicroelectronics）

  > - [Nucleo C092RC开发板](../boards_st_nucleo/P003_Nucleo_C092RC.md#nucleo_c092rc)（nucleo_c092rc）
  > - STM32MP257F-DK 探索套件（Discovery Kit）（stm32mp257f_dk）（[STM32MP257F-DK探索套件（Discovery Kit）](../boards_st_discovery_eval/P050_STM32MP257F-DK_Discovery_Kit.md#stm32mp257f_dk)）
  > - STM32WBA65I 探索套件（Discovery Kit）（stm32wba65i_dk1）（[STM32WBA65I探索套件（Discovery Kit）](../boards_st_discovery_eval/P060_STM32WBA65I_Discovery_kit.md#stm32wba65i_dk1)）
- 德州仪器（Texas Instruments）

  > - [MSPM0G3519 Launchpad](../boards_ti/P019_MSPM0G3519_Launchpad.md#lp_mspm0g3519)开发板（lp_mspm0g3519）
  > - [MSPM0L2228 Launchpad](../boards_ti/P020_MSPM0L2228_Launchpad.md#lp_mspm0l2228)开发板（lp_mspm0l2228）
- Toradex AG

  > - [Verdin AM62](../boards_starfive_trenz/P019_Verdin_AM62.md#verdin_am62)开发板（verdin_am62）
- Waveshare Electronics微雪电子

  > - [RP2040-GEEK](../boards_waveshare_tail/P015_RP2040-GEEK.md#rp2040_geek)开发板（rp2040_geek）
  > - [RP2040-Keyboard-3](../boards_waveshare_tail/P016_RP2040-Keyboard-3.md#rp2040_keyboard_3)开发板（rp2040_keyboard_3）
  > - [RP2040-Matrix](../boards_waveshare_tail/P017_RP2040-Matrix.md#rp2040_matrix)开发板（rp2040_matrix）
- WeAct Studio

  > - [Black Pill STM32H523](../boards_weact/P004_Black_Pill_STM32H523.md#blackpill_h523ce)开发板（blackpill_h523ce）
  > - [Black Pill STM32U585](../boards_weact/P005_Black_Pill_STM32U585.md#blackpill_u585ci)开发板（blackpill_u585ci）
  > - [ESP32-C3-Mini](../boards_weact/P009_ESP32-C3-Mini.md#weact_esp32c3_mini)开发板（weact_esp32c3_mini）
  > - [ESP32-C6-Mini](../boards_weact/P010_ESP32-C6-Mini.md#weact_esp32c6_mini)开发板（weact_esp32c6_mini）
  > - [ESP32-S3-Mini](../boards_weact/P012_ESP32-S3-Mini.md#weact_esp32s3_mini)开发板（weact_esp32s3_mini）
  > - STM32G030 核心板（Core Board） 1.0（weact_stm32g030_core）（[STM32G030核心板1.0](../boards_weact/P021_STM32G030_Core_Board_1.0.md#weact_stm32g030_core)）
  > - STM32WB55 核心板（Core Board） V1.0（weact_stm32wb55_core）（[STM32WB55核心板V1.0](../boards_weact/P025_STM32WB55_Core_Board_V1.0.md#weact_stm32wb55_core)）
  > - [ESP32-S3-B](../boards_weact/P011_ESP32-S3-B.md#weact_esp32s3_b)开发板（weact_esp32s3_b）

<a id="new-shields"></a>

<a id="shields-added-in-zephyr-4-3"></a>

## 新增扩展板（New Shields）

> - [Adafruit 24LC32 EEPROM扩展板（Shield）](../boards_shields/P003_Adafruit_24LC32_EEPROM_Shield.md#adafruit-24lc32)
> - [Adafruit AHT20扩展板（Shield）](../boards_shields/P008_Adafruit_AHT20_Shield.md#adafruit-aht20)
> - [Adafruit APDS9960扩展板（Shield）](../boards_shields/P009_Adafruit_APDS9960_Shield.md#adafruit-apds9960)
> - [Adafruit DPS310扩展板（Shield）](../boards_shields/P012_Adafruit_DPS310_Shield.md#adafruit-dps310)
> - [Adafruit DRV2605L扩展板（Shield）](../boards_shields/P013_Adafruit_DRV2605L_Shield.md#adafruit-drv2605l)
> - [Adafruit FeatherWing 128×32 OLED扩展板（Shield）](../boards_shields/P015_Adafruit_FeatherWing_128x32_OLED_Shield.md#adafruit-featherwing-128x32-oled)
> - [Adafruit HT16K33 LED矩阵扩展板（LED Matrix Shield）](../boards_shields/P018_Adafruit_HT16K33_LED_Matrix_Shield.md#adafruit-ht16k33)
> - [Adafruit I2C转8通道电磁阀驱动扩展板（Solenoid Driver Shield）](../boards_shields/P005_Adafruit_I2C_to_8_Channel_Solenoid_Driver_Shield.md#adafruit-8chan-solenoid)
> - [Adafruit INA219扩展板（Shield）](../boards_shields/P020_Adafruit_INA219_Shield.md#adafruit-ina219)
> - [Adafruit INA237扩展板（Shield）](../boards_shields/P022_Adafruit_INA237_Shield.md#adafruit-ina237)
> - [Adafruit LIS2MDL扩展板（Shield）](../boards_shields/P025_Adafruit_LIS2MDL_Shield.md#adafruit-lis2mdl)
> - [Adafruit LIS3DH扩展板（Shield）](../boards_shields/P026_Adafruit_LIS3DH_Shield.md#adafruit-lis3dh)
> - [Adafruit LTR-329扩展板（Shield）](../boards_shields/P029_Adafruit_LTR-329_Shield.md#adafruit-ltr329)
> - [Adafruit MCP9808扩展板（Shield）](../boards_shields/P032_Adafruit_MCP9808_Shield.md#adafruit-mcp9808)
> - [Adafruit PCF8523扩展板（Shield）](../boards_shields/P035_Adafruit_PCF8523_Shield.md#adafruit-pcf8523)
> - [Adafruit TSL2591扩展板（Shield）](../boards_shields/P037_Adafruit_TSL2591_Shield.md#adafruit-tsl2591)
> - [Adafruit VCNL4040扩展板（Shield）](../boards_shields/P038_Adafruit_VCNL4040_Shield.md#adafruit-vcnl4040)
> - [Adafruit VEML7700扩展板（Shield）](../boards_shields/P039_Adafruit_VEML7700_Shield.md#adafruit-veml7700)
> - [ArduCam CU450 OV5640摄像头模块（Camera Module）](../boards_shields/P044_ArduCam_CU450_OV5640_Camera_Module.md#arducam-cu450-ov5640)
> - [Arduino Modulino运动模块（Movement）](../boards_shields/P049_Arduino_Modulino_Movement.md#arduino-modulino-movement)
> - [Arduino Modulino温湿度模块（Thermo）](../boards_shields/P051_Arduino_Modulino_Thermo.md#arduino-modulino-thermo)
> - [MikroElektronika 3D Hall 3 Click三维霍尔扩展板](../boards_shields/P090_MikroElektronika_3D_Hall_3_Click.md#mikroe-3d-hall-3-click-shield)
> - [MikroElektronika Air Quality 3 Click空气质量扩展板](../boards_shields/P094_MikroElektronika_Air_Quality_3_Click.md#mikroe-air-quality-3-click-shield)
> - [MikroElektronika Ambient 2 Click环境光扩展板](../boards_shields/P095_MikroElektronika_Ambient_2_Click.md#mikroe-ambient-2-click-shield)
> - [MikroElektronika H Bridge 4 Click电机驱动扩展板](../boards_shields/P106_MikroElektronika_H_Bridge_4_Click.md#mikroe-h-bridge-4-click-shield)
> - [MikroElektronika Illuminance Click照度扩展板](../boards_shields/P107_MikroElektronika_Illuminance_Click.md#mikroe-illuminance-click-shield)
> - [MikroElektronika IR Gesture Click红外手势扩展板](../boards_shields/P108_MikroElektronika_IR_Gesture_Click.md#mikroe-ir-gesture-click-shield)
> - [MikroElektronika LSM6DSL Click惯性传感器扩展板](../boards_shields/P110_MikroElektronika_LSM6DSL_Click.md#mikroe-lsm6dsl-click-shield)
> - [MikroElektronika Pressure 3 Click气压扩展板](../boards_shields/P115_MikroElektronika_Pressure_3_Click.md#mikroe-pressure-3-click-shield)
> - [MikroElektronika Proximity 9 Click接近感测扩展板](../boards_shields/P116_MikroElektronika_Proximity_9_Click.md#mikroe-proximity-9-click-shield)
> - [MikroElektronika RTC 18 Click时钟扩展板](../boards_shields/P118_MikroElektronika_RTC_18_Click.md#mikroe-rtc-18-click-shield)
> - [Nordic nPM1304评估套件（EK）](../boards_shields/P127_nPM1304_EK.md#npm1304-ek)
> - [Olimex MIDI扩展板（SHIELD-MIDI）](../boards_shields/P142_Olimex_SHIELD-MIDI.md#olimex-shield-midi)
> - [瑞萨EK-RA8D1到RTK7EKA6M3B00001BU显示转接板（Display Adapter）](../boards_shields/P063_EK-RA8D1_to_RTK7EKA6M3B00001BU_Display_Adapter.md#ek-ra8d1-rtk7eka6m3b00001bu)
> - [瑞萨RTK0EG0019B01002BJ电容触摸应用扩展板（Capacitive Touch Application Shield）](../boards_shields/P157_RTK0EG0019B01002BJ_Capacitive_Touch_Application_Shield.md#rtk0eg0019b01002bj)
> - [Sierra Wireless HL/RC模块评估套件扩展板（Module Evaluation Kit Shield）](../boards_shields/P190_HL_RC_Module_Evaluation_Kit_Shield.md#swir-hl78xx-ev-kit)
> - [Sparkfun ENS160及BME280环境组合扩展板（Environmental Combo Shield）](../boards_shields/P172_Sparkfun_Environmental_Combo_Shield_with_ENS160_and_BME280.md#sparkfun-environmental-combo)
> - [Sparkfun RV8803扩展板（Shield）](../boards_shields/P174_Sparkfun_RV8803_Shield.md#sparkfun-rv8803)
> - [Sparkfun SHTC3扩展板（Shield）](../boards_shields/P175_Sparkfun_SHTC3_Shield.md#sparkfun-shtc3)

<a id="new-drivers"></a>

## 新增驱动（New Drivers）


- 模数转换器（ADC）

  > - [`adi,ad4170-adc`](../hardware/P915_ADIAD4170模数转换器绑定.md#dtbinding-adi-ad4170-adc)
  > - [`adi,ad4190-adc`](../hardware/P917_ADIAD4190模数转换器绑定.md#dtbinding-adi-ad4190-adc)
  > - [`adi,ad4195-adc`](../hardware/P919_ADIAD4195模数转换器绑定.md#dtbinding-adi-ad4195-adc)
  > - [`adi,max32-adc-b-me18`](../hardware/P862_ADIMAX32BME18模数转换器绑定.md#dtbinding-adi-max32-adc-b-me18)
  > - [`infineon,autanalog-sar-adc`](../hardware/P878_Infineon自主模拟逐次逼近ADC绑定.md#dtbinding-infineon-autanalog-sar-adc)
  > - [`infineon,hppass-sar-adc`](../hardware/P881_Infineon高性能模拟子系统SAR绑定.md#dtbinding-infineon-hppass-sar-adc)
  > - [`nxp,sar-adc`](../hardware/P854_NXP逐次逼近ADC绑定.md#dtbinding-nxp-sar-adc)
  > - [`renesas,rx-adc`](../hardware/P870_RenesasRX模数转换器绑定.md#dtbinding-renesas-rx-adc)
  > - [`renesas,rz-adc-c`](../hardware/P871_RenesasRZADCC绑定.md#dtbinding-renesas-rz-adc-c)
  > - [`silabs,iadc`](../hardware/P900_SiliconLabsIADC绑定.md#dtbinding-silabs-iadc)
- ARM 架构（ARM Architecture）

  > - [`microchip,sercom-g1`](../arm_timing_ethosu_control_binding_reference/P013_microchip_sercom-g1.md#std-dtcompatible-microchip-sercom-g1)
  > - [`nuvoton,numaker-npu`](../arm_nordic_nxp_control_binding_reference/P011_nuvoton_numaker-npu.md#std-dtcompatible-nuvoton-numaker-npu)
  > - [`renesas,ra-npu`](../arm_nordic_nxp_control_binding_reference/P019_renesas_ra-npu.md#std-dtcompatible-renesas-ra-npu)
- 音频（Audio）

  > - [`dlg,da7212`](../audio_pdm_codec_binding_reference/P008_dlg_da7212.md#std-dtcompatible-dlg-da7212)
  > - [`nxp,micfil`](../audio_pdm_codec_binding_reference/P014_nxp_micfil.md#std-dtcompatible-nxp-micfil)
- 辅助显示器（Auxiliary Display）

  > - [`titanmec,tm1637`](../auxdisplay_iio_tach_binding_reference/P009_titanmec_tm1637.md#std-dtcompatible-titanmec-tm1637)
- 高速缓存（Cache）

  > - [`bflb,l1c`](../memory_protection_binding_reference/P002_bflb_l1c.md#std-dtcompatible-bflb-l1c)
- 充电器（Charger）

  > - [`nxp,pca9422-charger`](../charger_binding_reference/P004_nxp_pca9422-charger.md#std-dtcompatible-nxp-pca9422-charger)
- 时钟控制（Clock Control）

  > - [`bflb,bl61x-clock-controller`](../clock_adi_atmel_bflb_binding_reference/P016_bflb_bl61x-clock-controller.md#std-dtcompatible-bflb-bl61x-clock-controller)
  > - [`bflb,bl70x-clock-controller`](../clock_adi_atmel_bflb_binding_reference/P017_bflb_bl70x-clock-controller.md#std-dtcompatible-bflb-bl70x-clock-controller)
  > - [`infineon,fixed-clock`](../timer_reference/P112_Infineon固定时钟绑定.md#dtbinding-infineon-fixed-clock)
  > - [`infineon,fixed-factor-clock`](../timer_reference/P113_Infineon固定比例时钟绑定.md#dtbinding-infineon-fixed-factor-clock)
  > - [`infineon,peri-div`](../clock_esp_infineon_microchip_binding_reference/P009_infineon_peri-div.md#std-dtcompatible-infineon-peri-div)
  > - [`mediatek,mt818x_cpuclk`](../clock_esp_infineon_microchip_binding_reference/P017_mediatek_mt818x_cpuclk.md#std-dtcompatible-mediatek-mt818x_cpuclk)
  > - [`microchip,sam-d5x-e5x-clock`](../clock_microchip_pic32_sam_binding_reference/P022_microchip_sam-d5x-e5x-clock.md#std-dtcompatible-microchip-sam-d5x-e5x-clock)
  > - [`nordic,nrf-iron-hsfll-local`](../clock_sam_nordic_binding_reference/P019_nordic_nrf-iron-hsfll-local.md#std-dtcompatible-nordic-nrf-iron-hsfll-local)
  > - [`nxp,mc-cgm`](../clock_nxp_pico_realtek_renesas_binding_reference/P010_nxp_mc-cgm.md#std-dtcompatible-nxp-mc-cgm)
  > - [`renesas,ra-cgc-utasel`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P005_renesas_ra-cgc-utasel.md#std-dtcompatible-renesas-ra-cgc-utasel)
  > - [`renesas,rz-cgc`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P014_renesas_rz-cgc.md#std-dtcompatible-renesas-rz-cgc)
  > - [`sifli,sf32lb-rcc-clk`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P026_sifli_sf32lb-rcc-clk.md#std-dtcompatible-sifli-sf32lb-rcc-clk)
  > - [`st,stm32f4-rcc`](../timer_reference/P127_STM32F4复位与时钟控制绑定.md#dtbinding-st-stm32f4-rcc)
  > - `st,stm32fx-pllsai-clock`
  > - [`st,stm32h5-rcc`](../timer_reference/P167_STM32H5复位与时钟控制绑定.md#dtbinding-st-stm32h5-rcc)
  > - [`st,stm32l0-hsi-clock`](../timer_reference/P147_STM32L0内部高速时钟绑定.md#dtbinding-st-stm32l0-hsi-clock)
  > - `st,stm32l4-pllsai-clock`
  > - [`ti,cc23x0-lf-xosc`](../clock_silabs_ti_xilinx_binding_reference/P019_ti_cc23x0-lf-xosc.md#std-dtcompatible-ti-cc23x0-lf-xosc)
- 比较器（Comparator）

  > - [`nxp,cmp`](../hardware/P743_NXP比较器绑定.md#dtbinding-nxp-cmp)
  > - [`renesas,ra-lvd`](../hardware/P750_RenesasRA电压检测器绑定.md#dtbinding-renesas-ra-lvd)
  > - [`renesas,rx-lvd`](../hardware/P751_RenesasRX电压检测器绑定.md#dtbinding-renesas-rx-lvd)
  > - [`st,stm32-comp`](../hardware/P739_STM32比较器绑定.md#dtbinding-st-stm32-comp)
  > - [`st,stm32g4-comp`](../hardware/P740_STM32G4比较器绑定.md#dtbinding-st-stm32g4-comp)
  > - [`st,stm32h7-comp`](../hardware/P741_STM32H7比较器绑定.md#dtbinding-st-stm32h7-comp)
- 计数器（Counter）

  > - [`infineon,tcpwm-counter`](../microchip_soc_counter_binding_reference/P002_infineon_tcpwm-counter.md#std-dtcompatible-infineon-tcpwm-counter)
  > - [`microchip,tcc-g1`](../microchip_soc_counter_binding_reference/P013_microchip_tcc-g1.md#std-dtcompatible-microchip-tcc-g1)
  > - [`nxp,imx-snvs-rtc`](../nxp_nuvoton_counter_binding_reference/P006_nxp_imx-snvs-rtc.md#std-dtcompatible-nxp-imx-snvs-rtc)
  > - [`nxp,lpit`](../nxp_nuvoton_counter_binding_reference/P012_nxp_lpit.md#std-dtcompatible-nxp-lpit)
  > - [`nxp,lpit-channel`](../nxp_nuvoton_counter_binding_reference/P011_nxp_lpit-channel.md#std-dtcompatible-nxp-lpit-channel)
  > - [`nxp,stm`](../renesas_realtek_counter_binding_reference/P001_nxp_stm.md#std-dtcompatible-nxp-stm)
  > - [`renesas,rz-cmtw-counter`](../renesas_realtek_counter_binding_reference/P016_renesas_rz-cmtw-counter.md#std-dtcompatible-renesas-rz-cmtw-counter)
- 中央处理器（CPU）

  > - [`arm,cortex-a78`](../cpu_arm_riscv_binding_reference/P015_arm_cortex-a78.md#std-dtcompatible-arm-cortex-a78)
  > - [`arm,cortex-m52`](../cpu_cortex_xtensa_binding_reference/P001_arm_cortex-m52.md#std-dtcompatible-arm-cortex-m52)
  > - [`arm,cortex-m52f`](../cpu_cortex_xtensa_binding_reference/P002_arm_cortex-m52f.md#std-dtcompatible-arm-cortex-m52f)
  > - [`intel,panther-lake`](../cpu_vendor_multiarc_binding_reference/P012_intel_panther-lake.md#std-dtcompatible-intel-panther-lake)
  > - [`renesas,rxv1`](../cpu_vendor_multiarc_binding_reference/P030_renesas_rxv1.md#std-dtcompatible-renesas-rxv1)
  > - [`renesas,rxv2`](../cpu_vendor_multiarc_binding_reference/P031_renesas_rxv2.md#std-dtcompatible-renesas-rxv2)
  > - [`renesas,rxv3`](../cpu_vendor_multiarc_binding_reference/P032_renesas_rxv3.md#std-dtcompatible-renesas-rxv3)
  > - [`snps,av5rhx`](../cpu_vendor_multiarc_binding_reference/P043_snps_av5rhx.md#std-dtcompatible-snps-av5rhx)
  > - [`snps,av5rmx`](../cpu_vendor_multiarc_binding_reference/P044_snps_av5rmx.md#std-dtcompatible-snps-av5rmx)
  > - [`xuantie,e907`](../cpu_vendor_multiarc_binding_reference/P055_xuantie_e907.md#std-dtcompatible-xuantie-e907)
- 循环冗余校验（CRC）

  > - [`renesas,ra-crc`](../crc_clock_monitor_binding_reference/P008_renesas_ra-crc.md#std-dtcompatible-renesas-ra-crc)
- 密码学加速器（Cryptographic Accelerator）

  > - [`espressif,esp32-aes`](../crypto_aes_sha_ccm_binding_reference/P007_espressif_esp32-aes.md#std-dtcompatible-espressif-esp32-aes)
  > - [`espressif,esp32-sha`](../crypto_aes_sha_ccm_binding_reference/P008_espressif_esp32-sha.md#std-dtcompatible-espressif-esp32-sha)
  > - [`nxp,els`](../crypto_secure_engine_st_ti_binding_reference/P003_nxp_els.md#std-dtcompatible-nxp-els)
  > - [`st,stm32-hash`](../crypto_secure_engine_st_ti_binding_reference/P017_st_stm32-hash.md#std-dtcompatible-st-stm32-hash)
- 数模转换器（DAC）

  > - [`adi,ad5601`](../hardware/P782_AD5601数模转换器绑定.md#dtbinding-adi-ad5601)
  > - [`adi,ad5611`](../hardware/P783_AD5611数模转换器绑定.md#dtbinding-adi-ad5611)
  > - [`adi,ad5621`](../hardware/P784_AD5621数模转换器绑定.md#dtbinding-adi-ad5621)
  > - [`atmel,samd5x-dac`](../hardware/P764_AtmelSAMD5x数模转换器绑定.md#dtbinding-atmel-samd5x-dac)
  > - [`silabs,vdac`](../hardware/P774_SiliconLabs电压数模转换器绑定.md#dtbinding-silabs-vdac)
- 调试（Debug）

  > - [`nordic,coresight-nrf`](../debug_binding_reference/P004_Nordic_CoreSight调试绑定.md#std-dtcompatible-nordic-coresight-nrf)
- 显示（Display）

  > - [`chipone,co5300`](../compatible_binding_reference/P023_chipone_co5300.md#std-dtcompatible-chipone-co5300)
  > - [`himax,hx8379c`](../display_adi_chipone_eink_binding_reference/P020_himax_hx8379c.md#std-dtcompatible-himax-hx8379c)
  > - [`jdi,lpm013m126`](../display_ilitek_matrix_nxp_binding_reference/P012_jdi_lpm013m126.md#std-dtcompatible-jdi-lpm013m126)
  > - [`nxp,imx-lcdifv3`](../display_ilitek_matrix_nxp_binding_reference/P020_nxp_imx-lcdifv3.md#std-dtcompatible-nxp-imx-lcdifv3)
  > - [`sitronix,st7305`](../display_sinowealth_sitronix_solomon_binding_reference/P003_sitronix_st7305.md#std-dtcompatible-sitronix-st7305)
  > - [`sitronix,st7306`](../display_sinowealth_sitronix_solomon_binding_reference/P004_sitronix_st7306.md#std-dtcompatible-sitronix-st7306)
  > - [`sitronix,st7567`](../compatible_binding_reference/P059_sitronix_st7567.md#std-dtcompatible-sitronix-st7567)
  > - [`solomon,ssd1357`](../display_solomon_oled_epd_binding_reference/P013_solomon_ssd1357.md#std-dtcompatible-solomon-ssd1357)
  > - [`ultrachip,uc8151d`](../display_st_ultrachip_zephyr_binding_reference/P005_ultrachip_uc8151d.md#std-dtcompatible-ultrachip-uc8151d)
  > - `waveshare,7inch-dsi-lcd-c`
  > - [`zephyr,hub12`](../display_st_ultrachip_zephyr_binding_reference/P013_zephyr_hub12.md#std-dtcompatible-zephyr-hub12)
- 直接存储器访问（DMA）

  > - [`andestech,atcdmacx00`](../dma_binding_reference/P008_andestech_atcdmacx00.md#std-dtcompatible-andestech-atcdmacx00)
  > - [`bflb,dma`](../dma_binding_reference/P012_bflb_dma.md#std-dtcompatible-bflb-dma)
  > - [`nuvoton,npcx-gdma`](../intel_microchip_dma_binding_reference/P017_nuvoton_npcx-gdma.md#std-dtcompatible-nuvoton-npcx-gdma)
  > - [`renesas,ra-dma`](../nxp_realtek_renesas_dma_binding_reference/P012_renesas_ra-dma.md#std-dtcompatible-renesas-ra-dma)
  > - [`renesas,rz-dmac`](../nxp_realtek_renesas_dma_binding_reference/P014_renesas_rz-dmac.md#std-dtcompatible-renesas-rz-dmac)
  > - [`sifli,sf32lb-dmac`](../nxp_realtek_renesas_dma_binding_reference/P017_sifli_sf32lb-dmac.md#std-dtcompatible-sifli-sf32lb-dmac)
  > - [`silabs,gpdma`](../nxp_realtek_renesas_dma_binding_reference/P018_silabs_gpdma.md#std-dtcompatible-silabs-gpdma)
- 以太网（Ethernet）

  > - [`intel,eth-plat`](../ethernet_mac_mdio_binding_reference/P011_intel_eth-plat.md#std-dtcompatible-intel-eth-plat)
  > - [`intel,igc-mac`](../ethernet_mac_mdio_binding_reference/P012_intel_igc-mac.md#std-dtcompatible-intel-igc-mac)
  > - [`microchip,ksz9131`](../ethernet_phy_renesas_rockchip_binding_reference/P002_microchip_ksz9131.md#std-dtcompatible-microchip-ksz9131)
  > - [`microchip,sam-ethernet-controller`](../ethernet_mdio_microchip_binding_reference/P019_microchip_sam-ethernet-controller.md#std-dtcompatible-microchip-sam-ethernet-controller)
  > - [`nxp,imx-netc`](../ethernet_nxp_phy_binding_reference/P008_nxp_imx-netc.md#std-dtcompatible-nxp-imx-netc)
  > - [`nxp,imx-netc-blk-ctrl`](../ethernet_nxp_phy_binding_reference/P005_nxp_imx-netc-blk-ctrl.md#std-dtcompatible-nxp-imx-netc-blk-ctrl)
  > - [`virtio,net`](../hardware/P587_VirtIO网络设备绑定.md#dtbinding-virtio-net)
- 闪存控制器（Flash Controller）

  > - [`adi,max32-spixf-nor`](../flash_adi_microchip_nordic_binding_reference/P002_adi_max32-spixf-nor.md#std-dtcompatible-adi-max32-spixf-nor)
  > - `bflb,flash-controller`
  > - [`ite,it51xxx-manual-flash-1k`](../flash_adi_microchip_nordic_binding_reference/P019_ite_it51xxx-manual-flash-1k.md#std-dtcompatible-ite-it51xxx-manual-flash-1k)
  > - [`microchip,nvmctrl-g1-flash`](../flash_adi_microchip_nordic_binding_reference/P022_microchip_nvmctrl-g1-flash.md#std-dtcompatible-microchip-nvmctrl-g1-flash)
  > - [`nordic,nrf-mramc`](../flash_adi_microchip_nordic_binding_reference/P027_nordic_nrf-mramc.md#std-dtcompatible-nordic-nrf-mramc)
  > - [`nxp,kinetis-ftfc`](../flash_nuvoton_nxp_renesas_binding_reference/P015_nxp_kinetis-ftfc.md#std-dtcompatible-nxp-kinetis-ftfc)
  > - [`nxp,xspi-nor`](../flash_nuvoton_nxp_renesas_binding_reference/P019_nxp_xspi-nor.md#std-dtcompatible-nxp-xspi-nor)
  > - [`renesas,ra-flash-lp-controller`](../flash_nuvoton_nxp_renesas_binding_reference/P028_renesas_ra-flash-lp-controller.md#std-dtcompatible-renesas-ra-flash-lp-controller)
  > - [`renesas,ra-mram-controller`](../flash_nuvoton_nxp_renesas_binding_reference/P029_renesas_ra-mram-controller.md#std-dtcompatible-renesas-ra-mram-controller)
  > - [`renesas,rz-qspi-spibsc`](../flash_renesas_st_ti_binding_reference/P002_renesas_rz-qspi-spibsc.md#std-dtcompatible-renesas-rz-qspi-spibsc)
  > - [`renesas,rz-qspi-xspi`](../flash_renesas_st_ti_binding_reference/P003_renesas_rz-qspi-xspi.md#std-dtcompatible-renesas-rz-qspi-xspi)
- 文件系统（File System）

  > - [`zephyr,fstab,ext2`](../storage_filesystem_binding_reference/P004_zephyr_fstab_ext2.md#std-dtcompatible-zephyr-fstab-ext2)
- 电量计（Fuel Gauge）

  > - [`adi,ltc2959`](../fuel_gauge_binding_reference/P002_adi_ltc2959.md#std-dtcompatible-adi-ltc2959)
  > - [`silergy,sy24561`](../fuel_gauge_binding_reference/P008_silergy_sy24561.md#std-dtcompatible-silergy-sy24561)
  > - [`ti,bq40z50`](../fuel_gauge_binding_reference/P010_ti_bq40z50.md#std-dtcompatible-ti-bq40z50)
- 通用输入输出（GPIO）

  > - [`aesc,gpio`](../gpio_adi_headers_ambiq_binding_reference/P013_aesc_gpio.md#std-dtcompatible-aesc-gpio)
  > - [`arducam,ffc-40pin-connector`](../gpio_adi_headers_ambiq_binding_reference/P022_arducam_ffc-40pin-connector.md#std-dtcompatible-arducam-ffc-40pin-connector)
  > - [`bflb,bl60x_70x-gpio`](../gpio_connectors_bflb_esp_binding_reference/P005_bflb_bl60x_70x-gpio.md#std-dtcompatible-bflb-bl60x_70x-gpio)
  > - `bflb,bl61x-gpio`
  > - [`fobe,quill-header`](../gpio_connectors_bflb_esp_binding_reference/P025_fobe_quill-header.md#std-dtcompatible-fobe-quill-header)
  > - [`microchip,port-g1-gpio`](../gpio_microchip_nordic_nuvoton_binding_reference/P001_microchip_port-g1-gpio.md#std-dtcompatible-microchip-port-g1-gpio)
  > - [`microchip,sam-pio4`](../gpio_microchip_nordic_nuvoton_binding_reference/P002_microchip_sam-pio4.md#std-dtcompatible-microchip-sam-pio4)
  > - [`nxp,pca6408`](../gpio_nxp_expanders_binding_reference/P009_nxp_pca6408.md#std-dtcompatible-nxp-pca6408)
  > - [`nxp,pcal6408`](../gpio_nxp_expanders_binding_reference/P016_nxp_pcal6408.md#std-dtcompatible-nxp-pcal6408)
  > - [`nxp,pcal6416`](../gpio_nxp_expanders_binding_reference/P018_nxp_pcal6416.md#std-dtcompatible-nxp-pcal6416)
  > - [`nxp,pcal9538`](../gpio_nxp_expanders_binding_reference/P022_nxp_pcal9538.md#std-dtcompatible-nxp-pcal9538)
  > - [`nxp,pcal9539`](../gpio_nxp_expanders_binding_reference/P023_nxp_pcal9539.md#std-dtcompatible-nxp-pcal9539)
  > - [`nxp,pcal9722`](../gpio_nxp_expanders_binding_reference/P024_nxp_pcal9722.md#std-dtcompatible-nxp-pcal9722)
  > - [`sifli,sf32lb-gpio`](../gpio_silabs_st_connectors_binding_reference/P010_sifli_sf32lb-gpio.md#std-dtcompatible-sifli-sf32lb-gpio)
  > - [`sifli,sf32lb-gpio-parent`](../gpio_silabs_st_connectors_binding_reference/P009_sifli_sf32lb-gpio-parent.md#std-dtcompatible-sifli-sf32lb-gpio-parent)
  > - [`silabs,exp-header`](../gpio_silabs_st_connectors_binding_reference/P011_silabs_exp-header.md#std-dtcompatible-silabs-exp-header)
  > - [`silabs,gpio`](../gpio_silabs_st_connectors_binding_reference/P015_silabs_gpio.md#std-dtcompatible-silabs-gpio)
  > - [`silabs,gpio-port`](../gpio_silabs_st_connectors_binding_reference/P014_silabs_gpio-port.md#std-dtcompatible-silabs-gpio-port)
- 硬件信息（Hardware Information）

  > - `nxp,cmc-reset-cause`
  > - [`nxp,imx-src-rev2`](../hwinfo_binding_reference/P007_nxp_imx-src-rev2.md#std-dtcompatible-nxp-imx-src-rev2)
  > - [`nxp,rstctl-hwinfo`](../hwinfo_binding_reference/P013_nxp_rstctl-hwinfo.md#std-dtcompatible-nxp-rstctl-hwinfo)
- 集成电路间总线（I2C）

  > - `infineon,cat1-i2c-pdl`
  > - [`renesas,ra-i2c-sci`](../i2c_nxp_pico_renesas_binding_reference/P013_renesas_ra-i2c-sci.md#std-dtcompatible-renesas-ra-i2c-sci)
  > - [`renesas,rz-iic`](../i2c_nxp_pico_renesas_binding_reference/P017_renesas_rz-iic.md#std-dtcompatible-renesas-rz-iic)
  > - [`silabs,i2c`](../i2c_stm32_ti_mux_binding_reference/P005_silabs_i2c.md#std-dtcompatible-silabs-i2c)
  > - [`ti,cc23x0-i2c`](../i2c_stm32_ti_mux_binding_reference/P011_ti_cc23x0-i2c.md#std-dtcompatible-ti-cc23x0-i2c)
- 改进型集成电路间总线（I3C）

  > - [`adi,max32-i3c`](../i3c_smbus_binding_reference/P001_adi_max32-i3c.md#std-dtcompatible-adi-max32-i3c)
- 低速率无线个域网（IEEE 802.15.4）

  > - [`st,stm32wba-ieee802154`](../lora_ieee802154_binding_reference/P010_st_stm32wba-ieee802154.md#std-dtcompatible-st-stm32wba-ieee802154)
- 输入（Input）

  > - [`chipsemi,chsc5x`](../input_adc_touch_matrix_binding_reference/P007_chipsemi_chsc5x.md#std-dtcompatible-chipsemi-chsc5x)
  > - [`nxp,mcux-kpp`](../input_keyboard_optical_ctsu_binding_reference/P010_nxp_mcux-kpp.md#std-dtcompatible-nxp-mcux-kpp)
  > - [`renesas,ra-ctsu`](../input_touch_lvgl_gesture_binding_reference/P001_renesas_ra-ctsu.md#std-dtcompatible-renesas-ra-ctsu)
  > - [`renesas,rx-ctsu`](../input_touch_lvgl_gesture_binding_reference/P005_renesas_rx-ctsu.md#std-dtcompatible-renesas-rx-ctsu)
- 中断控制器（Interrupt Controller）

  > - [`hazard3,hazard3-intc`](../riscv_interrupt_binding_reference/P003_hazard3_hazard3-intc.md#std-dtcompatible-hazard3-hazard3-intc)
  > - [`microchip,dmec-ecia-girq`](../infineon_microchip_interrupt_binding_reference/P006_microchip_dmec-ecia-girq.md#std-dtcompatible-microchip-dmec-ecia-girq)
  > - [`nxp,wuu`](../nxp_interrupt_binding_reference/P007_nxp_wuu.md#std-dtcompatible-nxp-wuu)
  > - [`renesas,rz-icu`](../renesas_interrupt_binding_reference/P006_renesas_rz-icu.md#std-dtcompatible-renesas-rz-icu)
  > - [`renesas,rz-intc`](../renesas_interrupt_binding_reference/P008_renesas_rz-intc.md#std-dtcompatible-renesas-rz-intc)
  > - [`sifive,clic-draft`](../riscv_interrupt_binding_reference/P007_sifive_clic-draft.md#std-dtcompatible-sifive-clic-draft)
- 发光二极管（LED）

  > - [`leds-group-multicolor`](../led_issi_nordic_nxp_binding_reference/P010_leds-group-multicolor.md#std-dtcompatible-leds-group-multicolor)
  > - [`nxp,pca9533`](../led_issi_nordic_nxp_binding_reference/P018_nxp_pca9533.md#std-dtcompatible-nxp-pca9533)
- 灯带（LED Strip）

  > - [`worldsemi,ws2812-uart`](../led_strip_binding_reference/P013_worldsemi_ws2812-uart.md#std-dtcompatible-worldsemi-ws2812-uart)
- 邮箱（Mailbox）

  > - [`renesas,ra-ipc-mbox`](../intercore_reference/P051_RenesasRA邮箱绑定.md#dtbinding-renesas-ra-ipc-mbox)
- 管理数据输入输出（MDIO）

  > - [`intel,igc-mdio`](../ethernet_mac_mdio_binding_reference/P018_intel_igc-mdio.md#std-dtcompatible-intel-igc-mdio)
- 存储器控制器（Memory Controller）

  > - [`bflb,bl61x-psram`](../memory_controller_hyperbus_smc_binding_reference/P004_bflb_bl61x-psram.md#std-dtcompatible-bflb-bl61x-psram)
  > - [`motorola,mc146818-bbram`](../memory_controller_hyperbus_smc_binding_reference/P013_motorola_mc146818-bbram.md#std-dtcompatible-motorola-mc146818-bbram)
  > - [`nxp,xspi-psram`](../memory_controller_sdram_psram_binding_reference/P003_nxp_xspi-psram.md#std-dtcompatible-nxp-xspi-psram)
  > - [`st,stm32-ospi-psram`](../memory_controller_sdram_psram_binding_reference/P014_st_stm32-ospi-psram.md#std-dtcompatible-st-stm32-ospi-psram)
- 多功能设备（MFD）

  > - [`motorola,mc146818-mfd`](../hardware/P713_MC146818多功能设备绑定.md#dtbinding-motorola-mc146818-mfd)
  > - [`nxp,pca9422`](../hardware/P689_PCA9422多功能设备绑定.md#dtbinding-nxp-pca9422)
  > - [`nxp,sc18is606`](../hardware/P704_SC18IS606多功能设备绑定.md#dtbinding-nxp-sc18is606)
  > - [`sifli,sf32lb-rcc`](../hardware/P716_SF32LB复位与时钟控制绑定.md#dtbinding-sifli-sf32lb-rcc)
- MIPI显示串行接口（MIPI DSI）

  > - [`nxp,mipi-dsi-dwc`](../mipi_dbi_dsi_binding_reference/P015_nxp_mipi-dsi-dwc.md#std-dtcompatible-nxp-mipi-dsi-dwc)
  > - [`st,stm32u5-mipi-dsi`](../mipi_dbi_dsi_binding_reference/P019_st_stm32u5-mipi-dsi.md#std-dtcompatible-st-stm32u5-mipi-dsi)
- 其他绑定（Miscellaneous）

  > - [`nxp,imx93-mediamix`](../misc_adi_nordic_binding_reference/P025_nxp_imx93-mediamix.md#std-dtcompatible-nxp-imx93-mediamix)
  > - [`nxp,rt600-dsp-ctrl`](../misc_nxp_renesas_zephyr_binding_reference/P004_nxp_rt600-dsp-ctrl.md#std-dtcompatible-nxp-rt600-dsp-ctrl)
  > - [`nxp,rt700-dsp-ctrl-hifi4`](../misc_nxp_renesas_zephyr_binding_reference/P005_nxp_rt700-dsp-ctrl-hifi4.md#std-dtcompatible-nxp-rt700-dsp-ctrl-hifi4)
  > - [`renesas,rx-dtc`](../misc_nxp_renesas_zephyr_binding_reference/P022_renesas_rx-dtc.md#std-dtcompatible-renesas-rx-dtc)
  > - [`st,stm32-npu`](../misc_nxp_renesas_zephyr_binding_reference/P037_st_stm32-npu.md#std-dtcompatible-st-stm32-npu)
- 调制解调器（Modem）

  > - [`quectel,bg96`](../modem_fibocom_nordic_quectel_binding_reference/P011_quectel_bg96.md#std-dtcompatible-quectel-bg96)
  > - [`swir,hl7812`](../modem_sierra_telit_ublox_binding_reference/P006_swir_hl7812.md#std-dtcompatible-swir-hl7812)
  > - [`swir,hl7812-gnss`](../modem_sierra_telit_ublox_binding_reference/P004_swir_hl7812-gnss.md#std-dtcompatible-swir-hl7812-gnss)
  > - [`swir,hl7812-offload`](../modem_sierra_telit_ublox_binding_reference/P005_swir_hl7812-offload.md#std-dtcompatible-swir-hl7812-offload)
  > - [`swir,hl78xx`](../modem_sierra_telit_ublox_binding_reference/P009_swir_hl78xx.md#std-dtcompatible-swir-hl78xx)
  > - [`swir,hl78xx-gnss`](../modem_sierra_telit_ublox_binding_reference/P007_swir_hl78xx-gnss.md#std-dtcompatible-swir-hl78xx-gnss)
  > - [`swir,hl78xx-offload`](../modem_sierra_telit_ublox_binding_reference/P008_swir_hl78xx-offload.md#std-dtcompatible-swir-hl78xx-offload)
- 多位串行外设接口（Multi-Bit SPI）

  > - `nordic,nrf-qspi-v2`
- 存储技术设备（MTD）

  > - `andestech,qspi-nor-xip`
  > - [`atmel,at25xv021a`](../mtd_atmel_bouffalo_binding_reference/P007_atmel_at25xv021a.md#std-dtcompatible-atmel-at25xv021a)
  > - [`infineon,fm25xxx`](../mtd_atmel_bouffalo_binding_reference/P019_infineon_fm25xxx.md#std-dtcompatible-infineon-fm25xxx)
  > - [`jedec,qspi-nor`](../mtd_atmel_bouffalo_binding_reference/P025_jedec_qspi-nor.md#std-dtcompatible-jedec-qspi-nor)
  > - [`renesas,ra-nv-mram`](../mtd_nxp_st_ti_partition_binding_reference/P009_renesas_ra-nv-mram.md#std-dtcompatible-renesas-ra-nv-mram)
  > - [`renesas,ra-qspi-nor`](../mtd_nxp_st_ti_partition_binding_reference/P010_renesas_ra-qspi-nor.md#std-dtcompatible-renesas-ra-qspi-nor)
  > - [`sifli,sf32lb-mpi-qspi-nor`](../mtd_nxp_st_ti_partition_binding_reference/P012_sifli_sf32lb-mpi-qspi-nor.md#std-dtcompatible-sifli-sf32lb-mpi-qspi-nor)
- 运算放大器（OPAMP）

  > - [`nxp,opamp`](../hardware/P732_NXP运算放大器绑定.md#dtbinding-nxp-opamp)
  > - [`nxp,opamp-fast`](../hardware/P731_NXP高速运算放大器绑定.md#dtbinding-nxp-opamp-fast)
- 引脚控制（Pin Control）

  > - [`ambiq,apollo2-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P004_ambiq_apollo2-pinctrl.md#std-dtcompatible-ambiq-apollo2-pinctrl)
  > - [`microchip,port-g1-pinctrl`](../pinctrl_infineon_nordic_nxp_binding_reference/P006_microchip_port-g1-pinctrl.md#std-dtcompatible-microchip-port-g1-pinctrl)
  > - [`nxp,imx-blkctrl-ns-aon`](../pinctrl_infineon_nordic_nxp_binding_reference/P019_nxp_imx-blkctrl-ns-aon.md#std-dtcompatible-nxp-imx-blkctrl-ns-aon)
  > - [`nxp,imx-blkctrl-wakeup`](../pinctrl_infineon_nordic_nxp_binding_reference/P020_nxp_imx-blkctrl-wakeup.md#std-dtcompatible-nxp-imx-blkctrl-wakeup)
  > - [`nxp,mcxe31x-siul2-pinctrl`](../pinctrl_nxp_pico_binding_reference/P015_nxp_mcxe31x-siul2-pinctrl.md#std-dtcompatible-nxp-mcxe31x-siul2-pinctrl)
  > - [`sifli,sf32lb52x-pinmux`](../pinctrl_renesas_silabs_binding_reference/P023_sifli_sf32lb52x-pinmux.md#std-dtcompatible-sifli-sf32lb52x-pinmux)
- 电源管理（Power Management）

  > - [`ite,it8xxx2-power-elpm`](../power_control_binding_reference/P005_ite_it8xxx2-power-elpm.md#std-dtcompatible-ite-it8xxx2-power-elpm)
  > - [`nxp,cmc`](../power_control_binding_reference/P014_nxp_cmc.md#std-dtcompatible-nxp-cmc)
  > - [`nxp,spc`](../stm32_soc_power_binding_reference/P001_nxp_spc.md#std-dtcompatible-nxp-spc)
  > - [`nxp,vbat`](../stm32_soc_power_binding_reference/P002_nxp_vbat.md#std-dtcompatible-nxp-vbat)
  > - [`renesas,ra-battery-backup`](../stm32_soc_power_binding_reference/P004_renesas_ra-battery-backup.md#std-dtcompatible-renesas-ra-battery-backup)
  > - [`sifli,sf32lb-aon`](../stm32_soc_power_binding_reference/P005_sifli_sf32lb-aon.md#std-dtcompatible-sifli-sf32lb-aon)
  > - [`sifli,sf32lb52x-pmuc`](../stm32_soc_power_binding_reference/P006_sifli_sf32lb52x-pmuc.md#std-dtcompatible-sifli-sf32lb52x-pmuc)
- 电源域（Power Domain）

  > - [`nordic,nrfs-gdpwr`](../power_domain_binding_reference/P002_nordic_nrfs-gdpwr.md#std-dtcompatible-nordic-nrfs-gdpwr)
  > - [`nordic,nrfs-swext`](../power_domain_binding_reference/P003_nordic_nrfs-swext.md#std-dtcompatible-nordic-nrfs-swext)
  > - [`silabs,siwx91x-power-domain`](../power_domain_binding_reference/P010_silabs_siwx91x-power-domain.md#std-dtcompatible-silabs-siwx91x-power-domain)
- 脉宽调制（PWM）

  > - [`ambiq,ctimer-pwm`](../pwm_adi_esp_infineon_binding_reference/P004_ambiq_ctimer-pwm.md#std-dtcompatible-ambiq-ctimer-pwm)
  > - [`ambiq,timer-pwm`](../pwm_adi_esp_infineon_binding_reference/P005_ambiq_timer-pwm.md#std-dtcompatible-ambiq-timer-pwm)
  > - [`infineon,tcpwm-pwm`](../pwm_adi_esp_infineon_binding_reference/P019_infineon_tcpwm-pwm.md#std-dtcompatible-infineon-tcpwm-pwm)
  > - [`microchip,tcc-g1-pwm`](../pwm_intel_microchip_nxp_binding_reference/P011_microchip_tcc-g1-pwm.md#std-dtcompatible-microchip-tcc-g1-pwm)
  > - [`renesas,rz-mtu-pwm`](../pwm_stm32_ti_generic_binding_reference/P002_renesas_rz-mtu-pwm.md#std-dtcompatible-renesas-rz-mtu-pwm)
  > - [`ti,cc23x0-lgpt-pwm`](../pwm_stm32_ti_generic_binding_reference/P016_ti_cc23x0-lgpt-pwm.md#std-dtcompatible-ti-cc23x0-lgpt-pwm)
- 四线SPI（Quad SPI）

  > - [`adi,max32-spixf`](../qspi_ospi_xspi_binding_reference/P003_adi_max32-spixf.md#std-dtcompatible-adi-max32-spixf)
  > - [`renesas,ra-qspi`](../qspi_ospi_xspi_binding_reference/P008_renesas_ra-qspi.md#std-dtcompatible-renesas-ra-qspi)
  > - [`renesas,rz-spibsc`](../qspi_ospi_xspi_binding_reference/P009_renesas_rz-spibsc.md#std-dtcompatible-renesas-rz-spibsc)
  > - [`renesas,rz-xspi`](../qspi_ospi_xspi_binding_reference/P010_renesas_rz-xspi.md#std-dtcompatible-renesas-rz-xspi)
- 稳压器（Regulator）

  > - [`nxp,pca9422-regulator`](../hardware/P669_PCA9422稳压器绑定.md#dtbinding-nxp-pca9422-regulator)
  > - [`nxp,vrefv1`](../hardware/P653_NXP参考电压V1绑定.md#dtbinding-nxp-vrefv1)
- 保留内存（Reserved Memory）

  > - [`renesas,ofs-memory`](../memory_protection_binding_reference/P011_renesas_ofs-memory.md#std-dtcompatible-renesas-ofs-memory)
- 复位控制器（Reset Controller）

  > - [`microchip,rstc-g1-reset`](../reset_controller_binding_reference/P006_microchip_rstc-g1-reset.md#std-dtcompatible-microchip-rstc-g1-reset)
  > - [`nxp,mrcc-reset`](../reset_controller_binding_reference/P010_nxp_mrcc-reset.md#std-dtcompatible-nxp-mrcc-reset)
  > - [`sifli,sf32lb-rcc-rctl`](../reset_controller_binding_reference/P016_sifli_sf32lb-rcc-rctl.md#std-dtcompatible-sifli-sf32lb-rcc-rctl)
- 保持存储器（Retained Memory）

  > - [`sifli,sf32lb-rtc-backup`](../hardware/P628_SF32LB_RTC备份内存绑定.md#dtbinding-sifli-sf32lb-rtc-backup)
  > - [`silabs,buram`](../hardware/P629_SiliconLabs备份RAM绑定.md#dtbinding-silabs-buram)
- 随机数生成器（RNG）

  > - [`ambiq,puf-trng`](../rng_binding_reference/P003_ambiq_puf-trng.md#std-dtcompatible-ambiq-puf-trng)
  > - [`nxp,els-trng`](../rng_binding_reference/P017_nxp_els-trng.md#std-dtcompatible-nxp-els-trng)
- 实时时钟（RTC）

  > - [`microcrystal,rv3032`](../microchip_microcrystal_nxp_rtc_binding_reference/P007_microcrystal_rv3032.md#std-dtcompatible-microcrystal-rv3032)
  > - [`nxp,pcf85063a`](../microchip_microcrystal_nxp_rtc_binding_reference/P015_nxp_pcf85063a.md#std-dtcompatible-nxp-pcf85063a)
  > - [`renesas,ra-rtc`](../soc_rtc_binding_reference/P006_renesas_ra-rtc.md#std-dtcompatible-renesas-ra-rtc)
  > - [`sifli,sf32lb-rtc`](../soc_rtc_binding_reference/P008_sifli_sf32lb-rtc.md#std-dtcompatible-sifli-sf32lb-rtc)
  > - [`silabs,rtcc`](../soc_rtc_binding_reference/P011_silabs_rtcc.md#std-dtcompatible-silabs-rtcc)
  > - [`silabs,sysrtc`](../soc_rtc_binding_reference/P013_silabs_sysrtc.md#std-dtcompatible-silabs-sysrtc)
  > - [`ti,mspm0-rtc`](../soc_rtc_binding_reference/P017_ti_mspm0-rtc.md#std-dtcompatible-ti-mspm0-rtc)
  > - [`zephyr,rtc-counter`](../hardware/P553_RTC计数器适配绑定.md#dtbinding-zephyr-rtc-counter)
- 瑞萨 RX（Renesas RX）

  > - [`renesas,rx-swint`](../platform_rmt_openthread_binding_reference/P012_renesas_rx-swint.md#std-dtcompatible-renesas-rx-swint)
- SD 主机控制器（SDHC）

  > - [`microchip,sama7g5-sdmmc`](../sdhc_binding_reference/P011_microchip_sama7g5-sdmmc.md#std-dtcompatible-microchip-sama7g5-sdmmc)
  > - `st,stm32-sdio`
- 传感器（Sensors）

  > - [`allegro,als31300`](../sensor_adi_accel_bioz_binding_reference/P025_allegro_als31300.md#std-dtcompatible-allegro-als31300)
  > - [`invensense,icm42686`](../sensor_espressif_honeywell_invensense_binding_reference/P027_invensense_icm42686.md#std-dtcompatible-invensense-icm42686)
  > - [`invensense,icm4268x`](../sensor_espressif_honeywell_invensense_binding_reference/P029_invensense_icm4268x.md#std-dtcompatible-invensense-icm4268x)
  > - [`maxbotix,mb7040`](../sensor_liteon_maxim_temperature_binding_reference/P011_maxbotix_mb7040.md#std-dtcompatible-maxbotix-mb7040)
  > - [`maxim,max32664c`](../sensor_liteon_maxim_temperature_binding_reference/P025_maxim_max32664c.md#std-dtcompatible-maxim-max32664c)
  > - [`microchip,mtch9010`](../sensor_microchip_nordic_nxp_binding_reference/P010_microchip_mtch9010.md#std-dtcompatible-microchip-mtch9010)
  > - [`nxp,pmc-tmpsns`](../sensor_nxp_qdec_optical_binding_reference/P011_nxp_pmc-tmpsns.md#std-dtcompatible-nxp-pmc-tmpsns)
  > - [`nxp,tmpsns`](../sensor_nxp_qdec_optical_binding_reference/P015_nxp_tmpsns.md#std-dtcompatible-nxp-tmpsns)
  > - [`omron,2smpb-02e`](../sensor_nxp_qdec_optical_binding_reference/P017_omron_2smpb-02e.md#std-dtcompatible-omron-2smpb-02e)
  > - [`omron,d6f-p0001`](../sensor_nxp_qdec_optical_binding_reference/P018_omron_d6f-p0001.md#std-dtcompatible-omron-d6f-p0001)
  > - [`omron,d6f-p0010`](../sensor_nxp_qdec_optical_binding_reference/P019_omron_d6f-p0010.md#std-dtcompatible-omron-d6f-p0010)
  > - [`pni,rm3100`](../compatible_binding_reference/P054_pni_rm3100.md#std-dtcompatible-pni-rm3100)
  > - [`st,iis3dwb`](../sensor_silabs_st_industrial_binding_reference/P020_st_iis3dwb.md#std-dtcompatible-st-iis3dwb)
  > - [`ti,hdc302x`](../sensor_st_ti_power_capacitance_binding_reference/P019_ti_hdc302x.md#std-dtcompatible-ti-hdc302x)
  > - [`ti,ina228`](../sensor_st_ti_power_capacitance_binding_reference/P022_ti_ina228.md#std-dtcompatible-ti-ina228)
  > - [`ti,ina7xx`](../sensor_st_ti_power_capacitance_binding_reference/P028_ti_ina7xx.md#std-dtcompatible-ti-ina7xx)
  > - [`vishay,veml6046`](../sensor_ti_vishay_wurth_sensing_binding_reference/P015_vishay_veml6046.md#std-dtcompatible-vishay-veml6046)
  > - [`we,wsen-isds-2536030320001`](../compatible_binding_reference/P099_we_wsen-isds-2536030320001.md#std-dtcompatible-we-wsen-isds-2536030320001)
  > - [`we,wsen-pdms-25131308XXX05`](../compatible_binding_reference/P102_we_wsen-pdms-25131308XXX05.md#std-dtcompatible-we-wsen-pdms-25131308XXX05)
- 串行控制器（Serial Controller）

  > - `infineon,cat1-uart-pdl`
  > - [`microchip,sercom-g1-uart`](../uart_espressif_infineon_microchip_binding_reference/P019_microchip_sercom-g1-uart.md#std-dtcompatible-microchip-sercom-g1-uart)
  > - [`sifli,sf32lb-usart`](../uart_silabs_stm32_ti_binding_reference/P004_sifli_sf32lb-usart.md#std-dtcompatible-sifli-sf32lb-usart)
  > - [`virtio,console`](../hardware/P591_VirtIO控制台绑定.md#dtbinding-virtio-console)
  > - [`zephyr,uart-bitbang`](../uart_ti_wch_virtual_binding_reference/P016_zephyr_uart-bitbang.md#std-dtcompatible-zephyr-uart-bitbang)
- 串行外设接口（SPI）

  > - [`egis,et171-spi`](../spi_adi_atmel_esp_binding_reference/P013_egis_et171-spi.md#std-dtcompatible-egis-et171-spi)
  > - `infineon,cat1-spi-pdl`
  > - [`nxp,sc18is606-spi`](../spi_flexspi_nxp_renesas_binding_reference/P006_nxp_sc18is606-spi.md#std-dtcompatible-nxp-sc18is606-spi)
  > - [`renesas,rz-spi`](../spi_flexspi_nxp_renesas_binding_reference/P022_renesas_rz-spi.md#std-dtcompatible-renesas-rz-spi)
  > - [`ti,omap-mcspi`](../spi_stm32_ti_xilinx_binding_reference/P018_ti_omap-mcspi.md#std-dtcompatible-ti-omap-mcspi)
- 系统控制器（System Controller）

  > - [`sifli,sf32lb-cfg`](../edac_syscon_binding_reference/P007_sifli_sf32lb-cfg.md#std-dtcompatible-sifli-sf32lb-cfg)
- 转速计（Tachometer）

  > - [`zephyr,tach-gpio`](../auxdisplay_iio_tach_binding_reference/P020_zephyr_tach-gpio.md#std-dtcompatible-zephyr-tach-gpio)
- 定时器（Timer）

  > - [`ambiq,ctimer`](../mcu_timer_binding_reference/P001_ambiq_ctimer.md#std-dtcompatible-ambiq-ctimer)
  > - [`ambiq,timer`](../mcu_timer_binding_reference/P003_ambiq_timer.md#std-dtcompatible-ambiq-timer)
  > - [`infineon,tcpwm`](../mcu_timer_binding_reference/P009_infineon_tcpwm.md#std-dtcompatible-infineon-tcpwm)
  > - [`microchip,xec-basic-timer`](../microchip_nordic_nxp_realtek_timer_binding_reference/P003_microchip_xec-basic-timer.md#std-dtcompatible-microchip-xec-basic-timer)
  > - [`renesas,rz-cmtw`](../renesas_timer_binding_reference/P005_renesas_rz-cmtw.md#std-dtcompatible-renesas-rz-cmtw)
  > - [`renesas,rz-mtu`](../renesas_timer_binding_reference/P009_renesas_rz-mtu.md#std-dtcompatible-renesas-rz-mtu)
  > - [`st,stm32wb0-radio-timer`](../stm32_ti_silabs_timer_binding_reference/P010_st_stm32wb0-radio-timer.md#std-dtcompatible-st-stm32wb0-radio-timer)
- 通用串行总线（USB）

  > - `espressif,esp32-usb-otg`
- 视频（Video）

  > - [`himax,hm01b0`](../video_camera_endpoint_binding_reference/P005_himax_hm01b0.md#std-dtcompatible-himax-hm01b0)
  > - [`renesas,ra-ceu`](../video_camera_endpoint_binding_reference/P020_renesas_ra-ceu.md#std-dtcompatible-renesas-ra-ceu)
  > - [`st,stm32-jpeg`](../video_st_sony_emulation_binding_reference/P006_st_stm32-jpeg.md#std-dtcompatible-st-stm32-jpeg)
  > - [`st,stm32-venc`](../video_st_sony_emulation_binding_reference/P007_st_stm32-venc.md#std-dtcompatible-st-stm32-venc)
- 看门狗（Watchdog）

  > - [`nxp,cop`](../nxp_nordic_nuvoton_watchdog_binding_reference/P006_nxp_cop.md#std-dtcompatible-nxp-cop)
  > - [`renesas,rx-iwdt`](../realtek_renesas_silabs_watchdog_binding_reference/P006_renesas_rx-iwdt.md#std-dtcompatible-renesas-rx-iwdt)
  > - [`renesas,rz-wdt`](../realtek_renesas_silabs_watchdog_binding_reference/P007_renesas_rz-wdt.md#std-dtcompatible-renesas-rz-wdt)
  > - [`sifli,sf32lb-wdt`](../realtek_renesas_silabs_watchdog_binding_reference/P010_sifli_sf32lb-wdt.md#std-dtcompatible-sifli-sf32lb-wdt)
  > - [`ti,j7-rti-wdt`](../stm32_ti_xilinx_watchdog_binding_reference/P006_ti_j7-rti-wdt.md#std-dtcompatible-ti-j7-rti-wdt)
  > - [`xlnx,versal-wwdt`](../stm32_ti_xilinx_watchdog_binding_reference/P011_xlnx_versal-wwdt.md#std-dtcompatible-xlnx-versal-wwdt)
- 无线局域网（Wi-Fi）

  > - [`nordic,wlan`](../wifi_nordic_nxp_simulation_binding_reference/P009_nordic_wlan.md#std-dtcompatible-nordic-wlan)
- 扩展串行外设接口（XSPI）

  > - [`nxp,xspi`](../qspi_ospi_xspi_binding_reference/P015_nxp_xspi.md#std-dtcompatible-nxp-xspi)

<a id="new-samples"></a>

## 新增示例（New Samples）


- [通用模数转换器数据流（Generic ADC Stream）](../hardware/P441_ADC通用流示例.md#adc_stream)
- [脉宽调制捕获（PWM Capture）](../hardware/P169_PWM输入捕获示例.md#capture)
- [受限应用协议上传（CoAP Upload）](../networking/P071_CoAP上传示例.md#coap-upload)
- [按需CPU调频（On-demand CPU frequency scaling）](../power/P019_按需CPU调频示例.md#cpu_freq_on_demand)
- [循环冗余校验驱动（Cyclic Redundancy Check Drivers，CRC）](../hardware/P042_CRC校验示例.md#crc_drivers)
- [循环冗余校验子系统（CRC Subsys）](../data_utilities/P002_CRC子系统示例.md#crc_subsys)
- [EXT2文件系统fstab示例](../storage/P081_Ext2挂载表示例.md#ext2-fstab)
- [FRDM-MCXA156低功耗DAC、运算放大器及低功耗ADC示例（lpdac / opamp / lpadc）](../hardware/P099_FRDM模拟信号链示例.md#frdm_mcxa156_lpdac_opamp_lpadc)
- [HL78xx调制解调器驱动入门（Hello hl78xx Modem Driver）](../driver_samples/P020_HL78xx调制解调器示例.md#hello_hl78xx)
- [插桩（Instrumentation）](../observability/P019_函数插桩示例.md#instrumentation)
- [时延监测客户端（Latmon Client）](../networking/P095_Latmon客户端示例.md#latmon-client)
- [MAX32664C与MAX86141传感器集线器（Sensor Hub）](../sensors/P081_MAX32664C与MAX86141传感器集线器示例.md#max32664c)
- [管理组件传输协议USB端点节点示例（MCTP USB Endpoint Node Sample）](../usb/P191_MCTPUSB端点示例.md#mctp-usb-endpoint)
- [管理组件传输协议I2C GPIO端点节点示例（MCTP I2C GPIO Endpoint Node Sample）](../basic_samples/P052_MCTPI2C端点示例.md#mctp_i2c_bus_endpoint)
- 通过I2C与GPIO传输的PMCI MCTP示例（mctp_i2c_bus_owner）
- [消息队列（Message Queue）](../basic_samples/P026_消息队列示例.md#msg_queue)
- [MIDI2网络传输（Network Transport）](../networking/P219_MIDI2网络传输示例.md#netmidi2)
- [OCPP充电点（Charge Point）](../networking/P182_OCPP充电桩示例.md#ocpp)
- [运算放大器（Operational Amplifier，OPAMP）输出测量示例](../hardware/P092_运算放大器输出测量示例.md#opamp_output_measure)
- [OpenThread边界路由器（Border Router）](../networking/P173_OpenThread边界路由器.md#openthread-border-router)
- [生产者与消费者（Producer / Consumer）](../basic_samples/P045_实时IO生产者消费者示例.md#producer_consumer)
- [服务质量（Quality of Service）](../networking/P122_以太网服务质量示例.md#quality-of-service)
- [红黑树数据结构（Red-Black Tree Data Structure）](../basic_samples/P033_红黑树示例.md#red-black-tree)
- [使用比较器的瑞萨低电压检测示例（Low-voltage Detection）](../board_samples/P046_Renesas低电压检测.md#renesas_lvd)
- [RTK0EG0019B01002BJ电容触摸应用扩展板（Capacitive Touch Application Shield）](../shield_samples/P007_Renesas电容触摸扩展板.md#rtk0eg0019b01002bj)
- [VEML6046 RGBIR颜色传感器（Color Sensor）](../sensors/P062_VEML6046颜色传感器示例.md#veml6046)
- [virtiofs文件系统（Filesystem）](../storage/P030_Virtiofs文件系统示例.md#virtiofs)

<a id="libraries-subsystems"></a>

## 库与子系统（Libraries / Subsystems）


- 固件（Firmware）


  - 系统控制与管理接口（SCMI）


    - 新增ARM_SCMI_CHAN_SEM_TIMEOUT_USEC，允许配置通道信号量超时。
    - 直接使用[scmi_status_to_errno()](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gaec0ffd1352d0106633fd15be8fc20aa2)检查返回的命令状态码。
    - [scmi_send_message()](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html#gacba26fb193852024636dda1e4ef0ee53)新增参数，允许用户指定是否使用轮询（Polling）。
    - [NXP] 新增多项NXP专用CPU协议相关功能。
- 日志（Logging）：


  - 新增混合形式的限速日志宏（Rate-limited Logging Macros），避免高频消息淹没日志。系统同时提供便捷宏，使用[CONFIG_LOG_RATELIMIT_INTERVAL_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_RATELIMIT_INTERVAL_MS)中的默认间隔，以及显式速率宏，接受自定义速率参数。该设计遵循Linux的printk_ratelimited模式，同时提供更大灵活性。限速以宏调用位置为单位，每个不同调用位置均有独立速率限制。可用[CONFIG_LOG_RATELIMIT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_RATELIMIT)全局启用或禁用限速；禁用时，可通过[CONFIG_LOG_RATELIMIT_FALLBACK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_RATELIMIT_FALLBACK)选择记录全部消息或全部丢弃。详见[限速日志（Rate-limited Logging）](https://docs.zephyrproject.org/latest/services/logging/index.html#logging-ratelimited)。
- Mbed TLS密码与TLS库


  - 新增[CONFIG_PSA_CRYPTO](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)，简化PSA Crypto API提供方（Provider）的启用。若启用[CONFIG_BUILD_WITH_TFM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)，提供方为TF-M，并设置[CONFIG_PSA_CRYPTO_PROVIDER_TFM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO_PROVIDER_TFM)；否则为Mbed TLS，并设置[CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO_PROVIDER_MBEDTLS)。另新增[CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO_PROVIDER_CUSTOM)，允许最终用户提供自定义实现。
  - 从3.6.4更新到3.6.5，发行说明见以下链接：


    - [https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.5](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.5)
- 安全存储（Secure Storage）


  - 移除实验性状态标记。（[GitHub #96483](https://github.com/zephyrproject-rtos/zephyr/issues/96483)）

<a id="other-notable-changes"></a>

## 其他主要变更（Other Notable Changes）


- 从源码树移除仅面向仿真器的Nordic Semiconductor nRF54L09 PDK（nrf54l09pdk）。实际硬件可用后，将以正式开发板定义替代。
- 移除Nordic Semiconductor nRF54L20 PDK（nrf54l20pdk）支持，因为它已被[nRF54LM20 DK](../boards_nordic/P014_nRF54LM20_DK.md#nrf54lm20dk)（nrf54lm20dk）替代。

## 译注

本页按对应版本的官方发行说明翻译；“新增”“弃用”“当前”等描述均以该版本为背景。安全编号、开发板目标、设备树compatible、代码和源码路径保留原始标识；不会将原文中的历史保密期说明作为当前状态承诺。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Zephyr 4.2 发行说明](P002_Zephyr_4.2_发行说明.md) · [本模块主线目录](../reading/releases_notes.md) · [全部主线](../reading/README.md) · [下一篇：Zephyr 4.4 发行说明](P004_Zephyr_4.4_发行说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_Zephyr_4.2_发行说明.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_Zephyr_4.4_发行说明.md)

</details>

<!-- reading-navigation:end -->
