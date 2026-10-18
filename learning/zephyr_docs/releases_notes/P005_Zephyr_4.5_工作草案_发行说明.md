---
id: learning.zephyr-docs.releases-notes.page-5
title: Zephyr 4.5 工作草案 发行说明
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/release-notes-4.5.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zephyr-4-5-0-working-draft"></a>

<a id="zephyr-4-5"></a>

# 第5章\_Zephyr 4.5.0（工作草案，Working Draft）

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/release-notes-4.5.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Zephyr 4.5.0版本现已发布。译注：这是原文草案中的发布措辞；本页标题仍明确标为工作草案，不据此认定已正式发布。

本版本的主要增强包括：

新增架构：英飞凌TriCore（Infineon TriCore）与高通Hexagon（Qualcomm Hexagon）

Zephyr现在支持用于AURIX汽车微控制器的英飞凌TriCore架构，以及高通Hexagon数字信号处理器（DSP）架构。（[英飞凌TriCore架构（Infineon TriCore Architecture）](https://docs.zephyrproject.org/latest/boards/index.html#arch=tricore)；[高通Hexagon DSP架构（Qualcomm Hexagon）](https://docs.zephyrproject.org/latest/boards/index.html#arch=hexagon)）

多媒体流水线（Multimedia Pipeline，mpipe）

新增实验性多媒体流水线（mpipe）子系统，受GStreamer启发，将源、变换及接收端元素（Source / Transform / Sink）连接成零拷贝流水线，为构建媒体应用提供框架。（[多媒体流水线（Multimedia Pipeline，mpipe）](../services_overview/P012_多媒体流水线.md#mpipe)）

网络功能增强（Networking Enhancements）

IP协议栈的多项优化，使zperf回环基准测试中的TCP吞吐量最高提升21%。（[zperf回环基准测试（Loopback Benchmark）](../networking/P098_zperf确定性回环吞吐量.md#zperf-loopback-icount)）

网络协议栈还新增以下功能：


- [QUIC](../networking/P143_QUIC传输接口.md#quic-transport-interface)及[HTTP/3](../networking/P055_HTTP服务器库.md#http-server-interface)支持。
- 安全外壳（SSH）服务器及客户端，包括Shell后端。（[安全外壳服务器及客户端（SSH Server and Client）](../networking/P221_SSH服务端与客户端示例.md#ssh-server-client)）
- 模型上下文协议（Model Context Protocol，MCP）服务器，使AI代理可使用设备提供的工具。（[模型上下文协议（MCP）服务器](../networking/P178_MCP服务器.md#mcp-server-interface)）
- 网关功能：IPv4转发、网络地址转换（NAT）及[DHCPv6](../networking/P031_DHCPv6.md#dhcpv6-interface)前缀委派（Prefix Delegation）。

新增驱动类别（New Driver Classes）

Zephyr 4.5新增多种驱动API：


- [蜂鸣器（Buzzer）](../hardware/P124_蜂鸣器.md#buzzer-api)，面向PWM或GPIO驱动的无源及有源蜂鸣器；
- [时钟监测（Clock Monitor）](../hardware/P102_时钟监视器.md#clock-monitor-api)，用于运行时观测时钟频率；
- 数字可寻址照明接口（Digital Addressable Lighting Interface，[DALI](../hardware/P133_数字可寻址照明接口.md#dali-api)）；
- 局部互连网络（Local Interconnect Network，[LIN](../hardware/P072_本地互连网络.md#lin)）汽车串行总线；
- 硬件信号[多路复用器（MUX）](https://docs.zephyrproject.org/latest/hardware/peripherals/mux.html#mux-api)；
- [脉冲输入输出（Pulse IO）](https://docs.zephyrproject.org/latest/hardware/peripherals/pulse_io.html#pulse-io-api)，用于产生及捕获定时数字边沿的硬件，适用于可寻址LED灯带及红外收发器等。

安全与软件物料清单（SBOM）改进

本次发布改进SBOM生成、加固检查及密码加速：


- 支持[SPDX 3.0软件物料清单（SBOM）](../west/P008_其他Zephyr扩展命令.md#west-spdx)，包括[构建配置文件（Build Profile）](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html#west-spdx-build-profile)。
- 重构加固工具，加入通用弱点枚举（CWE）引用及持续集成（CI）支持。（[加固工具（Hardening Tool）](../security/P005_安全加固工具.md#hardening)）
- 在部分Silicon Labs、NXP及STM32设备上提供硬件加速的[PSA Crypto](../crypto/P003_PSA密码学.md#psa-crypto)。

模拟与测试改进（Simulation and Testing）

本次发布扩展模拟目标及测试工具：


- 为native_sim新增基于宿主机的外设，包括Wi-Fi、音频、视频、LED及宿主目录挂载。（[native_sim外设](../native_reference/P004_Native_Simulator本机模拟器.md#native-sim-peripherals)）
- 为QEMU目标新增[VirtIO](https://docs.zephyrproject.org/latest/hardware/virtualization/virtio.html#virtio)驱动：块设备、输入、GPIO、I2C及SPI。
- Twister支持多设备测试及[多工具链构建](https://docs.zephyrproject.org/latest/develop/twister/index.html#twister-toolchain-selection)。（[多设备测试（Multi-device Testing）](https://docs.zephyrproject.org/latest/develop/twister/index.html#twister-multi-duts-testing)）
- 为网络协议栈提供测试与测试控制标记法第3版（TTCN-3）一致性测试套件。（[TTCN-3一致性测试套件](../networking/P155_TTCN3协议一致性测试.md#ttcn3-testing)）

调试与诊断（Debugging and Diagnostics）

本次发布新增多种调试及诊断工具：


- [ZASSERT()](https://docs.zephyrproject.org/latest/kernel/services/other/assert.html#assert)支持按模块及文件设置断言级别。
- 通过[CONFIG_SYS_HEAP_SANITIZER_ASAN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_HEAP_SANITIZER_ASAN)在native_sim上、通过[CONFIG_SYS_HEAP_KASAN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_HEAP_KASAN)在实际目标上检测堆内存错误。
- 新增跟踪功能：终端查看器、Perfetto导出、Shell及插桩跟踪宏单元（ITM）后端。（[tracing](https://docs.zephyrproject.org/latest/services/tracing/index.html#tracing)）

扩展开发板支持（Expanded Board Support）

本次发布新增178款开发板及29款扩展板（Shield）支持。（[新增开发板](#boards-added-in-zephyr-4-5)；[新增扩展板](#shields-added-in-zephyr-4-5)）

应用从Zephyr v4.4.0迁移到v4.5.0所需或建议的修改，见单独的[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)。

以下各节按组件提供详细变更列表。

<a id="security-vulnerability-related"></a>

## 安全漏洞相关变更（Security Vulnerability Related）

本版本修复以下通用漏洞披露（CVE）项：


- <a id="index-0"></a>

  [CVE 2026-8718](https://www.cve.org/CVERecord?id=CVE-2026-8718)：原发行说明记载的保密期截至2026-08-08。
- <a id="index-1"></a>

  [CVE 2026-9263](https://www.cve.org/CVERecord?id=CVE-2026-9263)：原发行说明记载的保密期截至2026-06-28。

<a id="api-changes"></a>

## API变更（API Changes）

<a id="removed-apis-and-options"></a>

### 已移除的API与选项（Removed APIs and Options）


- 架构（Architectures）

  > - ARM架构
  >
  >   > - `CONFIG_PLATFORM_SPECIFIC_INIT`
  >   > - `z_arm_platform_init()`
  > - RISC-V架构
  >
  >   > - `CONFIG_EXTRA_EXCEPTION_INFO`
  > - x86
  >
  >   > - `CONFIG_SSE`
  >   > - `CONFIG_SSE_FP_MATH`
  > - Xtensa架构
  >
  >   > - `CONFIG_XTENSA_BACKTRACE_EXCEPTION_DUMP_HOOK`
- 蓝牙（Bluetooth）


  - 控制器（Controller）


    - `CONFIG_BT_CTRL_ADV_ADI_IN_SCAN_RSP`
  - 主机（Host）


    - 移除CONFIG_BT_RECV_CONTEXT选择项及其CONFIG_BT_RECV_WORKQ_SYS、CONFIG_BT_RECV_WORKQ_BT选项。主机现在始终在专用蓝牙接收（RX）工作队列处理低优先级HCI数据包，即原CONFIG_BT_RECV_WORKQ_BT的行为。见迁移指南。
    - 部分主机工作项从系统工作队列移至专用蓝牙RX工作队列；这些工作项触发的应用回调现在运行于蓝牙RX线程。受影响回调类别见迁移指南。
    - 移除CONFIG_BT_HCI_RAW_H4及CONFIG_BT_HCI_RAW_H4_ENABLE。它们自Zephyr 4.2起即已无效，因为HCI原始层从该版本开始无条件对全部缓冲区采用H:4数据包编码。仍设置这些选项的应用可直接删除它们。
    - CONFIG_BT_AUTO_PHY_UPDATE由BT_AUTO_PHY_CENTRAL及BT_AUTO_PHY_PERIPHERAL选择项替代。
    - `_bt_gatt_ccc`
    - `BT_GATT_CCC_INITIALIZER`
    - `CONFIG_BT_CONN_TX_MAX`
    - `CONFIG_BT_FIXED_PASSKEY`
    - `bt_passkey_set()`
    - `BT_PASSKEY_INVALID`
  - 蓝牙网状网络（Mesh）


    - `CONFIG_BT_MESH_BLOB_IO_FLASH_WITH_ERASE`
    - `CONFIG_BT_MESH_BLOB_IO_FLASH_WITHOUT_ERASE`
  - 服务（Services）


    - `CONFIG_BT_DIS_MANUF`
    - `CONFIG_BT_DIS_MODEL`
- 开发板（Boards）

  > - 移除以下已弃用的开发板别名：
  >
  >
  >   - `arduino_uno_r4_minima`
  >   - `arduino_uno_r4_wifi`
  >   - `esp32c6_devkitc`
  >   - `esp32_devkitc_wroom/esp32/procpu`
  >   - `esp32_devkitc_wroom/esp32/appcpu`
  >   - `esp32_devkitc_wrover/esp32/procpu`
  >   - `esp32_devkitc_wrover/esp32/appcpu`
  >   - `neorv32`
  >   - `panb511evb`
  >   - `raytac_an54l15q_db/nrf54l15/cpuapp`
  >   - `scobc_module1`
  >   - `xiao_esp32c6`
  > - 以下开发板目标的旧名称已弃用，并重命名为：
  >
  >
  >   - adafruit_metro_rp2350/rp2350b/m33改为adafruit_metro_rp2350/rp2350b/m33_0。
  >   - motion_2350_pro/rp2350a/m33改为motion_2350_pro/rp2350a/m33_0。
  >   - motion_2350_pro/rp2350a/hazard3改为motion_2350_pro/rp2350a/hazard3_0。
  >   - beetle_rp2350/rp2350a/m33改为beetle_rp2350/rp2350a/m33_0。
  >   - beetle_rp2350/rp2350a/hazard3改为beetle_rp2350/rp2350a/hazard3_0。
  >   - pico2_spe/rp2350a/m33改为pico2_spe/rp2350a/m33_0。
  >   - pico_plus2/rp2350b/m33改为pico_plus2/rp2350b/m33_0。
  >   - pico_plus2/rp2350b/hazard3改为pico_plus2/rp2350b/hazard3_0。
  >   - rpi_pico2/rp2350a/m33改为rpi_pico2/rp2350a/m33_0。
  >   - rpi_pico2/rp2350a/m33/w改为rpi_pico2/rp2350a/m33_0/w。
  >   - rpi_pico2/rp2350a/m33/mcuboot改为rpi_pico2/rp2350a/m33_0/mcuboot。
  >   - rpi_pico2/rp2350a/m33/w/mcuboot改为rpi_pico2/rp2350a/m33_0/w/mcuboot。
  >   - rpi_pico2/rp2350a/hazard3改为rpi_pico2/rp2350a/hazard3_0。
  >   - xiao_rp2350/rp2350a/m33改为xiao_rp2350/rp2350a/m33_0。
  >   - xiao_rp2350/rp2350a/hazard3改为xiao_rp2350/rp2350a/hazard3_0。
  >   - rp2350_zero/rp2350a/m33改为rp2350_zero/rp2350a/m33_0。
  >   - rp2350_zero/rp2350a/hazard3改为rp2350_zero/rp2350a/hazard3_0。
  >   - rp2350b_core/rp2350b/m33改为rp2350b_core/rp2350b/m33_0。
  >   - rp2350b_core/rp2350b/hazard3改为rp2350b_core/rp2350b/hazard3_0。
  >   - w5500_evb_pico2/rp2350a/m33改为w5500_evb_pico2/rp2350a/m33_0。
  >   - w6100_evb_pico2/rp2350a/m33改为w6100_evb_pico2/rp2350a/m33_0。
  >   - w6300_evb_pico2/rp2350a/m33改为w6300_evb_pico2/rp2350a/m33_0。
- 构建系统（Build System）

  > - `CONFIG_BUILD_NO_GAP_FILL`
  > - `cmake/app/boilerplate.cmake`
  > - 开发板修订版本Kconfig片段<board>_<revision>.conf由<board>_<revision>_defconfig替代。
  > - zephyr_code_relocate(FILES ...)中的模式展开由file(GLOB ...)替代。
  > - CMake的flash、debug、debugserver、attach及rtt目标由对应West命令替代。
  > - WEST_DIR构建系统变量。
  > - ZephyrUnittest CMake包由find_package(Zephyr COMPONENTS unittest)替代。
- 控制器局域网（CAN）

  > - `bus-speed`
  > - `bus-speed-data`
- 比较器（Comparator）

  > - [nxp,kinetis-acmp](../hardware/P745_NXPKinetis模拟比较器绑定.md#dtbinding-nxp-kinetis-acmp)的nxp,enable-output-pin、nxp,use-unfiltered-output、nxp,high-speed-mode、nxp,enable-sample、nxp,filter-count、nxp,filter-period及nxp,window-mode属性。
- 计数器（Counter）

  > - `CONFIG_COUNTER_MAXIM_DS3231`
  > - [nxp,lptmr](../nxp_nuvoton_counter_binding_reference/P013_nxp_lptmr.md#std-dtcompatible-nxp-lptmr)的prescaler属性。
- 设备更新服务（hawkBit）

  > - `<zephyr/mgmt/hawkbit.h>`
- 设备树（Devicetree）

  > - `zephyr,memory-region-mpu`
- 以太网（Ethernet）

  > - CONFIG_ETH_NUMAKER对应的NuMaker以太网驱动，由[CONFIG_ETH_NUMAKER_DWC_ETHER_1000](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_NUMAKER_DWC_ETHER_1000)替代。见迁移指南。
- 调试（Debug）


  - 根据实验性API策略，直接移除CONFIG_ASSERT_CUSTOM_HEADER及其zephyr_custom_assert.h包含钩子，不设弃用期。需要自定义断言处理的应用，应覆写弱符号Zassert钩子zassert_fail、zassert_vprint及zassert_post_action。
- 可装载链接扩展（LLEXT）

  > - llext_get_fn_table由llext_get_fn_table_entry替代。
- Mbed TLS密码与TLS库

  > - `CONFIG_MBEDTLS_MD`
  > - `CONFIG_MBEDTLS_LMS`
  > - `CONFIG_MBEDTLS_TLS_VERSION_1_2`
  > - `CONFIG_MBEDTLS_DTLS`
  > - `CONFIG_MBEDTLS_TLS_VERSION_1_3`
  > - `CONFIG_MBEDTLS_TLS_SESSION_TICKETS`
  > - `CONFIG_MBEDTLS_CTR_DRBG_ENABLED`
  > - `CONFIG_MBEDTLS_HMAC_DRBG_ENABLED`
- MCU启动加载器（MCUboot）

  > - CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_WITHOUT_SCRATCH由[CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE)替代。
- 微控制器管理（MCUmgr）

  > - `CONFIG_MCUMGR_GRP_OS_INFO_HARDWARE_INFO_SHORT_HARDWARE_PLATFORM`
- 网络（Networking）

  > - `CONFIG_NET_TC_SKIP_FOR_HIGH_PRIO`
  > - `CONFIG_NET_SOCKETS_POLL_MAX`
  > - CONFIG_NET_TEST_PROTOCOL及唯一被其测试的samples/net/sockets/tcp示例。
  > - `CONFIG_NET_GPTP_CLOCK_ACCURACY_*`
  > - `net_ipv6_set_hop_limit()`
  > - `net_if_ipv4_get_netmask()`
  > - `net_if_ipv4_set_netmask()`
  > - `net_if_ipv4_set_netmask_by_index()`
  > - `openthread_state_changed_cb_register()`
  > - `openthread_state_changed_cb_unregister()`
  > - `openthread_start()`
  > - `openthread_api_mutex_lock()`
  > - `openthread_api_mutex_try_lock()`
  > - `openthread_api_mutex_unlock()`
  > - `struct openthread_state_changed_cb`
  > - `TLS_CREDENTIAL_SERVER_CERTIFICATE`
  > - `start_11r_roaming`
  > - `IEEE802154_HW_SLEEP_TO_TX`
- Nordic半导体

  > - [nordic,owned-memory](../memory_protection_binding_reference/P010_nordic_owned-memory.md#std-dtcompatible-nordic-owned-memory)及[nordic,owned-partitions](../mtd_microchip_nordic_nxp_binding_reference/P011_nordic_owned-partitions.md#std-dtcompatible-nordic-owned-partitions)的owner-id、perm-read、perm-write、perm-execute、perm-secure及non-secure-callable属性。
  > - CONFIG_BOARD_ENABLE_CPUNET由[CONFIG_SOC_NRF53_CPUNET_ENABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF53_CPUNET_ENABLE)替代。
  > - `CONFIG_GPIO_AS_PINRESET`
  > - CONFIG_NRFS_LOCAL_DOMAIN_DVFS_SCALE_DOWN_AFTER_INIT由[CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_REQ_LOW_FREQ](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_HSFLL_LOCAL_REQ_LOW_FREQ)替代。
  > - `CONFIG_SOC_DCDC_NRF52X`
  > - `CONFIG_SOC_DCDC_NRF52X_HV`
  > - `CONFIG_SOC_DCDC_NRF53X_APP`
  > - `CONFIG_SOC_DCDC_NRF53X_NET`
  > - `CONFIG_SOC_DCDC_NRF53X_HV`
- 可移植操作系统接口（POSIX）

  > - `CONFIG_POSIX_READER_WRITER_LOCKS`
- 随机数（Random）

  > - `CONFIG_CTR_DRBG_CSPRNG_GENERATOR`
  > - `CONFIG_CS_CTR_DRBG_PERSONALIZATION`
- 命令行（Shell）

  > - kernel log_level由log enable替代。
- 串行外设接口（SPI）

  > - 移除[SPI_CONFIG_DT](../hardware/P318_SPI公共接口.md#gaf7d4888063e5b739f2a3bee295962bfe)、[SPI_CONFIG_DT_INST](../hardware/P318_SPI公共接口.md#ga67837cbae6f29c5f8ad9a05dbc9b05f8)、[SPI_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga43857c934651c4bfb3823a5080a4a294)、[SPI_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#gac9537325ca3188121d0f8c382c798ca1)、[SPI_DT_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga1eec8a77be8a512e8b0fa74d270877e5)、[SPI_DT_INST_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga4e5633f6e8da22f4c00a723a669b2d9a)及[SPI_CS_CONTROL_INIT](../hardware/P318_SPI公共接口.md#ga81308d27cd78e65f0a3ddaa918f2a74a)中的可选delay参数。
- 流式Flash（Stream Flash）

  > - `stream_flash_erase_page()`
- 跟踪（Tracing）


  - 移除_track_list_k_*对象跟踪链表头、SYS_PORT_TRACK_NEXT()及include/zephyr/tracing/tracking.h。对象跟踪现在通过[对象核心框架（Object Core Framework）](../kernel/P048_内核对象核心.md#object-cores-api)枚举对象。
- Zephyr测试框架（ZTest）

  > - `CONFIG_ZTEST_SHUFFLE_SUITE_REPEAT_COUNT`
  > - `CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT`
- 移除自Zephyr 4.0起弃用的west sign对imgtool的支持。
- 移除自Zephyr 4.3起弃用的字典日志脚本scripts/logging/dictionary/log_parser_uart.py，请改用[scripts/logging/dictionary/live_log_parser.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/logging/dictionary/live_log_parser.py)。
- 移除west flash、west debug及其他调用运行器（Runner）的命令中的--skip-rebuild选项，该选项自Zephyr 4.3起弃用。请改用--no-rebuild。

<a id="deprecated-apis-and-options"></a>

### 已弃用的API与选项（Deprecated APIs and Options）


- 音频编解码器（Audio Codec）


  - 弃用audio_codec_api结构体，音频编解码器驱动现在应使用[DEVICE_API](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)宏声明驱动API。
- 蓝牙（Bluetooth）


  - 弃用[CONFIG_BT_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CUSTOM)协议栈选择项。它源于整个蓝牙主机可在Zephyr蓝牙API之后卸载实现的时期，树内已无使用者；HCI传输现在是常规设备驱动。基于HCI的[CONFIG_BT_HCI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)是树内仅存选项，而choice本身保留为树外协议栈扩展点。
  - 弃用HCI驱动的setup()操作、[bt_hci_setup()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)、[bt_hci_setup_params](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__setup__params.html)、[CONFIG_BT_HCI_SETUP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)及H:4驱动的bt_h4_vnd_setup()钩子。驱动应改为在[bt_hci_driver_api.open](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__api.html#a889d9a3553c4dd04595198dcfaf61d23)中经自己的传输完成厂商专用初始化。见迁移指南。
- 构建系统（Build System）


  - 弃用zephyr_file_copy() CMake函数，请改用CMake原生file(COPY_FILE ...)命令。
- 时钟控制（Clock Control）


  - 弃用函数z_nrf_clock_control_get_onoff()，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用宏CLOCK_CONTROL_NRF_K32SRC_ACCURACY，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用宏CLOCK_CONTROL_NRF_K32SRC，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用宏CLOCK_CONTROL_NRF_SUBSYS_HFAUDIO，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用宏CLOCK_CONTROL_NRF_SUBSYS_HFAUDIO，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用宏CLOCK_CONTROL_NRF_SUBSYS_HF24M，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用宏CLOCK_CONTROL_NRF_SUBSYS_HF24M，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用宏CLOCK_CONTROL_NRF_SUBSYS_HF，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用枚举clock_control_nrf_type，详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用[CONFIG_CLOCK_CONTROL_NRF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF)及所有依赖它的Kconfig选项，详情见迁移指南。相关定义位于drivers/clock_control/Kconfig.nrf及modules/hal_nordic/nrfx/Kconfig。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
- 控制器局域网（Controller Area Network，CAN）


  - 弃用[can_set_state_change_callback()](../hardware/P362_CAN控制器接口.md#gacda2bc21fa0cbd7b3406dd096827923c)，改用[can_init_state_change_callback()](../hardware/P362_CAN控制器接口.md#gabf813d9f21982f674b213708adee9e96)、[can_add_state_change_callback()](../hardware/P362_CAN控制器接口.md#gace0dd2797a133bd293d34a9ac5348e2a)及[can_remove_state_change_callback()](../hardware/P362_CAN控制器接口.md#ga5c1c7633e020aec2936a6ce3ba68b256)。新API允许注册多个CAN控制器状态变化回调。（[GitHub #117889](https://github.com/zephyrproject-rtos/zephyr/issues/117889)）
- CPU负载（CPU Load）


  - 弃用[CONFIG_CPU_LOAD_METRIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_METRIC)及[cpu_load_metric_get()](../observability/P049_CPU负载接口.md#ga3333539cf7d8a6916cbbec9cd1f5bf59)。CPU负载指标模块已并入统一CPU负载模块；请使用[CONFIG_CPU_LOAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD)，选择[CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_BACKEND_RUNTIME_STATS)后端，并调用[cpu_load_get_cpu()](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)。（[CPU负载（CPU Load）](../observability/P007_CPU负载.md#cpu-load)）
- 数字麦克风接口（DMIC）


  - 弃用_dmic_ops结构体，数字麦克风（DMIC）驱动现在应使用[DEVICE_API](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)宏声明驱动API。
- 电量计（Fuel Gauge）


  - 弃用多个电量计（Fuel Gauge）属性枚举及联合体字段，改用明确包含单位后缀的新版本。
- 远距离无线通信（LoRa）


  - [lora_recv_duty_cycle()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5d1802eed6067734ca45c70e3114b272)重命名为[lora_recv_duty_cycle_async()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga2192d812e6203f6361b8beaeb1d7361c)，与现有同步／异步（Sync / Async）命名约定一致。
- 微控制器管理（MCUmgr）


  - 弃用[smp_transport_get_mtu_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__smp.html#ga2085e89b99428a61596d90e084d7c5e2)类型及[smp_transport_api_t](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport__api__t.html)中的get_mtu成员，因为SMP层不使用它们。详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 弃用[CONFIG_MCUMGR_TRANSPORT_UART_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UART_MTU)及[CONFIG_MCUMGR_TRANSPORT_SHELL_MTU](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SHELL_MTU)，因为它们仅设置已弃用get_mtu回调的返回值。详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
- Nordic半导体


  - 弃用内部SoC平台Kconfig符号NRF_PLATFORM_HALTIUM及NRF_PLATFORM_LUMOS，请改用具体的SOC_SERIES_*选项。
  - Sysbuild Kconfig选项SB_CONFIG_NRF_HALTIUM_GENERATE_UICR重命名为SB_CONFIG_NRF_GENERATE_UICR。
  - Nordic SoC头文件<haltium_power.h>及<haltium_pm_s2ram.h>分别重命名为<soc_power.h>及<soc_pm_s2ram.h>。
- 树莓派（Raspberry Pi）


  - 为使RP2350双核簇命名符合硬件模型v2（Hardware Model v2），弃用SOC_RP2350A_HAZARD3、SOC_RP2350A_M33、SOC_RP2350B_HAZARD3及SOC_RP2350B_M33，以及soc.yml中对应的hazard3／m33 CPU簇名称，改用SOC_RP2350A_HAZARD3_0、SOC_RP2350A_M33_0、SOC_RP2350B_HAZARD3_0及SOC_RP2350B_M33_0，以及hazard3_0／m33_0簇名称。旧Kconfig符号及soc.yml条目将在未来版本移除；树内开发板均已迁移。
- 实时输入输出（RTIO）


  - 弃用RTIO_SQE_CANCELED标志。取消状态移入[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)的原子状态字，应通过[rtio_iodev_sqe_is_canceled()](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga8c497b13ca1b4f3c1988b1091244e7bc)检查。详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
- 环形缓冲区（Ring Buffer）


  - 弃用环形缓冲区条目API：ring_buf_item_init()、ring_buf_item_put()、ring_buf_item_get()及ring_buf_item_space_get()，改用[sys_ringq](../ringq_reference/P002_环形队列结构.md)，见[sys_ringq数据结构（Data Structure）](https://docs.zephyrproject.org/latest/kernel/data_structures/ringq.html#fixed-size-ringq-api)。
  - 弃用零拷贝申请／完成（Claim/Finish）API：ring_buf_put_claim()、ring_buf_put_finish()、ring_buf_get_claim()及ring_buf_get_finish()，改用[ring_buf_put_ptr()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga7877a84b56da9077422dd732e25654d9)／[ring_buf_get_ptr()](../ringbuffer_reference/P001_环形缓冲区公共接口.md#gad3990b5a2ae63166b76c6d1db179a215)。仍使用旧API的代码必须启用[CONFIG_RING_BUFFER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RING_BUFFER)。
  - 弃用[CONFIG_RING_BUFFER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RING_BUFFER)。环形缓冲区API现在仅由头文件实现且始终可用，不再需要该选项。它仅作为已弃用的兼容开关，在树外代码迁移期间恢复旧Claim/Finish及条目API。
- 网络缓冲区（Network Buffers）


  - 弃用[net_buf_max_len()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga65924b8234c91dfc09069ba06242a6b7)及[net_buf_simple_max_len()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7476ec7222d074e7dc9783e7ed9cd800)，改用[net_buf_tailroom()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaecbc6adf16469e3366c88445ea7a553a)及[net_buf_simple_tailroom()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga73e2c42fc23e857a46553084b747c996)。详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
- 网络（Networking）


  - 弃用链路本地多播名称解析（LLMNR）支持，即[CONFIG_LLMNR_RESOLVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLMNR_RESOLVER)及[CONFIG_LLMNR_RESPONDER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLMNR_RESPONDER)。LLMNR正逐步退出使用，请改用多播DNS（mDNS）：[CONFIG_MDNS_RESOLVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESOLVER)／[CONFIG_MDNS_RESPONDER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER)。
- 网络链路层（Networking Link Layer）


  - 弃用[CONFIG_NET_L2_PTP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP)，改用[CONFIG_NET_L2_PTP_TIMESTAMPING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。
- 串行外设接口（SPI）


  - SPI API现在使用控制器／外围设备（Controller / Peripheral）及串行数据输出／输入（SDO / SDI）术语。弃用SPI_OP_MODE_MASTER／SPI_OP_MODE_SLAVE，改用[SPI_OP_MODE_CONTROLLER](../hardware/P318_SPI公共接口.md#gace0f0d954c2bd7d603c4003289c11102)／[SPI_OP_MODE_PERIPHERAL](../hardware/P318_SPI公共接口.md#gaa1f42ffeac36380f4d1d8f84bda2990b)；[spi_config](../hardware/P320_SPI控制器配置结构.md).slave改为peripheral；SPI_MOSI_OVERRUN_*宏改为[SPI_SDO_OVERRUN_UNKNOWN](../hardware/P318_SPI公共接口.md#ga1dbef324b98a8921507de0da1c4e4fa6)、[SPI_SDO_OVERRUN_DT](../hardware/P318_SPI公共接口.md#gaf66331d56f20e0c37f2a3cff998c6bce)及[SPI_SDO_OVERRUN_DT_INST](../hardware/P318_SPI公共接口.md#ga0e05910cd0be7211389514b7b4edc0cc)；CONFIG_SPI_SLAVE改为[CONFIG_SPI_PERIPHERAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_PERIPHERAL)；设备树compatible zephyr,bt-hci-spi-slave改为[zephyr,bt-hci-spi-peripheral](../bluetooth_st_transport_binding_reference/P010_zephyr_bt-hci-spi-peripheral.md#std-dtcompatible-zephyr-bt-hci-spi-peripheral)。迁移指南所列绑定的mosi-gpios／miso-gpios类属性也已弃用。
- 定时器（Timer）


  - 新增[sys_clock_no_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gacb9fad0efce687f8701dd90408a2ec7c)钩子处理[CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE)，替代以ticks=K_TICKS_FOREVER调用[sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)。
  - 新增[sys_clock_idle_enter()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaab6df10ce3054ee84921aa90a1bc53d1)钩子处理进入低功耗状态，替代以idle=true调用[sys_clock_set_timeout()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga48b323a58eb10bcb05eba2c273a47181)。
- 通用串行总线（USB）


  - 弃用[st,stm32u5-otghs-phy](../phy_binding_reference/P007_st_stm32u5-otghs-phy.md#std-dtcompatible-st-stm32u5-otghs-phy)的clock-reference属性。请不再指定此属性，底层驱动已不需要它。
- 视频（Video）


  - 视频驱动API头文件<zephyr/drivers/video.h>中的全部函数移至视频子系统头文件<zephyr/video/video.h>，应用仅需更新#include路径。
- Zephyr元工具West


  - 弃用west spdx --init。启用[CONFIG_BUILD_OUTPUT_META](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_OUTPUT_META)的构建现在会自动向CMake请求west spdx读取的基于文件的API，无需在配置前准备构建目录。见[软件物料清单：west spdx（Software Bill of Materials）](../west/P008_其他Zephyr扩展命令.md#west-spdx)。
- 工作队列（Work Queue）


  - 弃用k_work_q.thread，改用k_work_q.thread_id。

<a id="new-apis-and-options"></a>

### 新增API与选项（New APIs and Options）


- 模数转换器（ADC）


  - 新增可选[adc_driver_api.ref_get](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#a1566edae1939a32d5ff712e38c4bb998)回调及[adc_ref_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7a4d12848b6ffb948b60f080abe3ac4d)，使应用与[adc_raw_to_millivolts_dt()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga11cf9c8f345a83f66704af83a2a26911)可针对任意[adc_reference](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga91b0f997d73739cf9f7349b7581e1f56)，使用由驱动维护的运行时毫伏换算基准。当回调为NULL时，[ADC_REF_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709)仍以静态[adc_driver_api.ref_internal](https://docs.zephyrproject.org/latest/doxygen/html/structadc__driver__api.html#ad12d4f5fa0eb0e45e14553deab0edbed)为后备；[adc_ref_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7a4d12848b6ffb948b60f080abe3ac4d)失败时，[adc_raw_to_millivolts_dt()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga11cf9c8f345a83f66704af83a2a26911)回退到通道设备树属性zephyr,vref-mv。
  - [CONFIG_ADC_STM32_VREFINT_CALIBRATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_STM32_VREFINT_CALIBRATE)：初始化及sequence.calibrate时，通过VREFINT测量VREF+。
- 架构（Architectures）


  - [CONFIG_ARM_MPU_CM7_UNMAPPED_REGION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_MPU_CM7_UNMAPPED_REGION)：为Arm Cortex-M7未映射地址设置兜底MPU区域，规避勘误1013783。
  - [CONFIG_CORTEX_M_ERRATUM_440977_WORKAROUND](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_ERRATUM_440977_WORKAROUND)：写入BASEPRI提高优先级后保留指令同步屏障（ISB）。Arm Cortex-M7默认启用，因为其r0p0／r0p1内核受勘误440977影响。其他Cortex-M内核不再在中断锁定／解锁快速路径执行屏障，从而加快内核高频路径。
  - [CONFIG_EXCEPTION_DUMP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXCEPTION_DUMP)：默认启用；对空间受限的构建可禁用，将故障处理器输出从编译结果中移除。
  - [CONFIG_RISCV_ISA_EXT_ZKR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_ISA_EXT_ZKR)：RISC-V Zkr熵源扩展，根据设备树riscv,isa-extensions属性启用。
  - [CONFIG_RISCV_USER_STRING_NLEN_VALIDATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_USER_STRING_NLEN_VALIDATE)：RISC-V的arch_user_string_nlen()逐块验证用户字符串，不依赖故障修复机制，适用于加载访问故障不精确的SoC。
  - [CONFIG_RISCV_SOC_HAS_SYSCALL_INTMASK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_SOC_HAS_SYSCALL_INTMASK)：RISC-V SoC钩子，在用户模式系统调用主体内屏蔽中断，无需清除mstatus.MIE。
  - [CONFIG_RISCV_SOC_SYSCALL_CLOSE_ECALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_SOC_SYSCALL_CLOSE_ECALL)：RISC-V SoC钩子，在用户模式系统调用主体执行前退出ecall异常，适用于该异常尚未结束时无法递送调用主体所触发故障的SoC。
- 音频（Audio）


  - [`pcm_stream_cfg.gain_db`](https://docs.zephyrproject.org/latest/doxygen/html/structpcm__stream__cfg.html#a64a94db251a8ff9358040bc23cba6de5)
  - [`audio_codec_eq_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structaudio__codec__eq__cfg.html)
- 蓝牙（Bluetooth）


  - 音频（Audio）


    - [`bt_aics_client_free_instance()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gab660d2d4603de3837a3b93ce11e4d0fd)
    - [`bt_ascs_register()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga04eddf75bc1f2deafee5d6b234dd5b07)
    - [`bt_ascs_unregister()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html#ga2a87430dd2b2a04985c2faffb0b033a3)
    - [`bt_bap_unicast_client_qos_from_group()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gad963bdda290df96036a68b00cc940eca)
    - [`bt_bap_qos_cfg_eq()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gad106ae43201100940d9145d291fe9ca3)
    - [`bt_bap_unicast_group_info.c_to_p_interval`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#aa310b32478893830907878f59a65f876)
    - [`bt_bap_unicast_group_info.p_to_c_interval`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a70883292203e5f37f71238f0b659aa31)
    - [`bt_bap_unicast_group_info.c_to_p_latency`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a9c12fa3c837c300528dce41c8789e301)
    - [`bt_bap_unicast_group_info.p_to_c_latency`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a25208a4e06afd726c6f6f0714233526a)
    - [`bt_bap_unicast_group_info.framing`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a0cfbd31f735e4d18ac95f2e7d2a31f9a)
    - [`bt_bap_unicast_group_info.packing`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#ac701205d557f5cdb27663e2521082681)
    - [`bt_bap_unicast_group_info.has_been_connected`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a180fe8c6c0081da2f2cb38b3df0fadaf)
    - [`bt_bap_unicast_group_info.c_to_p_ft`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a1e49ada1c3a60ac73e29cc32f95a9533)
    - [`bt_bap_unicast_group_info.p_to_c_ft`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#a15731dd811989ea465f2b2b490502db4)
    - [`bt_bap_unicast_group_info.iso_interval`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__info.html#aee9990d7b3a7e7c8230fb5f4eb7198b8)
    - [`bt_cap_initiator_cb.unicast_start_codec_configured`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a64c9b0fb0bdfcc7434d8f2854a20a666)
    - [`bt_cap_initiator_cb.unicast_start_qos_configured`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a5ef6349113a1c786a0441b6c494286d1)
    - [`bt_cap_initiator_cb.unicast_start_enabled`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a06b2f73a6f6f8f3f88cd4c5bd87f4fbc)
    - [`bt_cap_initiator_cb.unicast_start_connected`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a8452b3c6775d1608272893719dd3887d)
    - [`bt_cap_initiator_cb.unicast_start_started`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a65d8dd89661f92b2e71e90b69a8b4320)
    - [`bt_cap_initiator_cb.unicast_stop_disabled`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a8001c24d64df0881dbfd78382c2a2db7)
    - [`bt_cap_initiator_cb.unicast_stop_stopped`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a8c20d933b9ee1c1412d7ad719ff24683)
    - [`bt_cap_initiator_cb.unicast_stop_released`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__initiator__cb.html#a8f659ac17a242eab12c404f59e42d149)
    - [`bt_vocs_client_free_instance()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html#gaf210fd531117b9a22a52746266c72c08)
  - 经典蓝牙（Classic）


    - [`CONFIG_BT_SMP_DERIVE_LTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_DERIVE_LTK)
    - [`CONFIG_BT_SMP_DERIVE_LK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_DERIVE_LK)
    - [`bt_sdp_unregister_service()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga71e7d75850becf4ead62668c8e7bebbc)
  - HCI驱动（HCI Drivers）


    - [`BT_HCI_PKT_CMD_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5c26db578cf6b427e7009fbbd692253e)
    - [`BT_HCI_PKT_CMD_DEFINE_STATIC`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga0cc8ce4451e316f72cceda47c3a68b10)
    - [BT_HCI_PKT_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga97349aa18498cfd9a61817f1d149aa29)及[BT_HCI_PKT_CMD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga08079006c088d639abc45077c7a09532)。
    - [`bt_hci_pkt_reset_cmd()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga7f6c2d3674275bb9ce6752cf3f7e3228)
    - [`bt_hci_pkt_push_cmd_hdr()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#gac9d4ade374ccf35895cf601cdd6b3f79)
    - [`bt_hci_pkt_pull_cmd_complete()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5494d5cdc68840408f6b4b254dd474c9)
    - [`bt_hci_pkt_pull_cmd_status()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga591c10d3d94a29be93ff5c4eb690201f)
    - [bt_hci_pkt_parse_cmd_rsp()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga588ed90a133f526c4abfa3fcd87ad8e5)及[bt_hci_pkt_cmd_rsp](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__pkt__cmd__rsp.html)。
    - [`bt_hci_lockstep`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__lockstep.html)
    - [`bt_hci_lockstep_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga02ea7a0ad2bbb7d8ee9845122e34f8ab)
    - [`bt_hci_lockstep_feed()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gacb84fdafc6376483e12a8b7ec391fa7c)
    - [`bt_hci_lockstep_cmd_send_sync()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)
    - [`bt_hci_lockstep_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga1d2d42b2db398cf4449b337588897f56)
    - [bt_h4_vnd_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html#ga4ac11c5a18b0891a04bb791e2f7c15bd)及[CONFIG_BT_H4_VND_OPEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_H4_VND_OPEN)。
    - [bt_hci_driver_data](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__data.html)及[bt_hci_driver_config](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__config.html)。
    - [BT_DT_HCI_DRIVER_CONFIG_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga3c8d5a12ea0c52d0934ee57c213f1fbe)及[BT_DT_HCI_DRIVER_CONFIG_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga6814df9213fa7e3d6506dcf25d6feae4)。
    - [bt_hci_recv()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga407beb20238b8fe6fdbd4ef199eb1f6c)及[bt_hci_recv_err()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaad2dc7f911913468a1440fad91cb3d62)。
    - [bt_hci_set_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga9df830679cdec440f96e37b608c7fdf7)及[bt_hci_get_public_addr()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)。
    - [`bt_hci_can_close()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga4baab0790149536873e5d9e0cb14359f)
  - 主机（Host）


    - [`bt_att_get_max_notify_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga653a0fc8803d7deebb0be93c8cf7910a)
    - [`bt_att_get_max_indicate_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2edca82fff038f16e6f7d09bc1db59a8)
    - [`bt_conn_take()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf073384538a67c242b00150904176f66)
    - [`bt_conn_drop()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf1aeec9b9893450423cf066a6f471824)
    - [`bt_id_reset_irk()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7a595421c232b15ad96b52f0300fd960)
    - [`BT_IRK_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga17419cd0fcc4660f09ac5dbad3a042f2)
    - [`bt_iso_chan_state_str()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4d4c9b8d6d83abcc8d3b337101922800)
    - [`bt_iso_chan_ops.send_failed`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__ops.html#a750ac5c12155602a32b1f02bb2dc8fba)
    - [`bt_iso_get_chan_by_conn()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa3407502145a77e08993220f7ce51b4a)
    - [`bt_le_per_adv_update_did()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga59e9fc635846ab92af19d483de58ed88)
    - [bt_le_adv_param.tx_power](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__adv__param.html#a1c09c2bcf9600a644e194ecd3367d200)及[BT_LE_ADV_OPT_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56)，用于为每个扩展广播集请求特定发送功率。
    - [`bt_conn_cb.le_param_update_rejected`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__cb.html#a2179943b5f64302e38c64f075a5b6a9e)
    - 新增HCI设备特殊处理标记（Quirk）BT_HCI_QUIRK_NO_FLOW_CONTROL，面向声称支持却拒绝控制器到主机流量控制命令的控制器。
    - [bt_rfcomm_dlc.rx_credit_limit](https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__dlc.html#a27157f693d91aac6aaafe1bd70593404)用于配置每个数据链路连接（DLC）的初始接收信用数（RX Credit Count）。
    - [bt_rfcomm_dlc_recv_complete()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2ce765351798976136c3096a9a7f9465)向对端归还接收信用。应用可在[bt_rfcomm_dlc_ops.recv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__dlc__ops.html#ab8ef2f8c1d27eee20d0b5e7fce6f7354)回调中返回-EINPROGRESS，将缓冲区释放及流控信用补充延迟到处理完成。
    - [bt_le_bond_addr_res_support()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5b5e51f79896d674bf6b70b2251e79d4)、[bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)及[bt_conn_auth_info_cb.addr_res_support_read](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__auth__info__cb.html#a44896258f0221d4f0a55cc1fb785b06c)。
    - [`BT_LE_SCAN_OPT_EXT_FILTER_POLICY`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a79cdd7e96e41f4236642edfbcb1b666d)
    - [`CONFIG_BT_SCAN_EXT_FILTER_POLICY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_EXT_FILTER_POLICY)
    - [`bt_le_scan_recv_info.direct_addr`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__recv__info.html#a8885283f39e3ece5d7ff7d5b5d588696)
  - 蓝牙网状网络（Mesh）


    - [`bt_mesh_lpn_timing`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__lpn__timing.html)
    - [`bt_mesh_stat_lpn_timing_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#ga240344c421ff810578b9d0e06a11fe56)
    - [`bt_mesh_stat_lpn_timing_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__stat.html#gaf4ca44edb393329569052707aa9a8f18)
    - [`CONFIG_BT_MESH_LPN_OFFER_WAIT_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LPN_OFFER_WAIT_TIMEOUT)
- 时钟控制（Clock Control）


  - `CLOCK_CONTROL_NRF_ONOFF`
  - compatible为nordic,nrf-clock-hfclk、nordic,nrf-clock-lfclk、nordic,nrf-clock-hfclk192m、nordic,nrf-clock-hfclk24m、nordic,nrf-clock-hfclkaudio、nordic,nrf-clock-xo及nordic,nrf-clock-xo24m的设备，现在支持clock_control_request()、clock_control_request_sync()、clock_control_release()及clock_control_cancel_or_release()。详情见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
- 计数器（Counter）


  - [CONFIG_COUNTER_CAPTURE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_CAPTURE)、[counter_capture_dt_spec](../timer_reference/P033_计数器捕获设备树规格.md)、[counter_capture_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__capture.html#ga13c4ff7dbd26816076419d15fb4f541e)、[counter_capture_configure_64()](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__capture.html#gaddc084e8532204e4fb2d0970318203cb)、[counter_enable_capture()](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__capture.html#gae4bfc624cbbe94fa05ee123b28ceeae5)及[counter_disable_capture()](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__capture.html#ga21af0e583d2b23d7236659a5693e6437)，并提供设备树辅助机制配置输入捕获（Input Capture）。（[GitHub #89127](https://github.com/zephyrproject-rtos/zephyr/issues/89127)、#108713）（[GitHub #108713](https://github.com/zephyrproject-rtos/zephyr/issues/108713)）
- CPU调频（CPUFreq）


  - [`CONFIG_CPU_FREQ_POLICY_TIMING_NOISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_POLICY_TIMING_NOISE)
- 密码功能（Crypto）


  - [`CRYPTO_CIPHER_MODE_CFB`](../crypto/P012_密码算法会话接口.md#ggaeedaf8017f8d6518f7dedef365bbae43ae8b346d201fa958d301b846f12ebe06a)
  - [`CRYPTO_CIPHER_MODE_OFB`](../crypto/P012_密码算法会话接口.md#ggaeedaf8017f8d6518f7dedef365bbae43ab2f91833207039719131357a81fb55a3)
  - [`cipher_cfb_op()`](../crypto/P012_密码算法会话接口.md#gaca8a543c5e1b0bd8d4a6a8982cca8d8c)
  - [`cipher_ofb_op()`](../crypto/P012_密码算法会话接口.md#gaa7772d10a48395f93eb035480de15308)
  - [CRYPTO_HASH_ALGO_SHA3_224](../crypto/P023_密码散列会话接口.md#ggaaea88501aa8243eacc8c57ac0914ac7aae59cb77c519cf091146bb342e58c30b2)、[CRYPTO_HASH_ALGO_SHA3_256](../crypto/P023_密码散列会话接口.md#ggaaea88501aa8243eacc8c57ac0914ac7aad470c06cca5794bc694f33c79ad5a0f9)、[CRYPTO_HASH_ALGO_SHA3_384](../crypto/P023_密码散列会话接口.md#ggaaea88501aa8243eacc8c57ac0914ac7aa9412f53aa2c8e5656cdc221ff9264f15)及[CRYPTO_HASH_ALGO_SHA3_512](../crypto/P023_密码散列会话接口.md#ggaaea88501aa8243eacc8c57ac0914ac7aa696675338b646149dbaff2a81fe0b827)。（[GitHub #118321](https://github.com/zephyrproject-rtos/zephyr/issues/118321)）
  - [CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS)提供实验性PSA Crypto硬件加速，使用STM32的AES、CRYP、SAES及HASH外设。（[GitHub #119888](https://github.com/zephyrproject-rtos/zephyr/issues/119888)）
- 调试（Debug）


  - 引入ZASSERT，提供按模块／文件细分的断言机制。各源文件通过ZASSERT_MODULE(<MODULE>)选择断言模块，级别由CONFIG_ASSERT_MODULE_<MODULE>_LEVEL解析，可按文件覆写。共有四级：关闭（Off，编译时移除）、简略（Terse，仅检查）、普通（Normal，检查与位置）、详细（Verbose，检查、位置、条件及消息）。可通过弱符号钩子zassert_fail()、zassert_vprint()及zassert_post_action()定制失败行为。旧__ASSERT()系列作为ZASSERT DEFAULT模块上的轻量兼容层，基本保持原有用法。
- 设备树（Devicetree）


  - [`DT_IRQN_BY_NAME`](../dt_irq_reference/P001_设备树中断属性宏.md#ga40d8bb5d041e4eba011da71357920c43)
  - [`DT_INST_IRQN_BY_NAME`](../dt_instance_reference/P001_设备树驱动实例宏.md#gabb3150acf98012f7cb2781c803d69d14)
- 显示（Display）


  - [`PIXEL_FORMAT_YUYV`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca5c905dcfaca35e58c14513f2e3a61091)
  - [`PANEL_PIXEL_FORMAT_YUYV`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaee786c1944da1234c8c258be385fda92)
- 熵（Entropy）


  - [CONFIG_ENTROPY_RISCV_ZKR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_RISCV_ZKR)：基于RISC-V Zkr扩展seed控制与状态寄存器（CSR）的架构熵驱动。
- FIDO2身份认证


  - [`fido2_up_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7fb0da6d327ef0be220d32558ea6be2)
  - [`FIDO2_BLE_SERVICE_UUID_VAL`](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#aaca1dbd2854544f0c691d7eba104a065)
  - [`FIDO2_BLE_SERVICE_DATA_PAIRING_MODE`](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a5e293d6509138c129b1f8c78b27cec45)
  - [`CONFIG_FIDO2_TRANSPORT_BLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_TRANSPORT_BLE)
  - [`CONFIG_FIDO2_BLE_REQUIRE_AUTHENTICATED_LINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_BLE_REQUIRE_AUTHENTICATED_LINK)
  - [`CONFIG_FIDO2_BLE_RX_WORKQ_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_BLE_RX_WORKQ_STACK_SIZE)
  - [`CONFIG_FIDO2_BLE_CONTROL_POINT_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_BLE_CONTROL_POINT_LENGTH)
  - [`CONFIG_FIDO2_BLE_RX_QUEUE_DEPTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_BLE_RX_QUEUE_DEPTH)
  - [`CONFIG_FIDO2_BLE_TX_FRAME_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_BLE_TX_FRAME_COUNT)
  - [`CONFIG_FIDO2_BLE_KEEPALIVE_INTERVAL_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_BLE_KEEPALIVE_INTERVAL_MS)
  - [`CONFIG_FIDO2_BLE_RX_TIMEOUT_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_BLE_RX_TIMEOUT_MS)
- 电量计（Fuel Gauge）


  - [fuel_gauge_set_buffer_prop()](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac63f43b6023b9f2183001d6876fe328a)及可选[fuel_gauge_driver_api.set_buffer_property](https://docs.zephyrproject.org/latest/doxygen/html/structfuel__gauge__driver__api.html#aa9963e6744222271ab45e2eabbf69f87)回调用于写入可变长度缓冲区属性，与[fuel_gauge_get_buffer_prop()](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga7e6cb77d2d4dd7a0feb25c92d031614c)对称。
- 触觉反馈（Haptics）


  - [`haptics_monitor`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)
  - [`haptics_monitor_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaf86396239e200ecf8ea00fe339e416ca)
  - [`haptics_source`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)
  - [`haptics_trigger_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabd96eff4adc560173e4e887e09dcb34b)
  - [`haptics_config`](../hardware/P151_触觉源配置联合体.md)
  - [`haptics_calibrate()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaa8a7f36b4b37f7512f9f46133d9f4d1b)
  - [`haptics_monitor_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabf1e580def265fe9bf95f2116d30e6b2)
  - [`haptics_monitor_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gad379139afa8aff76647f180c80706f79)
  - [`haptics_select_source()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga891fa4c05a4844a658603651e8aabfc5)
  - [`haptics_set_level()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaae134ab4f57a7301dbc16cb379f08192)
  - [`haptics_set_trigger()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga26851a2c1eafd8da31a3087b0219c6bf)
  - [`haptics_stream_samples()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga94b7c216edd6adf14a354b64dbc8a396)
  - [`haptics_trigger()`](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gafb18ed221c2ae5e5b643130bc3d3c8ec)
- 硬件自旋锁（HWSPINLOCK）


  - [`HWSPINLOCK_SPINLOCK_ARRAY_DT_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gacca85debd57e9b20ed7c31725dd378ed)
  - [`HWSPINLOCK_SPINLOCK_ARRAY_DT_INST_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#ga5e8973a8983aec78817f51e3dd2ca96f)
  - [`HWSPINLOCK_COMMON_CONFIG_FROM_DT_NODE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#gaee1e3139a76d606f3e06de3e8396fc0e)
  - [`HWSPINLOCK_COMMON_CONFIG_FROM_DT_INST`](https://docs.zephyrproject.org/latest/doxygen/html/group__hwspinlock__interface.html#ga407261f758074c18d96cdf23b5df776f)
- Kconfig配置系统


  - 新增预处理函数dt_partition_mtd。（[GitHub #111599](https://github.com/zephyrproject-rtos/zephyr/issues/111599)）
- 内核（Kernel）


  - [`k_obj_core_evict_range()`](../object_core_reference/P001_对象核心公共接口.md#ga64185c8579bc615f7c5baeeba7f1f1c9)
  - [`CONFIG_OBJ_CORE_MAX_DYNAMIC_OBJECTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OBJ_CORE_MAX_DYNAMIC_OBJECTS)
  - [`CONFIG_OBJ_CORE_EVICT_ON_FREE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OBJ_CORE_EVICT_ON_FREE)
  - [`CONFIG_OBJ_CORE_QUEUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OBJ_CORE_QUEUE)
  - [`k_thread_runtime_stats_is_enabled()`](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html#a8954eb04bd70207b9aeff112782a1e40)
  - [`atomic_test_and_set_bit_to()`](https://docs.zephyrproject.org/latest/doxygen/html/group__atomic__apis.html#gab3a75498f5cff5c142b609560157e65a)
  - [`K_MSGQ_DEFINE_STATIC`](../msgstack_reference/P001_消息队列公共接口.md#ga15e39d40c8659be688d41e2201959c4c)
  - [`K_MSGQ_DEFINE_TYPE`](../msgstack_reference/P001_消息队列公共接口.md#gab17e888412dd4d299dc68816a24de78a)
  - [`K_MSGQ_DEFINE_STATIC_TYPE`](../msgstack_reference/P001_消息队列公共接口.md#ga0f01b9e30429458e184f202c3701c54a)
  - [`k_sleep_ticks()`](../thread_core_reference/P001_线程公共接口.md#ga5ad6bcbcf89f9a9fbf6929388e2a7842)
  - 新增带命名空间前缀的中断控制API，建议新代码使用；原无前缀名称仍完整支持。新名称为[k_irq_lock()](../fatal_irq_reference/P007_中断服务接口.md#gad4a27741fdbb40d4a7d1c7cea10eff03)、[k_irq_unlock()](../fatal_irq_reference/P007_中断服务接口.md#ga4a5a523c81da5c75d25c58d7702b7144)、[k_irq_enable()](../fatal_irq_reference/P007_中断服务接口.md#ga502c7221c97faad1399465e21880fef1)、[k_irq_disable()](../fatal_irq_reference/P007_中断服务接口.md#ga432cfe25e5846d7a0a665043e623d3b6)、[k_irq_is_enabled()](../fatal_irq_reference/P007_中断服务接口.md#gabba768c3c87a40641982e4b0654c0d26)、[k_irq_connect_dynamic()](../fatal_irq_reference/P007_中断服务接口.md#ga2835209c4f3809b5d22fc84c1bdce935)及[k_irq_disconnect_dynamic()](../fatal_irq_reference/P007_中断服务接口.md#gae2f1cb1c6babc98ff59d9e87daccb0c5)。
- 本地互连网络（LIN）


  - [`lin_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga752004d89d50932711c3aa6189874478)
  - [`lin_stop()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaefe6f3853ea2f70d8ba4d6ab86f62b57)
  - [`lin_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga97468832dddf9e21b33e93a36c60102a)
  - [`lin_get_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga9410aa6989aea2cc173e7f36dcaf6be7)
  - [`lin_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga2a2afff5c7524504f24860673c24a217)
  - [`lin_receive()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga13e0a57996ba2f010bcda6561298b658)
  - [`lin_response()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gafae0fa8e806c2856f61642ef80368ec8)
  - [`lin_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga58c5052899f49601a91d6da614ea8c82)
  - [`lin_wakeup_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga0fe3631c3f9b7100162b5f48e83bd6e3)
  - [`lin_set_event_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga07ec84c466d94f6057d7852998b2fbb2)
  - [`lin_set_rx_filter()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga7594e89b4fc3a018c1cd0010bd4a6ac1)
  - [`lin_get_transceiver()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga880b0c5dd454342160bcf454de5105e9)
  - [`CONFIG_LIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIN)
- 远距离无线通信（LoRa）


  - [`lora_recv_duty_cycle()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5d1802eed6067734ca45c70e3114b272)
  - [`lora_recv_duty_cycle_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga2192d812e6203f6361b8beaeb1d7361c)
  - [`lora_energy_detect()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gacf4c29b613fc525cfdc0b961c39981b4)
  - [`lora_rssi()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga75d2c701f482d35cfbdd94906b8799c9)
- 管理（Management）


  - 微控制器管理（MCUmgr）


    - 新增SPI MCUmgr SMP传输支持，可通过[CONFIG_MCUMGR_TRANSPORT_SPI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SPI)启用。
    - 新增实验性[传输管理组（Transport Management Group）](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_groups/smp_group_11.html#mcumgr-smp-group-11)，配置项包括[CONFIG_MCUMGR_GRP_TRANSPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT)、[CONFIG_MCUMGR_GRP_TRANSPORT_LOCKING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT_LOCKING)、[CONFIG_MCUMGR_GRP_TRANSPORT_MAX_BRIDGES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT_MAX_BRIDGES)、[CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT)、[CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE)、[CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE_GROUP_ID](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE_GROUP_ID)、[CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION)及[CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS)。
- 调制解调器（Modem）


  - [`CELLULAR_MODEM_INFO_SERIAL_NUMBER`](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ggad6e38e31d82075c51933fcbb2ff2de30aa8bf7a6878c6a635681e6f65275966ed)
- 多媒体流水线（Multimedia Pipeline）


  - [CONFIG_MPIPE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE)，见[多媒体流水线（Multimedia Pipeline，mpipe）](../services_overview/P012_多媒体流水线.md#mpipe)。
  - [`CONFIG_MPIPE_BASE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_BASE)
  - [`CONFIG_MPIPE_DUMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_DUMP)
  - [`CONFIG_MPIPE_PLAYER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_PLAYER)
- 网络（Network）


  - 新增[net_eth_set_if_type_wifi()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa64462598843dd9f6e731198498aea31)，将以太网接口类型设为Wi-Fi。
  - 新增公开的邻居缓存（Neighbor Cache）API：[net_if_ipv4_nbr_flush()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga7f8e34c1001e89d759d3a1e6a5538647)及[net_if_ipv6_nbr_flush()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaaa6c3d31d3a40cab6cf9e4f4af959b89)清除接口学习到的全部邻居；[net_if_ipv4_nbr_rm()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga5e676ccb2b0cf22410e595d61d8363ce)及[net_if_ipv6_nbr_rm()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gac6bc061b5b0facc5023da2a835fb9bb3)删除单个邻居。在以太网链路上，IPv4邻居缓存就是ARP缓存。
  - 新增[net_dhcpv4_set_reboot_hint()](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4.html#ga167e66033d902d7ffcab801b738db224)，为DHCPv4客户端提供先前租用的地址，用于INIT-REBOOT流程。
  - 新增mDNS响应器接口策略[CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST)及[CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST)，配合[CONFIG_MDNS_RESPONDER_IFACE_LIST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_IFACE_LIST)控制响应器在哪些网络接口工作。
  - 新增[mdns_responder_enable_iface()](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html#ae8b53e59ec3e159e34ffda276a2f72dc)及[mdns_responder_disable_iface()](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html#a085957294062f9948c213070dc912a34)，通过[CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL)在运行时启用或禁用某网络接口上的mDNS响应器。
  - 新增支持IPv6前缀委派（Prefix Delegation）的DHCPv6服务器[CONFIG_NET_DHCPV6_SERVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV6_SERVER)，提供[net_dhcpv6_server_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#ga5fdf013a85ca7701ad92c8f50c1b0ed0)、[net_dhcpv6_server_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gae090b9103bc0110eca408d3a3989c574)及[net_dhcpv6_server_foreach_lease()](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6__server.html#gaaedb437385fa27b8454bfc670ff9aa71)。
  - 新增IPv6路由器角色，即发送路由器通告（Router Advertisement）的[CONFIG_NET_IPV6_ND_RA_TX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ND_RA_TX)，提供[net_if_ipv6_router_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga1c062890f66b97dbb723339fede121ff)、[net_if_ipv6_router_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gaa56d3dbc96301e6fa70ee61b08c29841)及[net_if_ipv6_prefix_set_advertise()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga9ff61003d36ee19af27a9b1b24b22170)。
  - DHCPv6客户端新增请求路由器（Requesting Router）支持，可经[net_dhcpv6_params.downstream_ifaces](https://docs.zephyrproject.org/latest/doxygen/html/structnet__dhcpv6__params.html#ad66949eb34540dbe8808dc9aea9e6368)将获得的前缀再委派到下游链路。
  - 新增[net_eth_mcast_addr_add()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3e578035be797bbbafafa56dedaa8320)、[net_eth_mcast_addr_rm()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga3cd2e9abc38bdd7eb0cb3932d96fd90e)及[net_eth_mcast_addr_foreach()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga80adc03695a8fbb9dbc9dd3adec78c04)。以太网链路层（L2）现在跟踪接口监听的链路层多播地址，仅在首个使用者加入或最后一个使用者退出时，才要求驱动修改接收过滤器。此前IP层加入及数据包套接字成员关系分别转发给驱动，退出某组可能使设备停止监听另一组所需的同一链路层地址；IPv4多播地址以32:1映射到链路层地址，容易出现此问题。驱动也可将ETHERNET_CONFIG_TYPE_FILTER视为地址变化提示，用[net_eth_mcast_addr_foreach()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga80adc03695a8fbb9dbc9dd3adec78c04)遍历并重新设置过滤器，适用于按地址哈希过滤的设备。接口可跟踪地址数等于已启用子系统的请求总数，应用需要更多时可用[CONFIG_NET_L2_ETHERNET_MCAST_FILTER_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_MCAST_FILTER_COUNT)增加。传给[net_eth_mac_filter()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga920bddac077675d544a21fb5650c945e)或NET_REQUEST_ETHERNET_SET_MAC_FILTER的多播目标地址也按相同方式计数，因此应用设置的每个过滤器现在也必须由应用取消；取消从未设置的过滤器会返回-ENOENT。
  - 在ZSOCK_SOL_PACKET层新增ZSOCK_PACKET_ADD_MEMBERSHIP及ZSOCK_PACKET_DROP_MEMBERSHIP套接字选项，由[CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP)启用，使数据包套接字可请求网络接口开始或停止监听额外L2多播地址。对于以太网，若设备支持过滤，则将地址写入其接收过滤器；不支持过滤的设备原本就会上送该组流量。接口无法满足加入请求时会向应用报错：无法再跟踪地址返回ENOMEM，非以太网接口返回ENOTSUP。成员变化通过[NET_EVENT_PACKET_MCAST_MEMBERSHIP_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabfb799347776323486fb0d4563e31b3b)及[NET_EVENT_PACKET_MCAST_MEMBERSHIP_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaec5574f6308a89db36c2793bce6d5dcb)网络管理事件报告。关闭套接字时自动退出仍保留的成员关系，[CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP_COUNT)控制同时有效的成员关系数量。
  - <a id="index-2"></a>

    新增对已接收TCP数据的选择性确认（Selective Acknowledgment，SACK），遵循[RFC 2018](https://datatracker.ietf.org/doc/html/rfc2018.html)，由[CONFIG_NET_TCP_SACK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP_SACK)控制且默认启用。Zephyr现在在握手中声明SACK能力，并报告接收队列保留的乱序数据，使支持SACK的发送方仅重传缺失数据。收到的SACK块尚未用于本端重传。
  - [`CONFIG_PTP_NETWORK_MODE_HYBRID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_NETWORK_MODE_HYBRID)
  - zperf新增实验性[iperf3](../networking/P096_zperf网络流量生成器.md#zperf-iperf3)支持[CONFIG_NET_ZPERF_IPERF3](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_IPERF3)，可替代iPerf 2选项[CONFIG_NET_ZPERF_IPERF2](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_IPERF2)。两者使用相同的zperf API及Shell命令，见iperf3。
  - 新增简单网络时间协议（SNTP）服务器[CONFIG_SNTP_SERVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP_SERVER)，在所有启用的地址族上通过UDP端口123响应时间查询。应用先设置系统时钟，再通过[sntp_server_clock_source()](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp__server.html#ga36c5b4a695294c7ad6777fe79d08b798)告知时钟来源；此前服务器会告知客户端不可使用其时间。SNTP客户端现在仅由[CONFIG_SNTP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP)选择，二者共享[CONFIG_SNTP_LIB](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP_LIB)。
  - 新增[dns_resolve_is_active()](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3cf4e94af65585d89b4a0650dbd9d46e)，无需读取上下文内部字段即可检查DNS解析上下文是否活动。
  - <a id="index-3"></a>

    新增[coap_client_reregister_observe()](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga17f5d111a03ca0c02b83f5ad96c1caa8)，无需拆除现有观察关系即可刷新CoAP观察，遵循[RFC 7641](https://datatracker.ietf.org/doc/html/rfc7641.html)重新注册机制。
  - <a id="index-4"></a>

    新增[coap_age_is_newer()](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga998a3b01a3a535614183ac08da101811)，比较CoAP Observe选项值的新旧，见[RFC 7641第3.4节](https://datatracker.ietf.org/doc/html/rfc7641.html#section-3.4)。
  - [net_config_init_clock_via_sntp()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#gad1c288429f1178e165ed1429f87b3b81)通过SNTP设置系统时钟。
  - [`net_config_sntp_set_server()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html#ga4d71cd03a40db9155b29fab43f7d5ec5)
  - <a id="index-5"></a>

    新增实验性实时传输协议（[RTP](../networking/P141_RTP实时传输协议.md#rtp-interface)，[RFC 3550](https://datatracker.ietf.org/doc/html/rfc3550.html)）协议栈[CONFIG_RTP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP)，通过UDP收发媒体流；支持BSD套接字传输[CONFIG_RTP_TRANSPORT_SOCKET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_SOCKET)及原始net_pkt传输[CONFIG_RTP_TRANSPORT_NET_PKT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_NET_PKT)。见RTP。
  - 新增[CONFIG_NET_GPTP_STATIC_TIME_RECEIVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_STATIC_TIME_RECEIVER)，使广义精确时间协议（gPTP）节点作为静态配置的时间接收方，可经不发送Announce消息的IEEE 802.1AS汽车配置文件网桥实现同步。
- 可移植操作系统接口（POSIX）


  - [CONFIG_POSIX_AEP_CHOICE_NETAPP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_AEP_CHOICE_NETAPP)：Zephyr专用子配置文件，包含PSE52功能及PSE53网络接口，不支持多进程。
- 电源管理（Power Management）


  - [`LOG_DBG_PM_DEVICE_RUNTIME_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga2a68dbbec6d2968c9190d215a6ff42f0)
  - [`LOG_WRN_PM_DEVICE_RUNTIME_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga15ba7cc248e64ccff04832c7df8c6bf2)
  - [`LOG_ERR_PM_DEVICE_RUNTIME_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga29129dc0c154a35427ec70054e2051a8)
  - [`LOG_DBG_PM_DEVICE_RUNTIME_PUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gabfcf43f78f33a88d127ac32a33232d87)
  - [`LOG_WRN_PM_DEVICE_RUNTIME_PUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga836f0d108058445f2d56f51e302d3d23)
  - [`LOG_ERR_PM_DEVICE_RUNTIME_PUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gac0f1ec7880587923d7fb3d6014e61bde)
  - [`LOG_INST_DBG_PM_DEVICE_RUNTIME_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga6445dee8f12a72908bc6fdd3067cd12b)
  - [`LOG_INST_WRN_PM_DEVICE_RUNTIME_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gabc2ae088e167472c95c2a0b5a51d80c3)
  - [`LOG_INST_ERR_PM_DEVICE_RUNTIME_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gaf16aa376b083f9a0354362cd36b8fd5d)
  - [`LOG_INST_DBG_PM_DEVICE_RUNTIME_PUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga6eb42fa94d4eec9750833577b133458e)
  - [`LOG_INST_WRN_PM_DEVICE_RUNTIME_PUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#ga964c1ec1b6562d39fad8d183fa7f6f18)
  - [`LOG_INST_ERR_PM_DEVICE_RUNTIME_PUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device__runtime.html#gacdeb875b048dbaf97bb32977cc6b1001)
- 脉冲输入输出（Pulse IO）


  - 新增[脉冲输入输出（Pulse IO）](https://docs.zephyrproject.org/latest/hardware/peripherals/pulse_io.html#pulse-io-api)子系统，为在GPIO线上产生及捕获定时数字边沿的硬件提供不依赖厂商的API。
- 环形缓冲区（Ring Buffer）


  - [sys_ringq](../ringq_reference/P002_环形队列结构.md)，见[sys_ringq数据结构（Data Structure）](https://docs.zephyrproject.org/latest/kernel/data_structures/ringq.html#fixed-size-ringq-api)。
  - [`ring_buf_put_ptr()`](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga7877a84b56da9077422dd732e25654d9)
  - [`ring_buf_get_ptr()`](../ringbuffer_reference/P001_环形缓冲区公共接口.md#gad3990b5a2ae63166b76c6d1db179a215)
  - [`ring_buf_commit()`](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga50e1cb774f39d3cda234b55a3102cf2f)
  - [`ring_buf_consume()`](../ringbuffer_reference/P001_环形缓冲区公共接口.md#ga8afdb493f570b9a70af35012b427f1bd)
- 安全存储（Secure Storage）


  - [CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM)允许自行实现[secure_storage_its_transform_aead_crypt()](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html#a59a656fec3b4347c2bd6ac4843877856)。（[GitHub #118542](https://github.com/zephyrproject-rtos/zephyr/issues/118542)）
  - [`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE)
  - `CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE_IS_CONFIGURABLE`
- 定时器（Timer）


  - `z_sys_clock_lpm_enter()`
- USB Type-C 接口（USB Type-C）


  - [`CONFIG_USBC_LOG_PD_MSG_NAMES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_LOG_PD_MSG_NAMES)
- 实用工具（Utilities）


  - [ARGS_UNUSED](../util_reference/P001_通用工具公共接口.md#ga9981e0f0529ce8ab1e8079fc1c312cfe)可将多个参数标记为未使用。
- Zephyr消息总线（Zbus）


  - [`CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_CHANNEL_REGISTRATION)
  - [`zbus_runtime_channel_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#gafbee704332c7fd8be1fa02d0a7db3439)
  - [`zbus_runtime_channel_register()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga7dc8f173f0aea59bda8e452c1eda1e28)
  - [`zbus_runtime_channel_unregister()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#gad3d2ffd95149099b5f816366404f7474)

<a id="new-boards"></a>

<a id="boards-added-in-zephyr-4-5"></a>

## 新增开发板（New Boards）


- Adafruit Industries, LLC


  - [Adafruit Feather ESP32C6](../boards_adafruit_feather_esp32_rp2040/P004_Adafruit_Feather_ESP32C6.md#adafruit_feather_esp32c6)开发板（adafruit_feather_esp32c6）
  - [TRRS Trinkey](../boards_adafruit_itsybitsy_metro_qt_trinkey/P014_TRRS_Trinkey.md#adafruit_trrs_trinkey)开发板（adafruit_trrs_trinkey）
- Advanced Micro Devices（AMD）, Inc.


  - ACP 7.0 Xtensa 音频数字信号处理器（Audio DSP）开发板（acp_7_0_adsp）（[ACP 7.0 Xtensa音频数字信号处理器（Audio DSP）](../boards_amd/P002_ACP_7.0_Xtensa_Audio_DSP.md#acp_7_0_adsp)）
  - ACP 7.X Xtensa 音频数字信号处理器（Audio DSP）开发板（acp_7_x_adsp）（[ACP 7.X Xtensa音频数字信号处理器（Audio DSP）](../boards_amd/P003_ACP_7.X_Xtensa_Audio_DSP.md#acp_7_x_adsp)）
  - [AMD Zynq UltraScale+ MPSoC APU](../boards_amd/P012_AMD_Zynq_UltraScale_MPSoC_APU.md#zynqmp_apu)开发板（zynqmp_apu）
  - [AMD Zynq UltraScale+ MPSoC RPU](../boards_amd/P013_AMD_Zynq_UltraScale_MPSoC_RPU.md#zynqmp_rpu)开发板（zynqmp_rpu）
- Aesc Silicon


  - [ElemRV Flask-H](../boards_aesc_aithinker_alientek/P001_ElemRV_Flask-H.md#elemrv_flask_h)开发板（elemrv_flask_h）
- 安信可（Ai-Thinker Co., Ltd.）


  - Ai-Thinker M64P-32S 开发板（Development Board）（ai_m64p_32s_kit）（[安信可Ai-Thinker M64P-32S开发板（Development Board）](../boards_aesc_aithinker_alientek/P006_Ai-Thinker_M64P-32S_Development_Board.md#ai_m64p_32s_kit)）
  - AiPi-Eyes-S2 多功能开发板（Multi-Functional Development Board）（aipi_eyes_s2）（[AiPi-Eyes-S2多功能开发板（Multi-Functional Development Board）](../boards_aesc_aithinker_alientek/P008_AiPi-Eyes-S2_Multi-Functional_Development_Board.md#aipi_eyes_s2)）
- Alif Semiconductor


  - Alif Balletto B1 开发套件（Development Kit）（balletto_b1_dk）（[Alif Balletto B1开发套件（Development Kit）](../boards_alif_ambiq/P001_Alif_Balletto_B1_Development_Kit.md#balletto_b1_dk)）
  - Alif Balletto B1 入门套件（StartKit）（balletto_b1_sk）（[Alif Balletto B1入门套件（StartKit）](../boards_alif_ambiq/P002_Alif_Balletto_B1_StartKit.md#balletto_b1_sk)）
  - Alif Ensemble E1C 入门套件（StartKit）（ensemble_e1c_sk）（[Alif Ensemble E1C入门套件（StartKit）](../boards_alif_ambiq/P004_Alif_Ensemble_E1C_StartKit.md#ensemble_e1c_sk)）
  - Alif Ensemble E8 人工智能／机器学习应用套件（AI/ML AppKit）（ensemble_e8_ak）（[Alif Ensemble E8人工智能／机器学习应用套件（AI/ML AppKit）](../boards_alif_ambiq/P005_Alif_Ensemble_E8_AI_ML_AppKit.md#ensemble_e8_ak)）
- Analog Devices, Inc.


  - [EVAL-ADIN1140D1Z](../boards_adi_ethernet_platforms/P004_EVAL-ADIN1140D1Z.md#adi_eval_adin1140d1z)开发板（adi_eval_adin1140d1z）
  - [MAX32651EVKIT](../boards_adi_max32_max78_sdp/P003_MAX32651EVKIT.md#max32651evkit)开发板（max32651evkit）
- Antmicro


  - STM32H7 HDMI开发板（stm32h7_hdmi_board）（[STM32H7 HDMI开发板（Board）](../boards_andes_antmicro/P005_STM32H7_HDMI_Board.md#stm32h7_hdmi_board)）
  - [STM32H7 Renode参考平台（Reference Platform）](../boards_andes_antmicro/P006_STM32H7_Renode_Reference_Platform.md#stm32h7_renode_reference_board)（stm32h7_renode_reference_board）
- Arduino


  - [Arduino Nano RP2040 Connect](../boards_arduino/P007_Arduino_Nano_RP2040_Connect.md#arduino_nano_connect)开发板（arduino_nano_connect）
  - [Arduino Nano R4](../boards_arduino/P009_Arduino_Nano_R4.md#arduino_nano_r4)开发板（arduino_nano_r4）
  - [Arduino Nesso N1](../boards_arduino/P010_Arduino_Nesso_N1.md#arduino_nesso_n1)开发板（arduino_nesso_n1）
- Arm公司（ARM Ltd.）


  - Arm Corstone-1000-A320 固定虚拟平台（Fixed Virtual Platform）（fvp_corstone1000）（[Arm Corstone-1000-A320固定虚拟平台（FVP）](../boards_arm/P003_Arm_Corstone-1000-A320_Fixed_Virtual_Platform.md#fvp_corstone1000)）
- Armfly


  - [Armfly STM32H743XIH6](../boards_armfly_aspeed_degu/P002_Armfly_STM32H743XIH6.md#armfly_stm32h743xih6)开发板（armfly_stm32h743xih6）
- Barth Elektronik GmbH


  - [STG-800 lococube mini-PLC](../boards_barth_bbc_blueclover/P002_STG-800_lococube_mini-PLC.md#stg_800)开发板（stg_800）
- BeagleBoard.org基金会（Foundation）


  - [BeagleBadge](../boards_beagle/P001_BeagleBadge.md#beaglebadge)开发板（beaglebadge）
  - [BeagleConnect Zepto](../boards_beagle/P004_BeagleConnect_Zepto.md#beagleconnect_zepto)开发板（beagleconnect_zepto）
  - [PocketBeagle 2 Industrial](../boards_beagle/P010_PocketBeagle_2_Industrial.md#pocketbeagle_2_industrial)开发板（pocketbeagle_2_industrial）
- BLIIoT科技有限公司（BLIIoT Technology Co., Ltd.）


  - [BLIIoT ARMxy BL350 AM62x M4](../boards_bouffalo_qnx_bliiot_blues/P007_BLIIoT_ARMxy_BL350_AM62x_M4.md#am62x_m4_bl350)开发板（am62x_m4_bl350）
- 博流（南京）有限公司（Bouffalo Lab）


  - Bouffalo Lab BL618 G0 评估板（Evaluation Board）（bl618g0）（[博流BL618 G0评估板（Evaluation Board）](../boards_bouffalo_qnx_bliiot_blues/P002_Bouffalo_Lab_BL618_G0_evaluation_board.md#bl618g0)）
- CAN-module, FOP


  - [CANBRIDGE G473](../boards_broadcom_bytesatwork_canmodule/P007_CANBRIDGE_G473.md#canbridge_g473)开发板（canbridge_g473）
  - [USBCAN ISO](../boards_broadcom_bytesatwork_canmodule/P009_USBCAN_ISO.md#usbcan_iso)开发板（usbcan_iso）
  - [USBCANFD DUAL](../boards_broadcom_bytesatwork_canmodule/P010_USBCANFD_DUAL.md#usbcanfd_dual)开发板（usbcanfd_dual）
  - [USBCANFD SOLO](../boards_broadcom_bytesatwork_canmodule/P011_USBCANFD_SOLO.md#usbcanfd_solo)开发板（usbcanfd_solo）
- 高级计算发展中心（C-DAC / Centre for Development of Advanced Computing）


  - ARIES v3.0 开发板（Development Board）（aries_v3）（[ARIES v3.0开发板（Development Board）](../boards_cdac_to_cthings/P001_ARIES_v3.0_Development_Board.md#aries_v3)）
- 成都亿佰特电子科技（Chengdu Ebyte Electronic Technology）


  - Ebyte E80 模块开发板（Module Development Board） (HF)（e80_900mbl_01）（[亿佰特E80模块开发板，高频版（Ebyte E80 Module Development Board / HF）](../boards_ebyte_to_enjoydigital/P002_Ebyte_E80_Module_Development_Board_HF.md#e80_900mbl_01)）
  - Ebyte EoRa-HUB-900TB 模块测试套件（Module Test Kit）（eora_hub_900tb）（[亿佰特EoRa-HUB-900TB模块测试套件（Module Test Kit）](../boards_ebyte_to_enjoydigital/P003_Ebyte_EoRa-HUB-900TB_Module_Test_Kit.md#eora_hub_900tb)）
- Chengdu Heltec Automation Technology Co., Ltd.（成都惠利特自动化科技有限公司）


  - [Heltec T114 v2](../boards_gd_to_iar/P026_Heltec_T114_v2.md#heltec_t114_v2)开发板（heltec_t114_v2）
- Cirrus Logic, Inc.公司


  - [CRD40L26-POC-C](../boards_cdac_to_cthings/P007_CRD40L26-POC-C.md#crd40l26)开发板（crd40l26）
- Core Devices LLC公司


  - [Pebble Round 2](../boards_cdac_to_cthings/P014_Pebble_Round_2.md#pr2)开发板（pr2）
- DH electronics GmbH公司


  - [DHSBC STM32MP255C](../boards_cypress_to_dragino/P013_DHSBC_STM32MP255C.md#stm32mp255c_dhsbc)开发板（stm32mp255c_dhsbc）
- Digilent, Inc.公司


  - [ZedBoard](../boards_cypress_to_dragino/P016_ZedBoard.md#zedboard)开发板（zedboard）
- 东莞市慧勤智远科技有限公司（Dongguan Waiken-Smart Technology Co., Ltd.）


  - GD32F470ZIT6 核心板（Core Board）（gd32f470zit6_core）（[GD32F470ZIT6核心板（Core Board）](../boards_waveshare_tail/P001_GD32F470ZIT6_Core_Board.md#gd32f470zit6_core)）
- emtrion GmbH公司


  - [emSBC-NEON-CM7](../boards_ebyte_to_enjoydigital/P018_emSBC-NEON-CM7.md#emsbc_neon_cm7)开发板（emsbc_neon_cm7）
- EnjoyDigital


  - [LiteX VexiiRiscv](../boards_ebyte_to_enjoydigital/P024_LiteX_VexiiRiscv.md#litex_vexiiriscv)开发板（litex_vexiiriscv）
- 乐鑫信息科技（Espressif Systems）


  - [ESP32-C61-DevKitC](../boards_espressif/P022_ESP32-C61-DevKitC.md#esp32c61_devkitc)开发板（esp32c61_devkitc）
  - [ESP32-P4-Function-EV-Board](../boards_espressif/P025_ESP32-P4-Function-EV-Board.md#esp32p4_function_ev_board)开发板（esp32p4_function_ev_board）
  - [ESP32-P4X-Function-EV-Board](../boards_espressif/P026_ESP32-P4X-Function-EV-Board.md#esp32p4x_function_ev_board)开发板（esp32p4x_function_ev_board）
  - [ESP32-S3-BOX-3](../boards_espressif/P029_ESP32-S3-BOX-3.md#esp32s3_box3)开发板（esp32s3_box3）
- Eurovibes


  - [基于STM32G431的Sertest-NG开发板](../boards_eurovibes_ezurio/P002_STM32G431_based_Sertest-NG_board.md#eurovibes_stm32g431_sertest-ng)（eurovibes_stm32g431_sertest-ng）
- FlySky


  - [FlySky FS-i6S](../boards_fanke_to_gardena/P009_FlySky_FS-i6S.md#fs_i6s)开发板（fs_i6s）
- 兆易创新半导体（GigaDevice Semiconductor）


  - [GD32C231C-EVAL](../boards_gd_to_iar/P002_GD32C231C-EVAL.md#gd32c231c_eval)开发板（gd32c231c_eval）
- Heimann Sensor GmbH


  - Heimann HTPA 评估板（Eval Board） (rev0)（htpa_eval）（[Heimann HTPA评估板，rev0版本](../boards_gd_to_iar/P024_Heimann_HTPA_Eval_Board_rev0.md#htpa_eval)）
- 英飞凌科技（Infineon Technologies）


  - [PSOC™ 4000T](../boards_infineon_innblue/P004_PSOC_4000T.md#cy8cproto_040t)开发板（cy8cproto_040t）
  - [PSOC™ 4000T AUTO](../boards_infineon_innblue/P005_PSOC_4000T_AUTO.md#cy8cproto_040t_auto)开发板（cy8cproto_040t_auto）
  - PSOC™ Control C3M5 连接卡（Connectivity Card） 2（kit_psc3m5_cc2）（[PSOC Control C3M5通信卡2（Connectivity Card 2）](../boards_infineon_innblue/P011_PSOC_Control_C3M5_Connectivity_Card_2.md#kit_psc3m5_cc2)）
  - PSOC™ Control C3M6 评估套件（Evaluation Kit）（kit_psc3m6_eval）（[PSOC Control C3M6评估套件（Evaluation Kit）](https://docs.zephyrproject.org/latest/boards/infineon/kit_psc3m6_eval/doc/index.html#kit_psc3m6_eval)）
  - [Kit T2G-C2-D-6M Lite](../boards_infineon_innblue/P018_Kit_T2G-C2-D-6M_Lite.md#kit_t2g_c2d6m_lite)开发板（kit_t2g_c2d6m_lite）
- 英特尔公司（Intel Corporation）


  - [Nova Lake RVP](../boards_intel_ite/P015_Nova_Lake_RVP.md#intel_nvl_s_rvp)开发板（intel_nvl_s_rvp）
- Jhoinrch


  - [RH02](../boards_jhoinrch_to_kws/P002_RH02.md#rh02)开发板（rh02）
  - [RH02 Plus (2026)](../boards_jhoinrch_to_kws/P003_RH02_Plus_2026.md#rh02_plus_2026)开发板（rh02_plus_2026）
- KAGA FEI Co., Ltd.


  - [EC4L15BA1-EVB](../boards_jhoinrch_to_kws/P006_EC4L15BA1-EVB.md#ec4l15ba1)开发板（ec4l15ba1）
- KinCony Electronics Co., Ltd.


  - [KC868-A8](../boards_jhoinrch_to_kws/P013_KC868-A8.md#kincony_kc868_a8)开发板（kincony_kc868_a8）
- 制造商：LilyGO（Shenzhen Xinyuan Electronic Technology Co., Ltd）


  - [LilyGO T-Deck / T-Deck Plus](../boards_lilygo_to_m5stack/P002_LilyGO_T-Deck_T-Deck_Plus.md#t_deck)开发板（t_deck）
- M5Stack


  - [PaperColor](../boards_lilygo_to_m5stack/P027_PaperColor.md#m5stack_paper_color)开发板（m5stack_paper_color）
  - [M5Stack StackChan](../boards_lilygo_to_m5stack/P028_M5Stack_StackChan.md#m5stack_stackchan)开发板（m5stack_stackchan）
  - [M5Stack StickS3](../boards_lilygo_to_m5stack/P030_M5Stack_StickS3.md#m5stack_sticks3)开发板（m5stack_sticks3）
  - [Unit C6L](../boards_lilygo_to_m5stack/P031_Unit_C6L.md#m5stack_unitc6l)开发板（m5stack_unitc6l）
- Makerfabs


  - [Matouch MTRO128G](../boards_madmachine_to_mediatek/P012_Matouch_MTRO128G.md#matouch_mtro128g)开发板（matouch_mtro128g）
- 联发科技（MediaTek Inc.）


  - [Genio 510 EVK](../boards_madmachine_to_mediatek/P014_Genio_510_EVK.md#mt8370_genio_510_evk)开发板（mt8370_genio_510_evk）
  - [Genio 700 EVK](../boards_madmachine_to_mediatek/P015_Genio_700_EVK.md#mt8390_genio_700_evk)开发板（mt8390_genio_700_evk）
- 微芯科技（Microchip Technology Inc.）


  - [Microchip M2S010 MKR Kit](../boards_microchip/P006_Microchip_M2S010_MKR_Kit.md#m2s010_mkr_kit)开发板（m2s010_mkr_kit）
  - [Microchip M2S Hello FPGA Kit](../boards_microchip/P007_Microchip_M2S_Hello_FPGA_Kit.md#m2s_hello_fpga_kit)开发板（m2s_hello_fpga_kit）
  - [PIC32CK GC01 Curiosity Ultra](../boards_microchip/P014_PIC32CK_GC01_Curiosity_Ultra.md#pic32ck_gc01_cult)开发板（pic32ck_gc01_cult）
  - [PIC32CK SG01 Curiosity Ultra](../boards_microchip/P015_PIC32CK_SG01_Curiosity_Ultra.md#pic32ck_sg01_cult)开发板（pic32ck_sg01_cult）
  - [PIC32CM GC00 Curiosity Pro](../boards_microchip/P016_PIC32CM_GC00_Curiosity_Pro.md#pic32cm_gc00_cpro)开发板（pic32cm_gc00_cpro）
  - [PIC32CM SG00 Curiosity Pro](../boards_microchip/P020_PIC32CM_SG00_Curiosity_Pro.md#pic32cm_sg00_cpro)开发板（pic32cm_sg00_cpro）
  - [SAMA5D27 SOM1 Kit1](../boards_microchip/P028_SAMA5D27_SOM1_Kit1.md#sama5d27_som1_ek1)开发板（sama5d27_som1_ek1）
- MuseLab Electronics


  - [MuseLab nanoCH32V317](../boards_mikroe_to_mxchip/P009_MuseLab_nanoCH32V317.md#nano_ch32v317)开发板（nano_ch32v317）
  - [MuseLab nanoCH57x](../boards_mikroe_to_mxchip/P010_MuseLab_nanoCH57x.md#nano_ch57x)开发板（nano_ch57x）
- Nordic Semiconductor


  - [nRF54LV10 DK](../boards_nordic/P015_nRF54LV10_DK.md#nrf54lv10dk)开发板（nrf54lv10dk）
  - [nRF93M1 DK](../boards_nordic/P022_nRF93M1_DK.md#nrf93m1dk)开发板（nrf93m1dk）
- Norik Systems


  - [DECT NR+ USB Dongle](../boards_norik_to_nuvoton/P001_DECT_NR_USB_Dongle.md#dect_nr_plus_usb_dongle)开发板（dect_nr_plus_usb_dongle）
- NUCODE Co., Ltd.（nuworks.io）


  - [NUCODE NU32](../boards_norik_to_nuvoton/P006_NUCODE_NU32.md#nucode_nu32)开发板（nucode_nu32）
  - [NUCODE NU40](../boards_norik_to_nuvoton/P007_NUCODE_NU40.md#nucode_nu40)开发板（nucode_nu40）
- 新唐科技（Nuvoton Technology Corporation）


  - [NUMAKER M031KI](../boards_norik_to_nuvoton/P015_NUMAKER_M031KI.md#numaker_m031ki)开发板（numaker_m031ki）
  - [NUMAKER M3351KI](../boards_norik_to_nuvoton/P018_NUMAKER_M3351KI.md#numaker_m3351ki)开发板（numaker_m3351ki）
- 恩智浦半导体（NXP Semiconductors）


  - [FRDM-IMXRT1152](../boards_nxp_frdm_imx_kinetis/P003_FRDM-IMXRT1152.md#frdm_imxrt1152)开发板（frdm_imxrt1152）
  - [FRDM-IMXRT700](../boards_nxp_frdm_imx_kinetis/P005_FRDM-IMXRT700.md#frdm_imxrt700)开发板（frdm_imxrt700）
  - [i.MX952 EVK](../boards_nxp_imx_evk/P009_i.MX952_EVK.md#imx952_evk)开发板（imx952_evk）
  - [LPC845-BRK](../boards_nxp_lpc/P001_LPC845-BRK.md#lpc845brk)开发板（lpc845brk）
  - [LPCXpresso54628](../boards_nxp_lpc/P005_LPCXpresso54628.md#lpcxpresso54628)开发板（lpcxpresso54628）
  - [MIMXRT2660-EVK](../boards_nxp_imx_rt_multicore/P004_MIMXRT2660-EVK.md#mimxrt2660_evk)开发板（mimxrt2660_evk）
  - [MIMXRT685-AUD-EVK](../boards_nxp_imx_rt_multicore/P006_MIMXRT685-AUD-EVK.md#mimxrt685_aud_evk)开发板（mimxrt685_aud_evk）
  - [MR-MCXN-T1](../boards_nxp_remaining/P007_MR-MCXN-T1.md#mr_mcxn_t1)开发板（mr_mcxn_t1）
  - [MR-NavQ95B](../boards_nxp_remaining/P008_MR-NavQ95B.md#mr_navq95b)开发板（mr_navq95b）
- OLIMEX Ltd.


  - [ESP32-P4-PC](../boards_octavo_olimex_openhw_openisa/P003_ESP32-P4-PC.md#esp32p4_pc)开发板（esp32p4_pc）
- 其他（Others）


  - BL704L 开发板（Development Board）（bl704l_dvk）（[BL704L开发板（Development Board）](../boards_other_vendors/P001_BL704L_Development_Board.md#bl704l_dvk)）
  - [ESP32-H2-SUPERMINI](../boards_other_vendors/P010_ESP32-H2-SUPERMINI.md#esp32h2_supermini)开发板（esp32h2_supermini）
  - JZ-F407VET6 工业控制板（Industrial Control Board）（jz_f407vet6）（[JZ-F407VET6工业控制板](../boards_other_vendors/P013_JZ-F407VET6_Industrial_Control_Board.md#jz_f407vet6)）
  - STM32 调试探针（Debug Probe）（stm32_debug_probe）（[STM32调试探针（Debug Probe）](../boards_other_vendors/P017_STM32_Debug_Probe.md#stm32_debug_probe)）
- Pine64


  - PineCone BL602 评估板（Evaluation Board）（pinecone）（[PineCone BL602评估板](../boards_pimoroni_radxa/P005_PineCone_BL602_Evaluation_Board.md#pinecone)）
- QEMU模拟器


  - QEMU仿真： ARM Cortex-A72（qemu_cortex_a72）（[QEMU仿真：ARM Cortex-A72](../qemu_arm_reference/P002_QEMU_Cortex_A72仿真开发板.md#qemu_cortex_a72)）
  - QEMU仿真： Hexagon（qemu_hexagon）（[QEMU仿真：Hexagon](../qemu_other_reference/P005_QEMU_Hexagon仿真开发板.md#qemu_hexagon)）
  - QEMU仿真： Infineon AURIX TC39x（qemu_tc3x）（[QEMU仿真：Infineon AURIX TC39x](../qemu_other_reference/P006_QEMU_Infineon_AURIX_TC39x与TC4Dx仿真开发板.md#qemu_tc3x)）
  - QEMU仿真： Infineon AURIX TC4Dx（qemu_tc4x）（[QEMU仿真：Infineon AURIX TC4Dx](../qemu_other_reference/P006_QEMU_Infineon_AURIX_TC39x与TC4Dx仿真开发板.md#qemu_tc4x)）
- Radxa


  - [Radxa ROCK 3B](../boards_pimoroni_radxa/P018_Radxa_ROCK_3B.md#rock_3b)开发板（rock_3b）
  - [ROCK 5B+](../boards_pimoroni_radxa/P019_ROCK_5B.md#rock_5b_plus)开发板（rock_5b_plus）
- Raspberry Pi基金会（Foundation）


  - [Raspberry Pi Zero 2 W](../boards_rak_raspberry_raytac/P014_Raspberry_Pi_Zero_2_W.md#rpi_zero_2w)开发板（rpi_zero_2w）
- Raytac Corporation


  - [AN54LV-DB-15](../boards_rak_raspberry_raytac/P016_AN54LV-DB-15.md#raytac_an54lv_db_15)开发板（raytac_an54lv_db_15）
- Realtek Semiconductor Corp.


  - RTL8721Dx 评估板（Evaluation Board）（pke8721daf_c13_f10）（[RTL8721Dx评估板（Evaluation Board）](../boards_realtek_ruiside_sifive/P002_RTL8721Dx_Evaluation_Board.md#pke8721daf_c13_f10)）
- 瑞萨电子（Renesas Electronics Corporation）


  - RX74M 评估套件（Evaluation Kit）（ek_rx74m）（[RX74M评估套件](../boards_renesas_rx_rz/P002_RX74M_Evaluation_Kit.md#ek_rx74m)）
  - RX74N 评估套件（Evaluation Kit）（ek_rx74n）（[RX74N评估套件](../boards_renesas_rx_rz/P003_RX74N_Evaluation_Kit.md#ek_rx74n)）
  - [R-Car Ironhide开发板](../boards_renesas_rx_rz/P018_R-Car_Ironhide.md#rcar_ironhide_x5h)（rcar_ironhide_x5h）
  - RZ/A3M 评估套件（Evaluation Kit）（rza3m_ek）（[RZ/A3M评估套件](../boards_renesas_rx_rz/P025_RZ_A3M_Evaluation_Kit.md#rza3m_ek)）
- Seeed Technology Co., Ltd


  - [reTerminal E1001](../boards_seeed/P004_reTerminal_E1001.md#reterminal_e1001)开发板（reterminal_e1001）
  - [reTerminal E1003](../boards_seeed/P006_reTerminal_E1003.md#reterminal_e1003)开发板（reterminal_e1003）
  - [Wio Tracker L1](../boards_seeed/P009_Wio_Tracker_L1.md#wio_tracker_l1)开发板（wio_tracker_l1）
  - [XIAO ESP32C5](../boards_seeed/P013_XIAO_ESP32C5.md#xiao_esp32c5)开发板（xiao_esp32c5）
  - [XIAO nRF54LM20A](../boards_seeed/P018_XIAO_nRF54LM20A.md#xiao_nrf54lm20a)开发板（xiao_nrf54lm20a）
  - [XIAO nRF54LM20B](../boards_seeed/P019_XIAO_nRF54LM20B.md#xiao_nrf54lm20b)开发板（xiao_nrf54lm20b）
  - [XIAO STM32C5](../boards_seeed/P023_XIAO_STM32C5.md#xiao_stm32c5)开发板（xiao_stm32c5）
- SEGGER Microcontroller GmbH


  - NAND闪存评估器（[NAND Flash Evaluator](../boards_retronix_sifli/P018_NAND_Flash_Evaluator.md#nandeval_h743zi)）（nandeval_h743zi）
- SHAKTI处理器计划（Processor Program）


  - [Nexys Video (Ganga SoC)](../boards_retronix_sifli/P024_Nexys_Video_Ganga_SoC.md#nexys_ganga)开发板（nexys_ganga）
- 上海睿赛德电子科技有限公司（Shanghai Ruiside Electronic Technology Co., Ltd.）


  - [RA8P1 Titan](../boards_realtek_ruiside_sifive/P014_RA8P1_Titan.md#ra8p1_titan)开发板（ra8p1_titan）
  - [RA8P1 Titan Mini](../boards_realtek_ruiside_sifive/P015_RA8P1_Titan_Mini.md#ra8p1_titan_mini)开发板（ra8p1_titan_mini）
- 深圳嘉立创科技集团股份有限公司（Shenzhen JLC Technology Group Co., Ltd.）


  - [SkyStar GD32F407VET6](../boards_jhoinrch_to_kws/P005_SkyStar_GD32F407VET6.md#skystar_gd32f407vet6)开发板（skystar_gd32f407vet6）
- 深圳Luckfox科技有限公司（Shenzhen Luckfox Technology Co., Ltd.）


  - [Pico Ultra](../boards_lilygo_to_m5stack/P018_Pico_Ultra.md#pico_ultra)开发板（pico_ultra）
- Shenzhen Sipeed Technology Co., Ltd.


  - [Sipeed M0Sense](../boards_sipeed_sparkfun/P003_Sipeed_M0Sense.md#m0sense)开发板（m0sense）
  - [Sipeed M1S Dock](../boards_sipeed_sparkfun/P004_Sipeed_M1S_Dock.md#m1s_dock)开发板（m1s_dock）
  - [Tang Mega 138K Pro Dock](../boards_sipeed_sparkfun/P006_Tang_Mega_138K_Pro_Dock.md#tang_mega_138k_pro_dock)开发板（tang_mega_138k_pro_dock）
- 深圳迅龙软件有限公司（Shenzhen Xunlong Software CO.,Limited）


  - [Orange Pi Zero 2W](../boards_waveshare_tail/P053_Orange_Pi_Zero_2W.md#opi_zero2w)开发板（opi_zero2w）
- 芯科科技（Silicon Laboratories）


  - KG100S 无线电板（Radio Board） (KG100S-RB4332A)（kg100s_rb4332a）（[KG100S无线电板，KG100S-RB4332A](../boards_silabs/P024_KG100S_Radio_board_KG100S-RB4332A.md#kg100s_rb4332a)）
  - MGM260P 2.4 GHz +20 dBm 无线电板（Radio Board）（mgm260p_rb4351a）（[MGM260P 2.4 GHz +20 dBm无线电板](../boards_silabs/P050_MGM260P_2.4_GHz_20_dBm_Radio_Board.md#mgm260p_rb4351a)）
  - SiWx917Y Module Wi-Fi 6 and 低功耗蓝牙（Bluetooth LE） 探索套件（Explorer Kit） (BRD2708A)（siwx917_ek2708a）（[SiWx917Y模块Wi-Fi 6与低功耗蓝牙探索套件，BRD2708A](../boards_silabs/P014_SiWx917Y_Module_Wi-Fi_6_and_Bluetooth_LE_Explorer_Kit_BRD2708A.md#siwx917_ek2708a)）
  - SixG301 +10 dBm, 4 MB Flash 无线电板（Radio Board）（sixg301_rb4407a）（[SixG301 +10 dBm、4 MB闪存无线电板](../boards_silabs/P028_SixG301_10_dBm_4_MB_Flash_Radio_Board.md#sixg301_rb4407a)）
  - [EFR32xG21B 2.4 GHz 10 dBm (xG21-RB4195B)](../boards_silabs/P037_EFR32xG21B_2.4_GHz_10_dBm_xG21-RB4195B.md#xg21_rb4195b)开发板（xg21_rb4195b）
  - [EFR32xG21B 2.4 GHz 20 dBm (xG21-RB4196B)](../boards_silabs/P038_EFR32xG21B_2.4_GHz_20_dBm_xG21-RB4196B.md#xg21_rb4196b)开发板（xg21_rb4196b）
  - [EFR32xG22E 2.4 GHz 6 dBm (xG22-RB4415A)](../boards_silabs/P041_EFR32xG22E_2.4_GHz_6_dBm_xG22-RB4415A.md#xg22_rb4415a)开发板（xg22_rb4415a）
  - EFR32xG24 2.4 GHz 20 dBm 天线分集（Antenna Diversity） 无线电板（Radio Board）（xg24_rb4188a）（[EFR32xG24 2.4 GHz 20 dBm天线分集无线电板](../boards_silabs/P045_EFR32xG24_2.4_GHz_20_dBm_Antenna_Diversity_Radio_Board.md#xg24_rb4188a)）
  - EFR32xG26 开发套件（Dev Kit） (xG26-DK2608A)（xg26_dk2608a）（[EFR32xG26开发套件，xG26-DK2608A](../boards_silabs/P011_EFR32xG26_Dev_Kit_xG26-DK2608A.md#xg26_dk2608a)）
  - EFR32xG26 2.4 GHz +20 dBm 无线电板（Radio Board）（xg26_rb4121a）（[EFR32xG26 2.4 GHz +20 dBm无线电板](../boards_silabs/P053_EFR32xG26_2.4_GHz_20_dBm_Radio_Board.md#xg26_rb4121a)）
  - EFR32xG29 2.4 GHz 6 dBm 升压QFN40（Boost QFN40） (xG29-RB4413A)开发板（xg29_rb4413a）（[EFR32xG29 2.4 GHz 6 dBm升压（Boost）、QFN40无线电板，xG29-RB4413A](../boards_silabs/P060_EFR32xG29_2.4_GHz_6_dBm_Boost_QFN40_xG29-RB4413A.md#xg29_rb4413a)）
  - xGM240S +10 dBm SiP 模块无线电板（Module Radio Board） (xGM240-RB4318A)（xgm240_rb4318a）（[xGM240S +10 dBm系统级封装模块无线电板，xGM240-RB4318A](../boards_silabs/P048_xGM240S_10_dBm_SiP_Module_Radio_Board_xGM240-RB4318A.md#xgm240_rb4318a)）
- 意法半导体（STMicroelectronics）


  - [Nucleo G491RE开发板](../boards_st_nucleo/P039_Nucleo_G491RE.md#nucleo_g491re)（nucleo_g491re）
  - [Nucleo U545RE Q开发板](../boards_st_nucleo/P069_Nucleo_U545RE_Q.md#nucleo_u545re_q)（nucleo_u545re_q）
  - [Nucleo WL33CC1开发板](../boards_st_nucleo/P079_Nucleo_WL33CC1.md#nucleo_wl33cc1)（nucleo_wl33cc1）
  - [STM32-MICRIUM](../boards_st_discovery_eval/P014_STM32-MICRIUM.md#stm32_micrium)开发板（stm32_micrium）
- Sutajio Ko-Usagi PTE Ltd.


  - [Tomu](../boards_jhoinrch_to_kws/P015_Tomu.md#tomu)开发板（tomu）
- T3 Gemstone


  - [T3 Gemstone O1](../boards_starfive_trenz/P008_T3_Gemstone_O1.md#t3_gem_o1)开发板（t3_gem_o1）
- 德州仪器（Texas Instruments）


  - [AM13E230X Launchpad](../boards_ti/P015_AM13E230X_Launchpad.md#lp_am13e230)开发板（lp_am13e230）
  - [TI AM243x LaunchPad](../boards_ti/P016_TI_AM243x_LaunchPad.md#lp_am243)开发板（lp_am243）
  - [MSPM33C321A Launchpad](../boards_ti/P021_MSPM33C321A_Launchpad.md#lp_mspm33c321a)开发板（lp_mspm33c321a）
  - [TI Tiva C Series TM4C123G LaunchPad](../boards_ti/P025_TI_Tiva_C_Series_TM4C123G_LaunchPad.md#tm4c123gxl)开发板（tm4c123gxl）
- Trenz Electronic


  - [Trenz Electronic TE0950](../boards_starfive_trenz/P023_Trenz_Electronic_TE0950.md#te0950)开发板（te0950）
- Tuya Inc.


  - [TYZS3](../boards_ublox_misc/P002_TYZS3.md#tyzs3)开发板（tyzs3）
- u-blox


  - [EVK-NORA-B2](../boards_ublox_misc/P016_EVK-NORA-B2.md#ubx_evknorab2)开发板（ubx_evknorab2）
- Udoo


  - [UDOO KEY](../boards_ublox_misc/P018_UDOO_KEY.md#udoo_key)开发板（udoo_key）
- Umeta & Ikki Automotive Parts


  - [UIAPduino Pro Micro CH32V003](../boards_ublox_misc/P021_UIAPduino_Pro_Micro_CH32V003.md#uiapduino_pro_micro_ch32v003)开发板（uiapduino_pro_micro_ch32v003）
- Vicharak


  - [Shrike-fi](../boards_ublox_misc/P034_Shrike-fi.md#shrike_fi)开发板（shrike_fi）
- VIEWE Display Co., Ltd.


  - [VIEWE UEDX24240013-MD50E](../boards_ublox_misc/P037_VIEWE_UEDX24240013-MD50E.md#uedx24240013_md50e)开发板（uedx24240013_md50e）
  - [VIEWE UEDX32480035E-WB-A](../boards_ublox_misc/P039_VIEWE_UEDX32480035E-WB-A.md#uedx32480035e_wb_a)开发板（uedx32480035e_wb_a）
- Waveshare Electronics微雪电子


  - [Waveshare Core2350B](../boards_waveshare_tail/P003_Waveshare_Core2350B.md#core2350b)开发板（core2350b）
  - [ESP32-C6 LCD 1.47"开发板](../boards_waveshare_tail/P004_ESP32-C6_LCD_1.47.md#esp32c6_lcd_1_47)（esp32c6_lcd_1_47）
  - [ESP32-P4-WIFI6](../boards_waveshare_tail/P006_ESP32-P4-WIFI6.md#esp32p4_wifi6)开发板（esp32p4_wifi6）
  - [ESP32-P4-WIFI6-Dev-Kit](../boards_waveshare_tail/P007_ESP32-P4-WIFI6-Dev-Kit.md#esp32p4_wifi6_dev_kit)开发板（esp32p4_wifi6_dev_kit）
  - [Waveshare RP2350B Plus W](../boards_waveshare_tail/P021_Waveshare_RP2350B_Plus_W.md#rp2350b_plus_w)开发板（rp2350b_plus_w）
  - [Waveshare ESP32-P4-ETH](../boards_waveshare_tail/P005_Waveshare_ESP32-P4-ETH.md#waveshare_esp32p4_eth)开发板（waveshare_esp32p4_eth）
- WeAct Studio


  - WeActStudio CH32V00x核心板（CoreBoard）（ch32v00x_core）（[WeActStudio CH32V00xCoreBoard](../boards_weact/P008_WeActStudio_CH32V00xCoreBoard.md#ch32v00x_core)）
  - MiniSTM32H750 核心板（Core Board）（mini_stm32h750）（[MiniSTM32H750核心板](../boards_weact/P015_MiniSTM32H750_Core_Board.md#mini_stm32h750)）
  - [USB2CANFDV2](../boards_weact/P027_USB2CANFDV2.md#usb2canfdv2)开发板（usb2canfdv2）
  - WeAct RA4M1 核心板（Core Board）（weact_ra4m1_core）（[WeAct RA4M1核心板](../boards_weact/P017_WeAct_RA4M1_Core_Board.md#weact_ra4m1_core)）
- WinChipHead


  - [WCH CH32H417EVT](../boards_waveshare_tail/P022_WCH_CH32H417EVT.md#ch32h417evt)开发板（ch32h417evt）
  - [WCH CH32V103EVT](../boards_waveshare_tail/P026_WCH_CH32V103EVT.md#ch32v103evt)开发板（ch32v103evt）
  - [WCH CH32V203EVT](../boards_waveshare_tail/P027_WCH_CH32V203EVT.md#ch32v203c8t6evt)开发板（ch32v203c8t6evt）
  - [WCH CH32V305F-EVT-R0](../boards_waveshare_tail/P029_WCH_CH32V305F-EVT-R0.md#ch32v305f_evt_r0)开发板（ch32v305f_evt_r0）
- WIZnet Co., Ltd.


  - [W55RP20-EVB-Pico](../boards_waveshare_tail/P045_W55RP20-EVB-Pico.md#w55rp20_evb_pico)开发板（w55rp20_evb_pico）
  - [W6100-EVB-Pico](../boards_waveshare_tail/P046_W6100-EVB-Pico.md#w6100_evb_pico)开发板（w6100_evb_pico）
  - [W6100-EVB-Pico2](../boards_waveshare_tail/P047_W6100-EVB-Pico2.md#w6100_evb_pico2)开发板（w6100_evb_pico2）
  - [W6300-EVB-Pico2](../boards_waveshare_tail/P048_W6300-EVB-Pico2.md#w6300_evb_pico2)开发板（w6300_evb_pico2）

<a id="new-shields"></a>

<a id="shields-added-in-zephyr-4-5"></a>

## 新增扩展板（New Shields）


- [AD-APARDPFW-SL](../boards_shields/P002_AD-APARDPFW-SL.md#ad-apardpfw-sl)
- [Adafruit FeatherWing MAX3421E扩展板（Shield）](../boards_shields/P017_Adafruit_FeatherWing_MAX3421E_Shield.md#adafruit-featherwing-max3421e)
- [Adafruit ISM330DHCX扩展板（Shield）](../boards_shields/P024_Adafruit_ISM330DHCX_Shield.md#adafruit-ism330dhcx)
- [Analog Devices低速混合信号实验平台（Low-Speed Mixed-Signal Playground）](../boards_shields/P041_Analog_Devices_Low-Speed_Mixed-Signal_Playground.md#adi-lsmspg)
- [ArduCam Mega SPI摄像头扩展板（Camera Shield）](../boards_shields/P045_ArduCam_Mega_SPI_Camera_Shield.md#arducam-mega)
- [DFRobot Gravity TM6605触觉电机驱动模块（Haptic Motor Driver Module）](../boards_shields/P059_DFRobot_Gravity_TM6605_Haptic_Motor_Driver_Module.md#dfrobot-gravity-tm6605)
- [DH electronics DHSBC RS485 CAN扩展板（Shield）](../boards_shields/P060_DH_electronics_DHSBC_RS485_CAN_Shield.md#dhsbc-rs485-can-shield)
- [EVAL-AD5529R-ARDZ](../boards_shields/P066_EVAL-AD5529R-ARDZ.md#eval-ad5529r-ardz)
- [M5Stack Unit手势模块（Gesture）](../boards_shields/P084_M5Stack_Unit_Gesture.md#m5stack-unit-gesture-shield)
- [M5Stack Unit Mini OLED模块](../boards_shields/P085_M5Stack_Unit_Mini_OLED.md#m5stack-unit-minioled-shield)
- [MB1280 STMod+扇出扩展板（Fan-out Shield）](../boards_shields/P087_MB1280_STMod_fan-out_shield.md#mb1280-stmod-plus)
- [MikroElektronika DALI 2 Click照明总线扩展板](../boards_shields/P098_MikroElektronika_DALI_2_Click.md#mikroe-dali-2-click-shield)
- [MikroElektronika EERAM 3.3V Click存储扩展板](../boards_shields/P100_MikroElektronika_EERAM_3.3V_Click.md#mikroe-eeram-33v-click-shield)
- [MikroElektronika LIN Click总线扩展板](../boards_shields/P109_MikroElektronika_LIN_Click.md#mikroe-lin-click-shield)
- [MikroElektronika Two Wire ETH Click双线以太网扩展板](../boards_shields/P122_MikroElektronika_Two_Wire_ETH_Click.md#mikroe-two-wire-eth-click-shield)
- [NXP Arduino Wi-Fi及蓝牙扩展板（BT Shield）](../boards_shields/P134_NXP_Arduino_WiFi_and_BT_Shield.md#nxp-arduino-wifi-bt)
- [NXP M.2 IEEE 802.15.4 SPI无线协处理器扩展板（RCP Shield）](../boards_shields/P136_NXP_M.2_IEEE_802.15.4_SPI_RCP_Shield.md#nxp-m2-ieee802154)
- [NXP MX8 DSI OLED1A显示面板（Panel）](../boards_shields/P138_NXP_MX8_DSI_OLED1A_Panel.md#nxp-mx8-dsi-oled1a)
- [NXP MX9 DSI OLED显示面板（Panel）](../boards_shields/P139_NXP_MX9_DSI_OLED_Panel.md#nxp-mx9-dsi-oled)
- [OD-6010分段LCD面板扩展板（SLCD Panel Shield）](../boards_shields/P141_OD-6010_SLCD_Panel_Shield.md#od-6010-shield)
- [RAK19007第二代WisBlock基板（Base Board 2nd Gen）](../boards_shields/P147_RAK19007_WisBlock_Base_Board_2nd_Gen.md#rakwireless-rak19007)
- [RTKAPPLCDMS02001BE MIPI显示屏（Display）](../boards_shields/P159_RTKAPPLCDMS02001BE_MIPI_Display.md#rtkapplcdms02001be)
- [Seeed Studio XIAO COB LED驱动板（Driver Board）](../boards_shields/P163_Seeed_Studio_COB_LED_Driver_Board_for_XIAO.md#seeed-xiao-cob-led)
- [ST B-M2MEM-PACK1 M.2串行存储器套件](../boards_shields/P184_ST_B-M2MEM-PACK1_M.2_serial_memory_pack.md#st-b-m2mem-pack1-shield)
- [X-NUCLEO-67W61M1：Wi-Fi 6扩展板](../boards_shields/P202_X-NUCLEO-67W61M1_Wi-Fi_6_expansion_board.md#x-nucleo-67w61m1)
- [X-NUCLEO-GFX02Z1显示扩展板](../boards_shields/P206_X-NUCLEO-GFX02Z1_Display_expansion_board.md#x-nucleo-gfx02z1-shield)
- [X-NUCLEO-GNSS1A1：基于Teseo-LIV3F的GNSS扩展板](../boards_shields/P207_X-NUCLEO-GNSS1A1_GNSS_expansion_board_based_on_Teseo-LIV3F.md#x-nucleo-gnss1a1)
- [X-NUCLEO-PGEEZ1页式EEPROM扩展板（Page EEPROM）](../boards_shields/P215_X-NUCLEO-PGEEZ1_page_EEPROM_expansion_board.md#x-nucleo-pgeez1-shield)
- [X-NUCLEO-WBA25A1：低功耗蓝牙BLE扩展板](../boards_shields/P217_X-NUCLEO-WBA25A1_BLE_expansion_board.md#x-nucleo-wba25a1)

<a id="new-drivers"></a>

## 新增驱动（New Drivers）


- 模数转换器（ADC）


  - [adi,ad4190-8-adc](../hardware/P916_ADIAD4190-8模数转换器绑定.md#dtbinding-adi-ad4190-8-adc)（[GitHub #111922](https://github.com/zephyrproject-rtos/zephyr/issues/111922)）
  - [adi,ad4195-8-adc](../hardware/P918_ADIAD4195-8模数转换器绑定.md#dtbinding-adi-ad4195-8-adc)（[GitHub #111922](https://github.com/zephyrproject-rtos/zephyr/issues/111922)）
  - [adi,ade7913](../hardware/P922_ADIADE7913模数转换器绑定.md#dtbinding-adi-ade7913)（[GitHub #119917](https://github.com/zephyrproject-rtos/zephyr/issues/119917)）
  - [infineon,autanalog-sar-fifo](../hardware/P879_Infineon自主模拟SAR队列绑定.md#dtbinding-infineon-autanalog-sar-fifo)（[GitHub #110289](https://github.com/zephyrproject-rtos/zephyr/issues/110289)）
  - [infineon,autanalog-sar-fir](../hardware/P880_Infineon自主模拟SAR有限冲激响应滤波器绑定.md#dtbinding-infineon-autanalog-sar-fir)（[GitHub #110289](https://github.com/zephyrproject-rtos/zephyr/issues/110289)）
  - [m5stack,m5pm1-adc](../hardware/P924_M5PM1模数转换器绑定.md#dtbinding-m5stack-m5pm1-adc)（[GitHub #109961](https://github.com/zephyrproject-rtos/zephyr/issues/109961)）
  - [nxp,aon-lpadc](../hardware/P848_NXPAON低功耗ADC绑定.md#dtbinding-nxp-aon-lpadc)（[GitHub #114823](https://github.com/zephyrproject-rtos/zephyr/issues/114823)）
  - [realtek,ameba-adc](../hardware/P895_RealtekAmeba模数转换器绑定.md#dtbinding-realtek-ameba-adc)（[GitHub #106677](https://github.com/zephyrproject-rtos/zephyr/issues/106677)）
  - [realtek,bee-adc](../hardware/P896_RealtekBee模数转换器绑定.md#dtbinding-realtek-bee-adc)（[GitHub #105264](https://github.com/zephyrproject-rtos/zephyr/issues/105264)）
  - [renesas,ra-adc-b](../hardware/P867_RenesasRAADCB实例绑定.md#dtbinding-renesas-ra-adc-b)（[GitHub #111255](https://github.com/zephyrproject-rtos/zephyr/issues/111255)）
  - [renesas,ra-adc-b-controller](../hardware/P865_RenesasRAADCB控制器绑定.md#dtbinding-renesas-ra-adc-b-controller)（[GitHub #111255](https://github.com/zephyrproject-rtos/zephyr/issues/111255)）
  - [renesas,ra-adc-b-scan-group](../hardware/P866_RenesasRAADCB扫描组绑定.md#dtbinding-renesas-ra-adc-b-scan-group)（[GitHub #111255](https://github.com/zephyrproject-rtos/zephyr/issues/111255)）
  - [silabs,series3-adc](../hardware/P901_SiliconLabsSeries3模数转换器绑定.md#dtbinding-silabs-series3-adc)（[GitHub #117617](https://github.com/zephyrproject-rtos/zephyr/issues/117617)）
  - [ti,adc081c021](../hardware/P941_ADC081C021模数转换器绑定.md#dtbinding-ti-adc081c021)（[GitHub #114289](https://github.com/zephyrproject-rtos/zephyr/issues/114289)）
  - [ti,adc081c027](../hardware/P942_ADC081C027模数转换器绑定.md#dtbinding-ti-adc081c027)（[GitHub #114289](https://github.com/zephyrproject-rtos/zephyr/issues/114289)）
  - [ti,adc101c021](../hardware/P943_ADC101C021模数转换器绑定.md#dtbinding-ti-adc101c021)（[GitHub #114289](https://github.com/zephyrproject-rtos/zephyr/issues/114289)）
  - [ti,adc101c027](../hardware/P944_ADC101C027模数转换器绑定.md#dtbinding-ti-adc101c027)（[GitHub #114289](https://github.com/zephyrproject-rtos/zephyr/issues/114289)）
  - [ti,adc121c021](../hardware/P945_ADC121C021模数转换器绑定.md#dtbinding-ti-adc121c021)（[GitHub #114289](https://github.com/zephyrproject-rtos/zephyr/issues/114289)）
  - [ti,adc121c027](../hardware/P946_ADC121C027模数转换器绑定.md#dtbinding-ti-adc121c027)（[GitHub #114289](https://github.com/zephyrproject-rtos/zephyr/issues/114289)）
  - [ti,adc124s021](../hardware/P947_ADC124S021模数转换器绑定.md#dtbinding-ti-adc124s021)（[GitHub #110376](https://github.com/zephyrproject-rtos/zephyr/issues/110376)）
  - [ti,ads1118](../hardware/P955_ADS1118模数转换器绑定.md#dtbinding-ti-ads1118)（[GitHub #94152](https://github.com/zephyrproject-rtos/zephyr/issues/94152)）
  - [ti,ads1220](../hardware/P959_ADS1220模数转换器绑定.md#dtbinding-ti-ads1220)（[GitHub #102479](https://github.com/zephyrproject-rtos/zephyr/issues/102479)）
  - [ti,ads1262](../hardware/P962_ADS1262模数转换器绑定.md#dtbinding-ti-ads1262)（[GitHub #119341](https://github.com/zephyrproject-rtos/zephyr/issues/119341)）
  - [ti,ads1263](../hardware/P963_ADS1263模数转换器绑定.md#dtbinding-ti-ads1263)（[GitHub #119341](https://github.com/zephyrproject-rtos/zephyr/issues/119341)）
  - [ti,ads7828](../hardware/P966_ADS7828模数转换器绑定.md#dtbinding-ti-ads7828)（[GitHub #114359](https://github.com/zephyrproject-rtos/zephyr/issues/114359)）
  - [ti,ads7830](../hardware/P967_ADS7830模数转换器绑定.md#dtbinding-ti-ads7830)（[GitHub #114359](https://github.com/zephyrproject-rtos/zephyr/issues/114359)）
  - [ti,mspm0-adc12](../hardware/P908_TIMSPM0ADC12绑定.md#dtbinding-ti-mspm0-adc12)（[GitHub #94736](https://github.com/zephyrproject-rtos/zephyr/issues/94736)）
  - [ti,tla2528-adc](../hardware/P991_TLA2528模数转换器绑定.md#dtbinding-ti-tla2528-adc)（[GitHub #110722](https://github.com/zephyrproject-rtos/zephyr/issues/110722)）
  - [wisblock-adc](../hardware/P910_WisBlock模数转换器绑定.md#dtbinding-wisblock-adc)（[GitHub #113140](https://github.com/zephyrproject-rtos/zephyr/issues/113140)）
- ARM 架构（ARM Architecture）


  - [infineon,edge-npu](../arm_timing_ethosu_control_binding_reference/P010_infineon_edge-npu.md#std-dtcompatible-infineon-edge-npu)（[GitHub #106826](https://github.com/zephyrproject-rtos/zephyr/issues/106826)）
  - [nordic,nrf-wicr](../arm_nordic_nxp_control_binding_reference/P008_nordic_nrf-wicr.md#std-dtcompatible-nordic-nrf-wicr)（[GitHub #108141](https://github.com/zephyrproject-rtos/zephyr/issues/108141)）
  - [nordic,nrf71-uicr](../arm_nordic_nxp_control_binding_reference/P009_nordic_nrf71-uicr.md#std-dtcompatible-nordic-nrf71-uicr)（[GitHub #106134](https://github.com/zephyrproject-rtos/zephyr/issues/106134)）
  - [nordic,nrf71-wifi-antsw](../arm_nordic_nxp_control_binding_reference/P010_nordic_nrf71-wifi-antsw.md#std-dtcompatible-nordic-nrf71-wifi-antsw)（[GitHub #118028](https://github.com/zephyrproject-rtos/zephyr/issues/118028)）
- 音频（Audio）


  - [cirrus,cs35l56](../compatible_binding_reference/P027_cirrus_cs35l56.md#std-dtcompatible-cirrus-cs35l56)（[GitHub #116349](https://github.com/zephyrproject-rtos/zephyr/issues/116349)）
  - [cirrus,cs35l57](../compatible_binding_reference/P028_cirrus_cs35l57.md#std-dtcompatible-cirrus-cs35l57)（[GitHub #116349](https://github.com/zephyrproject-rtos/zephyr/issues/116349)）
  - [renesas,ra-pdm](../audio_pdm_codec_binding_reference/P015_renesas_ra-pdm.md#std-dtcompatible-renesas-ra-pdm)（[GitHub #119641](https://github.com/zephyrproject-rtos/zephyr/issues/119641)）
  - [st,stm32-dfsdm](../audio_stm32_ti_wolfson_binding_reference/P002_st_stm32-dfsdm.md#std-dtcompatible-st-stm32-dfsdm)（[GitHub #108302](https://github.com/zephyrproject-rtos/zephyr/issues/108302)）
  - [st,stm32-dfsdm-dmic](../audio_stm32_ti_wolfson_binding_reference/P001_st_stm32-dfsdm-dmic.md#std-dtcompatible-st-stm32-dfsdm-dmic)（[GitHub #108302](https://github.com/zephyrproject-rtos/zephyr/issues/108302)）
  - [st,stm32-mdf](../audio_stm32_ti_wolfson_binding_reference/P003_st_stm32-mdf.md#std-dtcompatible-st-stm32-mdf)（[GitHub #112277](https://github.com/zephyrproject-rtos/zephyr/issues/112277)）
  - [ti,tas2563](../audio_stm32_ti_wolfson_binding_reference/P006_ti_tas2563.md#std-dtcompatible-ti-tas2563)（[GitHub #103148](https://github.com/zephyrproject-rtos/zephyr/issues/103148)）
  - [ti,tlv320aic26](../audio_stm32_ti_wolfson_binding_reference/P008_ti_tlv320aic26.md#std-dtcompatible-ti-tlv320aic26)（[GitHub #106836](https://github.com/zephyrproject-rtos/zephyr/issues/106836)）
  - [wolfson,wm8960](../audio_stm32_ti_wolfson_binding_reference/P012_wolfson_wm8960.md#std-dtcompatible-wolfson-wm8960)（[GitHub #106212](https://github.com/zephyrproject-rtos/zephyr/issues/106212)）
  - [zephyr,dummy-codec](../audio_stm32_ti_wolfson_binding_reference/P014_zephyr_dummy-codec.md#std-dtcompatible-zephyr-dummy-codec)（[GitHub #109891](https://github.com/zephyrproject-rtos/zephyr/issues/109891)）
  - [zephyr,native-sim-dmic](../audio_stm32_ti_wolfson_binding_reference/P015_zephyr_native-sim-dmic.md#std-dtcompatible-zephyr-native-sim-dmic)（[GitHub #109898](https://github.com/zephyrproject-rtos/zephyr/issues/109898)）
- 辅助显示器（Auxiliary Display）


  - [nxp,slcd](../auxdisplay_iio_tach_binding_reference/P005_nxp_slcd.md#std-dtcompatible-nxp-slcd)（[GitHub #102796](https://github.com/zephyrproject-rtos/zephyr/issues/102796)）
  - [slcd-panel](../auxdisplay_iio_tach_binding_reference/P007_slcd-panel.md#std-dtcompatible-slcd-panel)（[GitHub #102796](https://github.com/zephyrproject-rtos/zephyr/issues/102796)）
- 蓝牙（Bluetooth）


  - [espressif,esp-hosted-mcu-bt-hci](../bluetooth_vendor_hci_binding_reference/P003_espressif_esp-hosted-mcu-bt-hci.md#std-dtcompatible-espressif-esp-hosted-mcu-bt-hci)（[GitHub #114532](https://github.com/zephyrproject-rtos/zephyr/issues/114532)）
  - [realtek,ameba-bt-hci](../bluetooth_vendor_hci_binding_reference/P010_realtek_ameba-bt-hci.md#std-dtcompatible-realtek-ameba-bt-hci)（[GitHub #109287](https://github.com/zephyrproject-rtos/zephyr/issues/109287)）
  - [zephyr,bt-hci-spi-peripheral](../bluetooth_st_transport_binding_reference/P010_zephyr_bt-hci-spi-peripheral.md#std-dtcompatible-zephyr-bt-hci-spi-peripheral)（[GitHub #116155](https://github.com/zephyrproject-rtos/zephyr/issues/116155)）
- 蜂鸣器（Buzzer）


  - [gpio-buzzer](../sound_haptic_binding_reference/P002_gpio-buzzer.md#std-dtcompatible-gpio-buzzer)（[GitHub #108911](https://github.com/zephyrproject-rtos/zephyr/issues/108911)）
  - [pwm-buzzer](../sound_haptic_binding_reference/P003_pwm-buzzer.md#std-dtcompatible-pwm-buzzer)（[GitHub #108911](https://github.com/zephyrproject-rtos/zephyr/issues/108911)）
- 控制器局域网（CAN）


  - [bflb,bl61x-can](../can_adi_atmel_nxp_binding_reference/P004_bflb_bl61x-can.md#std-dtcompatible-bflb-bl61x-can)（[GitHub #110672](https://github.com/zephyrproject-rtos/zephyr/issues/110672)）
  - [espressif,esp32-twaifd](../can_adi_atmel_nxp_binding_reference/P006_espressif_esp32-twaifd.md#std-dtcompatible-espressif-esp32-twaifd)（[GitHub #107680](https://github.com/zephyrproject-rtos/zephyr/issues/107680)）
  - [realtek,bee-can](../can_nxp_renesas_stm32_ti_binding_reference/P003_realtek_bee-can.md#std-dtcompatible-realtek-bee-can)（[GitHub #105411](https://github.com/zephyrproject-rtos/zephyr/issues/105411)）
  - [renesas,rcar-rscanfd](../can_nxp_renesas_stm32_ti_binding_reference/P008_renesas_rcar-rscanfd.md#std-dtcompatible-renesas-rcar-rscanfd)（[GitHub #109782](https://github.com/zephyrproject-rtos/zephyr/issues/109782)）
  - [renesas,rcar-rscanfd-global](../can_nxp_renesas_stm32_ti_binding_reference/P007_renesas_rcar-rscanfd-global.md#std-dtcompatible-renesas-rcar-rscanfd-global)（[GitHub #109782](https://github.com/zephyrproject-rtos/zephyr/issues/109782)）
- 充电器（Charger）


  - [adi,adp5360-charger](../charger_binding_reference/P001_adi_adp5360-charger.md#std-dtcompatible-adi-adp5360-charger)（[GitHub #105258](https://github.com/zephyrproject-rtos/zephyr/issues/105258)）
  - [silergy,sy6974b](../charger_binding_reference/P007_silergy_sy6974b.md#std-dtcompatible-silergy-sy6974b)（[GitHub #107439](https://github.com/zephyrproject-rtos/zephyr/issues/107439)）
  - [ti,bq24295](../charger_binding_reference/P009_ti_bq24295.md#std-dtcompatible-ti-bq24295)（[GitHub #114650](https://github.com/zephyrproject-rtos/zephyr/issues/114650)）
  - [ti,bq24296](../charger_binding_reference/P010_ti_bq24296.md#std-dtcompatible-ti-bq24296)（[GitHub #114650](https://github.com/zephyrproject-rtos/zephyr/issues/114650)）
  - [ti,bq24296m](../charger_binding_reference/P011_ti_bq24296m.md#std-dtcompatible-ti-bq24296m)（[GitHub #114650](https://github.com/zephyrproject-rtos/zephyr/issues/114650)）
  - [ti,bq24297](../charger_binding_reference/P012_ti_bq24297.md#std-dtcompatible-ti-bq24297)（[GitHub #114650](https://github.com/zephyrproject-rtos/zephyr/issues/114650)）
  - [ti,bq24298](../charger_binding_reference/P013_ti_bq24298.md#std-dtcompatible-ti-bq24298)（[GitHub #114650](https://github.com/zephyrproject-rtos/zephyr/issues/114650)）
- 时钟控制（Clock Control）


  - [adi,axi-clkgen](../clock_adi_atmel_bflb_binding_reference/P001_adi_axi-clkgen.md#std-dtcompatible-adi-axi-clkgen)（[GitHub #115291](https://github.com/zephyrproject-rtos/zephyr/issues/115291)）
  - [adi,max32-erfo](../clock_adi_atmel_bflb_binding_reference/P002_adi_max32-erfo.md#std-dtcompatible-adi-max32-erfo)（[GitHub #115434](https://github.com/zephyrproject-rtos/zephyr/issues/115434)）
  - [adi,max32-extclk](../clock_adi_atmel_bflb_binding_reference/P003_adi_max32-extclk.md#std-dtcompatible-adi-max32-extclk)（[GitHub #117709](https://github.com/zephyrproject-rtos/zephyr/issues/117709)）
  - [aesc,clock-controller](../clock_adi_atmel_bflb_binding_reference/P005_aesc_clock-controller.md#std-dtcompatible-aesc-clock-controller)（[GitHub #116703](https://github.com/zephyrproject-rtos/zephyr/issues/116703)）
  - [alif,clock-mux](../timer_reference/P115_Alif时钟多路复用绑定.md#dtbinding-alif-clock-mux)（[GitHub #119665](https://github.com/zephyrproject-rtos/zephyr/issues/119665)）
  - [bflb,bl616cl-clock-controller](../clock_adi_atmel_bflb_binding_reference/P015_bflb_bl616cl-clock-controller.md#std-dtcompatible-bflb-bl616cl-clock-controller)（[GitHub #112738](https://github.com/zephyrproject-rtos/zephyr/issues/112738)）
  - [bflb,bl808-clock-controller](../clock_adi_atmel_bflb_binding_reference/P020_bflb_bl808-clock-controller.md#std-dtcompatible-bflb-bl808-clock-controller)（[GitHub #105580](https://github.com/zephyrproject-rtos/zephyr/issues/105580)）
  - [bflb,mm-clk](../clock_adi_atmel_bflb_binding_reference/P024_bflb_mm-clk.md#std-dtcompatible-bflb-mm-clk)（[GitHub #105580](https://github.com/zephyrproject-rtos/zephyr/issues/105580)）
  - [infineon,cat1c-clk-hf](../clock_esp_infineon_microchip_binding_reference/P006_infineon_cat1c-clk-hf.md#std-dtcompatible-infineon-cat1c-clk-hf)（[GitHub #108259](https://github.com/zephyrproject-rtos/zephyr/issues/108259)）
  - [infineon,clk-osc](../timer_reference/P114_Infineon振荡器时钟绑定.md#dtbinding-infineon-clk-osc)（[GitHub #108259](https://github.com/zephyrproject-rtos/zephyr/issues/108259)）
  - [infineon,clk-pll](../clock_esp_infineon_microchip_binding_reference/P007_infineon_clk-pll.md#std-dtcompatible-infineon-clk-pll)（[GitHub #108259](https://github.com/zephyrproject-rtos/zephyr/issues/108259)）
  - [infineon,peri-clk](../clock_esp_infineon_microchip_binding_reference/P008_infineon_peri-clk.md#std-dtcompatible-infineon-peri-clk)（[GitHub #108259](https://github.com/zephyrproject-rtos/zephyr/issues/108259)）
  - [mediatek,mt8188-infracfg-ao](../clock_esp_infineon_microchip_binding_reference/P016_mediatek_mt8188-infracfg-ao.md#std-dtcompatible-mediatek-mt8188-infracfg-ao)（[GitHub #118658](https://github.com/zephyrproject-rtos/zephyr/issues/118658)）
  - [microchip,pic32ck-sg-gc-clock](../clock_esp_infineon_microchip_binding_reference/P022_microchip_pic32ck-sg-gc-clock.md#std-dtcompatible-microchip-pic32ck-sg-gc-clock)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-dfll48m](../clock_esp_infineon_microchip_binding_reference/P023_microchip_pic32ck-sg-gc-dfll48m.md#std-dtcompatible-microchip-pic32ck-sg-gc-dfll48m)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-gclkgen](../clock_esp_infineon_microchip_binding_reference/P024_microchip_pic32ck-sg-gc-gclkgen.md#std-dtcompatible-microchip-pic32ck-sg-gc-gclkgen)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-gclkperiph](../clock_esp_infineon_microchip_binding_reference/P025_microchip_pic32ck-sg-gc-gclkperiph.md#std-dtcompatible-microchip-pic32ck-sg-gc-gclkperiph)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-mclkcpu](../clock_microchip_pic32_binding_reference/P001_microchip_pic32ck-sg-gc-mclkcpu.md#std-dtcompatible-microchip-pic32ck-sg-gc-mclkcpu)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-mclkperiph](../clock_microchip_pic32_binding_reference/P002_microchip_pic32ck-sg-gc-mclkperiph.md#std-dtcompatible-microchip-pic32ck-sg-gc-mclkperiph)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-pll](../clock_microchip_pic32_binding_reference/P003_microchip_pic32ck-sg-gc-pll.md#std-dtcompatible-microchip-pic32ck-sg-gc-pll)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-rtc](../clock_microchip_pic32_binding_reference/P004_microchip_pic32ck-sg-gc-rtc.md#std-dtcompatible-microchip-pic32ck-sg-gc-rtc)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-xosc](../clock_microchip_pic32_binding_reference/P005_microchip_pic32ck-sg-gc-xosc.md#std-dtcompatible-microchip-pic32ck-sg-gc-xosc)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32ck-sg-gc-xosc32k](../clock_microchip_pic32_binding_reference/P006_microchip_pic32ck-sg-gc-xosc32k.md#std-dtcompatible-microchip-pic32ck-sg-gc-xosc32k)（[GitHub #116592](https://github.com/zephyrproject-rtos/zephyr/issues/116592)）
  - [microchip,pic32cm-sg-gc-clock](../clock_microchip_pic32_sam_binding_reference/P002_microchip_pic32cm-sg-gc-clock.md#std-dtcompatible-microchip-pic32cm-sg-gc-clock)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-dfll48m](../clock_microchip_pic32_sam_binding_reference/P003_microchip_pic32cm-sg-gc-dfll48m.md#std-dtcompatible-microchip-pic32cm-sg-gc-dfll48m)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-dpll](../clock_microchip_pic32_sam_binding_reference/P004_microchip_pic32cm-sg-gc-dpll.md#std-dtcompatible-microchip-pic32cm-sg-gc-dpll)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-gclkgen](../clock_microchip_pic32_sam_binding_reference/P005_microchip_pic32cm-sg-gc-gclkgen.md#std-dtcompatible-microchip-pic32cm-sg-gc-gclkgen)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-gclkperiph](../clock_microchip_pic32_sam_binding_reference/P006_microchip_pic32cm-sg-gc-gclkperiph.md#std-dtcompatible-microchip-pic32cm-sg-gc-gclkperiph)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-mclkdomain](../clock_microchip_pic32_sam_binding_reference/P007_microchip_pic32cm-sg-gc-mclkdomain.md#std-dtcompatible-microchip-pic32cm-sg-gc-mclkdomain)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-mclkperiph](../clock_microchip_pic32_sam_binding_reference/P008_microchip_pic32cm-sg-gc-mclkperiph.md#std-dtcompatible-microchip-pic32cm-sg-gc-mclkperiph)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-rtc](../clock_microchip_pic32_sam_binding_reference/P009_microchip_pic32cm-sg-gc-rtc.md#std-dtcompatible-microchip-pic32cm-sg-gc-rtc)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-xosc](../clock_microchip_pic32_sam_binding_reference/P010_microchip_pic32cm-sg-gc-xosc.md#std-dtcompatible-microchip-pic32cm-sg-gc-xosc)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,pic32cm-sg-gc-xosc32k](../clock_microchip_pic32_sam_binding_reference/P011_microchip_pic32cm-sg-gc-xosc32k.md#std-dtcompatible-microchip-pic32cm-sg-gc-xosc32k)（[GitHub #112582](https://github.com/zephyrproject-rtos/zephyr/issues/112582)）
  - [microchip,smartfusion2-clock](../clock_sam_nordic_binding_reference/P007_microchip_smartfusion2-clock.md#std-dtcompatible-microchip-smartfusion2-clock)（[GitHub #106926](https://github.com/zephyrproject-rtos/zephyr/issues/106926)）
  - [nordic,nrf-clock-hfclk](../clock_sam_nordic_binding_reference/P009_nordic_nrf-clock-hfclk.md#std-dtcompatible-nordic-nrf-clock-hfclk)（[GitHub #104658](https://github.com/zephyrproject-rtos/zephyr/issues/104658)）
  - [nordic,nrf-clock-hfclk192m](../clock_sam_nordic_binding_reference/P010_nordic_nrf-clock-hfclk192m.md#std-dtcompatible-nordic-nrf-clock-hfclk192m)（[GitHub #104658](https://github.com/zephyrproject-rtos/zephyr/issues/104658)）
  - [nordic,nrf-clock-hfclkaudio](../clock_sam_nordic_binding_reference/P011_nordic_nrf-clock-hfclkaudio.md#std-dtcompatible-nordic-nrf-clock-hfclkaudio)（[GitHub #104658](https://github.com/zephyrproject-rtos/zephyr/issues/104658)）
  - [nordic,nrf-clock-lfclk](../clock_sam_nordic_binding_reference/P012_nordic_nrf-clock-lfclk.md#std-dtcompatible-nordic-nrf-clock-lfclk)（[GitHub #104658](https://github.com/zephyrproject-rtos/zephyr/issues/104658)）
  - [nordic,nrf-clock-xo](../clock_sam_nordic_binding_reference/P013_nordic_nrf-clock-xo.md#std-dtcompatible-nordic-nrf-clock-xo)（[GitHub #104658](https://github.com/zephyrproject-rtos/zephyr/issues/104658)）
  - [nordic,nrf-clock-xo24m](../clock_sam_nordic_binding_reference/P014_nordic_nrf-clock-xo24m.md#std-dtcompatible-nordic-nrf-clock-xo24m)（[GitHub #104658](https://github.com/zephyrproject-rtos/zephyr/issues/104658)）
  - [nordic,nrf-lfrc](../clock_sam_nordic_binding_reference/P020_nordic_nrf-lfrc.md#std-dtcompatible-nordic-nrf-lfrc)（[GitHub #118582](https://github.com/zephyrproject-rtos/zephyr/issues/118582)）
  - [nuvoton,m4-hclk-clock](../clock_nordic_nuvoton_nxp_binding_reference/P004_nuvoton_m4-hclk-clock.md#std-dtcompatible-nuvoton-m4-hclk-clock)（[GitHub #103668](https://github.com/zephyrproject-rtos/zephyr/issues/103668)）
  - [nuvoton,m4-hxt-clock](../clock_nordic_nuvoton_nxp_binding_reference/P005_nuvoton_m4-hxt-clock.md#std-dtcompatible-nuvoton-m4-hxt-clock)（[GitHub #103668](https://github.com/zephyrproject-rtos/zephyr/issues/103668)）
  - [nuvoton,m4-lxt-clock](../clock_nordic_nuvoton_nxp_binding_reference/P006_nuvoton_m4-lxt-clock.md#std-dtcompatible-nuvoton-m4-lxt-clock)（[GitHub #103668](https://github.com/zephyrproject-rtos/zephyr/issues/103668)）
  - [nuvoton,m4-pll-clock](../clock_nordic_nuvoton_nxp_binding_reference/P007_nuvoton_m4-pll-clock.md#std-dtcompatible-nuvoton-m4-pll-clock)（[GitHub #103668](https://github.com/zephyrproject-rtos/zephyr/issues/103668)）
  - [nuvoton,numicro-m4-pcc](../clock_nordic_nuvoton_nxp_binding_reference/P012_nuvoton_numicro-m4-pcc.md#std-dtcompatible-nuvoton-numicro-m4-pcc)（[GitHub #103668](https://github.com/zephyrproject-rtos/zephyr/issues/103668)）
  - [nuvoton,numicro-m4-scc](../clock_nordic_nuvoton_nxp_binding_reference/P013_nuvoton_numicro-m4-scc.md#std-dtcompatible-nuvoton-numicro-m4-scc)（[GitHub #103668](https://github.com/zephyrproject-rtos/zephyr/issues/103668)）
  - [nxp,imx-ccm-rev3](../clock_nordic_nuvoton_nxp_binding_reference/P020_nxp_imx-ccm-rev3.md#std-dtcompatible-nxp-imx-ccm-rev3)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-ccm-rev3-root](../clock_nordic_nuvoton_nxp_binding_reference/P019_nxp_imx-ccm-rev3-root.md#std-dtcompatible-nxp-imx-ccm-rev3-root)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-cguana](../clock_nordic_nuvoton_nxp_binding_reference/P028_nxp_imx-cguana.md#std-dtcompatible-nxp-imx-cguana)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-cguana-avpll](../clock_nordic_nuvoton_nxp_binding_reference/P022_nxp_imx-cguana-avpll.md#std-dtcompatible-nxp-imx-cguana-avpll)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-cguana-core-pll](../clock_nordic_nuvoton_nxp_binding_reference/P023_nxp_imx-cguana-core-pll.md#std-dtcompatible-nxp-imx-cguana-core-pll)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-cguana-frac-pll](../clock_nordic_nuvoton_nxp_binding_reference/P024_nxp_imx-cguana-frac-pll.md#std-dtcompatible-nxp-imx-cguana-frac-pll)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-cguana-fro12m](../clock_nordic_nuvoton_nxp_binding_reference/P025_nxp_imx-cguana-fro12m.md#std-dtcompatible-nxp-imx-cguana-fro12m)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-cguana-fro192m](../clock_nordic_nuvoton_nxp_binding_reference/P026_nxp_imx-cguana-fro192m.md#std-dtcompatible-nxp-imx-cguana-fro192m)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx-cguana-sxosc](../clock_nordic_nuvoton_nxp_binding_reference/P027_nxp_imx-cguana-sxosc.md#std-dtcompatible-nxp-imx-cguana-sxosc)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [nxp,imx9-pll](../clock_nordic_nuvoton_nxp_binding_reference/P029_nxp_imx9-pll.md#std-dtcompatible-nxp-imx9-pll)（[GitHub #120033](https://github.com/zephyrproject-rtos/zephyr/issues/120033)）
  - [nxp,imxrt118x-arm-pll](../clock_nordic_nuvoton_nxp_binding_reference/P030_nxp_imxrt118x-arm-pll.md#std-dtcompatible-nxp-imxrt118x-arm-pll)（[GitHub #106881](https://github.com/zephyrproject-rtos/zephyr/issues/106881)）
  - [nxp,imxrt11xx-arm-pll](../clock_nxp_pico_realtek_renesas_binding_reference/P001_nxp_imxrt11xx-arm-pll.md#std-dtcompatible-nxp-imxrt11xx-arm-pll)（[GitHub #106881](https://github.com/zephyrproject-rtos/zephyr/issues/106881)）
  - [nxp,lpc84x-clock](../clock_nxp_pico_realtek_renesas_binding_reference/P009_nxp_lpc84x-clock.md#std-dtcompatible-nxp-lpc84x-clock)（[GitHub #105928](https://github.com/zephyrproject-rtos/zephyr/issues/105928)）
  - [nxp,mcxw7x-clock](../clock_nxp_pico_realtek_renesas_binding_reference/P012_nxp_mcxw7x-clock.md#std-dtcompatible-nxp-mcxw7x-clock)（[GitHub #101937](https://github.com/zephyrproject-rtos/zephyr/issues/101937)）
  - [renesas,rx-cgc-pllccr-type](../clock_renesas_rockchip_sifli_silabs_binding_reference/P009_renesas_rx-cgc-pllccr-type.md#std-dtcompatible-renesas-rx-cgc-pllccr-type)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
  - [rockchip,rk3588-cru](../clock_renesas_rockchip_sifli_silabs_binding_reference/P023_rockchip_rk3588-cru.md#std-dtcompatible-rockchip-rk3588-cru)（[GitHub #117985](https://github.com/zephyrproject-rtos/zephyr/issues/117985)）
  - [rockchip,rk3588-cru-clk](../clock_renesas_rockchip_sifli_silabs_binding_reference/P022_rockchip_rk3588-cru-clk.md#std-dtcompatible-rockchip-rk3588-cru-clk)（[GitHub #117985](https://github.com/zephyrproject-rtos/zephyr/issues/117985)）
  - [silabs,series-clock-output](../clock_renesas_rockchip_sifli_silabs_binding_reference/P028_silabs_series-clock-output.md#std-dtcompatible-silabs-series-clock-output)（[GitHub #118308](https://github.com/zephyrproject-rtos/zephyr/issues/118308)）
  - [silabs,series0-cmu](../clock_renesas_rockchip_sifli_silabs_binding_reference/P030_silabs_series0-cmu.md#std-dtcompatible-silabs-series0-cmu)（[GitHub #111754](https://github.com/zephyrproject-rtos/zephyr/issues/111754)）
  - [silabs,series0-hfxo](../clock_silabs_ti_xilinx_binding_reference/P001_silabs_series0-hfxo.md#std-dtcompatible-silabs-series0-hfxo)（[GitHub #111754](https://github.com/zephyrproject-rtos/zephyr/issues/111754)）
  - [silabs,series0-lfrco](../clock_silabs_ti_xilinx_binding_reference/P002_silabs_series0-lfrco.md#std-dtcompatible-silabs-series0-lfrco)（[GitHub #111754](https://github.com/zephyrproject-rtos/zephyr/issues/111754)）
  - [silabs,series0-lfxo](../clock_silabs_ti_xilinx_binding_reference/P003_silabs_series0-lfxo.md#std-dtcompatible-silabs-series0-lfxo)（[GitHub #111754](https://github.com/zephyrproject-rtos/zephyr/issues/111754)）
  - [silabs,siwx91x-clock-route](../clock_silabs_ti_xilinx_binding_reference/P011_silabs_siwx91x-clock-route.md#std-dtcompatible-silabs-siwx91x-clock-route)（[GitHub #113743](https://github.com/zephyrproject-rtos/zephyr/issues/113743)）
  - [silabs,siwx91x-cmu-aon](../clock_silabs_ti_xilinx_binding_reference/P012_silabs_siwx91x-cmu-aon.md#std-dtcompatible-silabs-siwx91x-cmu-aon)（[GitHub #113743](https://github.com/zephyrproject-rtos/zephyr/issues/113743)）
  - [silabs,siwx91x-cmu-hp](../clock_silabs_ti_xilinx_binding_reference/P013_silabs_siwx91x-cmu-hp.md#std-dtcompatible-silabs-siwx91x-cmu-hp)（[GitHub #113743](https://github.com/zephyrproject-rtos/zephyr/issues/113743)）
  - [silabs,siwx91x-cmu-ulp](../clock_silabs_ti_xilinx_binding_reference/P014_silabs_siwx91x-cmu-ulp.md#std-dtcompatible-silabs-siwx91x-cmu-ulp)（[GitHub #113743](https://github.com/zephyrproject-rtos/zephyr/issues/113743)）
  - [silabs,siwx91x-physical-clock](../clock_silabs_ti_xilinx_binding_reference/P015_silabs_siwx91x-physical-clock.md#std-dtcompatible-silabs-siwx91x-physical-clock)（[GitHub #113743](https://github.com/zephyrproject-rtos/zephyr/issues/113743)）
  - [silabs,siwx91x-pll](../clock_silabs_ti_xilinx_binding_reference/P016_silabs_siwx91x-pll.md#std-dtcompatible-silabs-siwx91x-pll)（[GitHub #113743](https://github.com/zephyrproject-rtos/zephyr/issues/113743)）
  - [silabs,socpll](../clock_silabs_ti_xilinx_binding_reference/P017_silabs_socpll.md#std-dtcompatible-silabs-socpll)（[GitHub #117617](https://github.com/zephyrproject-rtos/zephyr/issues/117617)）
  - [st,stm32h5-pll-clock](../timer_reference/P153_STM32H5锁相环时钟绑定.md#dtbinding-st-stm32h5-pll-clock)（[GitHub #110914](https://github.com/zephyrproject-rtos/zephyr/issues/110914)）
  - [st,stm32n6-msi-clock](../timer_reference/P161_STM32N6多速内部时钟绑定.md#dtbinding-st-stm32n6-msi-clock)（[GitHub #108997](https://github.com/zephyrproject-rtos/zephyr/issues/108997)）
  - [st,stm32wl3-rcc](../timer_reference/P176_STM32WL3复位与时钟控制绑定.md#dtbinding-st-stm32wl3-rcc)（[GitHub #114483](https://github.com/zephyrproject-rtos/zephyr/issues/114483)）
  - [ti,cdce913](../clock_silabs_ti_xilinx_binding_reference/P020_ti_cdce913.md#std-dtcompatible-ti-cdce913)（[GitHub #118204](https://github.com/zephyrproject-rtos/zephyr/issues/118204)）
  - [ti,cdce925](../clock_silabs_ti_xilinx_binding_reference/P021_ti_cdce925.md#std-dtcompatible-ti-cdce925)（[GitHub #118204](https://github.com/zephyrproject-rtos/zephyr/issues/118204)）
  - [ti,cdce937](../clock_silabs_ti_xilinx_binding_reference/P022_ti_cdce937.md#std-dtcompatible-ti-cdce937)（[GitHub #118204](https://github.com/zephyrproject-rtos/zephyr/issues/118204)）
  - [ti,cdce949](../clock_silabs_ti_xilinx_binding_reference/P023_ti_cdce949.md#std-dtcompatible-ti-cdce949)（[GitHub #118204](https://github.com/zephyrproject-rtos/zephyr/issues/118204)）
  - [wch,ch32h41x-pll-clock](../timer_reference/P190_CH32H41x锁相环时钟绑定.md#dtbinding-wch-ch32h41x-pll-clock)（[GitHub #111725](https://github.com/zephyrproject-rtos/zephyr/issues/111725)）
  - [xlnx,clkx5-wiz-1.0](../clock_silabs_ti_xilinx_binding_reference/P028_xlnx_clkx5-wiz-1.0.md#std-dtcompatible-xlnx-clkx5-wiz-1.0)（[GitHub #114205](https://github.com/zephyrproject-rtos/zephyr/issues/114205)）
- 时钟监测（Clock Monitor）


  - [nxp,cmu-fc](../crc_clock_monitor_binding_reference/P001_nxp_cmu-fc.md#std-dtcompatible-nxp-cmu-fc)（[GitHub #107879](https://github.com/zephyrproject-rtos/zephyr/issues/107879)）
  - [nxp,cmu-fm](../crc_clock_monitor_binding_reference/P002_nxp_cmu-fm.md#std-dtcompatible-nxp-cmu-fm)（[GitHub #107879](https://github.com/zephyrproject-rtos/zephyr/issues/107879)）
  - [nxp,fmeas](../crc_clock_monitor_binding_reference/P003_nxp_fmeas.md#std-dtcompatible-nxp-fmeas)（[GitHub #112650](https://github.com/zephyrproject-rtos/zephyr/issues/112650)）
  - [nxp,freqme](../crc_clock_monitor_binding_reference/P004_nxp_freqme.md#std-dtcompatible-nxp-freqme)（[GitHub #112403](https://github.com/zephyrproject-rtos/zephyr/issues/112403)）
- 比较器（Comparator）


  - [espressif,esp32-ana-cmpr](../hardware/P754_ESP32模拟比较器绑定.md#dtbinding-espressif-esp32-ana-cmpr)（[GitHub #113625](https://github.com/zephyrproject-rtos/zephyr/issues/113625)）
  - [infineon,autanalog-ptcomp-comp](../hardware/P735_Infineon可编程阈值比较器通道绑定.md#dtbinding-infineon-autanalog-ptcomp-comp)（[GitHub #107488](https://github.com/zephyrproject-rtos/zephyr/issues/107488)）
  - [infineon,hppass-csg-comp](../hardware/P736_Infineon斜坡发生器比较器绑定.md#dtbinding-infineon-hppass-csg-comp)（[GitHub #109879](https://github.com/zephyrproject-rtos/zephyr/issues/109879)）
  - [infineon,lp-comp](../hardware/P737_Infineon低功耗比较器绑定.md#dtbinding-infineon-lp-comp)（[GitHub #104636](https://github.com/zephyrproject-rtos/zephyr/issues/104636)）
  - [infineon,lp-comp-channel](../hardware/P738_Infineon低功耗比较器通道绑定.md#dtbinding-infineon-lp-comp-channel)（[GitHub #104636](https://github.com/zephyrproject-rtos/zephyr/issues/104636)）
  - [nxp,lpacmp](../hardware/P746_NXP低功耗模拟比较器绑定.md#dtbinding-nxp-lpacmp)（[GitHub #114754](https://github.com/zephyrproject-rtos/zephyr/issues/114754)）
  - [ti,mspm0-comparator](../hardware/P758_TIMSPM0比较器绑定.md#dtbinding-ti-mspm0-comparator)（[GitHub #94737](https://github.com/zephyrproject-rtos/zephyr/issues/94737)）
  - [wch,ch5xx-comparator](../hardware/P759_WCHCH5xx比较器绑定.md#dtbinding-wch-ch5xx-comparator)（[GitHub #115343](https://github.com/zephyrproject-rtos/zephyr/issues/115343)）
- 计数器（Counter）


  - [arm,crsas-ma2-counter](../counter_binding_reference/P008_arm_crsas-ma2-counter.md#std-dtcompatible-arm-crsas-ma2-counter)（[GitHub #112815](https://github.com/zephyrproject-rtos/zephyr/issues/112815)）
  - [arm,crsas-ma2-timer](../counter_binding_reference/P009_arm_crsas-ma2-timer.md#std-dtcompatible-arm-crsas-ma2-timer)（[GitHub #112815](https://github.com/zephyrproject-rtos/zephyr/issues/112815)）
  - [microcrystal,rv3028-counter](../microchip_soc_counter_binding_reference/P014_microcrystal_rv3028-counter.md#std-dtcompatible-microcrystal-rv3028-counter)（[GitHub #115957](https://github.com/zephyrproject-rtos/zephyr/issues/115957)）
  - [nxp,irtc-wake-timer](../nxp_nuvoton_counter_binding_reference/P008_nxp_irtc-wake-timer.md#std-dtcompatible-nxp-irtc-wake-timer)（[GitHub #111552](https://github.com/zephyrproject-rtos/zephyr/issues/111552)）
  - [nxp,sysctr](../renesas_realtek_counter_binding_reference/P002_nxp_sysctr.md#std-dtcompatible-nxp-sysctr)（[GitHub #106300](https://github.com/zephyrproject-rtos/zephyr/issues/106300)）
  - [nxp,tstmr](../renesas_realtek_counter_binding_reference/P004_nxp_tstmr.md#std-dtcompatible-nxp-tstmr)（[GitHub #112255](https://github.com/zephyrproject-rtos/zephyr/issues/112255)）
  - [nxp,wake-timer](../renesas_realtek_counter_binding_reference/P005_nxp_wake-timer.md#std-dtcompatible-nxp-wake-timer)（[GitHub #110811](https://github.com/zephyrproject-rtos/zephyr/issues/110811)）
  - [realtek,ameba-counter](../renesas_realtek_counter_binding_reference/P009_realtek_ameba-counter.md#std-dtcompatible-realtek-ameba-counter)（[GitHub #106664](https://github.com/zephyrproject-rtos/zephyr/issues/106664)）
  - [realtek,bee-counter-rtc](../renesas_realtek_counter_binding_reference/P010_realtek_bee-counter-rtc.md#std-dtcompatible-realtek-bee-counter-rtc)（[GitHub #105193](https://github.com/zephyrproject-rtos/zephyr/issues/105193)）
  - [renesas,ra-ulpt-counter](../renesas_realtek_counter_binding_reference/P015_renesas_ra-ulpt-counter.md#std-dtcompatible-renesas-ra-ulpt-counter)（[GitHub #113188](https://github.com/zephyrproject-rtos/zephyr/issues/113188)）
  - [ti,k3-rtc-counter](../stm32_ti_xilinx_counter_binding_reference/P010_ti_k3-rtc-counter.md#std-dtcompatible-ti-k3-rtc-counter)（[GitHub #104048](https://github.com/zephyrproject-rtos/zephyr/issues/104048)）
  - [wch,adtm](../stm32_ti_xilinx_counter_binding_reference/P012_wch_adtm.md#std-dtcompatible-wch-adtm)（[GitHub #109728](https://github.com/zephyrproject-rtos/zephyr/issues/109728)）
  - [xlnx,ttc](../stm32_ti_xilinx_counter_binding_reference/P015_xlnx_ttc.md#std-dtcompatible-xlnx-ttc)（[GitHub #103117](https://github.com/zephyrproject-rtos/zephyr/issues/103117)）
  - [xlnx,ttc-counter](../stm32_ti_xilinx_counter_binding_reference/P014_xlnx_ttc-counter.md#std-dtcompatible-xlnx-ttc-counter)（[GitHub #103117](https://github.com/zephyrproject-rtos/zephyr/issues/103117)）
  - [xlnx,zynqmp-rtc](../stm32_ti_xilinx_counter_binding_reference/P016_xlnx_zynqmp-rtc.md#std-dtcompatible-xlnx-zynqmp-rtc)（[GitHub #107684](https://github.com/zephyrproject-rtos/zephyr/issues/107684)）
- 中央处理器（CPU）


  - [adi,max32-m4f-cpu1](../cpu_arm_riscv_binding_reference/P001_adi_max32-m4f-cpu1.md#std-dtcompatible-adi-max32-m4f-cpu1)（[GitHub #105310](https://github.com/zephyrproject-rtos/zephyr/issues/105310)）
  - [arm,armv8](../cpu_arm_riscv_binding_reference/P004_arm_armv8.md#std-dtcompatible-arm-armv8)（[GitHub #114145](https://github.com/zephyrproject-rtos/zephyr/issues/114145)）
  - [arm,cortex-a32](../cpu_arm_riscv_binding_reference/P005_arm_cortex-a32.md#std-dtcompatible-arm-cortex-a32)（[GitHub #107644](https://github.com/zephyrproject-rtos/zephyr/issues/107644)）
  - [arm,cortex-a57](../cpu_arm_riscv_binding_reference/P010_arm_cortex-a57.md#std-dtcompatible-arm-cortex-a57)（[GitHub #114109](https://github.com/zephyrproject-rtos/zephyr/issues/114109)）
  - [arm,cortex-a720](../cpu_arm_riscv_binding_reference/P013_arm_cortex-a720.md#std-dtcompatible-arm-cortex-a720)（[GitHub #113087](https://github.com/zephyrproject-rtos/zephyr/issues/113087)）
  - [arm,cortex-r8f](../cpu_cortex_xtensa_binding_reference/P016_arm_cortex-r8f.md#std-dtcompatible-arm-cortex-r8f)（[GitHub #114145](https://github.com/zephyrproject-rtos/zephyr/issues/114145)）
  - [infineon,tricore](../cpu_vendor_multiarc_binding_reference/P003_infineon_tricore.md#std-dtcompatible-infineon-tricore)（[GitHub #107516](https://github.com/zephyrproject-rtos/zephyr/issues/107516)）
  - [intel,nova-lake](../cpu_vendor_multiarc_binding_reference/P011_intel_nova-lake.md#std-dtcompatible-intel-nova-lake)（[GitHub #111818](https://github.com/zephyrproject-rtos/zephyr/issues/111818)）
  - [intel,x86_64](../cpu_vendor_multiarc_binding_reference/P016_intel_x86_64.md#std-dtcompatible-intel-x86_64)（[GitHub #115174](https://github.com/zephyrproject-rtos/zephyr/issues/115174)）
  - [litex,vexiiriscv-standard](../cpu_vendor_multiarc_binding_reference/P018_litex_vexiiriscv-standard.md#std-dtcompatible-litex-vexiiriscv-standard)（[GitHub #106609](https://github.com/zephyrproject-rtos/zephyr/issues/106609)）
  - [qcom,hexagon-v67](../cpu_vendor_multiarc_binding_reference/P027_qcom_hexagon-v67.md#std-dtcompatible-qcom-hexagon-v67)（[GitHub #107122](https://github.com/zephyrproject-rtos/zephyr/issues/107122)）
  - [renesas,rxv3e](../cpu_vendor_multiarc_binding_reference/P033_renesas_rxv3e.md#std-dtcompatible-renesas-rxv3e)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
  - [spinalhdl,vexiiriscv](../cpu_vendor_multiarc_binding_reference/P045_spinalhdl_vexiiriscv.md#std-dtcompatible-spinalhdl-vexiiriscv)（[GitHub #109932](https://github.com/zephyrproject-rtos/zephyr/issues/109932)）
  - [wch,qingke-v3c](../cpu_vendor_multiarc_binding_reference/P049_wch_qingke-v3c.md#std-dtcompatible-wch-qingke-v3c)（[GitHub #111171](https://github.com/zephyrproject-rtos/zephyr/issues/111171)）
  - [wch,qingke-v3f](../cpu_vendor_multiarc_binding_reference/P050_wch_qingke-v3f.md#std-dtcompatible-wch-qingke-v3f)（[GitHub #111725](https://github.com/zephyrproject-rtos/zephyr/issues/111725)）
  - [wch,qingke-v5f](../cpu_vendor_multiarc_binding_reference/P054_wch_qingke-v5f.md#std-dtcompatible-wch-qingke-v5f)（[GitHub #111725](https://github.com/zephyrproject-rtos/zephyr/issues/111725)）
- CPU 调频（CPU Frequency Scaling）


  - [zephyr,cpu-freq-thermal-cap](../hardware/P622_CPU调频温度约束绑定.md#dtbinding-zephyr-cpu-freq-thermal-cap)（[GitHub #108242](https://github.com/zephyrproject-rtos/zephyr/issues/108242)）
- 循环冗余校验（CRC）


  - [ambiq,hw-crc32](../crc_clock_monitor_binding_reference/P005_ambiq_hw-crc32.md#std-dtcompatible-ambiq-hw-crc32)（[GitHub #110366](https://github.com/zephyrproject-rtos/zephyr/issues/110366)）
- 密码学加速器（Cryptographic Accelerator）


  - [infineon,mxcrypto-crypto](../crypto_aes_sha_ccm_binding_reference/P009_infineon_mxcrypto-crypto.md#std-dtcompatible-infineon-mxcrypto-crypto)（[GitHub #108439](https://github.com/zephyrproject-rtos/zephyr/issues/108439)）
  - [infineon,mxcrypto-trng](../crypto_aes_sha_ccm_binding_reference/P010_infineon_mxcrypto-trng.md#std-dtcompatible-infineon-mxcrypto-trng)（[GitHub #108439](https://github.com/zephyrproject-rtos/zephyr/issues/108439)）
  - [infineon,mxcryptolite-crypto](../crypto_aes_sha_ccm_binding_reference/P011_infineon_mxcryptolite-crypto.md#std-dtcompatible-infineon-mxcryptolite-crypto)（[GitHub #109693](https://github.com/zephyrproject-rtos/zephyr/issues/109693)）
  - [infineon,mxcryptolite-trng](../crypto_aes_sha_ccm_binding_reference/P012_infineon_mxcryptolite-trng.md#std-dtcompatible-infineon-mxcryptolite-trng)（[GitHub #109693](https://github.com/zephyrproject-rtos/zephyr/issues/109693)）
  - [realtek,bee-aes](../crypto_secure_engine_st_ti_binding_reference/P007_realtek_bee-aes.md#std-dtcompatible-realtek-bee-aes)（[GitHub #114817](https://github.com/zephyrproject-rtos/zephyr/issues/114817)）
  - [realtek,bee-sha256](../crypto_secure_engine_st_ti_binding_reference/P008_realtek_bee-sha256.md#std-dtcompatible-realtek-bee-sha256)（[GitHub #114817](https://github.com/zephyrproject-rtos/zephyr/issues/114817)）
  - [silabs,series3-crypto](../crypto_secure_engine_st_ti_binding_reference/P013_silabs_series3-crypto.md#std-dtcompatible-silabs-series3-crypto)（[GitHub #117617](https://github.com/zephyrproject-rtos/zephyr/issues/117617)）
  - [st,stm32wba-pka](../crypto_secure_engine_st_ti_binding_reference/P019_st_stm32wba-pka.md#std-dtcompatible-st-stm32wba-pka)（[GitHub #116564](https://github.com/zephyrproject-rtos/zephyr/issues/116564)）
  - [ti,mspm0-aes](../crypto_secure_engine_st_ti_binding_reference/P021_ti_mspm0-aes.md#std-dtcompatible-ti-mspm0-aes)（[GitHub #94734](https://github.com/zephyrproject-rtos/zephyr/issues/94734)）
- 数模转换器（DAC）


  - [adi,ad5529r](../hardware/P780_AD5529R数模转换器绑定.md#dtbinding-adi-ad5529r)（[GitHub #106256](https://github.com/zephyrproject-rtos/zephyr/issues/106256)）
  - [infineon,autanalog-ctdac](../hardware/P778_Infineon自主模拟连续时间数模转换器绑定.md#dtbinding-infineon-autanalog-ctdac)（[GitHub #107490](https://github.com/zephyrproject-rtos/zephyr/issues/107490)）
  - [infineon,hppass-csg-dac](../hardware/P779_Infineon斜坡发生器数模转换器绑定.md#dtbinding-infineon-hppass-csg-dac)（[GitHub #109967](https://github.com/zephyrproject-rtos/zephyr/issues/109967)）
  - [microchip,dac-g2](../hardware/P777_MicrochipG2数模转换器绑定.md#dtbinding-microchip-dac-g2)（[GitHub #109820](https://github.com/zephyrproject-rtos/zephyr/issues/109820)）
  - [ti,dac43508](../hardware/P805_DAC43508数模转换器绑定.md#dtbinding-ti-dac43508)（[GitHub #112038](https://github.com/zephyrproject-rtos/zephyr/issues/112038)）
  - [ti,dac53508](../hardware/P808_DAC53508数模转换器绑定.md#dtbinding-ti-dac53508)（[GitHub #112038](https://github.com/zephyrproject-rtos/zephyr/issues/112038)）
  - [ti,dac63508](../hardware/P812_DAC63508数模转换器绑定.md#dtbinding-ti-dac63508)（[GitHub #112038](https://github.com/zephyrproject-rtos/zephyr/issues/112038)）
  - [ti,mspm0-dac](../hardware/P775_TIMSPM0数模转换器绑定.md#dtbinding-ti-mspm0-dac)（[GitHub #94725](https://github.com/zephyrproject-rtos/zephyr/issues/94725)）
- 数字音频接口（DAI）


  - [amd,acp-sdw-dai](../dai_binding_reference/P001_amd_acp-sdw-dai.md#std-dtcompatible-amd-acp-sdw-dai)（[GitHub #104450](https://github.com/zephyrproject-rtos/zephyr/issues/104450)）
  - [amd,tdm-dai](../dai_binding_reference/P002_amd_tdm-dai.md#std-dtcompatible-amd-tdm-dai)（[GitHub #108314](https://github.com/zephyrproject-rtos/zephyr/issues/108314)）
- 数字可寻址照明接口（DALI）


  - [zephyr,dali-pwm](../lin_dali_mctp_sensor_bus_binding_reference/P001_zephyr_dali-pwm.md#std-dtcompatible-zephyr-dali-pwm)（[GitHub #88128](https://github.com/zephyrproject-rtos/zephyr/issues/88128)）
- 磁盘（Disk）


  - [virtio,blk](../hardware/P585_VirtIO块设备绑定.md#dtbinding-virtio-blk)（[GitHub #112581](https://github.com/zephyrproject-rtos/zephyr/issues/112581)）
  - [zephyr,memc-ram-disk](../storage_filesystem_binding_reference/P002_zephyr_memc-ram-disk.md#std-dtcompatible-zephyr-memc-ram-disk)（[GitHub #111528](https://github.com/zephyrproject-rtos/zephyr/issues/111528)）
- 显示（Display）


  - [adi,adv7535](../display_adi_chipone_eink_binding_reference/P002_adi_adv7535.md#std-dtcompatible-adi-adv7535)（[GitHub #119977](https://github.com/zephyrproject-rtos/zephyr/issues/119977)）
  - [adi,adv7535-dsi](../display_adi_chipone_eink_binding_reference/P001_adi_adv7535-dsi.md#std-dtcompatible-adi-adv7535-dsi)（[GitHub #119977](https://github.com/zephyrproject-rtos/zephyr/issues/119977)）
  - [charlieplex-led-matrix](../display_adi_chipone_eink_binding_reference/P003_charlieplex-led-matrix.md#std-dtcompatible-charlieplex-led-matrix)（[GitHub #110137](https://github.com/zephyrproject-rtos/zephyr/issues/110137)）
  - [chipwealth,ch1115](../compatible_binding_reference/P024_chipwealth_ch1115.md#std-dtcompatible-chipwealth-ch1115)（[GitHub #107434](https://github.com/zephyrproject-rtos/zephyr/issues/107434)）
  - [chipwealth,ch1116](../compatible_binding_reference/P025_chipwealth_ch1116.md#std-dtcompatible-chipwealth-ch1116)（[GitHub #107434](https://github.com/zephyrproject-rtos/zephyr/issues/107434)）
  - [eink,ed2208-doa](../display_adi_chipone_eink_binding_reference/P012_eink_ed2208-doa.md#std-dtcompatible-eink-ed2208-doa)（[GitHub #109961](https://github.com/zephyrproject-rtos/zephyr/issues/109961)）
  - [eink,ed2208-gca](../display_adi_chipone_eink_binding_reference/P013_eink_ed2208-gca.md#std-dtcompatible-eink-ed2208-gca)（[GitHub #107510](https://github.com/zephyrproject-rtos/zephyr/issues/107510)）
  - [espressif,esp-dsi-display](../display_adi_chipone_eink_binding_reference/P014_espressif_esp-dsi-display.md#std-dtcompatible-espressif-esp-dsi-display)（[GitHub #116548](https://github.com/zephyrproject-rtos/zephyr/issues/116548)）
  - [fitipower,ek79007](../display_adi_chipone_eink_binding_reference/P015_fitipower_ek79007.md#std-dtcompatible-fitipower-ek79007)（[GitHub #116543](https://github.com/zephyrproject-rtos/zephyr/issues/116543)）
  - [himax,hx8353e](../display_adi_chipone_eink_binding_reference/P019_himax_hx8353e.md#std-dtcompatible-himax-hx8353e)（[GitHub #108055](https://github.com/zephyrproject-rtos/zephyr/issues/108055)）
  - [ilitek,ili9881c](../display_ilitek_matrix_nxp_binding_reference/P008_ilitek_ili9881c.md#std-dtcompatible-ilitek-ili9881c)（[GitHub #116701](https://github.com/zephyrproject-rtos/zephyr/issues/116701)）
  - [ite,it8951](../display_ilitek_matrix_nxp_binding_reference/P011_ite_it8951.md#std-dtcompatible-ite-it8951)（[GitHub #108591](https://github.com/zephyrproject-rtos/zephyr/issues/108591)）
  - [levetop,lt7680](../display_ilitek_matrix_nxp_binding_reference/P014_levetop_lt7680.md#std-dtcompatible-levetop-lt7680)（[GitHub #112389](https://github.com/zephyrproject-rtos/zephyr/issues/112389)）
  - [philips,pcd8544](../display_panel_renesas_sharp_binding_reference/P004_philips_pcd8544.md#std-dtcompatible-philips-pcd8544)（[GitHub #120029](https://github.com/zephyrproject-rtos/zephyr/issues/120029)）
  - [raspberrypi,bcm2711-framebuffer](../display_panel_renesas_sharp_binding_reference/P006_raspberrypi_bcm2711-framebuffer.md#std-dtcompatible-raspberrypi-bcm2711-framebuffer)（[GitHub #109522](https://github.com/zephyrproject-rtos/zephyr/issues/109522)）
  - [raydium,rm67199](../display_panel_renesas_sharp_binding_reference/P008_raydium_rm67199.md#std-dtcompatible-raydium-rm67199)（[GitHub #98554](https://github.com/zephyrproject-rtos/zephyr/issues/98554)）
  - [raydium,rm692c9](../display_panel_renesas_sharp_binding_reference/P010_raydium_rm692c9.md#std-dtcompatible-raydium-rm692c9)（[GitHub #93134](https://github.com/zephyrproject-rtos/zephyr/issues/93134)）
  - [renesas,rz-lcdc](../display_panel_renesas_sharp_binding_reference/P012_renesas_rz-lcdc.md#std-dtcompatible-renesas-rz-lcdc)（[GitHub #116701](https://github.com/zephyrproject-rtos/zephyr/issues/116701)）
  - [sinowealth,sh1107](../compatible_binding_reference/P057_sinowealth_sh1107.md#std-dtcompatible-sinowealth-sh1107)（[GitHub #107434](https://github.com/zephyrproject-rtos/zephyr/issues/107434)）
  - [socionext,dpu](../display_sinowealth_sitronix_solomon_binding_reference/P013_socionext_dpu.md#std-dtcompatible-socionext-dpu)（[GitHub #93134](https://github.com/zephyrproject-rtos/zephyr/issues/93134)）
  - [solomon,ssd1305](../compatible_binding_reference/P060_solomon_ssd1305.md#std-dtcompatible-solomon-ssd1305)（[GitHub #107434](https://github.com/zephyrproject-rtos/zephyr/issues/107434)）
  - [solomon,ssd1306b](../compatible_binding_reference/P062_solomon_ssd1306b.md#std-dtcompatible-solomon-ssd1306b)（[GitHub #107434](https://github.com/zephyrproject-rtos/zephyr/issues/107434)）
  - [solomon,ssd1315](../compatible_binding_reference/P064_solomon_ssd1315.md#std-dtcompatible-solomon-ssd1315)（[GitHub #107434](https://github.com/zephyrproject-rtos/zephyr/issues/107434)）
  - [solomon,ssd1683](../display_st_ultrachip_zephyr_binding_reference/P001_solomon_ssd1683.md#std-dtcompatible-solomon-ssd1683)（[GitHub #112893](https://github.com/zephyrproject-rtos/zephyr/issues/112893)）
  - [st,neochrom-gpu2d](../display_st_ultrachip_zephyr_binding_reference/P002_st_neochrom-gpu2d.md#std-dtcompatible-st-neochrom-gpu2d)（[GitHub #105970](https://github.com/zephyrproject-rtos/zephyr/issues/105970)）
  - [st,stm32-dma2d](../display_st_ultrachip_zephyr_binding_reference/P003_st_stm32-dma2d.md#std-dtcompatible-st-stm32-dma2d)（[GitHub #103687](https://github.com/zephyrproject-rtos/zephyr/issues/103687)）
  - [ultrachip,uc8253](../display_st_ultrachip_zephyr_binding_reference/P009_ultrachip_uc8253.md#std-dtcompatible-ultrachip-uc8253)（[GitHub #113230](https://github.com/zephyrproject-rtos/zephyr/issues/113230)）
  - [zephyr,panel-color-palette](../display_panel_renesas_sharp_binding_reference/P002_zephyr_panel-color-palette.md#std-dtcompatible-zephyr-panel-color-palette)（[GitHub #107945](https://github.com/zephyrproject-rtos/zephyr/issues/107945)）
- 直接存储器访问（DMA）


  - [adi,axi-dmac](../dma_binding_reference/P001_adi_axi-dmac.md#std-dtcompatible-adi-axi-dmac)（[GitHub #115303](https://github.com/zephyrproject-rtos/zephyr/issues/115303)）
  - [amd,acp-host-dma](../dma_binding_reference/P004_amd_acp-host-dma.md#std-dtcompatible-amd-acp-host-dma)（[GitHub #104450](https://github.com/zephyrproject-rtos/zephyr/issues/104450)）
  - [amd,acp-sdw-dma](../dma_binding_reference/P005_amd_acp-sdw-dma.md#std-dtcompatible-amd-acp-sdw-dma)（[GitHub #104450](https://github.com/zephyrproject-rtos/zephyr/issues/104450)）
  - [amd,acp-tdm-dma](../dma_binding_reference/P006_amd_acp-tdm-dma.md#std-dtcompatible-amd-acp-tdm-dma)（[GitHub #108314](https://github.com/zephyrproject-rtos/zephyr/issues/108314)）
  - [amd,versal2-dma-1.0](../dma_binding_reference/P007_amd_versal2-dma-1.0.md#std-dtcompatible-amd-versal2-dma-1.0)（[GitHub #101685](https://github.com/zephyrproject-rtos/zephyr/issues/101685)）
  - [infineon,mdma](../intel_microchip_dma_binding_reference/P002_infineon_mdma.md#std-dtcompatible-infineon-mdma)（[GitHub #110847](https://github.com/zephyrproject-rtos/zephyr/issues/110847)）
  - [microchip,dmac-g3-dma](../intel_microchip_dma_binding_reference/P015_microchip_dmac-g3-dma.md#std-dtcompatible-microchip-dmac-g3-dma)（[GitHub #109209](https://github.com/zephyrproject-rtos/zephyr/issues/109209)）
  - [nxp,gdma](../nxp_realtek_renesas_dma_binding_reference/P002_nxp_gdma.md#std-dtcompatible-nxp-gdma)（[GitHub #104868](https://github.com/zephyrproject-rtos/zephyr/issues/104868)）
  - [realtek,ameba-gdma](../nxp_realtek_renesas_dma_binding_reference/P010_realtek_ameba-gdma.md#std-dtcompatible-realtek-ameba-gdma)（[GitHub #105366](https://github.com/zephyrproject-rtos/zephyr/issues/105366)）
  - [realtek,bee-dma](../nxp_realtek_renesas_dma_binding_reference/P011_realtek_bee-dma.md#std-dtcompatible-realtek-bee-dma)（[GitHub #104754](https://github.com/zephyrproject-rtos/zephyr/issues/104754)）
  - [renesas,rza2m-dma](../nxp_realtek_renesas_dma_binding_reference/P015_renesas_rza2m-dma.md#std-dtcompatible-renesas-rza2m-dma)（[GitHub #107009](https://github.com/zephyrproject-rtos/zephyr/issues/107009)）
  - [ti,mspm0-dma](../stm32_ti_xilinx_dma_binding_reference/P014_ti_mspm0-dma.md#std-dtcompatible-ti-mspm0-dma)（[GitHub #91502](https://github.com/zephyrproject-rtos/zephyr/issues/91502)）
  - [xlnx,zynqmp-dma-1.0](../stm32_ti_xilinx_dma_binding_reference/P018_xlnx_zynqmp-dma-1.0.md#std-dtcompatible-xlnx-zynqmp-dma-1.0)（[GitHub #101685](https://github.com/zephyrproject-rtos/zephyr/issues/101685)）
- 分布式交换架构（DSA）


  - [zephyr,dsa-port](../network_radio_frontend_binding_reference/P002_zephyr_dsa-port.md#std-dtcompatible-zephyr-dsa-port)（[GitHub #116605](https://github.com/zephyrproject-rtos/zephyr/issues/116605)）
- 数字信号处理（DSP）


  - [nxp,powerquad](../sound_haptic_binding_reference/P004_nxp_powerquad.md#std-dtcompatible-nxp-powerquad)（[GitHub #110745](https://github.com/zephyrproject-rtos/zephyr/issues/110745)）
- 错误检测与纠正（EDAC）


  - [nxp,mecc](../edac_syscon_binding_reference/P004_nxp_mecc.md#std-dtcompatible-nxp-mecc)（[GitHub #105341](https://github.com/zephyrproject-rtos/zephyr/issues/105341)）
- 增强型串行外设接口（ESPI）


  - [intel,espi-peci](../espi_binding_reference/P001_intel_espi-peci.md#std-dtcompatible-intel-espi-peci)（[GitHub #103773](https://github.com/zephyrproject-rtos/zephyr/issues/103773)）
  - [nxp,espi](../espi_binding_reference/P015_nxp_espi.md#std-dtcompatible-nxp-espi)（[GitHub #110318](https://github.com/zephyrproject-rtos/zephyr/issues/110318)）
  - [nxp,espi-taf](../espi_binding_reference/P014_nxp_espi-taf.md#std-dtcompatible-nxp-espi-taf)（[GitHub #110318](https://github.com/zephyrproject-rtos/zephyr/issues/110318)）
- 以太网（Ethernet）


  - [adi,adin1140](../ethernet_mac_mdio_binding_reference/P002_adi_adin1140.md#std-dtcompatible-adi-adin1140)（[GitHub #109227](https://github.com/zephyrproject-rtos/zephyr/issues/109227)）
  - [adi,adin1140-mdio](../ethernet_mac_mdio_binding_reference/P014_adi_adin1140-mdio.md#std-dtcompatible-adi-adin1140-mdio)（[GitHub #109227](https://github.com/zephyrproject-rtos/zephyr/issues/109227)）
  - [adi,adin1140-phy](../ethernet_nxp_phy_binding_reference/P015_adi_adin1140-phy.md#std-dtcompatible-adi-adin1140-phy)（[GitHub #109227](https://github.com/zephyrproject-rtos/zephyr/issues/109227)）
  - [brcm,genet](../ethernet_mac_mdio_binding_reference/P006_brcm_genet.md#std-dtcompatible-brcm-genet)（[GitHub #113360](https://github.com/zephyrproject-rtos/zephyr/issues/113360)）
  - [brcm,genet-mdio](../ethernet_mac_mdio_binding_reference/P017_brcm_genet-mdio.md#std-dtcompatible-brcm-genet-mdio)（[GitHub #113360](https://github.com/zephyrproject-rtos/zephyr/issues/113360)）
  - [microchip,gmac-g1-eth](../ethernet_mdio_microchip_binding_reference/P016_microchip_gmac-g1-eth.md#std-dtcompatible-microchip-gmac-g1-eth)（[GitHub #105275](https://github.com/zephyrproject-rtos/zephyr/issues/105275)）
  - [microchip,gmac-g1-mdio](../ethernet_mac_mdio_binding_reference/P020_microchip_gmac-g1-mdio.md#std-dtcompatible-microchip-gmac-g1-mdio)（[GitHub #105275](https://github.com/zephyrproject-rtos/zephyr/issues/105275)）
  - [microchip,lan8840](../ethernet_phy_renesas_rockchip_binding_reference/P004_microchip_lan8840.md#std-dtcompatible-microchip-lan8840)（[GitHub #110896](https://github.com/zephyrproject-rtos/zephyr/issues/110896)）
  - [nxp,imx-netc-vsi](../ethernet_nxp_phy_binding_reference/P007_nxp_imx-netc-vsi.md#std-dtcompatible-nxp-imx-netc-vsi)（[GitHub #114331](https://github.com/zephyrproject-rtos/zephyr/issues/114331)）
  - [rockchip,rk3588-gmac](../ethernet_phy_renesas_rockchip_binding_reference/P018_rockchip_rk3588-gmac.md#std-dtcompatible-rockchip-rk3588-gmac)（[GitHub #117985](https://github.com/zephyrproject-rtos/zephyr/issues/117985)）
  - [snps,dwmac](../ethernet_synopsys_st_xilinx_binding_reference/P007_snps_dwmac.md#std-dtcompatible-snps-dwmac)（[GitHub #114760](https://github.com/zephyrproject-rtos/zephyr/issues/114760)）
  - [snps,dwmac-mdio](../ethernet_mdio_microchip_binding_reference/P010_snps_dwmac-mdio.md#std-dtcompatible-snps-dwmac-mdio)（[GitHub #108046](https://github.com/zephyrproject-rtos/zephyr/issues/108046)）
  - [snps,dwmac-ptp-clock](../ethernet_synopsys_st_xilinx_binding_reference/P006_snps_dwmac-ptp-clock.md#std-dtcompatible-snps-dwmac-ptp-clock)（[GitHub #114242](https://github.com/zephyrproject-rtos/zephyr/issues/114242)）
  - [wch,ch9120](../ethernet_synopsys_st_xilinx_binding_reference/P015_wch_ch9120.md#std-dtcompatible-wch-ch9120)（[GitHub #111708](https://github.com/zephyrproject-rtos/zephyr/issues/111708)）
  - [wiznet,w5100s](../ethernet_synopsys_st_xilinx_binding_reference/P017_wiznet_w5100s.md#std-dtcompatible-wiznet-w5100s)（[GitHub #113315](https://github.com/zephyrproject-rtos/zephyr/issues/113315)）
  - [wiznet,w6300](../ethernet_synopsys_st_xilinx_binding_reference/P020_wiznet_w6300.md#std-dtcompatible-wiznet-w6300)（[GitHub #102727](https://github.com/zephyrproject-rtos/zephyr/issues/102727)）
  - [xlnx,gem-mdio](../ethernet_mdio_microchip_binding_reference/P012_xlnx_gem-mdio.md#std-dtcompatible-xlnx-gem-mdio)（[GitHub #87313](https://github.com/zephyrproject-rtos/zephyr/issues/87313)）
  - [zephyr,native-ptp-clock](../ethernet_synopsys_st_xilinx_binding_reference/P025_zephyr_native-ptp-clock.md#std-dtcompatible-zephyr-native-ptp-clock)（[GitHub #109265](https://github.com/zephyrproject-rtos/zephyr/issues/109265)）
  - [zephyr,native-tap](../ethernet_synopsys_st_xilinx_binding_reference/P026_zephyr_native-tap.md#std-dtcompatible-zephyr-native-tap)（[GitHub #117068](https://github.com/zephyrproject-rtos/zephyr/issues/117068)）
- 固件（Firmware）


  - [arm,scmi-reset](../hardware/P605_SCMI复位协议绑定.md#dtbinding-arm-scmi-reset)（[GitHub #106306](https://github.com/zephyrproject-rtos/zephyr/issues/106306)）
  - [raspberrypi,bcm283x-firmware](../hardware/P611_BCM283x固件绑定.md#dtbinding-raspberrypi-bcm283x-firmware)（[GitHub #107536](https://github.com/zephyrproject-rtos/zephyr/issues/107536)）
- 闪存控制器（Flash Controller）


  - [aesc,spi-flash-controller](../flash_adi_microchip_nordic_binding_reference/P003_aesc_spi-flash-controller.md#std-dtcompatible-aesc-spi-flash-controller)（[GitHub #110957](https://github.com/zephyrproject-rtos/zephyr/issues/110957)）
  - [infineon,rram-controller](../flash_adi_microchip_nordic_binding_reference/P016_infineon_rram-controller.md#std-dtcompatible-infineon-rram-controller)（[GitHub #108532](https://github.com/zephyrproject-rtos/zephyr/issues/108532)）
  - [intel,pflash-cfi01](../flash_adi_microchip_nordic_binding_reference/P018_intel_pflash-cfi01.md#std-dtcompatible-intel-pflash-cfi01)（[GitHub #112714](https://github.com/zephyrproject-rtos/zephyr/issues/112714)）
  - [microchip,igloo2-envm-controller](../flash_adi_microchip_nordic_binding_reference/P021_microchip_igloo2-envm-controller.md#std-dtcompatible-microchip-igloo2-envm-controller)（[GitHub #111817](https://github.com/zephyrproject-rtos/zephyr/issues/111817)）
  - [microchip,nvmctrl-g2](../flash_adi_microchip_nordic_binding_reference/P023_microchip_nvmctrl-g2.md#std-dtcompatible-microchip-nvmctrl-g2)（[GitHub #108440](https://github.com/zephyrproject-rtos/zephyr/issues/108440)）
  - [microchip,nvmctrl-g3](../flash_adi_microchip_nordic_binding_reference/P024_microchip_nvmctrl-g3.md#std-dtcompatible-microchip-nvmctrl-g3)（[GitHub #109747](https://github.com/zephyrproject-rtos/zephyr/issues/109747)）
  - [microchip,smartfusion2-flash-controller](../flash_adi_microchip_nordic_binding_reference/P025_microchip_smartfusion2-flash-controller.md#std-dtcompatible-microchip-smartfusion2-flash-controller)（[GitHub #106926](https://github.com/zephyrproject-rtos/zephyr/issues/106926)）
  - [nxp,iap-fmc84x](../flash_nuvoton_nxp_renesas_binding_reference/P013_nxp_iap-fmc84x.md#std-dtcompatible-nxp-iap-fmc84x)（[GitHub #105928](https://github.com/zephyrproject-rtos/zephyr/issues/105928)）
  - [realtek,ameba-flash-controller](../flash_nuvoton_nxp_renesas_binding_reference/P022_realtek_ameba-flash-controller.md#std-dtcompatible-realtek-ameba-flash-controller)（[GitHub #106690](https://github.com/zephyrproject-rtos/zephyr/issues/106690)）
  - [realtek,bee-nor-flash-controller](../flash_nuvoton_nxp_renesas_binding_reference/P023_realtek_bee-nor-flash-controller.md#std-dtcompatible-realtek-bee-nor-flash-controller)（[GitHub #107007](https://github.com/zephyrproject-rtos/zephyr/issues/107007)）
  - [renesas,ra-faci](../flash_nuvoton_nxp_renesas_binding_reference/P025_renesas_ra-faci.md#std-dtcompatible-renesas-ra-faci)（[GitHub #109125](https://github.com/zephyrproject-rtos/zephyr/issues/109125)）
  - [renesas,ra-fcb](../flash_nuvoton_nxp_renesas_binding_reference/P026_renesas_ra-fcb.md#std-dtcompatible-renesas-ra-fcb)（[GitHub #109125](https://github.com/zephyrproject-rtos/zephyr/issues/109125)）
  - [silabs,series3-extmem](../flash_renesas_st_ti_binding_reference/P008_silabs_series3-extmem.md#std-dtcompatible-silabs-series3-extmem)（[GitHub #117617](https://github.com/zephyrproject-rtos/zephyr/issues/117617)）
  - [ti,mspm0-flash-controller](../flash_renesas_st_ti_binding_reference/P032_ti_mspm0-flash-controller.md#std-dtcompatible-ti-mspm0-flash-controller)（[GitHub #115203](https://github.com/zephyrproject-rtos/zephyr/issues/115203)）
  - [wch,ch32v-flash-controller](../flash_renesas_st_ti_binding_reference/P034_wch_ch32v-flash-controller.md#std-dtcompatible-wch-ch32v-flash-controller)（[GitHub #113980](https://github.com/zephyrproject-rtos/zephyr/issues/113980)）
  - [zephyr,semihost-flash](../flash_renesas_st_ti_binding_reference/P035_zephyr_semihost-flash.md#std-dtcompatible-zephyr-semihost-flash)（[GitHub #112945](https://github.com/zephyrproject-rtos/zephyr/issues/112945)）
- 现场可编程门阵列（FPGA）


  - [renesas,slg47910](../fpga_binding_reference/P007_renesas_slg47910.md#std-dtcompatible-renesas-slg47910)（[GitHub #107551](https://github.com/zephyrproject-rtos/zephyr/issues/107551)）
- 电量计（Fuel Gauge）


  - [adi,adp5360-fuel-gauge](../fuel_gauge_binding_reference/P001_adi_adp5360-fuel-gauge.md#std-dtcompatible-adi-adp5360-fuel-gauge)（[GitHub #105258](https://github.com/zephyrproject-rtos/zephyr/issues/105258)）
- 全球导航卫星系统（GNSS）


  - [ericsson,f5521gw](../gnss_fingerprint_binding_reference/P003_ericsson_f5521gw.md#std-dtcompatible-ericsson-f5521gw)（[GitHub #113055](https://github.com/zephyrproject-rtos/zephyr/issues/113055)）
  - [u-blox,m10](../gnss_fingerprint_binding_reference/P011_u-blox_m10.md#std-dtcompatible-u-blox-m10)（[GitHub #110846](https://github.com/zephyrproject-rtos/zephyr/issues/110846)）
- 通用输入输出与接插件（GPIO & Headers）


  - [allwinner,sun50i-h618-gpio](../gpio_adi_headers_ambiq_binding_reference/P014_allwinner_sun50i-h618-gpio.md#std-dtcompatible-allwinner-sun50i-h618-gpio)（[GitHub #110502](https://github.com/zephyrproject-rtos/zephyr/issues/110502)）
  - [allwinner,sunxi-gpio](../gpio_adi_headers_ambiq_binding_reference/P015_allwinner_sunxi-gpio.md#std-dtcompatible-allwinner-sunxi-gpio)（[GitHub #110502](https://github.com/zephyrproject-rtos/zephyr/issues/110502)）
  - [arduino-mega-header](../gpio_adi_headers_ambiq_binding_reference/P024_arduino-mega-header.md#std-dtcompatible-arduino-mega-header)（[GitHub #105160](https://github.com/zephyrproject-rtos/zephyr/issues/105160)）
  - [cdac,thejas32-gpio](../gpio_connectors_bflb_esp_binding_reference/P010_cdac_thejas32-gpio.md#std-dtcompatible-cdac-thejas32-gpio)（[GitHub #114202](https://github.com/zephyrproject-rtos/zephyr/issues/114202)）
  - [diodes,pi4ioe5v6408](../gpio_connectors_bflb_esp_binding_reference/P016_diodes_pi4ioe5v6408.md#std-dtcompatible-diodes-pi4ioe5v6408)（[GitHub #108505](https://github.com/zephyrproject-rtos/zephyr/issues/108505)）
  - [esp-01-header](../gpio_connectors_bflb_esp_binding_reference/P021_esp-01-header.md#std-dtcompatible-esp-01-header)（[GitHub #109705](https://github.com/zephyrproject-rtos/zephyr/issues/109705)）
  - [gpio-mmio-latch](../gpio_connectors_bflb_esp_binding_reference/P028_gpio-mmio-latch.md#std-dtcompatible-gpio-mmio-latch)（[GitHub #105732](https://github.com/zephyrproject-rtos/zephyr/issues/105732)）
  - [m5stack,m5pm1-gpio](../gpio_infineon_intel_ite_microchip_binding_reference/P016_m5stack_m5pm1-gpio.md#std-dtcompatible-m5stack-m5pm1-gpio)（[GitHub #109961](https://github.com/zephyrproject-rtos/zephyr/issues/109961)）
  - [mr-mcxn-t1-header](../gpio_microchip_nordic_nuvoton_binding_reference/P007_mr-mcxn-t1-header.md#std-dtcompatible-mr-mcxn-t1-header)（[GitHub #117414](https://github.com/zephyrproject-rtos/zephyr/issues/117414)）
  - [nordic,npm10xx-gpio](../gpio_microchip_nordic_nuvoton_binding_reference/P010_nordic_npm10xx-gpio.md#std-dtcompatible-nordic-npm10xx-gpio)（[GitHub #108508](https://github.com/zephyrproject-rtos/zephyr/issues/108508)）
  - [nordic,nrf71-p4-gpio](../gpio_microchip_nordic_nuvoton_binding_reference/P018_nordic_nrf71-p4-gpio.md#std-dtcompatible-nordic-nrf71-p4-gpio)（[GitHub #118802](https://github.com/zephyrproject-rtos/zephyr/issues/118802)）
  - [nxp,imx-gpio-v2](../gpio_microchip_nordic_nuvoton_binding_reference/P029_nxp_imx-gpio-v2.md#std-dtcompatible-nxp-imx-gpio-v2)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [raspberrypi,bcm283x-gpio](../gpio_raspberrypi_renesas_binding_reference/P003_raspberrypi_bcm283x-gpio.md#std-dtcompatible-raspberrypi-bcm283x-gpio)（[GitHub #110788](https://github.com/zephyrproject-rtos/zephyr/issues/110788)）
  - [realtek,rts5817-gpio](../gpio_raspberrypi_renesas_binding_reference/P012_realtek_rts5817-gpio.md#std-dtcompatible-realtek-rts5817-gpio)（[GitHub #105542](https://github.com/zephyrproject-rtos/zephyr/issues/105542)）
  - [renesas,rx-gpio-ioport](../gpio_raspberrypi_renesas_binding_reference/P018_renesas_rx-gpio-ioport.md#std-dtcompatible-renesas-rx-gpio-ioport)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
  - [renesas,rz-gpio-mipi-header](../gpio_raspberrypi_renesas_binding_reference/P024_renesas_rz-gpio-mipi-header.md#std-dtcompatible-renesas-rz-gpio-mipi-header)（[GitHub #116701](https://github.com/zephyrproject-rtos/zephyr/issues/116701)）
  - [st,m2-memory-connector](../gpio_silabs_st_connectors_binding_reference/P027_st_m2-memory-connector.md#std-dtcompatible-st-m2-memory-connector)（[GitHub #109004](https://github.com/zephyrproject-rtos/zephyr/issues/109004)）
  - [st,stmod-plus-connector](../gpio_ti_xilinx_sdl_binding_reference/P001_st_stmod-plus-connector.md#std-dtcompatible-st-stmod-plus-connector)（[GitHub #109705](https://github.com/zephyrproject-rtos/zephyr/issues/109705)）
  - [st-zio-header](../gpio_ti_xilinx_sdl_binding_reference/P004_st-zio-header.md#std-dtcompatible-st-zio-header)（[GitHub #115412](https://github.com/zephyrproject-rtos/zephyr/issues/115412)）
  - [ti,tca9554](../gpio_ti_xilinx_sdl_binding_reference/P021_ti_tca9554.md#std-dtcompatible-ti-tca9554)（[GitHub #111041](https://github.com/zephyrproject-rtos/zephyr/issues/111041)）
  - [ti,tla2528-gpio](../gpio_ti_xilinx_sdl_binding_reference/P022_ti_tla2528-gpio.md#std-dtcompatible-ti-tla2528-gpio)（[GitHub #110722](https://github.com/zephyrproject-rtos/zephyr/issues/110722)）
  - [virtio,gpio](../hardware/P588_VirtIO_GPIO控制器绑定.md#dtbinding-virtio-gpio)（[GitHub #114983](https://github.com/zephyrproject-rtos/zephyr/issues/114983)）
  - [wch,ch5xx-gpio](../gpio_ti_xilinx_sdl_binding_reference/P023_wch_ch5xx-gpio.md#std-dtcompatible-wch-ch5xx-gpio)（[GitHub #111171](https://github.com/zephyrproject-rtos/zephyr/issues/111171)）
  - [wisblock-io-slot](../gpio_ti_xilinx_sdl_binding_reference/P026_wisblock-io-slot.md#std-dtcompatible-wisblock-io-slot)（[GitHub #113140](https://github.com/zephyrproject-rtos/zephyr/issues/113140)）
  - [wisblock-sensor-slot](../gpio_ti_xilinx_sdl_binding_reference/P027_wisblock-sensor-slot.md#std-dtcompatible-wisblock-sensor-slot)（[GitHub #113140](https://github.com/zephyrproject-rtos/zephyr/issues/113140)）
- 触觉反馈（Haptics）


  - [cirrus,cs40l26](../compatible_binding_reference/P029_cirrus_cs40l26.md#std-dtcompatible-cirrus-cs40l26)（[GitHub #106934](https://github.com/zephyrproject-rtos/zephyr/issues/106934)）
  - [cirrus,cs40l27](../compatible_binding_reference/P030_cirrus_cs40l27.md#std-dtcompatible-cirrus-cs40l27)（[GitHub #106934](https://github.com/zephyrproject-rtos/zephyr/issues/106934)）
  - [cirrus,cs40l50](../compatible_binding_reference/P031_cirrus_cs40l50.md#std-dtcompatible-cirrus-cs40l50)（[GitHub #105683](https://github.com/zephyrproject-rtos/zephyr/issues/105683)）
  - [cirrus,cs40l51](../compatible_binding_reference/P032_cirrus_cs40l51.md#std-dtcompatible-cirrus-cs40l51)（[GitHub #105683](https://github.com/zephyrproject-rtos/zephyr/issues/105683)）
  - [cirrus,cs40l52](../compatible_binding_reference/P033_cirrus_cs40l52.md#std-dtcompatible-cirrus-cs40l52)（[GitHub #105683](https://github.com/zephyrproject-rtos/zephyr/issues/105683)）
  - [cirrus,cs40l53](../compatible_binding_reference/P034_cirrus_cs40l53.md#std-dtcompatible-cirrus-cs40l53)（[GitHub #105683](https://github.com/zephyrproject-rtos/zephyr/issues/105683)）
  - [titanmec,tm6605](../sound_haptic_binding_reference/P018_titanmec_tm6605.md#std-dtcompatible-titanmec-tm6605)（[GitHub #109104](https://github.com/zephyrproject-rtos/zephyr/issues/109104)）
- 硬件信息（Hardware Information）


  - [nxp,lpc-pmc-hwinfo](../hwinfo_binding_reference/P008_nxp_lpc-pmc-hwinfo.md#std-dtcompatible-nxp-lpc-pmc-hwinfo)（[GitHub #114693](https://github.com/zephyrproject-rtos/zephyr/issues/114693)）
  - [nxp,mc-rgm](../hwinfo_binding_reference/P010_nxp_mc-rgm.md#std-dtcompatible-nxp-mc-rgm)（[GitHub #111359](https://github.com/zephyrproject-rtos/zephyr/issues/111359)）
  - [nxp,otp-uid](../hwinfo_binding_reference/P011_nxp_otp-uid.md#std-dtcompatible-nxp-otp-uid)（[GitHub #111493](https://github.com/zephyrproject-rtos/zephyr/issues/111493)）
  - [wch,esig](../hwinfo_binding_reference/P015_wch_esig.md#std-dtcompatible-wch-esig)（[GitHub #115101](https://github.com/zephyrproject-rtos/zephyr/issues/115101)）
  - [zephyr,hwinfo-nvmem](../hwinfo_binding_reference/P016_zephyr_hwinfo-nvmem.md#std-dtcompatible-zephyr-hwinfo-nvmem)（[GitHub #118693](https://github.com/zephyrproject-rtos/zephyr/issues/118693)）
- 集成电路间总线（I2C）


  - [ambiq,ios-i2c](../i2c_adi_atmel_esp_binding_reference/P004_ambiq_ios-i2c.md#std-dtcompatible-ambiq-ios-i2c)（[GitHub #96059](https://github.com/zephyrproject-rtos/zephyr/issues/96059)）
  - [brcm,bcm2711-i2c](../i2c_adi_atmel_esp_binding_reference/P013_brcm_bcm2711-i2c.md#std-dtcompatible-brcm-bcm2711-i2c)（[GitHub #105601](https://github.com/zephyrproject-rtos/zephyr/issues/105601)）
  - [ene,kb106x-i2c](../i2c_adi_atmel_esp_binding_reference/P016_ene_kb106x-i2c.md#std-dtcompatible-ene-kb106x-i2c)（[GitHub #106693](https://github.com/zephyrproject-rtos/zephyr/issues/106693)）
  - [realtek,ameba-i2c](../i2c_nxp_pico_renesas_binding_reference/P009_realtek_ameba-i2c.md#std-dtcompatible-realtek-ameba-i2c)（[GitHub #108235](https://github.com/zephyrproject-rtos/zephyr/issues/108235)）
  - [realtek,bee-i2c](../i2c_nxp_pico_renesas_binding_reference/P010_realtek_bee-i2c.md#std-dtcompatible-realtek-bee-i2c)（[GitHub #105028](https://github.com/zephyrproject-rtos/zephyr/issues/105028)）
  - [virtio,i2c](../hardware/P589_VirtIO_I2C控制器绑定.md#dtbinding-virtio-i2c)（[GitHub #115003](https://github.com/zephyrproject-rtos/zephyr/issues/115003)）
  - [zephyr,i2c-target-tmp103](../i2c_stm32_ti_mux_binding_reference/P021_zephyr_i2c-target-tmp103.md#std-dtcompatible-zephyr-i2c-target-tmp103)（[GitHub #114727](https://github.com/zephyrproject-rtos/zephyr/issues/114727)）
- 集成电路间音频总线（I2S）


  - [zephyr,native-sim-i2s](../i2s_binding_reference/P019_zephyr_native-sim-i2s.md#std-dtcompatible-zephyr-native-sim-i2s)（[GitHub #109902](https://github.com/zephyrproject-rtos/zephyr/issues/109902)）
- 改进型集成电路间总线（I3C）


  - [microchip,xec-i3c](../i3c_smbus_binding_reference/P005_microchip_xec-i3c.md#std-dtcompatible-microchip-xec-i3c)（[GitHub #116252](https://github.com/zephyrproject-rtos/zephyr/issues/116252)）
- 低速率无线个域网（IEEE 802.15.4）


  - [bflb,ieee802154](../lora_ieee802154_binding_reference/P002_bflb_ieee802154.md#std-dtcompatible-bflb-ieee802154)（[GitHub #112921](https://github.com/zephyrproject-rtos/zephyr/issues/112921)）
  - [silabs,efr32-ieee802154](../lora_ieee802154_binding_reference/P009_silabs_efr32-ieee802154.md#std-dtcompatible-silabs-efr32-ieee802154)（[GitHub #108596](https://github.com/zephyrproject-rtos/zephyr/issues/108596)）
- 输入（Input）


  - [adsemi,tsm12](../input_adc_touch_matrix_binding_reference/P003_adsemi_tsm12.md#std-dtcompatible-adsemi-tsm12)（[GitHub #120170](https://github.com/zephyrproject-rtos/zephyr/issues/120170)）
  - [tbs,crsf](../input_touch_lvgl_gesture_binding_reference/P009_tbs_crsf.md#std-dtcompatible-tbs-crsf)（[GitHub #106941](https://github.com/zephyrproject-rtos/zephyr/issues/106941)）
  - [virtio,input](../hardware/P590_VirtIO输入设备绑定.md#dtbinding-virtio-input)（[GitHub #111029](https://github.com/zephyrproject-rtos/zephyr/issues/111029)）
- 中断控制器（Interrupt Controller）


  - [amd,acp-intc](../soc_interrupt_binding_reference/P002_amd_acp-intc.md#std-dtcompatible-amd-acp-intc)（[GitHub #104450](https://github.com/zephyrproject-rtos/zephyr/issues/104450)）
  - [brcm,bcm2835-armctrl-ic](../soc_interrupt_binding_reference/P003_brcm_bcm2835-armctrl-ic.md#std-dtcompatible-brcm-bcm2835-armctrl-ic)（[GitHub #110189](https://github.com/zephyrproject-rtos/zephyr/issues/110189)）
  - [brcm,bcm2836-l1-intc](../soc_interrupt_binding_reference/P004_brcm_bcm2836-l1-intc.md#std-dtcompatible-brcm-bcm2836-l1-intc)（[GitHub #110189](https://github.com/zephyrproject-rtos/zephyr/issues/110189)）
  - [cdac,thejas32-intc](../riscv_interrupt_binding_reference/P002_cdac_thejas32-intc.md#std-dtcompatible-cdac-thejas32-intc)（[GitHub #114202](https://github.com/zephyrproject-rtos/zephyr/issues/114202)）
  - [infineon,aurix-ir](../infineon_microchip_interrupt_binding_reference/P001_infineon_aurix-ir.md#std-dtcompatible-infineon-aurix-ir)（[GitHub #107516](https://github.com/zephyrproject-rtos/zephyr/issues/107516)）
  - [infineon,sysintc](../infineon_microchip_interrupt_binding_reference/P003_infineon_sysintc.md#std-dtcompatible-infineon-sysintc)（[GitHub #108259](https://github.com/zephyrproject-rtos/zephyr/issues/108259)）
  - [infineon,sysintc-mux](../infineon_microchip_interrupt_binding_reference/P002_infineon_sysintc-mux.md#std-dtcompatible-infineon-sysintc-mux)（[GitHub #108259](https://github.com/zephyrproject-rtos/zephyr/issues/108259)）
  - [microchip,smartfusion2-h2f-irqctrl](../infineon_microchip_interrupt_binding_reference/P008_microchip_smartfusion2-h2f-irqctrl.md#std-dtcompatible-microchip-smartfusion2-h2f-irqctrl)（[GitHub #106926](https://github.com/zephyrproject-rtos/zephyr/issues/106926)）
  - [qcom,hvm-pic](../multiarch_interrupt_binding_reference/P008_qcom_hvm-pic.md#std-dtcompatible-qcom-hvm-pic)（[GitHub #107122](https://github.com/zephyrproject-rtos/zephyr/issues/107122)）
  - [renesas,rx-icum](../renesas_interrupt_binding_reference/P003_renesas_rx-icum.md#std-dtcompatible-renesas-rx-icum)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
- 处理器间／进程间通信（IPC）


  - [infineon,ipc](../intercore_reference/P099_Infineon处理器间通信绑定.md#dtbinding-infineon-ipc)（[GitHub #117744](https://github.com/zephyrproject-rtos/zephyr/issues/117744)）
  - [nxp,ipc-rpmsg-lite](../intercore_reference/P105_NXPRPMSG-Lite后端绑定.md#dtbinding-nxp-ipc-rpmsg-lite)（[GitHub #104807](https://github.com/zephyrproject-rtos/zephyr/issues/104807)）
- 发光二极管（LED）


  - [awinic,aw9523b-led](../led_issi_nordic_nxp_binding_reference/P002_awinic_aw9523b-led.md#std-dtcompatible-awinic-aw9523b-led)（[GitHub #115299](https://github.com/zephyrproject-rtos/zephyr/issues/115299)）
  - [issi,is31fl3193](../led_issi_nordic_nxp_binding_reference/P005_issi_is31fl3193.md#std-dtcompatible-issi-is31fl3193)（[GitHub #107555](https://github.com/zephyrproject-rtos/zephyr/issues/107555)）
  - [nordic,npm10xx-led](../led_issi_nordic_nxp_binding_reference/P012_nordic_npm10xx-led.md#std-dtcompatible-nordic-npm10xx-led)（[GitHub #108756](https://github.com/zephyrproject-rtos/zephyr/issues/108756)）
  - [nxp,pca9530](../led_issi_nordic_nxp_binding_reference/P015_nxp_pca9530.md#std-dtcompatible-nxp-pca9530)（[GitHub #112203](https://github.com/zephyrproject-rtos/zephyr/issues/112203)）
  - [nxp,pca9531](../led_issi_nordic_nxp_binding_reference/P016_nxp_pca9531.md#std-dtcompatible-nxp-pca9531)（[GitHub #112203](https://github.com/zephyrproject-rtos/zephyr/issues/112203)）
  - [nxp,pca9532](../led_issi_nordic_nxp_binding_reference/P017_nxp_pca9532.md#std-dtcompatible-nxp-pca9532)（[GitHub #112203](https://github.com/zephyrproject-rtos/zephyr/issues/112203)）
  - [ti,lp5860](../led_sct_ti_xpowers_binding_reference/P011_ti_lp5860.md#std-dtcompatible-ti-lp5860)（[GitHub #108801](https://github.com/zephyrproject-rtos/zephyr/issues/108801)）
  - [ti,lp5861](../led_sct_ti_xpowers_binding_reference/P012_ti_lp5861.md#std-dtcompatible-ti-lp5861)（[GitHub #108801](https://github.com/zephyrproject-rtos/zephyr/issues/108801)）
  - [ti,lp5862](../led_sct_ti_xpowers_binding_reference/P013_ti_lp5862.md#std-dtcompatible-ti-lp5862)（[GitHub #108801](https://github.com/zephyrproject-rtos/zephyr/issues/108801)）
  - [ti,lp5864](../led_sct_ti_xpowers_binding_reference/P014_ti_lp5864.md#std-dtcompatible-ti-lp5864)（[GitHub #108801](https://github.com/zephyrproject-rtos/zephyr/issues/108801)）
  - [ti,lp5866](../led_sct_ti_xpowers_binding_reference/P015_ti_lp5866.md#std-dtcompatible-ti-lp5866)（[GitHub #108801](https://github.com/zephyrproject-rtos/zephyr/issues/108801)）
  - [ti,lp5868](../led_sct_ti_xpowers_binding_reference/P016_ti_lp5868.md#std-dtcompatible-ti-lp5868)（[GitHub #108801](https://github.com/zephyrproject-rtos/zephyr/issues/108801)）
  - [zephyr,fake-leds](../hardware/P546_伪LED控制器绑定.md#dtbinding-zephyr-fake-leds)（[GitHub #110819](https://github.com/zephyrproject-rtos/zephyr/issues/110819)）
  - [zephyr,native-linux-leds](../led_sct_ti_xpowers_binding_reference/P020_zephyr_native-linux-leds.md#std-dtcompatible-zephyr-native-linux-leds)（[GitHub #111189](https://github.com/zephyrproject-rtos/zephyr/issues/111189)）
- 灯带（LED Strip）


  - [worldsemi,ws2812-bflb-wo](../led_strip_binding_reference/P007_worldsemi_ws2812-bflb-wo.md#std-dtcompatible-worldsemi-ws2812-bflb-wo)（[GitHub #105325](https://github.com/zephyrproject-rtos/zephyr/issues/105325)）
  - [worldsemi,ws2812-pulse-io](../led_strip_binding_reference/P010_worldsemi_ws2812-pulse-io.md#std-dtcompatible-worldsemi-ws2812-pulse-io)（[GitHub #110466](https://github.com/zephyrproject-rtos/zephyr/issues/110466)）
- 本地互连网络（LIN）


  - [renesas,ra-lin-sci-b](../lin_dali_mctp_sensor_bus_binding_reference/P002_renesas_ra-lin-sci-b.md#std-dtcompatible-renesas-ra-lin-sci-b)（[GitHub #95975](https://github.com/zephyrproject-rtos/zephyr/issues/95975)）
- 远距离无线通信（LoRa）


  - [semtech,lr1121](../lora_ieee802154_binding_reference/P019_semtech_lr1121.md#std-dtcompatible-semtech-lr1121)（[GitHub #109912](https://github.com/zephyrproject-rtos/zephyr/issues/109912)）
- 邮箱（Mailbox）


  - [arm,mhuv2](../intercore_reference/P034_ArmMHUv2邮箱绑定.md#dtbinding-arm-mhuv2)（[GitHub #110686](https://github.com/zephyrproject-rtos/zephyr/issues/110686)）
  - [brcm,bcm2711-mbox](../intercore_reference/P036_BCM2711邮箱绑定.md#dtbinding-brcm-bcm2711-mbox)（[GitHub #107536](https://github.com/zephyrproject-rtos/zephyr/issues/107536)）
  - [infineon,mbox](../intercore_reference/P038_Infineon邮箱绑定.md#dtbinding-infineon-mbox)（[GitHub #117744](https://github.com/zephyrproject-rtos/zephyr/issues/117744)）
  - [renesas,rcar-mfis-mbox](../intercore_reference/P052_RenesasR-Car邮箱绑定.md#dtbinding-renesas-rcar-mfis-mbox)（[GitHub #108868](https://github.com/zephyrproject-rtos/zephyr/issues/108868)）
- 微控制器管理（MCUmgr）


  - [zephyr,smp-spi](../network_radio_frontend_binding_reference/P006_zephyr_smp-spi.md#std-dtcompatible-zephyr-smp-spi)（[GitHub #106947](https://github.com/zephyrproject-rtos/zephyr/issues/106947)）
- 存储器控制器（Memory Controller）


  - [bflb,bl808-psram-uhs](../memory_controller_hyperbus_smc_binding_reference/P006_bflb_bl808-psram-uhs.md#std-dtcompatible-bflb-bl808-psram-uhs)（[GitHub #110702](https://github.com/zephyrproject-rtos/zephyr/issues/110702)）
  - [bflb,bl808-psram-uhs-controller](../memory_controller_hyperbus_smc_binding_reference/P005_bflb_bl808-psram-uhs-controller.md#std-dtcompatible-bflb-bl808-psram-uhs-controller)（[GitHub #110702](https://github.com/zephyrproject-rtos/zephyr/issues/110702)）
  - [bflb,sf-bank](../memory_controller_hyperbus_smc_binding_reference/P007_bflb_sf-bank.md#std-dtcompatible-bflb-sf-bank)（[GitHub #107223](https://github.com/zephyrproject-rtos/zephyr/issues/107223)）
  - [bflb,sf-controller](../memory_controller_hyperbus_smc_binding_reference/P008_bflb_sf-controller.md#std-dtcompatible-bflb-sf-controller)（[GitHub #107223](https://github.com/zephyrproject-rtos/zephyr/issues/107223)）
  - [nxp,imx-snvs-gpr](../memory_controller_sdram_psram_binding_reference/P001_nxp_imx-snvs-gpr.md#std-dtcompatible-nxp-imx-snvs-gpr)（[GitHub #109842](https://github.com/zephyrproject-rtos/zephyr/issues/109842)）
  - [nxp,sramc](../memory_controller_sdram_psram_binding_reference/P002_nxp_sramc.md#std-dtcompatible-nxp-sramc)（[GitHub #118087](https://github.com/zephyrproject-rtos/zephyr/issues/118087)）
- MIPI 显示串行接口（MIPI-DSI）


  - [espressif,esp-mipi-dsi](../mipi_dbi_dsi_binding_reference/P012_espressif_esp-mipi-dsi.md#std-dtcompatible-espressif-esp-mipi-dsi)（[GitHub #116548](https://github.com/zephyrproject-rtos/zephyr/issues/116548)）
  - [renesas,rz-mipi-dsi](../mipi_dbi_dsi_binding_reference/P017_renesas_rz-mipi-dsi.md#std-dtcompatible-renesas-rz-mipi-dsi)（[GitHub #116701](https://github.com/zephyrproject-rtos/zephyr/issues/116701)）
- 其他绑定（Miscellaneous）


  - [adi,tmc6460](../compatible_binding_reference/P009_adi_tmc6460.md#std-dtcompatible-adi-tmc6460)（[GitHub #113438](https://github.com/zephyrproject-rtos/zephyr/issues/113438)）
  - [espressif,esp32-ppa](../misc_adi_nordic_binding_reference/P008_espressif_esp32-ppa.md#std-dtcompatible-espressif-esp32-ppa)（[GitHub #117658](https://github.com/zephyrproject-rtos/zephyr/issues/117658)）
  - [nxp,imx93-video-pll](../misc_nxp_renesas_zephyr_binding_reference/P001_nxp_imx93-video-pll.md#std-dtcompatible-nxp-imx93-video-pll)（[GitHub #98554](https://github.com/zephyrproject-rtos/zephyr/issues/98554)）
  - [nxp,mcxw-hw-params](../misc_nxp_renesas_zephyr_binding_reference/P002_nxp_mcxw-hw-params.md#std-dtcompatible-nxp-mcxw-hw-params)（[GitHub #108974](https://github.com/zephyrproject-rtos/zephyr/issues/108974)）
  - [raspberrypi,pico-powman](../misc_nxp_renesas_zephyr_binding_reference/P012_raspberrypi_pico-powman.md#std-dtcompatible-raspberrypi-pico-powman)（[GitHub #115474](https://github.com/zephyrproject-rtos/zephyr/issues/115474)）
  - [renesas,rx-sci-b](../misc_nxp_renesas_zephyr_binding_reference/P025_renesas_rx-sci-b.md#std-dtcompatible-renesas-rx-sci-b)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
  - [renesas,rx-system-controller](../misc_nxp_renesas_zephyr_binding_reference/P027_renesas_rx-system-controller.md#std-dtcompatible-renesas-rx-system-controller)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
  - [ti,tdp2004](../misc_nxp_renesas_zephyr_binding_reference/P039_ti_tdp2004.md#std-dtcompatible-ti-tdp2004)（[GitHub #111950](https://github.com/zephyrproject-rtos/zephyr/issues/111950)）
- 调制解调器（Modem）


  - [fibocom,le250](../modem_fibocom_nordic_quectel_binding_reference/P001_fibocom_le250.md#std-dtcompatible-fibocom-le250)（[GitHub #114755](https://github.com/zephyrproject-rtos/zephyr/issues/114755)）
  - [nordic,nrf91-sm-v2](../modem_fibocom_nordic_quectel_binding_reference/P003_nordic_nrf91-sm-v2.md#std-dtcompatible-nordic-nrf91-sm-v2)（[GitHub #115058](https://github.com/zephyrproject-rtos/zephyr/issues/115058)）
  - [nordic,nrf93m1](../modem_fibocom_nordic_quectel_binding_reference/P004_nordic_nrf93m1.md#std-dtcompatible-nordic-nrf93m1)（[GitHub #106289](https://github.com/zephyrproject-rtos/zephyr/issues/106289)）
  - [quectel,bc66](../modem_fibocom_nordic_quectel_binding_reference/P006_quectel_bc66.md#std-dtcompatible-quectel-bc66)（[GitHub #111279](https://github.com/zephyrproject-rtos/zephyr/issues/111279)）
  - [quectel,bc660k](../modem_fibocom_nordic_quectel_binding_reference/P007_quectel_bc660k.md#std-dtcompatible-quectel-bc660k)（[GitHub #111279](https://github.com/zephyrproject-rtos/zephyr/issues/111279)）
  - [quectel,bc66x](../modem_fibocom_nordic_quectel_binding_reference/P008_quectel_bc66x.md#std-dtcompatible-quectel-bc66x)（[GitHub #111279](https://github.com/zephyrproject-rtos/zephyr/issues/111279)）
  - [quectel,bg770](../modem_fibocom_nordic_quectel_binding_reference/P009_quectel_bg770.md#std-dtcompatible-quectel-bg770)（[GitHub #114859](https://github.com/zephyrproject-rtos/zephyr/issues/114859)）
  - [quectel,eg21-g](../modem_fibocom_nordic_quectel_binding_reference/P013_quectel_eg21-g.md#std-dtcompatible-quectel-eg21-g)（[GitHub #115561](https://github.com/zephyrproject-rtos/zephyr/issues/115561)）
  - [quectel,eg915u](../modem_fibocom_nordic_quectel_binding_reference/P016_quectel_eg915u.md#std-dtcompatible-quectel-eg915u)（[GitHub #95921](https://github.com/zephyrproject-rtos/zephyr/issues/95921)）
  - [telit,le910c1tx](../modem_sierra_telit_ublox_binding_reference/P010_telit_le910c1tx.md#std-dtcompatible-telit-le910c1tx)（[GitHub #106716](https://github.com/zephyrproject-rtos/zephyr/issues/106716)）
  - [telit,lex10q1](../modem_sierra_telit_ublox_binding_reference/P011_telit_lex10q1.md#std-dtcompatible-telit-lex10q1)（[GitHub #109206](https://github.com/zephyrproject-rtos/zephyr/issues/109206)）
  - [trasna,lexi-r10](../modem_sierra_telit_ublox_binding_reference/P014_trasna_lexi-r10.md#std-dtcompatible-trasna-lexi-r10)（[GitHub #107308](https://github.com/zephyrproject-rtos/zephyr/issues/107308)）
- 存储技术设备（MTD）


  - [bflb,sf-device](../mtd_atmel_bouffalo_binding_reference/P011_bflb_sf-device.md#std-dtcompatible-bflb-sf-device)（[GitHub #107223](https://github.com/zephyrproject-rtos/zephyr/issues/107223)）
  - [bflb,sf-flash](../mtd_atmel_bouffalo_binding_reference/P012_bflb_sf-flash.md#std-dtcompatible-bflb-sf-flash)（[GitHub #107223](https://github.com/zephyrproject-rtos/zephyr/issues/107223)）
  - [infineon,s28hx512t](../mtd_atmel_bouffalo_binding_reference/P020_infineon_s28hx512t-mspi.md#std-dtcompatible-infineon-s28hx512t)（[GitHub #102513](https://github.com/zephyrproject-rtos/zephyr/issues/102513)）
  - [is66wv](../mtd_atmel_bouffalo_binding_reference/P023_is66wv-mspi.md#std-dtcompatible-is66wv)（[GitHub #111074](https://github.com/zephyrproject-rtos/zephyr/issues/111074)）
  - [microchip,flash-g2](../mtd_microchip_nordic_nxp_binding_reference/P003_microchip_flash-g2.md#std-dtcompatible-microchip-flash-g2)（[GitHub #108440](https://github.com/zephyrproject-rtos/zephyr/issues/108440)）
  - [microchip,flash-g3](../mtd_microchip_nordic_nxp_binding_reference/P004_microchip_flash-g3.md#std-dtcompatible-microchip-flash-g3)（[GitHub #109747](https://github.com/zephyrproject-rtos/zephyr/issues/109747)）
  - [microcrystal,rv3028-eeprom](../mtd_microchip_nordic_nxp_binding_reference/P006_microcrystal_rv3028-eeprom.md#std-dtcompatible-microcrystal-rv3028-eeprom)（[GitHub #115759](https://github.com/zephyrproject-rtos/zephyr/issues/115759)）
  - [mxicy,mx25um51345g](../mtd_microchip_nordic_nxp_binding_reference/P008_mxicy_mx25um51345g.md#std-dtcompatible-mxicy-mx25um51345g)（[GitHub #112458](https://github.com/zephyrproject-rtos/zephyr/issues/112458)）
  - [nordic,tz-nonsecure](../mtd_microchip_nordic_nxp_binding_reference/P013_nordic_tz-nonsecure.md#std-dtcompatible-nordic-tz-nonsecure)（[GitHub #108883](https://github.com/zephyrproject-rtos/zephyr/issues/108883)）
  - [nordic,tz-secure](../mtd_microchip_nordic_nxp_binding_reference/P014_nordic_tz-secure.md#std-dtcompatible-nordic-tz-secure)（[GitHub #108883](https://github.com/zephyrproject-rtos/zephyr/issues/108883)）
  - [nxp,imx-flexspi-nand](../mtd_microchip_nordic_nxp_binding_reference/P022_nxp_imx-flexspi-nand.md#std-dtcompatible-nxp-imx-flexspi-nand)（[GitHub #104870](https://github.com/zephyrproject-rtos/zephyr/issues/104870)）
  - [nxp,mcxw-ifr](../mtd_nxp_st_ti_partition_binding_reference/P002_nxp_mcxw-ifr.md#std-dtcompatible-nxp-mcxw-ifr)（[GitHub #108974](https://github.com/zephyrproject-rtos/zephyr/issues/108974)）
  - [realtek,bee-nor-flash](../mtd_nxp_st_ti_partition_binding_reference/P008_realtek_bee-nor-flash.md#std-dtcompatible-realtek-bee-nor-flash)（[GitHub #107007](https://github.com/zephyrproject-rtos/zephyr/issues/107007)）
  - [st,m95p32](../mtd_nxp_st_ti_partition_binding_reference/P014_st_m95p32-mspi.md#std-dtcompatible-st-m95p32)（[GitHub #117991](https://github.com/zephyrproject-rtos/zephyr/issues/117991)）
  - [winbond,w25q512nw](../mtd_nxp_st_ti_partition_binding_reference/P021_winbond_w25q512nw.md#std-dtcompatible-winbond-w25q512nw)（[GitHub #112458](https://github.com/zephyrproject-rtos/zephyr/issues/112458)）
- 多位串行外设接口（Multi-Bit SPI）


  - [cdns,xspi-nor](../mspi_binding_reference/P003_cdns_xspi-nor.md#std-dtcompatible-cdns-xspi-nor)（[GitHub #102513](https://github.com/zephyrproject-rtos/zephyr/issues/102513)）
  - [microchip,xec-qmspi-controller](../mspi_binding_reference/P004_microchip_xec-qmspi-controller.md#std-dtcompatible-microchip-xec-qmspi-controller)（[GitHub #113243](https://github.com/zephyrproject-rtos/zephyr/issues/113243)）
  - [microchip,xec-qmspi-device](../mspi_binding_reference/P005_microchip_xec-qmspi-device-mspi.md#std-dtcompatible-microchip-xec-qmspi-device)（[GitHub #113243](https://github.com/zephyrproject-rtos/zephyr/issues/113243)）
  - [nxp,qspi](../mspi_binding_reference/P008_nxp_qspi.md#std-dtcompatible-nxp-qspi)（[GitHub #108953](https://github.com/zephyrproject-rtos/zephyr/issues/108953)）
  - [st,nor](../mspi_binding_reference/P010_st_nor-mspi.md#std-dtcompatible-st-nor)（[GitHub #113368](https://github.com/zephyrproject-rtos/zephyr/issues/113368)）
  - [st,psram-device](../mspi_binding_reference/P011_st_psram-device-mspi.md#std-dtcompatible-st-psram-device)（[GitHub #105219](https://github.com/zephyrproject-rtos/zephyr/issues/105219)）
  - [zephyr,peripheral-device](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mspi/zephyr%2Cperipheral-device-mspi.html#std-dtcompatible-zephyr-peripheral-device)（[GitHub #103754](https://github.com/zephyrproject-rtos/zephyr/issues/103754)）
- 多功能设备（Multi-Function Device）


  - [ambiq,ios](../hardware/P700_Ambiq输入输出从控制器绑定.md#dtbinding-ambiq-ios)（[GitHub #96059](https://github.com/zephyrproject-rtos/zephyr/issues/96059)）
  - [infineon,autanalog](../hardware/P720_Infineon自主模拟子系统绑定.md#dtbinding-infineon-autanalog)（[GitHub #106227](https://github.com/zephyrproject-rtos/zephyr/issues/106227)）
  - [infineon,autanalog-ac-state](../hardware/P721_Infineon自主模拟控制器状态绑定.md#dtbinding-infineon-autanalog-ac-state)（[GitHub #106227](https://github.com/zephyrproject-rtos/zephyr/issues/106227)）
  - [infineon,autanalog-ctb](../hardware/P722_Infineon连续时间模块绑定.md#dtbinding-infineon-autanalog-ctb)（[GitHub #107489](https://github.com/zephyrproject-rtos/zephyr/issues/107489)）
  - [infineon,autanalog-prb](../hardware/P659_Infineon可编程参考模块绑定.md#dtbinding-infineon-autanalog-prb)（[GitHub #107487](https://github.com/zephyrproject-rtos/zephyr/issues/107487)）
  - [infineon,autanalog-ptcomp](../hardware/P723_Infineon可编程阈值比较器绑定.md#dtbinding-infineon-autanalog-ptcomp)（[GitHub #107488](https://github.com/zephyrproject-rtos/zephyr/issues/107488)）
  - [infineon,hppass-ac-state](../hardware/P725_Infineon高性能模拟控制器状态绑定.md#dtbinding-infineon-hppass-ac-state)（[GitHub #109196](https://github.com/zephyrproject-rtos/zephyr/issues/109196)）
  - [infineon,hppass-analog](../hardware/P724_Infineon高性能可编程模拟子系统绑定.md#dtbinding-infineon-hppass-analog)（[GitHub #109196](https://github.com/zephyrproject-rtos/zephyr/issues/109196)）
  - [infineon,hppass-csg](../hardware/P726_Infineon斜坡发生器绑定.md#dtbinding-infineon-hppass-csg)（[GitHub #109694](https://github.com/zephyrproject-rtos/zephyr/issues/109694)）
  - [infineon,mxcrypto](../hardware/P727_Infineon加密硬件模块绑定.md#dtbinding-infineon-mxcrypto)（[GitHub #108439](https://github.com/zephyrproject-rtos/zephyr/issues/108439)）
  - [infineon,mxcryptolite](../hardware/P728_Infineon轻量加密硬件模块绑定.md#dtbinding-infineon-mxcryptolite)（[GitHub #109693](https://github.com/zephyrproject-rtos/zephyr/issues/109693)）
  - [m5stack,m5pm1](../hardware/P682_M5PM1多功能设备绑定.md#dtbinding-m5stack-m5pm1)（[GitHub #109961](https://github.com/zephyrproject-rtos/zephyr/issues/109961)）
  - [silabs,emu](../hardware/P717_Silabs能量管理单元绑定.md#dtbinding-silabs-emu)（[GitHub #120576](https://github.com/zephyrproject-rtos/zephyr/issues/120576)）
  - [ti,tla2528](../hardware/P718_TLA2528多功能设备绑定.md#dtbinding-ti-tla2528)（[GitHub #110722](https://github.com/zephyrproject-rtos/zephyr/issues/110722)）
- 多路复用器（MUX）


  - [adi,adgm3121](../mux_w1_binding_reference/P002_adi_adgm3121.md#std-dtcompatible-adi-adgm3121)（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
  - [adi,adgm3121-gpio](../mux_w1_binding_reference/P001_adi_adgm3121-gpio.md#std-dtcompatible-adi-adgm3121-gpio)（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
  - [gpio-mux](../mux_w1_binding_reference/P003_gpio-mux.md#std-dtcompatible-gpio-mux)（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
  - [nxp,inputmux](../mux_w1_binding_reference/P004_nxp_inputmux.md#std-dtcompatible-nxp-inputmux)（[GitHub #109379](https://github.com/zephyrproject-rtos/zephyr/issues/109379)）
  - [nxp,trgmux](../mux_w1_binding_reference/P005_nxp_trgmux.md#std-dtcompatible-nxp-trgmux)（[GitHub #112088](https://github.com/zephyrproject-rtos/zephyr/issues/112088)）
- 网络（Networking）


  - [st,stm32wba-radio](../network_radio_frontend_binding_reference/P016_st_stm32wba-radio.md#std-dtcompatible-st-stm32wba-radio)（[GitHub #110546](https://github.com/zephyrproject-rtos/zephyr/issues/110546)）
- 运算放大器（OPAMP）


  - [infineon,autanalog-ctb-opamp](../hardware/P730_Infineon连续时间模块运算放大器绑定.md#dtbinding-infineon-autanalog-ctb-opamp)（[GitHub #107489](https://github.com/zephyrproject-rtos/zephyr/issues/107489)）
- 一次性可编程存储器（OTP Memory）


  - [adi,axi-sysid](../otp_binding_reference/P001_adi_axi-sysid.md#std-dtcompatible-adi-axi-sysid)（[GitHub #115280](https://github.com/zephyrproject-rtos/zephyr/issues/115280)）
  - [nordic,npm10xx-uicr](../otp_binding_reference/P003_nordic_npm10xx-uicr.md#std-dtcompatible-nordic-npm10xx-uicr)（[GitHub #119928](https://github.com/zephyrproject-rtos/zephyr/issues/119928)）
  - [nxp,otpc](../otp_binding_reference/P005_nxp_otpc.md#std-dtcompatible-nxp-otpc)（[GitHub #111707](https://github.com/zephyrproject-rtos/zephyr/issues/111707)）
  - [nxp,rt7xx-ocotp](../otp_binding_reference/P006_nxp_rt7xx-ocotp.md#std-dtcompatible-nxp-rt7xx-ocotp)（[GitHub #108075](https://github.com/zephyrproject-rtos/zephyr/issues/108075)）
  - [realtek,rts5817-ocotp](../otp_binding_reference/P007_realtek_rts5817-ocotp.md#std-dtcompatible-realtek-rts5817-ocotp)（[GitHub #111141](https://github.com/zephyrproject-rtos/zephyr/issues/111141)）
- 高速外围组件互连（PCIe）


  - [brcm,iproc-pcie-ep-v2](../pcie_memory_virtualization_binding_reference/P006_brcm_iproc-pcie-ep-v2.md#std-dtcompatible-brcm-iproc-pcie-ep-v2)（[GitHub #111490](https://github.com/zephyrproject-rtos/zephyr/issues/111490)）
- 性能状态（Performance State）


  - [nxp,imx9-pstate](../power_state_wakeup_binding_reference/P001_nxp_imx9-pstate.md#std-dtcompatible-nxp-imx9-pstate)（[GitHub #120033](https://github.com/zephyrproject-rtos/zephyr/issues/120033)）
- 物理层（PHY）


  - [lin-transceiver-gpio](../phy_binding_reference/P002_lin-transceiver-gpio.md#std-dtcompatible-lin-transceiver-gpio)（[GitHub #95975](https://github.com/zephyrproject-rtos/zephyr/issues/95975)）
  - [st,stm32f7-usbphyc](../phy_binding_reference/P005_st_stm32f7-usbphyc.md#std-dtcompatible-st-stm32f7-usbphyc)（[GitHub #114696](https://github.com/zephyrproject-rtos/zephyr/issues/114696)）
  - [st,stm32n6-usbphyc](../phy_binding_reference/P006_st_stm32n6-usbphyc.md#std-dtcompatible-st-stm32n6-usbphyc)（[GitHub #114696](https://github.com/zephyrproject-rtos/zephyr/issues/114696)）
- 引脚控制（Pin Control）


  - [aesc,pinctrl](../pinctrl_adi_ambiq_arm_binding_reference/P002_aesc_pinctrl.md#std-dtcompatible-aesc-pinctrl)（[GitHub #108137](https://github.com/zephyrproject-rtos/zephyr/issues/108137)）
  - [arm,v2m_musca_b1-pinctrl](../pinctrl_adi_ambiq_arm_binding_reference/P012_arm_v2m_musca_b1-pinctrl.md#std-dtcompatible-arm-v2m_musca_b1-pinctrl)（[GitHub #114671](https://github.com/zephyrproject-rtos/zephyr/issues/114671)）
  - [brcm,bcm2712-pinctrl](../pinctrl_adi_ambiq_arm_binding_reference/P018_brcm_bcm2712-pinctrl.md#std-dtcompatible-brcm-bcm2712-pinctrl)（[GitHub #101635](https://github.com/zephyrproject-rtos/zephyr/issues/101635)）
  - [elan,em32-pinctrl](../pinctrl_adi_ambiq_arm_binding_reference/P019_elan_em32-pinctrl.md#std-dtcompatible-elan-em32-pinctrl)（[GitHub #103037](https://github.com/zephyrproject-rtos/zephyr/issues/103037)）
  - [mediatek,mt8188-pinctrl](../pinctrl_infineon_nordic_nxp_binding_reference/P005_mediatek_mt8188-pinctrl.md#std-dtcompatible-mediatek-mt8188-pinctrl)（[GitHub #118658](https://github.com/zephyrproject-rtos/zephyr/issues/118658)）
  - [nxp,lpc84x-iocon](../pinctrl_nxp_pico_binding_reference/P009_nxp_lpc84x-iocon.md#std-dtcompatible-nxp-lpc84x-iocon)（[GitHub #105928](https://github.com/zephyrproject-rtos/zephyr/issues/105928)）
  - [nxp,lpc84x-swm](../pinctrl_nxp_pico_binding_reference/P010_nxp_lpc84x-swm.md#std-dtcompatible-nxp-lpc84x-swm)（[GitHub #105928](https://github.com/zephyrproject-rtos/zephyr/issues/105928)）
  - [nxp,mcux-rt266x-pinctrl](../pinctrl_nxp_pico_binding_reference/P014_nxp_mcux-rt266x-pinctrl.md#std-dtcompatible-nxp-mcux-rt266x-pinctrl)（[GitHub #118702](https://github.com/zephyrproject-rtos/zephyr/issues/118702)）
  - [raspberrypi,rp1-pinctrl](../pinctrl_renesas_silabs_binding_reference/P001_raspberrypi_rp1-pinctrl.md#std-dtcompatible-raspberrypi-rp1-pinctrl)（[GitHub #101635](https://github.com/zephyrproject-rtos/zephyr/issues/101635)）
  - [renesas,rcar-pfc-x5h](../pinctrl_renesas_silabs_binding_reference/P008_renesas_rcar-pfc-x5h.md#std-dtcompatible-renesas-rcar-pfc-x5h)（[GitHub #108871](https://github.com/zephyrproject-rtos/zephyr/issues/108871)）
  - [renesas,rx-pinctrl-pfs](../pinctrl_renesas_silabs_binding_reference/P010_renesas_rx-pinctrl-pfs.md#std-dtcompatible-renesas-rx-pinctrl-pfs)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
  - [ti,tiva-c-pinctrl](../pinctrl_stm32_ti_xilinx_binding_reference/P015_ti_tiva-c-pinctrl.md#std-dtcompatible-ti-tiva-c-pinctrl)（[GitHub #110025](https://github.com/zephyrproject-rtos/zephyr/issues/110025)）
  - [wch,ch570-pinctrl](../pinctrl_stm32_ti_xilinx_binding_reference/P019_wch_ch570-pinctrl.md#std-dtcompatible-wch-ch570-pinctrl)（[GitHub #111171](https://github.com/zephyrproject-rtos/zephyr/issues/111171)）
  - [wch,h41x-afio](../pinctrl_stm32_ti_xilinx_binding_reference/P020_wch_h41x-afio.md#std-dtcompatible-wch-h41x-afio)（[GitHub #111725](https://github.com/zephyrproject-rtos/zephyr/issues/111725)）
- 电源域（Power Domain）


  - [raspberrypi,bcm283x-power](../power_domain_binding_reference/P009_raspberrypi_bcm283x-power.md#std-dtcompatible-raspberrypi-bcm283x-power)（[GitHub #112918](https://github.com/zephyrproject-rtos/zephyr/issues/112918)）
- 电源管理（Power Management）


  - [infineon,hibernate-wakeup](../power_control_binding_reference/P004_infineon_hibernate-wakeup.md#std-dtcompatible-infineon-hibernate-wakeup)（[GitHub #116691](https://github.com/zephyrproject-rtos/zephyr/issues/116691)）
  - [microchip,supc-g1](../power_control_binding_reference/P007_microchip_supc-g1.md#std-dtcompatible-microchip-supc-g1)（[GitHub #115872](https://github.com/zephyrproject-rtos/zephyr/issues/115872)）
  - [nuvoton,npcx-power-state](../power_control_binding_reference/P012_nuvoton_npcx-power-state.md#std-dtcompatible-nuvoton-npcx-power-state)（[GitHub #118685](https://github.com/zephyrproject-rtos/zephyr/issues/118685)）
  - [nxp,smc](../power_control_binding_reference/P020_nxp_smc.md#std-dtcompatible-nxp-smc)（[GitHub #102228](https://github.com/zephyrproject-rtos/zephyr/issues/102228)）
  - [st,stm32-pwr-wkupctrl](../stm32_soc_power_binding_reference/P009_st_stm32-pwr-wkupctrl.md#std-dtcompatible-st-stm32-pwr-wkupctrl)（[GitHub #114092](https://github.com/zephyrproject-rtos/zephyr/issues/114092)）
  - [st,stm32f1-pwr-wkupctrl](../stm32_soc_power_binding_reference/P011_st_stm32f1-pwr-wkupctrl.md#std-dtcompatible-st-stm32f1-pwr-wkupctrl)（[GitHub #114092](https://github.com/zephyrproject-rtos/zephyr/issues/114092)）
  - [st,stm32f7-pwr-wkupctrl](../stm32_soc_power_binding_reference/P012_st_stm32f7-pwr-wkupctrl.md#std-dtcompatible-st-stm32f7-pwr-wkupctrl)（[GitHub #114092](https://github.com/zephyrproject-rtos/zephyr/issues/114092)）
- 脉冲输入输出（Pulse IO）


  - [espressif,esp32-rmt](../platform_rmt_openthread_binding_reference/P008_espressif_esp32-rmt.md#std-dtcompatible-espressif-esp32-rmt)（[GitHub #110466](https://github.com/zephyrproject-rtos/zephyr/issues/110466)）
  - [zephyr,pulse-io-loopback](../hardware/P549_脉冲输入输出回环绑定.md#dtbinding-zephyr-pulse-io-loopback)（[GitHub #110466](https://github.com/zephyrproject-rtos/zephyr/issues/110466)）
- 脉宽调制（PWM）


  - [adi,axi-pwmgen](../pwm_adi_esp_infineon_binding_reference/P001_adi_axi-pwmgen.md#std-dtcompatible-adi-axi-pwmgen)（[GitHub #115319](https://github.com/zephyrproject-rtos/zephyr/issues/115319)）
  - [microchip,pwm-g1](../pwm_intel_microchip_nxp_binding_reference/P009_microchip_pwm-g1.md#std-dtcompatible-microchip-pwm-g1)（[GitHub #111745](https://github.com/zephyrproject-rtos/zephyr/issues/111745)）
  - [nxp,emios](../pwm_nxp_renesas_binding_reference/P001_nxp_emios.md#std-dtcompatible-nxp-emios)（[GitHub #111373](https://github.com/zephyrproject-rtos/zephyr/issues/111373)）
  - [nxp,emios-pwm](../pwm_intel_microchip_nxp_binding_reference/P020_nxp_emios-pwm.md#std-dtcompatible-nxp-emios-pwm)（[GitHub #111373](https://github.com/zephyrproject-rtos/zephyr/issues/111373)）
  - [nxp,ipwm](../pwm_nxp_renesas_binding_reference/P006_nxp_ipwm.md#std-dtcompatible-nxp-ipwm)（[GitHub #117075](https://github.com/zephyrproject-rtos/zephyr/issues/117075)）
  - [realtek,ameba-pwm](../pwm_nxp_renesas_binding_reference/P015_realtek_ameba-pwm.md#std-dtcompatible-realtek-ameba-pwm)（[GitHub #106669](https://github.com/zephyrproject-rtos/zephyr/issues/106669)）
  - [realtek,bee-pwm](../pwm_nxp_renesas_binding_reference/P016_realtek_bee-pwm.md#std-dtcompatible-realtek-bee-pwm)（[GitHub #105014](https://github.com/zephyrproject-rtos/zephyr/issues/105014)）
  - [ti,am3352-ecap](../pwm_stm32_ti_generic_binding_reference/P013_ti_am3352-ecap.md#std-dtcompatible-ti-am3352-ecap)（[GitHub #88860](https://github.com/zephyrproject-rtos/zephyr/issues/88860)）
  - [ti,am3352-ehrpwm](../pwm_stm32_ti_generic_binding_reference/P014_ti_am3352-ehrpwm.md#std-dtcompatible-ti-am3352-ehrpwm)（[GitHub #88757](https://github.com/zephyrproject-rtos/zephyr/issues/88757)）
  - [wch,adtm-pwm](../pwm_stm32_ti_generic_binding_reference/P018_wch_adtm-pwm.md#std-dtcompatible-wch-adtm-pwm)（[GitHub #109728](https://github.com/zephyrproject-rtos/zephyr/issues/109728)）
  - [wisblock-pwm](../pwm_stm32_ti_generic_binding_reference/P020_wisblock-pwm.md#std-dtcompatible-wisblock-pwm)（[GitHub #113140](https://github.com/zephyrproject-rtos/zephyr/issues/113140)）
  - [zephyr,pwm-bitbang](../pwm_stm32_ti_generic_binding_reference/P022_zephyr_pwm-bitbang.md#std-dtcompatible-zephyr-pwm-bitbang)（[GitHub #106536](https://github.com/zephyrproject-rtos/zephyr/issues/106536)）
- 稳压器（Regulator）


  - [adi,max20362-regulator](../hardware/P672_MAX20362稳压器绑定.md#dtbinding-adi-max20362-regulator)（[GitHub #116023](https://github.com/zephyrproject-rtos/zephyr/issues/116023)）
  - [gd,gd32-bldo](../hardware/P637_GD32备份低压差稳压器绑定.md#dtbinding-gd-gd32-bldo)（[GitHub #106501](https://github.com/zephyrproject-rtos/zephyr/issues/106501)）
  - [infineon,autanalog-prb-vref](../hardware/P650_Infineon自主模拟参考电压绑定.md#dtbinding-infineon-autanalog-prb-vref)（[GitHub #107487](https://github.com/zephyrproject-rtos/zephyr/issues/107487)）
  - [m5stack,m5pm1-regulator](../hardware/P675_M5PM1稳压器绑定.md#dtbinding-m5stack-m5pm1-regulator)（[GitHub #109961](https://github.com/zephyrproject-rtos/zephyr/issues/109961)）
  - [nxp,spc-bandgap-buffer](../hardware/P651_NXP带隙缓冲器绑定.md#dtbinding-nxp-spc-bandgap-buffer)（[GitHub #116489](https://github.com/zephyrproject-rtos/zephyr/issues/116489)）
  - [realtek,rts5817-regulator](../hardware/P678_RTS5817稳压器绑定.md#dtbinding-realtek-rts5817-regulator)（[GitHub #108545](https://github.com/zephyrproject-rtos/zephyr/issues/108545)）
  - [sifli,sf32lb52x-ldo](../hardware/P656_SF32LB52X低压差稳压器绑定.md#dtbinding-sifli-sf32lb52x-ldo)（[GitHub #108093](https://github.com/zephyrproject-rtos/zephyr/issues/108093)）
  - [ti,mspm0-vref](../hardware/P658_MSPM0参考电压绑定.md#dtbinding-ti-mspm0-vref)（[GitHub #94732](https://github.com/zephyrproject-rtos/zephyr/issues/94732)）
  - [ti,tps6287x](../hardware/P667_TPS6287x稳压器绑定.md#dtbinding-ti-tps6287x)（[GitHub #119432](https://github.com/zephyrproject-rtos/zephyr/issues/119432)）
- 复位控制器（Reset Controller）


  - [rockchip,rk3588-cru-rst](../reset_controller_binding_reference/P015_rockchip_rk3588-cru-rst.md#std-dtcompatible-rockchip-rk3588-cru-rst)（[GitHub #117985](https://github.com/zephyrproject-rtos/zephyr/issues/117985)）
  - [wch,ch32-rcc-rctl](../reset_controller_binding_reference/P019_wch_ch32-rcc-rctl.md#std-dtcompatible-wch-ch32-rcc-rctl)（[GitHub #115714](https://github.com/zephyrproject-rtos/zephyr/issues/115714)）
- 保持存储器（Retained Memory）


  - [gd,gd32-backup-sram](../hardware/P625_GD32备份SRAM绑定.md#dtbinding-gd-gd32-backup-sram)（[GitHub #106501](https://github.com/zephyrproject-rtos/zephyr/issues/106501)）
  - [microcrystal,rv3028-ram](../hardware/P626_RV3028保留内存绑定.md#dtbinding-microcrystal-rv3028-ram)（[GitHub #115956](https://github.com/zephyrproject-rtos/zephyr/issues/115956)）
- 随机数生成器（RNG）


  - [brcm,bcm2835-rng](../rng_binding_reference/P005_brcm_bcm2835-rng.md#std-dtcompatible-brcm-bcm2835-rng)（[GitHub #110191](https://github.com/zephyrproject-rtos/zephyr/issues/110191)）
  - [microchip,trng-g2-entropy](../rng_binding_reference/P011_microchip_trng-g2-entropy.md#std-dtcompatible-microchip-trng-g2-entropy)（[GitHub #108155](https://github.com/zephyrproject-rtos/zephyr/issues/108155)）
  - [realtek,ameba-trng](../soc_rng_binding_reference/P002_realtek_ameba-trng.md#std-dtcompatible-realtek-ameba-trng)（[GitHub #106670](https://github.com/zephyrproject-rtos/zephyr/issues/106670)）
  - [realtek,bee-trng](../soc_rng_binding_reference/P003_realtek_bee-trng.md#std-dtcompatible-realtek-bee-trng)（[GitHub #105335](https://github.com/zephyrproject-rtos/zephyr/issues/105335)）
- 实时时钟（RTC）


  - [ite,it8xxx2-rtc](../rtc_binding_reference/P009_ite_it8xxx2-rtc.md#std-dtcompatible-ite-it8xxx2-rtc)（[GitHub #106350](https://github.com/zephyrproject-rtos/zephyr/issues/106350)）
  - [microchip,rtc-mss](../microchip_microcrystal_nxp_rtc_binding_reference/P001_microchip_rtc-mss.md#std-dtcompatible-microchip-rtc-mss)（[GitHub #110842](https://github.com/zephyrproject-rtos/zephyr/issues/110842)）
  - [microchip,xec-hibtimer](../microchip_microcrystal_nxp_rtc_binding_reference/P002_microchip_xec-hibtimer.md#std-dtcompatible-microchip-xec-hibtimer)（[GitHub #111476](https://github.com/zephyrproject-rtos/zephyr/issues/111476)）
  - [microchip,xec-rtc](../microchip_microcrystal_nxp_rtc_binding_reference/P003_microchip_xec-rtc.md#std-dtcompatible-microchip-xec-rtc)（[GitHub #106116](https://github.com/zephyrproject-rtos/zephyr/issues/106116)）
  - [microcrystal,rv3028-rtc](../microchip_microcrystal_nxp_rtc_binding_reference/P006_microcrystal_rv3028-rtc.md#std-dtcompatible-microcrystal-rv3028-rtc)（[GitHub #112978](https://github.com/zephyrproject-rtos/zephyr/issues/112978)）
  - [nxp,rtc-analog](../microchip_microcrystal_nxp_rtc_binding_reference/P018_nxp_rtc-analog.md#std-dtcompatible-nxp-rtc-analog)（[GitHub #107196](https://github.com/zephyrproject-rtos/zephyr/issues/107196)）
  - [realtek,ameba-rtc](../soc_rtc_binding_reference/P004_realtek_ameba-rtc.md#std-dtcompatible-realtek-ameba-rtc)（[GitHub #105376](https://github.com/zephyrproject-rtos/zephyr/issues/105376)）
- SD 主机控制器（SDHC）


  - [bflb,sdhc](../sdhc_binding_reference/P004_bflb_sdhc.md#std-dtcompatible-bflb-sdhc)（[GitHub #105243](https://github.com/zephyrproject-rtos/zephyr/issues/105243)）
  - [microchip,sdhc-g1](../sdhc_binding_reference/P012_microchip_sdhc-g1.md#std-dtcompatible-microchip-sdhc-g1)（[GitHub #109211](https://github.com/zephyrproject-rtos/zephyr/issues/109211)）
  - [nuvoton,numaker-sdhc](../sdhc_binding_reference/P013_nuvoton_numaker-sdhc.md#std-dtcompatible-nuvoton-numaker-sdhc)（[GitHub #105437](https://github.com/zephyrproject-rtos/zephyr/issues/105437)）
  - [realtek,ameba-sdhost](../sdhc_binding_reference/P016_realtek_ameba-sdhost.md#std-dtcompatible-realtek-ameba-sdhost)（[GitHub #106687](https://github.com/zephyrproject-rtos/zephyr/issues/106687)）
  - [ti,am654-sdhci](../sdhc_binding_reference/P020_ti_am654-sdhci.md#std-dtcompatible-ti-am654-sdhci)（[GitHub #97172](https://github.com/zephyrproject-rtos/zephyr/issues/97172)）
- 传感器（Sensors）


  - [adi,adis1647x](../sensor_adi_accel_bioz_binding_reference/P003_adi_adis1647x.md#std-dtcompatible-adi-adis1647x)（[GitHub #110012](https://github.com/zephyrproject-rtos/zephyr/issues/110012)）
  - [adi,adxl313](../sensor_adi_accel_bioz_binding_reference/P009_adi_adxl313.md#std-dtcompatible-adi-adxl313)（[GitHub #114936](https://github.com/zephyrproject-rtos/zephyr/issues/114936)）
  - [adi,ltc4286](../sensor_adi_accel_bioz_binding_reference/P021_adi_ltc4286.md#std-dtcompatible-adi-ltc4286)（[GitHub #105618](https://github.com/zephyrproject-rtos/zephyr/issues/105618)）
  - [adi,max30009](../compatible_binding_reference/P007_adi_max30009.md#std-dtcompatible-adi-max30009)（[GitHub #112988](https://github.com/zephyrproject-rtos/zephyr/issues/112988)）
  - [ams,tcs34725](../sensor_ams_aosong_bosch_binding_reference/P005_ams_tcs34725.md#std-dtcompatible-ams-tcs34725)（[GitHub #118531](https://github.com/zephyrproject-rtos/zephyr/issues/118531)）
  - [bflb,tsen](../sensor_ams_aosong_bosch_binding_reference/P023_bflb_tsen.md#std-dtcompatible-bflb-tsen)（[GitHub #107717](https://github.com/zephyrproject-rtos/zephyr/issues/107717)）
  - [cfsensor,xgzp68xxd](../sensor_bosch_broadcom_espressif_binding_reference/P027_cfsensor_xgzp68xxd.md#std-dtcompatible-cfsensor-xgzp68xxd)（[GitHub #109675](https://github.com/zephyrproject-rtos/zephyr/issues/109675)）
  - [hamamatsu,s9706](../sensor_espressif_honeywell_invensense_binding_reference/P007_hamamatsu_s9706.md#std-dtcompatible-hamamatsu-s9706)（[GitHub #107607](https://github.com/zephyrproject-rtos/zephyr/issues/107607)）
  - [invensense,icm56622](../compatible_binding_reference/P045_invensense_icm56622.md#std-dtcompatible-invensense-icm56622)（[GitHub #112362](https://github.com/zephyrproject-rtos/zephyr/issues/112362)）
  - [invensense,icm56686](../compatible_binding_reference/P046_invensense_icm56686.md#std-dtcompatible-invensense-icm56686)（[GitHub #112362](https://github.com/zephyrproject-rtos/zephyr/issues/112362)）
  - [invensense,tad2144](../compatible_binding_reference/P048_invensense_tad2144.md#std-dtcompatible-invensense-tad2144)（[GitHub #107994](https://github.com/zephyrproject-rtos/zephyr/issues/107994)）
  - [maxim,max30102](../sensor_liteon_maxim_temperature_binding_reference/P018_maxim_max30102.md#std-dtcompatible-maxim-max30102)（[GitHub #108697](https://github.com/zephyrproject-rtos/zephyr/issues/108697)）
  - [maxim,max31826](../sensor_liteon_maxim_temperature_binding_reference/P021_maxim_max31826.md#std-dtcompatible-maxim-max31826)（[GitHub #112398](https://github.com/zephyrproject-rtos/zephyr/issues/112398)）
  - [meas,htu21d](../sensor_liteon_maxim_temperature_binding_reference/P028_meas_htu21d.md#std-dtcompatible-meas-htu21d)（[GitHub #106318](https://github.com/zephyrproject-rtos/zephyr/issues/106318)）
  - [meas,htu31d](../sensor_liteon_maxim_temperature_binding_reference/P029_meas_htu31d.md#std-dtcompatible-meas-htu31d)（[GitHub #107532](https://github.com/zephyrproject-rtos/zephyr/issues/107532)）
  - [meas,ms5637](../sensor_microchip_nordic_nxp_binding_reference/P002_meas_ms5637.md#std-dtcompatible-meas-ms5637)（[GitHub #106344](https://github.com/zephyrproject-rtos/zephyr/issues/106344)）
  - [microchip,pac194x](../sensor_microchip_nordic_nxp_binding_reference/P011_microchip_pac194x.md#std-dtcompatible-microchip-pac194x)（[GitHub #105902](https://github.com/zephyrproject-rtos/zephyr/issues/105902)）
  - [nordic,nrf-vbat](../sensor_microchip_nordic_nxp_binding_reference/P024_nordic_nrf-vbat.md#std-dtcompatible-nordic-nrf-vbat)（[GitHub #106102](https://github.com/zephyrproject-rtos/zephyr/issues/106102)）
  - [nxp,mcux-eqdc](../sensor_nxp_qdec_optical_binding_reference/P006_nxp_mcux-eqdc.md#std-dtcompatible-nxp-mcux-eqdc)（[GitHub #111927](https://github.com/zephyrproject-rtos/zephyr/issues/111927)）
  - [plantower,pmsa003i](../sensor_nxp_qdec_optical_binding_reference/P028_plantower_pmsa003i.md#std-dtcompatible-plantower-pmsa003i)（[GitHub #113377](https://github.com/zephyrproject-rtos/zephyr/issues/113377)）
  - [raspberrypi,bcm283x-vc-thermal](../sensor_realtek_rohm_sensirion_binding_reference/P002_raspberrypi_bcm283x-vc-thermal.md#std-dtcompatible-raspberrypi-bcm283x-vc-thermal)（[GitHub #110192](https://github.com/zephyrproject-rtos/zephyr/issues/110192)）
  - [realtek,bee-aon-qdec](../sensor_realtek_rohm_sensirion_binding_reference/P004_realtek_bee-aon-qdec.md#std-dtcompatible-realtek-bee-aon-qdec)（[GitHub #105129](https://github.com/zephyrproject-rtos/zephyr/issues/105129)）
  - [realtek,bee-basic-qdec](../sensor_realtek_rohm_sensirion_binding_reference/P005_realtek_bee-basic-qdec.md#std-dtcompatible-realtek-bee-basic-qdec)（[GitHub #105129](https://github.com/zephyrproject-rtos/zephyr/issues/105129)）
  - [realtek,bee-qdec](../sensor_realtek_rohm_sensirion_binding_reference/P006_realtek_bee-qdec.md#std-dtcompatible-realtek-bee-qdec)（[GitHub #105129](https://github.com/zephyrproject-rtos/zephyr/issues/105129)）
  - [sensylink,cht8315](../sensor_realtek_rohm_sensirion_binding_reference/P029_sensylink_cht8315.md#std-dtcompatible-sensylink-cht8315)（[GitHub #106391](https://github.com/zephyrproject-rtos/zephyr/issues/106391)）
  - [silabs,emu-temp](../sensor_silabs_st_industrial_binding_reference/P001_silabs_emu-temp.md#std-dtcompatible-silabs-emu-temp)（[GitHub #120576](https://github.com/zephyrproject-rtos/zephyr/issues/120576)）
  - [st,stm32-vddcore](../sensor_st_ti_power_capacitance_binding_reference/P002_st_stm32-vddcore.md#std-dtcompatible-st-stm32-vddcore)（[GitHub #108053](https://github.com/zephyrproject-rtos/zephyr/issues/108053)）
  - [st,vl53l5cx](../sensor_st_ti_power_capacitance_binding_reference/P009_st_vl53l5cx.md#std-dtcompatible-st-vl53l5cx)（[GitHub #105238](https://github.com/zephyrproject-rtos/zephyr/issues/105238)）
  - [ti,fdc1004](../sensor_st_ti_power_capacitance_binding_reference/P012_ti_fdc1004.md#std-dtcompatible-ti-fdc1004)（[GitHub #107233](https://github.com/zephyrproject-rtos/zephyr/issues/107233)）
  - [ti,tmp451](../sensor_ti_vishay_wurth_sensing_binding_reference/P011_ti_tmp451.md#std-dtcompatible-ti-tmp451)（[GitHub #108384](https://github.com/zephyrproject-rtos/zephyr/issues/108384)）
  - [zephyr,flow-meter](../sensor_ti_vishay_wurth_sensing_binding_reference/P029_zephyr_flow-meter.md#std-dtcompatible-zephyr-flow-meter)（[GitHub #111366](https://github.com/zephyrproject-rtos/zephyr/issues/111366)）
  - [zephyr,generic-emul-sensor](../hardware/P533_通用仿真传感器绑定.md#dtbinding-zephyr-generic-emul-sensor)（[GitHub #115609](https://github.com/zephyrproject-rtos/zephyr/issues/115609)）
  - [zephyr,native-linux-temp](../sensor_ti_vishay_wurth_sensing_binding_reference/P030_zephyr_native-linux-temp.md#std-dtcompatible-zephyr-native-linux-temp)（[GitHub #114563](https://github.com/zephyrproject-rtos/zephyr/issues/114563)）
- 串行控制器（Serial Controller）


  - [elan,em32-uart](../uart_adi_arm_atmel_binding_reference/P018_elan_em32-uart.md#std-dtcompatible-elan-em32-uart)（[GitHub #103037](https://github.com/zephyrproject-rtos/zephyr/issues/103037)）
  - [infineon,asclin-uart](../uart_espressif_infineon_microchip_binding_reference/P007_infineon_asclin-uart.md#std-dtcompatible-infineon-asclin-uart)（[GitHub #107516](https://github.com/zephyrproject-rtos/zephyr/issues/107516)）
  - [mediatek,mt8188-uart](../uart_espressif_infineon_microchip_binding_reference/P016_mediatek_mt8188-uart.md#std-dtcompatible-mediatek-mt8188-uart)（[GitHub #118658](https://github.com/zephyrproject-rtos/zephyr/issues/118658)）
  - [microchip,uart-g1](../uart_espressif_infineon_microchip_binding_reference/P020_microchip_uart-g1.md#std-dtcompatible-microchip-uart-g1)（[GitHub #114034](https://github.com/zephyrproject-rtos/zephyr/issues/114034)）
  - [nxp,lpc84x-uart](../uart_microchip_nordic_nxp_binding_reference/P016_nxp_lpc84x-uart.md#std-dtcompatible-nxp-lpc84x-uart)（[GitHub #105928](https://github.com/zephyrproject-rtos/zephyr/issues/105928)）
  - [renesas,rx-uart-sci-b](../uart_raspberrypi_realtek_renesas_binding_reference/P011_renesas_rx-uart-sci-b.md#std-dtcompatible-renesas-rx-uart-sci-b)（[GitHub #118284](https://github.com/zephyrproject-rtos/zephyr/issues/118284)）
  - [shakti,uart](../uart_silabs_stm32_ti_binding_reference/P002_shakti_uart.md#std-dtcompatible-shakti-uart)（[GitHub #113000](https://github.com/zephyrproject-rtos/zephyr/issues/113000)）
  - [snps,dw-apb-uart](../uart_silabs_stm32_ti_binding_reference/P011_snps_dw-apb-uart.md#std-dtcompatible-snps-dw-apb-uart)（[GitHub #120368](https://github.com/zephyrproject-rtos/zephyr/issues/120368)）
  - [ti,tiva-c-uart](../uart_ti_wch_virtual_binding_reference/P004_ti_tiva-c-uart.md#std-dtcompatible-ti-tiva-c-uart)（[GitHub #110025](https://github.com/zephyrproject-rtos/zephyr/issues/110025)）
  - [wch,ch5xx-uart](../uart_ti_wch_virtual_binding_reference/P005_wch_ch5xx-uart.md#std-dtcompatible-wch-ch5xx-uart)（[GitHub #111171](https://github.com/zephyrproject-rtos/zephyr/issues/111171)）
  - [wch,sdi-console](../uart_ti_wch_virtual_binding_reference/P006_wch_sdi-console.md#std-dtcompatible-wch-sdi-console)（[GitHub #109777](https://github.com/zephyrproject-rtos/zephyr/issues/109777)）
- 系统管理总线（SMbus）


  - [ite,it51xxx-smbus](../i3c_smbus_binding_reference/P012_ite_it51xxx-smbus.md#std-dtcompatible-ite-it51xxx-smbus)（[GitHub #114832](https://github.com/zephyrproject-rtos/zephyr/issues/114832)）
- 串行外设接口（SPI）


  - [microchip,flexcom-g1-spi](../spi_microchip_nordic_nxp_binding_reference/P006_microchip_flexcom-g1-spi.md#std-dtcompatible-microchip-flexcom-g1-spi)（[GitHub #107467](https://github.com/zephyrproject-rtos/zephyr/issues/107467)）
  - [nuvoton,numaker-usci-spi](../spi_microchip_nordic_nxp_binding_reference/P017_nuvoton_numaker-usci-spi.md#std-dtcompatible-nuvoton-numaker-usci-spi)（[GitHub #109123](https://github.com/zephyrproject-rtos/zephyr/issues/109123)）
  - [nxp,kinetis-l-spi](../spi_flexspi_nxp_renesas_binding_reference/P002_nxp_kinetis-l-spi.md#std-dtcompatible-nxp-kinetis-l-spi)（[GitHub #116378](https://github.com/zephyrproject-rtos/zephyr/issues/116378)）
  - [realtek,ameba-spi](../spi_flexspi_nxp_renesas_binding_reference/P011_realtek_ameba-spi.md#std-dtcompatible-realtek-ameba-spi)（[GitHub #108234](https://github.com/zephyrproject-rtos/zephyr/issues/108234)）
  - [realtek,bee-spi](../spi_flexspi_nxp_renesas_binding_reference/P012_realtek_bee-spi.md#std-dtcompatible-realtek-bee-spi)（[GitHub #104958](https://github.com/zephyrproject-rtos/zephyr/issues/104958)）
  - [realtek,rts5817-spi](../spi_flexspi_nxp_renesas_binding_reference/P013_realtek_rts5817-spi.md#std-dtcompatible-realtek-rts5817-spi)（[GitHub #106346](https://github.com/zephyrproject-rtos/zephyr/issues/106346)）
  - [renesas,rz-spi-b](../spi_flexspi_nxp_renesas_binding_reference/P021_renesas_rz-spi-b.md#std-dtcompatible-renesas-rz-spi-b)（[GitHub #107073](https://github.com/zephyrproject-rtos/zephyr/issues/107073)）
  - [ti,mspm0-spi](../spi_stm32_ti_xilinx_binding_reference/P017_ti_mspm0-spi.md#std-dtcompatible-ti-mspm0-spi)（[GitHub #94726](https://github.com/zephyrproject-rtos/zephyr/issues/94726)）
  - [virtio,spi](../hardware/P592_VirtIO_SPI控制器绑定.md#dtbinding-virtio-spi)（[GitHub #115010](https://github.com/zephyrproject-rtos/zephyr/issues/115010)）
  - [xlnx,zynqmp-qspi-1.0](../spi_stm32_ti_xilinx_binding_reference/P021_xlnx_zynqmp-qspi-1.0.md#std-dtcompatible-xlnx-zynqmp-qspi-1.0)（[GitHub #88466](https://github.com/zephyrproject-rtos/zephyr/issues/88466)）
- 系统控制器（System Controller）


  - [aesc,syscon](../edac_syscon_binding_reference/P006_aesc_syscon.md#std-dtcompatible-aesc-syscon)（[GitHub #116703](https://github.com/zephyrproject-rtos/zephyr/issues/116703)）
- 转速计（Tachometer）


  - [ene,kb106x-tach](../auxdisplay_iio_tach_binding_reference/P013_ene_kb106x-tach.md#std-dtcompatible-ene-kb106x-tach)（[GitHub #106739](https://github.com/zephyrproject-rtos/zephyr/issues/106739)）
- 定时器（Timer）


  - [amd,xps-timer-1.00.a](../system_timer_binding_reference/P004_amd_xps-timer-1.00.a.md#std-dtcompatible-amd-xps-timer-1.00.a)（[GitHub #113123](https://github.com/zephyrproject-rtos/zephyr/issues/113123)）
  - [infineon,aurix-stm](../mcu_timer_binding_reference/P006_infineon_aurix-stm.md#std-dtcompatible-infineon-aurix-stm)（[GitHub #107516](https://github.com/zephyrproject-rtos/zephyr/issues/107516)）
  - [microchip,pit-g1-timer](../microchip_nordic_nxp_realtek_timer_binding_reference/P001_microchip_pit-g1-timer.md#std-dtcompatible-microchip-pit-g1-timer)（[GitHub #114034](https://github.com/zephyrproject-rtos/zephyr/issues/114034)）
  - [qcom,hvm-timer](../mcu_timer_binding_reference/P013_qcom_hvm-timer.md#std-dtcompatible-qcom-hvm-timer)（[GitHub #107122](https://github.com/zephyrproject-rtos/zephyr/issues/107122)）
  - [st,stm32u5-lptim](../stm32_ti_silabs_timer_binding_reference/P009_st_stm32u5-lptim.md#std-dtcompatible-st-stm32u5-lptim)（[GitHub #112400](https://github.com/zephyrproject-rtos/zephyr/issues/112400)）
  - [ti,am26-rtitimer](../stm32_ti_silabs_timer_binding_reference/P011_ti_am26-rtitimer.md#std-dtcompatible-ti-am26-rtitimer)（[GitHub #102545](https://github.com/zephyrproject-rtos/zephyr/issues/102545)）
- 通用串行总线（USB）


  - [brcm,bcm2835-usb](../usb_controller_binding_reference/P008_brcm_bcm2835-usb.md#std-dtcompatible-brcm-bcm2835-usb)（[GitHub #110701](https://github.com/zephyrproject-rtos/zephyr/issues/110701)）
  - [espressif,esp32-usb-otg-hs](../usb_controller_binding_reference/P011_espressif_esp32-usb-otg-hs.md#std-dtcompatible-espressif-esp32-usb-otg-hs)（[GitHub #111508](https://github.com/zephyrproject-rtos/zephyr/issues/111508)）
  - [infineon,usbhs](../usb_controller_binding_reference/P012_infineon_usbhs.md#std-dtcompatible-infineon-usbhs)（[GitHub #106841](https://github.com/zephyrproject-rtos/zephyr/issues/106841)）
  - [infineon,xmc4xxx-usb](../usb_controller_binding_reference/P013_infineon_xmc4xxx-usb.md#std-dtcompatible-infineon-xmc4xxx-usb)（[GitHub #113279](https://github.com/zephyrproject-rtos/zephyr/issues/113279)）
  - [ite,it51xxx-usb](../usb_controller_binding_reference/P014_ite_it51xxx-usb.md#std-dtcompatible-ite-it51xxx-usb)（[GitHub #111002](https://github.com/zephyrproject-rtos/zephyr/issues/111002)）
  - [microchip,udphs-g1-udc](../usb_controller_binding_reference/P017_microchip_udphs-g1-udc.md#std-dtcompatible-microchip-udphs-g1-udc)（[GitHub #99620](https://github.com/zephyrproject-rtos/zephyr/issues/99620)）
  - [nordic,nrf-usbhs](../usb_soc_binding_reference/P003_nordic_nrf-usbhs.md#std-dtcompatible-nordic-nrf-usbhs)（[GitHub #117567](https://github.com/zephyrproject-rtos/zephyr/issues/117567)）
  - [nordic,nrf-usbhs-bc12](../usb_controller_binding_reference/P019_nordic_nrf-usbhs-bc12.md#std-dtcompatible-nordic-nrf-usbhs-bc12)（[GitHub #106759](https://github.com/zephyrproject-rtos/zephyr/issues/106759)）
  - [nordic,nrf-usbhs-phy-type1](../usb_controller_binding_reference/P020_nordic_nrf-usbhs-phy-type1.md#std-dtcompatible-nordic-nrf-usbhs-phy-type1)（[GitHub #117567](https://github.com/zephyrproject-rtos/zephyr/issues/117567)）
  - [nordic,nrf-usbhs-phy-type2](../usb_soc_binding_reference/P001_nordic_nrf-usbhs-phy-type2.md#std-dtcompatible-nordic-nrf-usbhs-phy-type2)（[GitHub #117567](https://github.com/zephyrproject-rtos/zephyr/issues/117567)）
  - [renesas,ra-uhc](../usb_soc_binding_reference/P017_renesas_ra-uhc.md#std-dtcompatible-renesas-ra-uhc)（[GitHub #82730](https://github.com/zephyrproject-rtos/zephyr/issues/82730)）
- 视频（Video）


  - [nxp,flexio-camera](../video_camera_endpoint_binding_reference/P007_nxp_flexio-camera.md#std-dtcompatible-nxp-flexio-camera)（[GitHub #109382](https://github.com/zephyrproject-rtos/zephyr/issues/109382)）
  - [nxp,jpegdec](../video_camera_endpoint_binding_reference/P009_nxp_jpegdec.md#std-dtcompatible-nxp-jpegdec)（[GitHub #101883](https://github.com/zephyrproject-rtos/zephyr/issues/101883)）
  - [nxp,pngdec](../video_camera_endpoint_binding_reference/P011_nxp_pngdec.md#std-dtcompatible-nxp-pngdec)（[GitHub #109973](https://github.com/zephyrproject-rtos/zephyr/issues/109973)）
  - [zephyr,native-sim-video-fifo](../video_st_sony_emulation_binding_reference/P008_zephyr_native-sim-video-fifo.md#std-dtcompatible-zephyr-native-sim-video-fifo)（[GitHub #119658](https://github.com/zephyrproject-rtos/zephyr/issues/119658)）
- 唤醒控制器（Wakeup Controller）


  - [nxp,sleepcon-wuc](../power_state_wakeup_binding_reference/P007_nxp_sleepcon-wuc.md#std-dtcompatible-nxp-sleepcon-wuc)（[GitHub #113447](https://github.com/zephyrproject-rtos/zephyr/issues/113447)）
  - [nxp,wuc-wuu](../power_state_wakeup_binding_reference/P008_nxp_wuc-wuu.md#std-dtcompatible-nxp-wuc-wuu)（[GitHub #100866](https://github.com/zephyrproject-rtos/zephyr/issues/100866)）
- 看门狗（Watchdog）


  - [arm,crsas-ma2-watchdog](../watchdog_binding_reference/P006_arm_crsas-ma2-watchdog.md#std-dtcompatible-arm-crsas-ma2-watchdog)（[GitHub #112700](https://github.com/zephyrproject-rtos/zephyr/issues/112700)）
  - [m5stack,m5pm1-wdt](../soc_pmic_watchdog_binding_reference/P009_m5stack_m5pm1-wdt.md#std-dtcompatible-m5stack-m5pm1-wdt)（[GitHub #109961](https://github.com/zephyrproject-rtos/zephyr/issues/109961)）
  - [nordic,npm10xx-wdt](../soc_pmic_watchdog_binding_reference/P012_nordic_npm10xx-wdt.md#std-dtcompatible-nordic-npm10xx-wdt)（[GitHub #109381](https://github.com/zephyrproject-rtos/zephyr/issues/109381)）
  - [nordic,nrf-gswdt](../nxp_nordic_nuvoton_watchdog_binding_reference/P001_nordic_nrf-gswdt.md#std-dtcompatible-nordic-nrf-gswdt)（[GitHub #110067](https://github.com/zephyrproject-rtos/zephyr/issues/110067)）
  - [nuvoton,numaker-wdt](../nxp_nordic_nuvoton_watchdog_binding_reference/P004_nuvoton_numaker-wdt.md#std-dtcompatible-nuvoton-numaker-wdt)（[GitHub #105247](https://github.com/zephyrproject-rtos/zephyr/issues/105247)）
  - [realtek,ameba-watchdog](../realtek_renesas_silabs_watchdog_binding_reference/P001_realtek_ameba-watchdog.md#std-dtcompatible-realtek-ameba-watchdog)（[GitHub #106672](https://github.com/zephyrproject-rtos/zephyr/issues/106672)）
  - [realtek,bee-core-wdt](../realtek_renesas_silabs_watchdog_binding_reference/P002_realtek_bee-core-wdt.md#std-dtcompatible-realtek-bee-core-wdt)（[GitHub #107021](https://github.com/zephyrproject-rtos/zephyr/issues/107021)）
  - [silabs,wdog](../realtek_renesas_silabs_watchdog_binding_reference/P013_silabs_wdog.md#std-dtcompatible-silabs-wdog)（[GitHub #117617](https://github.com/zephyrproject-rtos/zephyr/issues/117617)）
  - [ti,mspm0-watchdog](../stm32_ti_xilinx_watchdog_binding_reference/P007_ti_mspm0-watchdog.md#std-dtcompatible-ti-mspm0-watchdog)（[GitHub #95304](https://github.com/zephyrproject-rtos/zephyr/issues/95304)）
  - [xen,watchdog](../stm32_ti_xilinx_watchdog_binding_reference/P010_xen_watchdog.md#std-dtcompatible-xen-watchdog)（[GitHub #117564](https://github.com/zephyrproject-rtos/zephyr/issues/117564)）
- 无线局域网（Wi-Fi）


  - [bflb,wifi4](../wifi_esp_hosted_airoc_binding_reference/P002_bflb_wifi4.md#std-dtcompatible-bflb-wifi4)（[GitHub #112911](https://github.com/zephyrproject-rtos/zephyr/issues/112911)）
  - [bflb,wifi6](../wifi_esp_hosted_airoc_binding_reference/P003_bflb_wifi6.md#std-dtcompatible-bflb-wifi6)（[GitHub #113078](https://github.com/zephyrproject-rtos/zephyr/issues/113078)）
  - [espressif,esp-hosted-mcu](../compatible_binding_reference/P035_espressif_esp-hosted-mcu.md#std-dtcompatible-espressif-esp-hosted-mcu)（[GitHub #114532](https://github.com/zephyrproject-rtos/zephyr/issues/114532)）
  - [espressif,esp-hosted-mcu-wifi](../wifi_esp_hosted_airoc_binding_reference/P006_espressif_esp-hosted-mcu-wifi.md#std-dtcompatible-espressif-esp-hosted-mcu-wifi)（[GitHub #114532](https://github.com/zephyrproject-rtos/zephyr/issues/114532)）
  - [realtek,ameba-wifi](../wifi_nordic_nxp_simulation_binding_reference/P011_realtek_ameba-wifi.md#std-dtcompatible-realtek-ameba-wifi)（[GitHub #105614](https://github.com/zephyrproject-rtos/zephyr/issues/105614)）
  - [st,st67w611m1](../wifi_nordic_nxp_simulation_binding_reference/P013_st_st67w611m1.md#std-dtcompatible-st-st67w611m1)（[GitHub #111583](https://github.com/zephyrproject-rtos/zephyr/issues/111583)）
  - [zephyr,native-sim-wifi](../wifi_nordic_nxp_simulation_binding_reference/P014_zephyr_native-sim-wifi.md#std-dtcompatible-zephyr-native-sim-wifi)（[GitHub #110681](https://github.com/zephyrproject-rtos/zephyr/issues/110681)）
  - [zephyr,wifi-hwsim](../wifi_nordic_nxp_simulation_binding_reference/P015_zephyr_wifi-hwsim.md#std-dtcompatible-zephyr-wifi-hwsim)（[GitHub #111236](https://github.com/zephyrproject-rtos/zephyr/issues/111236)）

<a id="new-samples"></a>

## 新增示例（New Samples）


- [ADI MAX32 GPIO唤醒（Wakeup）](../board_samples/P042_ADI_MAX32的GPIO唤醒.md#adi-gpio-wakeup)
- [ADI电源模式（Power Modes）](../board_samples/P043_ADI电源模式.md#adi-pm)
- [断言（Assertions）](../observability/P063_断言示例.md#assert)
- [AutAnalog ADC有限冲激响应滤波器与FIFO（FIR + FIFO）](../board_samples/P061_AutAnalog的ADC_FIR与FIFO.md#autanalog_fir_fifo)
- [B-M2MEM-PACK1扩展板（Shield）](../shield_samples/P001_B_M2MEM_PACK1存储扩展板.md#b-m2mem-pack1)
- [通用音频配置文件（CAP）切换（Handover）](../bluetooth_samples/P071_CAP切换.md#bluetooth_cap_handover)
- [蜂鸣器音调（Buzzer Tone）](../hardware/P143_蜂鸣器音调示例.md#buzzer-tone)
- [时钟监测频率检查（Clock Monitor Frequency Check）](../hardware/P117_时钟频率检查示例.md#clock-monitor-check-freq)
- [时钟监测频率计（Clock Monitor Frequency Meter）](../hardware/P118_时钟频率测量示例.md#clock-monitor-measure-freq)
- [CoAP TCP客户端（Client）](../networking/P069_CoAP_TCP客户端示例.md#coap-client-tcp)
- [调色板显示（Color Palette Display）](../hardware/P179_调色板显示示例.md#color-palette)
- [通过Shell执行UDP核心转储（Coredump）](../observability/P064_UDP核心转储命令示例.md#coredump-udp-demo-shell)
- [带远程Shell的CoreSight系统跟踪宏单元（STM）](../board_samples/P024_CoreSight_STM远程Shell.md#coresight_stm_shell)
- [CPU频率热限制（Thermal Cap）](../power/P022_CPU调频温度上限示例.md#cpu_freq_thermal_cap)
- [CPU调频时序噪声示例（Timing Noise Sample）](../power/P021_时序噪声CPU调频示例.md#cpu_freq_timing_noise)
- [CS40L26触觉反馈驱动（Haptic Driver）](../hardware/P160_CS40L26触觉驱动示例.md#cs40l26)
- [数字可寻址照明接口（Digital Addressable Lighting Interface，DALI）](../driver_samples/P036_DALI照明接口示例.md#dali)
- [DHCPv6前缀委派（Prefix Delegation）](../networking/P036_DHCPv6前缀委派示例.md#dhcpv6-pd)
- [像素处理加速器（Pixel Processing Accelerator）](../board_samples/P098_像素处理加速器.md#esp32-ppa-srm)
- [ESP32正交解码器（Qdec）逐单元阈值触发](../board_samples/P097_正交解码器阈值触发.md#esp32-qdec-trigger)
- [ESP-NOW无线通信协议](../board_samples/P107_ESP_NOW无线通信.md#espnow)
- [FIDO2身份验证器（Authenticator）](../basic_samples/P057_FIDO2认证器示例.md#fido2)
- [流量计（Flow Meter）](../sensors/P078_流量计示例.md#flow-meter)
- [通过HTTP进行固件空中升级（Firmware Over-the-Air）](../firmware_update/P023_HTTP固件升级示例.md#fota-http)
- [系统关闭（System Off）：MCXE31B待机](../board_samples/P065_MCXE31B待机与唤醒.md#frdm-mcxe31b-system-off)
- [哈希硬件基准测试（Hash HW Benchmark）](../crypto/P028_散列性能测试示例.md#hash-bench)
- [I2C-Tiny-USB桥接（Bridge）](../usb/P068_USB转I2C桥接示例.md#i2c-tiny-usb)
- [通过LIN控制NCV7430 LED控制器](../driver_samples/P034_LIN灯光控制器示例.md#lin-ncv7430)
- [NCV7430模拟LIN响应器（Mock Responder）](../driver_samples/P035_LIN模拟响应节点示例.md#lin-ncv7430-responder)
- [LoRa占空比（Duty Cycle）](../driver_samples/P015_LoRa占空比示例.md#lora-duty-cycle)
- [LP586x LED矩阵（LED Matrix）](../hardware/P196_LP586x灯矩阵示例.md#lp586x)
- [模型上下文协议服务器入门（MCP Server Hello World）](../networking/P181_MCP服务器入门示例.md#mcp-server-hello-world)
- [带充电器、电量计及稳压器的多功能设备（Multi-Function Device，MFD）](../hardware/P122_多功能电源设备示例.md#mfd_charger)
- [RT700系统关闭（System Off）](../board_samples/P071_RT700系统关闭.md#mimxrt700_evk_system_off)
- [MSPI吞吐量性能测试（Throughput Performance Test）](../driver_samples/P024_MSPI吞吐量示例.md#mspi-throughput)
- [实时传输协议（RTP）](../networking/P142_RTP发送示例.md#net-rtp)
- [Nordic低功耗蓝牙（Bluetooth LE）活动期间写入Flash](../board_samples/P026_蓝牙活动期间写入Nordic闪存.md#nordic-flash)
- [nPM10xx用户信息配置寄存器（UICR）](../driver_samples/P044_nPM10xx_UICR示例.md#npm10xx_uicr)
- [NXP MCX挂起到RAM（Suspend-to-RAM）](../power/P052_NXP_MCX挂起到RAM示例.md#nxp_mcx_s2ram)
- [NXP MCX系统关闭（System Off）](../board_samples/P067_NXP_MCX系统关闭.md#nxp_mcx_system_off)
- [RT700 EVK双核电源管理（Dual-core Power Management）](../board_samples/P070_RT700双核电源管理.md#nxp_rt700_dual_core_pm)
- [NXP SmartDMA内存到内存传输（Memory-to-memory）](../board_samples/P073_SmartDMA内存到内存传输.md#nxp_smartdma_mem_to_mem)
- [对象核心（Object Cores）](../basic_samples/P027_对象核心示例.md#object_cores)
- [对象监视器（Object Monitor）](../basic_samples/P028_对象监视器示例.md#object_monitor)
- [精确定时（Precision Timing）](../basic_samples/P043_精确定时示例.md#precision_timing)
- [脉冲输入输出字节传输（pulse_io Byte Transfer）](../driver_samples/P041_脉冲IO字节传输示例.md#pulse_io_byte_transfer)
- [多单元正交解码器（Multi-unit Quadrature Decoder）](../sensors/P083_多单元正交解码器示例.md#qdec_multi)
- [QUIC回显客户端（Echo Client）](../networking/P145_QUIC回显客户端.md#quic-client-echo)
- [QUIC回显服务器（Echo Server）](../networking/P146_QUIC回显服务端.md#quic-service-echo)
- [RISC-V高级中断架构（AIA）对称多处理（SMP）UART回显](../driver_samples/P064_RISC_V_AIA多处理器中断示例.md#riscv-aia-smp-uart-echo)
- [RISC-V高级中断架构（AIA）UART回显](../driver_samples/P063_RISC_V_AIA中断示例.md#riscv-aia-uart-echo)
- [树莓派开发板信息（Raspberry Pi Board Info）](../board_samples/P051_Raspberry_Pi板信息.md#rpi-board-info)
- [进程间通信服务（IPC Service）：RPMsg-Lite后端](../intercore_reference/P097_IPC服务RPMSG-Lite示例.md#rpmsg-lite)
- [RW612电源管理Flash检查（PM Flash Check）](../board_samples/P066_RW612低功耗Flash擦写检查.md#rw612_pm_flash_check)
- [简单网络时间协议服务器（SNTP Server）](../networking/P039_SNTP服务器示例.md#sntp-server)
- [SPI实时输入输出（RTIO）回环](../driver_samples/P003_SPI实时IO回环示例.md#spi-rtio-loopback)
- [安全外壳服务器及客户端（SSH Server and Client）](../networking/P221_SSH服务端与客户端示例.md#ssh-server-client)
- [采用隧道磁阻（Tunnel Magneto Resistance，TMR）的TDK集成角度传感器](../sensors/P084_TDK_TAD2144隧道磁阻角度传感器示例.md#tad2144)
- [NXP Neutron上的TensorFlow Lite微控制器版本（TensorFlow Lite for Microcontrollers）](../board_samples/P080_Neutron微控制器机器学习推理.md#tflite-neutron)
- [可信固件M（TF-M）固件更新](../tfm/P010_TFM固件更新示例.md#tfm_fwu)
- [TM6605 触觉驱动器](../hardware/P163_TM6605触觉驱动示例.md#tm6605)
- [TMC6460电压模式（Voltage Mode）](../driver_samples/P049_TMC6460电压模式示例.md#tmc6460)
- [跟踪传感器流水线（Tracing a Sensor Pipeline）](../observability/P024_跟踪管线验证示例.md#tracing-pipeline)
- [时间敏感网络交换机（TSN Switch）](../networking/P124_TSN交换机示例.md#tsn-switch)
- [通过低功耗蓝牙（BLE）进行Wi-Fi配网（Provisioning）](../networking/P168_通过低功耗蓝牙配置WiFi.md#wifi-ble-provisioning)
- [Wi-Fi网状网络（Mesh）](../board_samples/P109_WiFi网状网络.md#wifi-mesh)
- [Wi-Fi网状网络IP（Mesh IP）](../board_samples/P110_WiFi网状网络IP通信.md#wifi-mesh-ip)
- [X-NUCLEO-IKS4A1扩展板：标准模式（模式1及I3C）](../hardware/P433_IKS4A1标准I3C示例.md#x-nucleo-iks4a1-std-i3c)
- [X-NUCLEO-PGEEZ1 M95P32扩展操作（Extended Operations）](../shield_samples/P023_PGEEZ1扩展存储操作.md#x-nucleo-pgeez1)
- [AXI时钟向导（Clocking Wizard）](../board_samples/P057_AXI时钟配置模块.md#xclk-wiz)
- [Zephyr内存存储（ZMS）周期计数验证（Cycle Count Verification）](../storage/P090_ZMS循环计数验证示例.md#zms-cycle-count)

<a id="libraries-subsystems"></a>

## 库与子系统（Libraries / Subsystems）


- 密码功能（Crypto）


  - 新增高级加密标准（AES）的密文反馈（CFB）及输出反馈（OFB）模式支持。
- Mbed TLS密码与TLS库


  - Mbed TLS更新到4.1.1，发行说明见此链接。（[此处](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-4.1.1)）
  - TF-PSA-Crypto更新到1.1.1，发行说明见此链接。（[此处](https://github.com/Mbed-TLS/TF-PSA-Crypto/releases/tag/tf-psa-crypto-1.1.1)）
  - 新增CONFIG_TF_PSA_CRYPTO_DISPATCH_DIR，使TF-PSA-Crypto可使用自定义密码操作分派（Dispatch）实现。采用能识别加速器的分派实现后，即可对密码操作进行硬件加速。
- 可信固件M（TF-M）


  - TF-M从2.2.2更新到2.3.1，发行说明见：


    - [https://trustedfirmware-m.readthedocs.io/en/latest/releases/2.3.0.html](https://trustedfirmware-m.readthedocs.io/en/latest/releases/2.3.0.html)
    - [https://trustedfirmware-m.readthedocs.io/en/tf-mv2.3.1/releases/2.3.1.html](https://trustedfirmware-m.readthedocs.io/en/tf-mv2.3.1/releases/2.3.1.html)
  - 将ZEPHYR_TOOLCHAIN_VARIANT设为zephyr/llvm后，现在可使用LLVM编译TF-M。
- 设备固件升级（DFU）


  - 新增[CONFIG_IMG_CUSTOM_SECTOR_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IMG_CUSTOM_SECTOR_SIZE)，使MCUboot可采用不同扇区大小，以缩小偏移交换（Swap-using-offset）的状态区域。
- 管理（Management）


  - 新增通过HTTP进行固件空中升级（[Firmware Over-the-Air over HTTP](https://docs.zephyrproject.org/latest/services/device_mgmt/fota_http.html#fota-http)）的库。该客户端通过HTTP或HTTPS将MCUboot镜像直接下载到次槽位，可选支持断点续传、跟随重定向、SHA-256校验及fota Shell命令。
- 远距离无线通信LoRa与LoRa广域网（LoRaWAN）


  - 新增原生LoRaWAN后端[CONFIG_LORA_MODULE_BACKEND_NATIVE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORA_MODULE_BACKEND_NATIVE)，直接在LoRa无线电驱动上实现LoRaWAN 1.0.x Class A，不依赖Semtech LoRaMac-node。目前支持EU868区域。
  - [`lora_modem_config.sync_word`](https://docs.zephyrproject.org/latest/doxygen/html/structlora__modem__config.html#af5ef0c5e3443a011d2ed6af3c95cc4db)
- 网络（Networking）


  - 新增卸载套接字本地端口跟踪[CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING)。卸载套接字在net_context层之外的卸载引擎中绑定，因此[net_context_port_in_use()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gad9350d40a884315ff9de4032a8d6ae71)此前无法发现它们。套接字层现在跟踪这些绑定，并提供net_socket_port_in_use()同时检查原生与卸载端口。mDNS探测端口选择及DNS服务发现（DNS-SD）服务检查改用该函数。
  - 精确时间协议（PTP）新增IEEE 802.3传输支持、数据包套接字接收时间戳及PTP Shell诊断。（[GitHub #106464](https://github.com/zephyrproject-rtos/zephyr/issues/106464)）
- 管理（Management）


  - 微控制器管理（MCUmgr）


    - 镜像管理客户端现在支持SHA-512镜像摘要，可在启用[CONFIG_MCUBOOT_BOOTLOADER_USES_SHA512](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_BOOTLOADER_USES_SHA512)的目标上列出镜像，并选择镜像进行测试或确认。
- 多媒体流水线（Multimedia Pipeline）


  - 引入实验性[多媒体流水线（Multimedia Pipeline，mpipe）](../services_overview/P012_多媒体流水线.md#mpipe)子系统，通过可复用的源、变换及接收端元素（Source / Transform / Sink）组成流水线，构建多媒体应用。应用可描述所需媒体流，无需自行驱动每个音频、视频或显示设备。
  - 基础插件提供与媒体类型无关的元素：能力过滤器（Caps Filter）、分流器（Tee）、队列（Queue），以及应用源与应用接收端（Application Source / Sink）。
  - 拓扑转储（Topology Dump）将流水线输出为Graphviz图；播放器（Player）通过工作线程及Shell驱动流水线。
- 网络（Networking）


  - 受限应用协议（CoAP）


    - <a id="index-6"></a>

      CoAP服务器接受[RFC 7641](https://datatracker.ietf.org/doc/html/rfc7641.html)允许的空令牌（Empty Token）观察注册，并以端点及该空令牌共同标识观察者。
  - 互联网组管理协议（IGMP）


    - <a id="index-7"></a>

      <a id="index-8"></a>

      按照[RFC 2236](https://datatracker.ietf.org/doc/html/rfc2236.html)及[RFC 3376](https://datatracker.ietf.org/doc/html/rfc3376.html)，主机现在响应特定组查询（Group-Specific Queries），在最大响应时间（Max Resp Time）范围内随机延迟响应，重传加入组时主动发送的报告，并在发现相应版本查询器时切换为IGMPv1或IGMPv2。报告发送次数由新选项[CONFIG_NET_IPV4_IGMP_ROBUSTNESS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_IGMP_ROBUSTNESS)决定。启用[CONFIG_NET_IPV4_IGMP_REQUIRE_ROUTER_ALERT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_IGMP_REQUIRE_ROUTER_ALERT)时，忽略不带IP路由器警报（Router Alert）选项的查询。
  - 多播侦听发现（MLD）


    - <a id="index-9"></a>

      <a id="index-10"></a>

      按照[RFC 2710](https://datatracker.ietf.org/doc/html/rfc2710.html)及[RFC 3810](https://datatracker.ietf.org/doc/html/rfc3810.html)，节点现在响应特定多播地址查询（Multicast Address Specific Queries），在最大响应延迟（Maximum Response Delay）范围内随机延迟响应，重传加入组时主动发送的报告，发现MLDv1查询器时切换到MLDv1，并丢弃缺少链路本地源地址或Router Alert选项的查询。不再为全节点组（All-nodes Group）发送报告；接口链路本地地址有效后，会重新报告全部组。报告发送次数由[CONFIG_NET_IPV6_MLD_ROBUSTNESS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_MLD_ROBUSTNESS)决定，禁用[CONFIG_NET_IPV6_MLD_V1_COMPAT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_MLD_V1_COMPAT)则忽略MLDv1消息。
- 安全存储（Secure Storage）


  - psa_its_get*()遇到身份验证失败或格式错误的条目时，现在返回PSA_ERROR_INVALID_SIGNATURE或PSA_ERROR_DATA_CORRUPT，替代PSA_ERROR_GENERIC_ERROR。
  - 修改条目的内部可信存储（ITS）操作现在串行执行；丢弃无法回读的条目时，记录警告。
  - 以data_size=0调用psa_its_get()时，现在报告条目是否存在且有效，不再始终返回PSA_SUCCESS。
- 精确定时（Precision Timing）


  - 引入实验性[精确定时（Precision Timing）](https://docs.zephyrproject.org/latest/kernel/precision_timing.html#precision-timing)机制，为PTP、gPTP及其他高分辨率时钟使用者提供可复用的带检查时间运算、时钟操作及比例积分（PI）控制。
- 视频（Video）


  - 引入视频子系统，承接此前视频驱动中的全部函数名称。
- Zephyr消息总线（Zbus）


  - [CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION)不再要求每个通道都有专用池；在调用[zbus_chan_set_msg_sub_pool()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga3f90d50f20e7779ef257676ac10da357)前，通道回退到共享池。
- 断言（__assert）

  > - 移除__ASSERT_ON定义。

<a id="devicetree"></a>

## 设备树（Devicetree）


- 节点现在可通过句柄（Phandle）引用子节点，而不会在依赖图中形成环或导致构建错误。新功能用法见[dependency-mode](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#dt-bindings-dependency-mode)。（[GitHub #108892](https://github.com/zephyrproject-rtos/zephyr/issues/108892)）


  - [`DT_NODELABEL_C_TOKEN`](../dt_identity_reference/P001_设备树节点标识宏.md#ga49b52b13e03f9a990795d2a36f608a09)
  - [`DT_NODELABEL_C_TOKEN_BY_IDX`](../dt_identity_reference/P001_设备树节点标识宏.md#gaa0b031b229787ad3642c2a93e5c15bd5)
- 绑定可用新的class:键声明设备类别成员关系，见类别（[Class](https://docs.zephyrproject.org/latest/build/dts/bindings-syntax.html#dt-bindings-class)），从而在构建时枚举某设备类别的全部节点：


  - [`DT_NODE_HAS_CLASS`](../dt_identity_reference/P002_设备树存在性与状态宏.md#ga5f93b6d849b8237c202e8aac25c1fb3d)
  - [`DT_HAS_CLASS_STATUS_OKAY`](../dt_identity_reference/P002_设备树存在性与状态宏.md#ga2d6233af945196a7bbd7b1ebee564eca)
  - [`DT_NUM_CLASS_STATUS_OKAY`](../dt_identity_reference/P002_设备树存在性与状态宏.md#ga07dff3a1ecc971516f0bea6db2faefa3)
  - [`DT_FOREACH_CLASS_STATUS_OKAY`](../dt_foreach_reference/P001_设备树遍历宏.md#gabdc4a38b13b22f7d5c3105c21e7dec05)
  - [`DT_FOREACH_CLASS_STATUS_OKAY_VARGS`](../dt_foreach_reference/P001_设备树遍历宏.md#gad3d809decfdd49a6326cb2b8134a750b)
  - Kconfig预处理函数$(dt_class_enabled,<class name>)。
- ADC Shell现在通过adc设备类别枚举控制器，替代硬编码compatible列表，因此也覆盖树外ADC驱动。
- I3C Shell现在通过i3c设备类别枚举控制器，替代硬编码compatible列表，因此也覆盖树外I3C驱动。

<a id="other-notable-changes"></a>

## 其他主要变更（Other Notable Changes）


- 模数转换器（ADC）


  - STM32 ADC驱动[st,stm32-adc](../hardware/P839_STM32模数转换器绑定.md#dtbinding-st-stm32-adc)启用[CONFIG_ADC_STM32_VREFINT_CALIBRATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_STM32_VREFINT_CALIBRATE)后，[adc_ref_internal()](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gad11845f5621d0b0d03da4b6484d79aa4)可能返回实测换算基准，而非设备树vref-mv。[st,stm32-vref](../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref)的io-channels属性指定的任意ADC均可执行测量，结果在整个SoC范围缓存。见迁移指南ADC章节。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - STM32G4 SoC的DTSI文件现在描述芯片实际具备的额外VREFINT输入：[st,stm32-vref](../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref)的vref3对应G491及以上型号的ADC3，vref4及vref5对应G473及以上型号的ADC4／ADC5。节点默认仍禁用，由开发板启用所需实例。ADC2没有VREFINT多路复用输入。
- 蓝牙（Bluetooth）


  - [CONFIG_BT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT)本身不再强制[CONFIG_SYSTEM_WORKQUEUE_PRIORITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_WORKQUEUE_PRIORITY)采用协作式优先级；仅向系统工作队列提交工作的组件才有此要求。因此，不包含这些组件的构建，例如驱动外部控制器的HCI原始镜像，可再次选择可抢占优先级。（[GitHub #119123](https://github.com/zephyrproject-rtos/zephyr/issues/119123)）
- 构建系统（Build System）


  - 最低CMake版本提高到3.28.0，Ubuntu 24.04 LTS软件包仓库中的CMake满足要求。发行版自带版本较旧时的处理方式，见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - 加固工具west build -t hardenconfig现在从经过模式验证的YAML数据库读取建议，替代CSV文件：配置文件定义位于scripts/kconfig/hardening.yaml，各子系统的hardening.yaml片段位于相关Kconfig文件旁。每条建议均包含在报告中展示的依据，并可引用CWE／CVE条目。建议分为base及strict配置文件，可通过-DHARDENCONFIG_PROFILE=选择；整数建议可表达最小／最大约束；提供JSON输出及失败退出码供CI使用；树外数据库可通过-DHARDENCONFIG_EXTRA_SOURCES=叠加。CI根据实际Kconfig树验证数据库，防止条目过时。（[加固工具（Hardening Tool）](../security/P005_安全加固工具.md#hardening)）
- 循环冗余校验（CRC）


  - 软件循环冗余校验（CRC）子系统、CRC驱动API及NXP CRC驱动新增CRC-32/MPEG-2支持，即[crc32_mpeg2()](../data_utilities/P003_CRC计算接口.md#gaee8a8a5c17b530efe9b331c5af97e2c8)／crc32_mpeg2_update。
- 内核（Kernel）


  - [对象核心框架（Object Core Framework）](../kernel/P048_内核对象核心.md#object-cores-api)不再将注册表状态保存在被跟踪对象内部。静态对象就地枚举，运行时初始化对象由有界注册表引用，因此内核对象可声明在栈上、嵌入随后释放的内存中或重新初始化，而不破坏注册表。栈存储中的对象不参与跟踪。
  - [CONFIG_SCHED_CPU_MASK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_CPU_MASK)不再依赖[CONFIG_SCHED_SIMPLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_SIMPLE)。三个调度器后端均支持CPU亲和性掩码：SCHED_SIMPLE为O(N)链表扫描，SCHED_SCALABLE为O(N)红黑树遍历，SCHED_MULTIQ为O(P·N)逐优先级桶扫描。各后端性能说明见更新后的[对称多处理（SMP）文档](https://docs.zephyrproject.org/latest/kernel/services/smp/smp.html#smp-cpu-mask)。
  - [CONFIG_SCHED_CPU_MASK_PIN_ONLY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_CPU_MASK_PIN_ONLY)现在同时在API边界cpu_mask_mod()及入队thread_runq()时，强制掩码仅含一个CPU位。PIN_ONLY模式下调用[k_thread_cpu_mask_clear()](../thread_core_reference/P001_线程公共接口.md#ga80b9c58df6600c7e79f16756c128f44c)、[k_thread_cpu_mask_enable_all()](../thread_core_reference/P001_线程公共接口.md#gaedcfeb0964ae72611791241580b2119d)或[k_thread_cpu_mask_disable()](../thread_core_reference/P001_线程公共接口.md#ga89e6c07ac112da75b2ef115d1a557d44)会触发断言失败。请用[k_thread_cpu_pin()](../thread_core_reference/P001_线程公共接口.md#gae9ebd9845e14ed02944ab9282a185c03)将线程重新分配到另一CPU。
- 定时器（Timer）


  - 启用[CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE)后，若停止时间基准会破坏[sys_clock_cycle_get_32()](../timer_reference/P086_系统时钟公共接口.md#ga42dcd1878309a82246dbfa26510f868a)／[sys_clock_cycle_get_64()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga25328a181bd0229ef5110c15e8452fc1)，驱动就不能仅因没有待处理超时而停止它；CPU运行时，这些函数必须持续计数。仅允许在[sys_clock_idle_enter()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaab6df10ce3054ee84921aa90a1bc53d1)中停止时间基准，此时保证后续调用[sys_clock_idle_exit()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga6ca2139000b8c75b1ed2c6c1f672ff79)。
  - 无周期节拍（Tickless）系统定时器驱动现在可基于共享实现头文件drivers/timer/system_timer_generic.h构建。该头文件统一处理此前各驱动自行实现的节拍记账：周期到节拍转换、通告基准、节拍对齐截止时刻，以及计数器回绕与范围处理。驱动可简化为少数以周期为单位的原语，即读取周期计数器和设置绝对比较触发。用法见迁移指南。（[GitHub #115844](https://github.com/zephyrproject-rtos/zephyr/issues/115844)）（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
- 网络（Networking）


  - DHCPv4客户端现在在所有放弃租约的路径上，均从接口移除租用地址、租约提供的DNS服务器及它安装的网关；请求被拒绝或地址被谢绝后，约等待10秒再重新启动。
- 无线局域网（Wi-Fi）


  - 移除samples/net/wifi/test_certs/rsa2k企业级测试证书，其私钥使用DES加密。请改用rsa2k_no_des。
  - 连接结果事件现在可通过[WIFI_STATUS_CONN_AUTH_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a008abc5c55c4ea7409f5b16be4f68a91)及[WIFI_STATUS_CONN_ASSOC_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8aeaccd303a2c836347555886f746b54eb)，区分接入点拒绝身份验证或关联；[wifi_status](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__status.html)携带导致失败的原始IEEE 802.11状态码及原因码。请求方（Supplicant）填写这些字段，Wi-Fi Shell在连接及断开结果中输出。（[GitHub #116704](https://github.com/zephyrproject-rtos/zephyr/issues/116704)）
  - ESP32 Wi-Fi驱动新增802.11k／v／r及多频段操作（MBO）支持，默认均关闭。[CONFIG_ESP32_WIFI_11KV_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_WIFI_11KV_SUPPORT)启用802.11k及802.11v；[CONFIG_ESP32_WIFI_MBO_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_WIFI_MBO_SUPPORT)在其基础上启用MBO；[CONFIG_ESP32_WIFI_11R_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_WIFI_11R_SUPPORT)启用802.11r。站点已关联时，wifi 11k及wifi 11v_btm_query命令现在可在ESP32使用。启用[CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_WIFI_SIGNAL_CHANGE_EVENT)后，连接的接入点信号变弱时产生[NET_EVENT_WIFI_SIGNAL_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8da47e9d3e594840fb7a7d59f45ea9ce)，供应用决定何时漫游。
  - wifi-tx-power-2g.yaml及wifi-tx-power-5g.yaml中的发送功率上限属性不再必填，并提供保守默认值，使尚未完成特性测量的开发板倾向于功率偏低，而非超过法规上限。已测得自身限制的开发板继续显式声明，因此现有开发板行为不变。
  - P2P新增设置本地设备名称及查询当前状态的Shell命令，由wifi_p2p_op中的WIFI_P2P_SET_DEV_NAME及WIFI_P2P_STATUS操作支持。wifi_p2p_params新增device_name及status成员，并新增WIFI_P2P_STATUS_BUF_SIZE缓冲区大小宏。
- MCU启动加载器（MCUboot）


  - [SB_CONFIG_BOOT_SIGNATURE_KEY_FILE](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOOT_SIGNATURE_KEY_FILE)现在接受逗号分隔的密钥文件列表，将每把密钥的公钥部分嵌入MCUboot。给出多把密钥时，MCUboot接受由其中任意一把签名的镜像。典型用途是开发启动加载器同时启动开发密钥与生产密钥签名的镜像，而生产启动加载器仅嵌入生产公钥。列表首项用于应用签名，其余项是仅用于验证的公钥。见二进制签名（[Signing Binaries](https://docs.zephyrproject.org/latest/build/signing/index.html#build-signing)）。
  - Espressif开发板在Sysbuild下不再强制仅覆盖（Overwrite-only）模式及无签名镜像。现在构建支持回滚的MCUboot偏移交换（Swap-using-offset）模式及RSA-2048签名应用，共享Espressif分区表也不再预留暂存分区（Scratch Partition）。见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
- 恩智浦（NXP）


  - NXP LPC的DTSI文件从平铺的dts/arm/nxp/lpc/目录，重组到按系列划分的lpc11u6x/、lpc51u68/、lpc54xxx/、lpc55xxx/及lpc84x/子目录。树外开发板包含路径的更新方法见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - NXP Kinetis的DTSI文件从平铺的dts/arm/nxp/kinetis/目录，重组到按系列划分的k2x/、k32lx/、k6x/、k8x/、ke1xf/、ke1xz/、kl2x/、kv5x/及kwx/子目录。树外开发板包含路径的更新方法见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - NXP MCX的DTSI文件从平铺的dts/arm/nxp/mcx/目录，重组到按系列划分的mcxa/、mcxc/、mcxe/、mcxl/、mcxn/及mcxw/子目录。树外开发板包含路径的更新方法见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - NXP i.MX RT的DTSI文件从平铺的dts/arm/nxp/imxrt/目录，重组到按系列划分的imxrt10xx/、imxrt11xx/、imxrt5xx/、imxrt6xx/、imxrt7xx/及imxrt118x/子目录。树外开发板包含路径的更新方法见迁移指南。（[迁移指南（Migration Guide）](../releases_guides/P007_迁移到Zephyr_4.5_工作草案.md#migration-4-5)）
  - NXP MCUX CTimer、GPT及LPTimer驱动新增计数器复位API支持。
  - 为NXP LPC55xx电源管理控制器（PMC）新增硬件信息（HWInfo）复位原因驱动。
- Arm


  - 以下开发板的非安全变体（Non-secure Variant）：

    [Arm Musca-S1](../boards_arm/P013_V2M_Musca-S1.md#v2m_musca_s1)（v2m_musca_s1/musca_s1/ns）已移除，因为TF-M移除了该板的平台支持。
  - 相应地，[Arm Musca-S1](../boards_arm/P013_V2M_Musca-S1.md#v2m_musca_s1)安全变体（v2m_musca_s1）也已弃用，以免部分支持造成混淆。

<a id="trusted-firmware-a"></a>

## 可信固件A（Trusted Firmware-A）


- 新增CONFIG_TFA_BUILD_FIP，用于配置固件镜像包（Firmware Image Package，FIP）生成。默认不生成FIP；可在prj.conf中设置CONFIG_TFA_BUILD_FIP=y启用，自定义开发板也可在其<board>_defconfig中设置。

## 译注

本页为Zephyr 4.5工作草案（Working Draft），内容仍可能变化。原文发布措辞按原样翻译并标注草案背景。安全编号、开发板目标、设备树compatible、代码和源码路径保留原始标识；不会将原文中的历史保密期说明作为当前状态承诺。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Zephyr 4.4 发行说明](P004_Zephyr_4.4_发行说明.md) · [本模块主线目录](../reading/releases_notes.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P004_Zephyr_4.4_发行说明.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)

</details>

<!-- reading-navigation:end -->
