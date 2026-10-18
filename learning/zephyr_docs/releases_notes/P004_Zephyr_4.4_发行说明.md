---
id: learning.zephyr-docs.releases-notes.page-4
title: Zephyr 4.4 发行说明
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/release-notes-4.4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zephyr-4-4-0"></a>

<a id="zephyr-4-4"></a>

# 第4章\_Zephyr 4.4.0版本

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/release-notes-4.4.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Zephyr 4.4.0版本现已发布。

本版本的主要增强包括：

开放RISC架构（OpenRISC）支持

Zephyr现在支持[OpenRISC架构](https://docs.zephyrproject.org/latest/boards/index.html#arch=openrisc)。

工具链更新：Zephyr SDK 1.0及C17

Zephyr 4.4是首个支持[Zephyr SDK 1.0](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)的版本，包含升级后的GNU工具链、实验性Clang/LLVM支持，以及跨平台QEMU和OpenOCD主机工具。

Zephyr现在默认以C17为最低要求的C语言标准版本。

网络功能增强（Networking Enhancements）

Wi-Fi管理协议栈现在支持[Wi-Fi点对点连接（Wi-Fi P2P / Wi-Fi Direct）](../networking/P163_WiFi管理接口.md#wifi-mgmt-p2p)，设备可直接发现并连接，无需传统接入点（AP）。

网络协议栈新增[WireGuard虚拟专用网络（VPN）](../networking/P211_WireGuard虚拟专用网示例.md#wireguard-vpn)支持，提供安全、低开销的隧道。

USB主机（USB Host）

实验性USB主机支持大幅扩展，新增主机类驱动框架；Zephyr设备作为USB主机时，可支持USB视频类（UVC）摄像头。

新增驱动类别（New Driver Classes）

Zephyr 4.4新增多种驱动API，包括：


- 一次性可编程存储器（One-Time Programmable，OTP）设备，用于配置及读取永久设备数据；（[一次性可编程（OTP）存储器设备](https://docs.zephyrproject.org/latest/hardware/peripherals/otp/index.html#otp)）
- [生物识别（Biometrics）API](https://docs.zephyrproject.org/latest/hardware/peripherals/biometrics.html#biometrics-api)，用于集成指纹扫描器或人脸识别系统等传感器；
- 唤醒控制器（Wake-up Controller，WUC）API，用于管理可使系统退出低功耗状态的唤醒源。（[唤醒控制器（WUC）API](../hardware/P103_唤醒控制器.md#wuc-api)）

Zbus异步监听器与代理（Async Listeners / Proxy Agents）

Zbus异步监听器通过工作队列（Workqueue）实现非阻塞的观察者回调。

Zbus代理通过进程间通信（IPC），将发布订阅消息机制扩展到CPU及域边界之外。（[Zbus代理（Proxy Agents）](https://docs.zephyrproject.org/latest/services/zbus/index.html#zbus-proxy-agent)）

基于调度压力的CPU调频（Pressure-based CPU Frequency Scaling）

实验性CPU调频子系统新增基于调度压力的策略，根据调度器负载调整CPU频率。（[CPU 调频（CPU Frequency Scaling）](https://docs.zephyrproject.org/latest/services/cpu_freq/index.html#cpu-freq)；[基于调度压力的策略（Pressure-based Policy）](https://docs.zephyrproject.org/latest/services/cpu_freq/policies/pressure.html#pressure-policy)）

ARM Cortex-M上下文切换性能改进（Context Switching）

通过[CONFIG_USE_SWITCH](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SWITCH)启用的ARM Cortex-M新上下文切换实现，可显著提高性能。

NAND闪存（NAND Flash）支持

新增闪存转换层（Flash Translation Layer，FTL）磁盘驱动[zephyr,ftl-dhara](../storage_filesystem_binding_reference/P001_zephyr_ftl-dhara.md#std-dtcompatible-zephyr-ftl-dhara)，提供磨损均衡（Wear Leveling）及坏块管理，使NAND闪存可作为标准磁盘设备使用。

开发体验改进（Developer Experience Improvements）

本次发布为开发及测试流程新增多种工具与改进：


- 新增仪表板（Dashboard），在单份报告中集中展示RAM/ROM占用、设备树配置、子系统初始化级别等构建信息。（[dashboard](https://docs.zephyrproject.org/latest/develop/optimizations/tools.html#dashboard)）
- 新增面向QEMU目标的显示驱动，在无法使用原生模拟器（Native Simulator）的环境中，简化带显示功能的应用开发。
- 新增堆加固（Heap Hardening）机制[CONFIG_SYS_HEAP_HARDENING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_HEAP_HARDENING)，提供多级运行时保护，防止堆损坏。
- 新增基于作用域的清理辅助机制，在C语言中离开作用域时执行RAII／defer风格的自动清理。（[基于作用域的清理辅助机制（Scope-based Cleanup Helpers）](https://docs.zephyrproject.org/latest/kernel/cleanup.html#cleanup-api)）
- 新增[ztest基准测试框架（Benchmarking Framework）](https://docs.zephyrproject.org/latest/develop/test/benchmark.html#ztest-benchmarking)，以统一方式创建周期精确的基准测试，支持自动采集数据、补偿测试开销及统计报告。

低功耗蓝牙主机资格认证（Bluetooth LE Host Qualification）

本次发布包含已成功通过资格认证的低功耗蓝牙（Bluetooth LE）主机协议栈，符合蓝牙核心规范6.2。认证范围覆盖GAP、ATT、GATT、L2CAP及SM等核心组件，以及设备信息服务（Device Information Service，DIS）。认证条目及对应设计编号（Design Number，DN）见：[https://qualification.bluetooth.com/ListingDetails/332380](https://qualification.bluetooth.com/ListingDetails/332380)。

扩展开发板支持（Expanded Board Support）

本次发布新增121款开发板及31款扩展板（Shield）支持。（[新增开发板](#boards-added-in-zephyr-4-4)；[新增扩展板](#shields-added-in-zephyr-4-4)）

应用从Zephyr v4.3.0迁移到v4.4.0所需或建议的修改，见单独的[迁移指南（Migration Guide）](../releases_guides/P006_迁移到Zephyr_4.4.md#migration-4-4)。

以下各节按组件提供详细变更列表。

<a id="security-vulnerability-related"></a>

## 安全漏洞相关变更（Security Vulnerability Related）

本版本修复以下通用漏洞披露（CVE）项：


- <a id="index-0"></a>

  [CVE 2025-53022](https://www.cve.org/CVERecord?id=CVE-2025-53022)：TF-M固件更新（FWU）未检查类型／长度／值（TLV）负载的长度。（[TF-M固件更新（FWU）未检查TLV负载长度](https://trustedfirmware-m.readthedocs.io/en/latest/security/security_advisories/fwu_tlv_payload_out_of_bounds_vulnerability.html)）
- <a id="index-1"></a>

  [CVE 2026-0849](https://www.cve.org/CVERecord?id=CVE-2026-0849)：Zephyr项目问题跟踪条目GHSA-ff4p-3ggg-prp6。（[Zephyr项目问题跟踪条目 GHSA-ff4p-3ggg-prp6](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-ff4p-3ggg-prp6)）
- <a id="index-2"></a>

  [CVE 2026-1677](https://www.cve.org/CVERecord?id=CVE-2026-1677)：原发行说明记载的保密期截至2026-04-15。
- <a id="index-3"></a>

  [CVE 2026-1678](https://www.cve.org/CVERecord?id=CVE-2026-1678)：Zephyr项目问题跟踪条目GHSA-536f-h63g-hj42。（[Zephyr项目问题跟踪条目 GHSA-536f-h63g-hj42](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-536f-h63g-hj42)）
- <a id="index-4"></a>

  [CVE 2026-1679](https://www.cve.org/CVERecord?id=CVE-2026-1679)：Zephyr项目问题跟踪条目GHSA-qx3g-5g22-fq5w。（[Zephyr项目问题跟踪条目 GHSA-qx3g-5g22-fq5w](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-qx3g-5g22-fq5w)）
- <a id="index-5"></a>

  [CVE 2026-1681](https://www.cve.org/CVERecord?id=CVE-2026-1681)：原发行说明记载的保密期截至2026-04-15。
- <a id="index-6"></a>

  [CVE 2026-4179](https://www.cve.org/CVERecord?id=CVE-2026-4179)：Zephyr项目问题跟踪条目GHSA-9xg7-g3q3-9prf。（[Zephyr项目问题跟踪条目 GHSA-9xg7-g3q3-9prf](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-9xg7-g3q3-9prf)）
- <a id="index-7"></a>

  [CVE 2026-5066](https://www.cve.org/CVERecord?id=CVE-2026-5066)：原发行说明记载的保密期截至2026-06-01。
- <a id="index-8"></a>

  [CVE 2026-5067](https://www.cve.org/CVERecord?id=CVE-2026-5067)：原发行说明记载的保密期截至2026-05-23。
- <a id="index-9"></a>

  [CVE 2026-5068](https://www.cve.org/CVERecord?id=CVE-2026-5068)：原发行说明记载的保密期截至2026-05-21。
- <a id="index-10"></a>

  [CVE 2026-5071](https://www.cve.org/CVERecord?id=CVE-2026-5071)：原发行说明记载的保密期截至2026-05-18。
- <a id="index-11"></a>

  [CVE 2026-5072](https://www.cve.org/CVERecord?id=CVE-2026-5072)：原发行说明记载的保密期截至2026-05-18。
- <a id="index-12"></a>

  [CVE 2026-5589](https://www.cve.org/CVERecord?id=CVE-2026-5589)：原发行说明记载的保密期截至2026-06-03。
- <a id="index-13"></a>

  [CVE 2026-5590](https://www.cve.org/CVERecord?id=CVE-2026-5590)：Zephyr项目问题跟踪条目GHSA-4vqm-pw24-g9jp。（[Zephyr项目问题跟踪条目 GHSA-4vqm-pw24-g9jp](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-4vqm-pw24-g9jp)）

<a id="api-changes"></a>

## API变更（API Changes）

<a id="removed-apis-and-options"></a>

### 已移除的API与选项（Removed APIs and Options）


- 架构（Architectures）


  - Xtensa架构


    - 下列选项已移除，因为它们属于架构自身的特性：


      - `CONFIG_XTENSA_MMU_DOUBLE_MAP`
      - `CONFIG_XTENSA_RPO_CACHE`
      - `CONFIG_XTENSA_CACHED_REGION`
      - `CONFIG_XTENSA_UNCACHED_REGION`
- 蓝牙（Bluetooth）


  - `CONFIG_BT_TBS_SUPPORTED_FEATURES`
  - 移除已弃用的bt_hci_cmd_create()，它已被[bt_hci_cmd_alloc()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a974e6e9262601e73537cbdcba7a7c93c)替代。
  - 控制器（Controller）


    - [CONFIG_BT_CTLR_ADV_AUX_SET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_AUX_SET)、[CONFIG_BT_CTLR_ADV_SYNC_SET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_SYNC_SET)及[CONFIG_BT_CTLR_ADV_DATA_BUF_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_DATA_BUF_MAX)不再依赖[CONFIG_BT_CTLR_ADVANCED_FEATURES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADVANCED_FEATURES)。
- 内核（Kernel）


  - 移除CONFIG_LINKER_USE_PINNED_SECTION及CONFIG_LINKER_GENERIC_SECTIONS_PRESENT_AT_BOOT。它们启用的选择性内核驻留（Kernel Pinning）机制，在任何请求分页（Demand Paging）淘汰算法下都不安全：CPU异常分派可能访问未显式列入__pinned_*集合的线程特权栈页；若该页已被淘汰，x86上会升级为双重故障#DF，ARM64上会发生嵌套中止（[GitHub #108773](https://github.com/zephyrproject-rtos/zephyr/issues/108773)）。Zephyr内核镜像现在始终驻留物理内存，请求分页仅适用于匿名映射[k_mem_map()](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gacf5f9c43ac2c31c376fed4a19f607feb)及显式__ondemand_*链接器段。
  - 移除__pinned_func、__pinned_data、__pinned_rodata、__pinned_bss及__pinned_noinit属性宏，以及相应汇编别名PINNED_TEXT、PINNED_RODATA、PINNED_DATA、PINNED_BSS及PINNED_NOINIT。
  - 移除K_KERNEL_PINNED_STACK_DEFINE、K_KERNEL_PINNED_STACK_ARRAY_DEFINE、K_KERNEL_PINNED_STACK_ARRAY_DECLARE、K_THREAD_PINNED_STACK_DEFINE及K_THREAD_PINNED_STACK_ARRAY_DEFINE宏。请改用对应的不带PINNED的宏。
- Mbed TLS密码与TLS库


  - `CONFIG_PSA_WANT_KEY_TYPE_DES`
  - `CONFIG_PSA_WANT_ECC_SECP_K1_192`
  - `CONFIG_PSA_WANT_ECC_SECP_R1_192`
  - `CONFIG_PSA_WANT_ECC_SECP_R1_224`
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
  - CONFIG_MBEDTLS_ENTROPY_POLL_ZEPHYR改名为[CONFIG_MBEDTLS_PSA_DRIVER_GET_ENTROPY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_DRIVER_GET_ENTROPY)。
  - CONFIG_MBEDTLS_PEM_CERTIFICATE_FORMAT替换为它以前启用的底层选项：[CONFIG_MBEDTLS_PEM_PARSE_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_PARSE_C)、[CONFIG_MBEDTLS_PEM_WRITE_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_WRITE_C)及[CONFIG_MBEDTLS_BASE64_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_BASE64_C)。
  - CONFIG_MBEDTLS_SERVER_NAME_INDICATION改名为[CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_SERVER_NAME_INDICATION)。
  - CONFIG_MBEDTLS_TEST改名为[CONFIG_MBEDTLS_DEBUG_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_DEBUG_C)。
- 随机数（Random）


  - CONFIG_CSPRNG_AVAILABLE改名为[CONFIG_ENTROPY_NODE_ENABLED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_NODE_ENABLED)。

<a id="deprecated-apis-and-options"></a>

### 已弃用的API与选项（Deprecated APIs and Options）


- 蓝牙（Bluetooth）


  - 蓝牙网状网络（Mesh）


    - 弃用bt_mesh_input_number()，应用应改用[bt_mesh_input_numeric()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabc9d68157928c2b343eddd08ef314d27)。
    - 弃用[bt_mesh_prov](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html)结构体中的output_number回调，应用应改用output_numeric回调。
    - 弃用[CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE)选项。
  - 主机（Host）


    - [bt_conn_le_info.interval](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__info.html#a95a1f635e53f16d5839cdd58f4bda962)已弃用，应改用[bt_conn_le_info.interval_us](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__info.html#a3bede29a6a5df282bde6a26f50ea9aee)。注意单位变化：interval以1.25毫秒为单位，interval_us以微秒为单位。
    - 弃用[CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE)，应用应改用[CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_NONE)。
    - 弃用[CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT)，应用应改用[CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_ENCRYPT)。
    - 弃用[CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN)，应用应改用[CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_GATT_WRITABLE_AUTHEN)。
    - 弃用[CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN)，应用应改用[CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN)。
  - 主机控制器接口（HCI）


    - 弃用[BT_HCI_LE_SUPERVISON_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a03dc93eec388a17c286d50395c683fcb)及[BT_HCI_LE_SUPERVISON_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a2564ee96b802cb887f67e3cc38f8f400)，改用[BT_HCI_LE_SUPERVISION_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a07b822f1a826f4824ec070c4b6822fe2)及[BT_HCI_LE_SUPERVISION_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a1357a2a7227e86df1c132207ba44d6db)。
- 熵（Entropy）

  > - 弃用[CONFIG_ENTROPY_PSA_CRYPTO_RNG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_PSA_CRYPTO_RNG)。
- 集成电路间音频总线（I2S）


  - 以下宏已弃用，并由功能相同、名称符合最新I2S规范修订版的宏替代。（[I2S规范最新修订版](https://www.nxp.com/docs/en/user-manual/UM11732.pdf)）


    - [I2S_OPT_BIT_CLK_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga54aaaa7f0403e4f03574ffcc6141a67f) → [I2S_OPT_BIT_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga36795543fd2423c7c0882e85b133f007)
    - [I2S_OPT_FRAME_CLK_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaedfc35128aae5058a17ef5601bdc73d2) → [I2S_OPT_FRAME_CLK_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga28ed57b0bfceaf91d30aac12de9a4c47)
    - [I2S_OPT_BIT_CLK_SLAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gaa76784ed4a645cb751b2c683bfa4be40) → [I2S_OPT_BIT_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga040259ad09d059b0c2865287a53abbc3)
    - [I2S_OPT_FRAME_CLK_SLAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga138640dfb430fe0565840078a7b23ace) → [I2S_OPT_FRAME_CLK_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gacf77b7fc22301b426c8faa88d9e5eb30)


- Mbed TLS密码与TLS库


  - 弃用[CONFIG_MBEDTLS_USER_CONFIG_ENABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_USER_CONFIG_ENABLE)及[CONFIG_MBEDTLS_CFG_FILE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CFG_FILE)，改用[CONFIG_MBEDTLS_CONFIG_FILE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CONFIG_FILE)。
  - 弃用CONFIG_MBEDTLS_LIBRARY，改用[CONFIG_MBEDTLS_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CUSTOM)。
- 可移植操作系统接口（POSIX）


  - 弃用[CONFIG_XOPEN_STREAMS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XOPEN_STREAMS)，改用[CONFIG_XSI_STREAMS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_STREAMS)。
- 随机数（Random）


  - 弃用CONFIG_CTR_DRBG_CSPRNG_GENERATOR，改用[CONFIG_PSA_CSPRNG_GENERATOR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CSPRNG_GENERATOR)。
- 传感器（Sensors）


  - 恩智浦（NXP）


    - 弃用mcux_lpcmp驱动[drivers/sensor/nxp/mcux_lpcmp/mcux_lpcmp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/mcux_lpcmp/mcux_lpcmp.c)，当前计划在Zephyr 4.6中与mcux_lpcmp示例一同移除。（[GitHub #100998](https://github.com/zephyrproject-rtos/zephyr/issues/100998)）
- 定时器（Timer）


  - 弃用旧Cortex-M SysTick低功耗伴随定时器兼容宏z_cms_lptim_hook_on_lpm_entry及z_cms_lptim_hook_on_lpm_exit，以及兼容头文件[drivers/timer/cortex_m_systick.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/cortex_m_systick.h)。树外SoC／平台代码应迁移到z_sys_clock_lpm_enter()、z_sys_clock_lpm_exit()及[include/zephyr/drivers/timer/system_timer_lpm.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/timer/system_timer_lpm.h)。旧Kconfig选项[CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE)、[CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER)、[CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS)及[CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM)也已弃用，分别改用[CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE)、[CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER)、[CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS)及[CONFIG_SYSTEM_TIMER_RESET_BY_LPM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_TIMER_RESET_BY_LPM)。弃用chosen属性/chosen/zephyr,cortex-m-idle-timer，改用/chosen/zephyr,system-timer-companion。兼容层当前计划在Zephyr 4.6.0中移除。

<a id="new-apis-and-options"></a>

### 新增API与选项（New APIs and Options）


- 模数转换器（ADC）


  - [`ADC_DT_SPEC_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga8bc36476f0362513f9257c658e0ef8c1)
  - [`ADC_DT_SPEC_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga3522baaa63a00ab672d7ee35a634017c)
  - [`ADC_DT_SPEC_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga9525d07f52b7e25fa65bdff8865260c9)
  - [`ADC_DT_SPEC_INST_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gae1504135e99a163d10fbe10a545c9a4a)
  - [`ADC_DT_SPEC_INST_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#gab6f02234d4eaf62e9c47694978cdae92)
  - [`ADC_DT_SPEC_INST_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga8a1965cb4d0eb32b746b26f0f2cef1c0)
  - [`adc_sequence.priority`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__sequence.html#a4e76d19d0b033f767f076d6d2a3abbb4)
  - [`CONFIG_ADC_SEQUENCE_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ADC_SEQUENCE_PRIORITY)
- 架构（Architectures）


  - Xtensa架构


    - [`CONFIG_XTENSA_MMU_USE_DEFAULT_MAPPINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MMU_USE_DEFAULT_MAPPINGS)
- 音频（Audio）


  - [`PDM_DT_IO_CFG_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga61b191e55cffb65950e151cf1f67aed4)
  - [`PDM_DT_HAS_LEFT_CHANNEL`](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga0cd5bf8dad26b9315619e13c4c74f300)
  - [`PDM_DT_HAS_RIGHT_CHANNEL`](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga0984dc3e571fd79f4700467e7305e5c6)
- 蓝牙（Bluetooth）


  - 音频（Audio）


    - [`bt_bap_ep_get_conn()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga575a109efb0fd1644634ce6e0288499b)
    - [`bt_ccp_call_control_client_cb.user_data`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ccp__call__control__client__cb.html#a1d4af4ea50002e2f3d24ed0d4bf21d83)
    - [`CONFIG_BT_TBS_MAX_FRIENDLY_NAME_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_MAX_FRIENDLY_NAME_LENGTH)
    - [`bt_cap_handover_cb.unicast_to_broadcast_created`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__cb.html#a46892bfd9ac055ae73634520b385fa51)
    - [`bt_tbs_client_get_by_index()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga20c6780a4624707a537e905e889510ca)
    - [`bt_bap_unicast_client_cb.supported_contexts`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__client__cb.html#a814a5b22c3f75b7708dac5cfdb55292f)
  - 主机（Host）


    - 新增[bt_gatt_cb_unregister()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5fb25c5eec91045dc4c7fd61ef7e528e) API，用于注销GATT回调处理函数。
    - [`bt_le_per_adv_sync_cb_unregister()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab1576c66b08dc855b2d17fc562f36724)
  - 等时通道（ISO）


    - 对于单播连接等时流（CIS）通道，现在始终先调用[bt_iso_chan_ops.disconnected](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__ops.html#a2069849352019362e5dc7d68f835f359)，再调用[bt_conn_cb.disconnected](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__cb.html#a8b8983b5b5b05c9e2dae242485b6c914)，使回调事件顺序更加确定。（[GitHub #104695](https://github.com/zephyrproject-rtos/zephyr/issues/104695)）
  - 蓝牙网状网络（Mesh）


    - [bt_mesh_input_numeric()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabc9d68157928c2b343eddd08ef314d27)用于提供配网（Provisioning）时带外（OOB）数值输入。
    - [bt_mesh_prov](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html)中的output_numeric回调用于在配网期间输出数值。
    - [CONFIG_BT_MESH_CDB_KEY_SYNC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CDB_KEY_SYNC)启用配置数据库（Configuration Database，CDB）与本地子网及应用密钥（AppKey）存储之间的密钥同步；密钥刷新过程中增加、删除或更新密钥时进行同步。此选项默认启用。
  - 服务（Services）


    - 引入警报通知服务（Alert Notification Service，ANS），通过[CONFIG_BT_ANS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ANS)启用。
- 构建系统（Build System）


  - 新增CMake函数zephyr_constants_library()，根据C结构体布局生成包含构建期常量的头文件。（[GitHub #104861](https://github.com/zephyrproject-rtos/zephyr/issues/104861)）
  - 新增[slot1-partition](../snippets/P017_Slot1分区配置片段.md#snippet-slot1-partition)配置片段（Snippet）。
  - 系统构建（Sysbuild）


    - 新增[SB_CONFIG_MERGED_HEX_FILES](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MERGED_HEX_FILES)，可生成[合并的Hex文件](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild-merged-hex-files)。
    - 新增实验性Sysbuild CMake函数ExternalZephyrVariantProject_Add()，可基于构建中已有镜像，为项目增加变体镜像（Variant Image）。（[变体镜像（Variant Images）](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild-zephyr-application)）
    - 新增[SB_CONFIG_MCUBOOT_DIRECT_XIP_GENERATE_VARIANT](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_DIRECT_XIP_GENERATE_VARIANT)，在MCUboot采用直接原地执行（Direct-XIP）模式时，允许Sysbuild项目自动生成槽位1镜像。
- CPU调频（CPUFreq）


  - [`CONFIG_CPU_FREQ_POLICY_PRESSURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_POLICY_PRESSURE)
- 数模转换器（DAC）


  - 新增数模转换器（DAC）驱动API。（[GitHub #104630](https://github.com/zephyrproject-rtos/zephyr/issues/104630)）


    - [`dac_dt_spec`](../hardware/P826_DAC设备树规格结构.md)
    - [`DAC_CHANNEL_CFG_DT`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga98b233d45a5e091f330657cdb4cec55b)
    - [`DAC_DT_SPEC_GET_BY_NAME`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga220c6d61ae537cefd98a0d912d0e62ab)
    - [`DAC_DT_SPEC_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga07f89cc0df2630b44bcd01a99d60fd03)
    - [`DAC_DT_SPEC_INST_GET_BY_NAME`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gaf813904b80505b6d98e434eb76abcd28)
    - [`DAC_DT_SPEC_INST_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga09baadf4436c502b23c34cb6c6a85ba0)
    - [`DAC_DT_SPEC_GET_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga23c61ff062c1745349b5ef5e8eee5454)
    - [`DAC_DT_SPEC_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga0ca5cf0282575457b7d28de0a5851c80)
    - [`DAC_DT_SPEC_INST_GET_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga62ff7a2763e90accd2bc2352a126ced2)
    - [`DAC_DT_SPEC_INST_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga01636bb214c44daae7a06e3fd42a7378)
    - [`DAC_DT_SPEC_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gaea739243d370edbcd2f9611a4bdf69b9)
    - [`DAC_DT_SPEC_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gaa8e67bb9affd8a1016cf1aed6a36813b)
    - [`DAC_DT_SPEC_INST_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga3cee5c59a0fdd0c576a7770a9ffa351e)
    - [`DAC_DT_SPEC_INST_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga76cc801e1e7d470a1f911cddadaf04b7)
    - [`dac_channel_setup_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gadde628b52a3579003f63b2480ac9254b)
    - [`dac_write_value_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga7ebbb348211b82e84f49f6dad7e28cbf)
    - [`dac_millivolts_to_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gaa266992a47b299804d37d713229eef42)
    - [`dac_microvolts_to_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gacea77754e7d0ae6e244f14b7ab05e086)
    - [`dac_x_to_raw_dt_chan()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga450f0f61564dfc503872a96e6eaac604)
    - [`dac_millivolts_to_raw_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gacd8cd34afed4409b6f3b079ef1b7fae7)
    - [`dac_microvolts_to_raw_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gad64df08bdb6d4e1d491dd21ef3d7da3b)
    - [`dac_is_ready_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga85babfb832acef6dc31c1af7d212f8f8)
- 直接存储器访问（DMA）


  - 新增直接存储器访问（DMA）驱动[nxp,4ch-dma](../intel_microchip_dma_binding_reference/P018_nxp_4ch-dma.md#std-dtcompatible-nxp-4ch-dma)。（[GitHub #97841](https://github.com/zephyrproject-rtos/zephyr/issues/97841)）
- 显示（Display）


  - [display_register_event_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga99b7e7da6b85bee97398a8a9b161c777)及[display_unregister_event_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gaa4e433439206bc426db363c64882a395)。
  - [`CONFIG_SSD1325_DEFAULT_CONTRAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSD1325_DEFAULT_CONTRAST)
  - [`CONFIG_SSD1325_CONV_BUFFER_LINES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSD1325_CONV_BUFFER_LINES)
  - `CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_XRGB_8888`
  - `CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_BGR_888`
  - `CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_ABGR_8888`
  - `CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_RGBA_8888`
  - `CONFIG_SDL_DISPLAY_DEFAULT_PIXEL_FORMAT_BGRA_8888`
  - [`PIXEL_FORMAT_XRGB_8888`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca20bb97558d4acdf225a157c40d9058ab)
  - [`PIXEL_FORMAT_BGR_888`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4625a834a26894db2da3547635a6e172)
  - [`PIXEL_FORMAT_ABGR_8888`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca049f2930dfd1efadfb17a113ba0d879d)
  - [`PIXEL_FORMAT_RGBA_8888`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca9de42e120e50119c2df1c503ed2e7a28)
  - [`PIXEL_FORMAT_BGRA_8888`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca142784152249100847b0e5c6d656191c)
  - [`PANEL_PIXEL_FORMAT_XRGB_8888`](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga1b25099c1904059561ea29f2c2f82750)
  - [`CONFIG_SDL_DISPLAY_ROUNDED_MASK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDL_DISPLAY_ROUNDED_MASK)
  - [`CONFIG_SDL_DISPLAY_ROUNDED_MASK_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDL_DISPLAY_ROUNDED_MASK_COLOR)
  - [sharp,ls0xx](../display_panel_renesas_sharp_binding_reference/P015_sharp_ls0xx.md#std-dtcompatible-sharp-ls0xx)的serial-vcom-inversion及serial-vcom-interval属性。
  - [`CONFIG_LS0XX_VCOM_THREAD_PRIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LS0XX_VCOM_THREAD_PRIO)
- 以太网（Ethernet）


  - 驱动的MAC地址配置支持NVMEM单元（Cell）。


    - [`net_eth_mac_load()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gaa0ef2f94fd18da9c5ea675b46faac8d0)
    - [`net_eth_mac_config`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__mac__config.html)
    - [NET_ETH_MAC_DT_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga59882ff8ad5a11c20c08f296edad367e)及[NET_ETH_MAC_DT_INST_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gac1bb10b6bcc64911128814b9b9de1926)。
  - 新增[ethernet_stats_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#gabfab900bfd7a9078e7ac2fd6aed9ce83)及[ethernet_api](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__api.html)中的可选get_stats_type回调，允许按通用、厂商专用或全部类型过滤以太网统计信息。支持厂商专用统计的驱动可实现get_stats_type，在只请求通用统计时跳过开销较大的固件查询。为保持向后兼容，现有get_stats API不变。
- 异常（Exception）


  - [`CONFIG_EXCEPTION_DUMP_HOOK_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXCEPTION_DUMP_HOOK_ONLY)
- 闪存（Flash）


  - jedec,mspi-nor现在允许通过设备树分别配置读取、写入及控制命令的MSPI参数。
  - Flash API新增扩展操作，支持标记坏块FLASH_EX_OP_MARK_BAD_BLOCK及检查坏块FLASH_EX_OP_IS_BAD_BLOCK。
- 触觉反馈（Haptics）


  - API新增错误回调（Error Callback）。


    - [haptics_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gace3de1e9bf3ad759a618405649a5537a)枚举触觉反馈设备（Haptics Devices）的常见故障条件。
    - [haptics_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gae0ec52bbeb07c255044a4257df43a396)提供错误回调的函数原型。
    - [haptics_register_error_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaef1b0ecdbeb529f7f10704d259f2f98f)向驱动注册错误回调。
- 硬件自旋锁（Hwspinlock）


  - 新增硬件自旋锁（Hardware Spinlock）驱动[nxp,sema42](../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42)。（[GitHub #101499](https://github.com/zephyrproject-rtos/zephyr/issues/101499)）
- 处理器间消息（IPM）


  - 邮箱后端的处理器间消息（IPM）回调现在正确处理仅传递信号（Signal-only）的邮箱用法。邮箱未提供数据缓冲区时，应用应能处理IPM回调中的NULL负载指针。
- 管理（Management）


  - 微控制器管理（MCUmgr）


    - [CONFIG_UART_MCUMGR_RAW_PROTOCOL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUMGR_RAW_PROTOCOL)、[CONFIG_MCUMGR_TRANSPORT_RAW_UART](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_UART)、[CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT)及[CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT_TIME_MS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_UART_INPUT_TIMEOUT_TIME_MS)的详情，见原始UART MCUmgr SMP传输（Raw UART MCUmgr SMP Transport）。（[原始UART MCUmgr SMP传输（Raw UART Transport）](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_transport.html#mcumgr-smp-transport-raw-uart)）
- Mbed TLS密码与TLS库


  - [`CONFIG_TF_PSA_CRYPTO_USER_CONFIG_FILE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TF_PSA_CRYPTO_USER_CONFIG_FILE)
  - [`CONFIG_PSA_WANT_ALG_SHAKE128`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHAKE128)
  - [`CONFIG_PSA_WANT_ALG_SHAKE256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_SHAKE256)
  - [`CONFIG_MBEDTLS_BASE64_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_BASE64_C)
  - [`CONFIG_MBEDTLS_PEM_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_PARSE_C)
  - [`CONFIG_MBEDTLS_PEM_WRITE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_WRITE_C)
  - [`CONFIG_MBEDTLS_PK_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PK_PARSE_C)
  - [`CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_KEYING_MATERIAL_EXPORT)
  - [`CONFIG_MBEDTLS_VERSION_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_VERSION_C)
  - [`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_CRT_PARSE_C)
  - [`CONFIG_MBEDTLS_X509_RSASSA_PSS_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_RSASSA_PSS_SUPPORT)
  - [`CONFIG_MBEDTLS_X509_USE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_X509_USE_C)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_256_CBC_SHA384)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS_PSK_WITH_AES_128_GCM_SHA256)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_ECJPAKE_WITH_AES_128_CCM_8)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_256_GCM_SHA384)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_GCM_SHA256)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_AES_128_CCM_SHA256)
  - [`CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CIPHERSUITE_TLS1_3_CHACHA20_POLY1305_SHA256)
- 调制解调器（Modem）


  - [`CONFIG_MODEM_HL78XX_AT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AT_SHELL)
  - [`CONFIG_MODEM_HL78XX_AIRVANTAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AIRVANTAGE)
- 非易失存储器（NVMEM）


  - Flash设备支持（Flash Device Support）


    - [`CONFIG_NVMEM_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM_FLASH)
    - [`CONFIG_NVMEM_FLASH_WRITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM_FLASH_WRITE)
- 网络（Networking）


  - 受限应用协议（CoAP）


    - [`CONFIG_COAP_CLIENT_MULTICAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_MULTICAST)
  - 动态主机配置协议（DHCP）


    - [`net_dhcpv4_server_set_address_validator_cb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html#ga240c9c47957ea66ba88cc2945f295e11)
  - 轻量级机器到机器协议（LwM2M）


    - [`CONFIG_LWM2M_SEND_SCHEDULER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_SEND_SCHEDULER)
    - [`CONFIG_LWM2M_IPSO_MAGNETOMETER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_IPSO_MAGNETOMETER)
    - [`lwm2m_cache_free_slots_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga00d29a0c4935fc255e74b8c22ac49de1)
  - 其他（Misc）


    - [`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)
    - [`CONFIG_NET_ZPERF_RAW_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_RAW_TX)
    - [`CONFIG_FTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FTP_CLIENT)
  - OpenThread协议栈


    - [`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR)
  - 套接字（Sockets）


    - 数据报传输层安全（DTLS）服务器套接字现在可在单个套接字上支持多个并行客户端会话。
    - [`CONFIG_NET_SOCKETS_TLS_CONNECT_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_TLS_CONNECT_TIMEOUT)
  - 无线局域网（Wi-Fi）


    - 新增Wi-Fi Direct点对点（P2P）模式支持。
    - 新增有线等效保密（Wired Equivalent Privacy，WEP）安全机制支持，默认禁用，可通过[CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP)启用。
    - 默认采用PSA Crypto替代旧密码实现，可通过[CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)控制。
    - [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CLEANUP_INTERVAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CLEANUP_INTERVAL)
    - [`CONFIG_WIFI_NM_HOSTAPD_CLEANUP_INTERVAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_HOSTAPD_CLEANUP_INTERVAL)
- 一次性可编程存储器（OTP）


  - 新增一次性可编程存储器（OTP）驱动API，通过[otp_program()](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#gacaba6f85fb9ba7c0683417b9a2a81a6a)编程、[otp_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#ga067683279ab5d0e9b5f32f83c6b12630)读取OTP设备（[GitHub #101292](https://github.com/zephyrproject-rtos/zephyr/issues/101292)）。也可经非易失性存储器（NVMEM）子系统访问OTP设备。可用选项如下：（[非易失性存储器（Non-Volatile Memory，NVMEM）](https://docs.zephyrproject.org/latest/services/storage/nvmem/index.html#nvmem)）


    - [`CONFIG_OTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP)
    - [`CONFIG_OTP_PROGRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP_PROGRAM)
    - [`CONFIG_OTP_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP_INIT_PRIORITY)
- 脉宽调制（PWM）


  - API扩展支持脉宽调制事件（PWM Events）。


    - [pwm_event_callback](../hardware/P257_PWM事件回调结构.md)保存PWM事件回调。
    - [pwm_init_event_callback()](../hardware/P255_PWM公共接口.md#gaf87ef431d50a482910e77e49d52a2e13)辅助初始化[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)对象。
    - [pwm_add_event_callback()](../hardware/P255_PWM公共接口.md#ga09d1b358df32e798e0345cd647450d54)添加回调。
    - [pwm_remove_event_callback()](../hardware/P255_PWM公共接口.md#ga83d9ec60d3fef69c97602365b979aece)移除回调。
    - [pwm_driver_api](../hardware/P259_PWM驱动函数表.md)中的manage_event_callback管理PWM事件。
    - [`CONFIG_PWM_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_EVENT)
- 电源（Power）


  - [st,stm32u5-pwr](../stm32_soc_power_binding_reference/P016_st_stm32u5-pwr.md#std-dtcompatible-st-stm32u5-pwr)的新voltage-scale属性，可在STM32U5系列上通过设备树手动选择电压档位（Voltage Scale），尤其支持在较低系统时钟频率下使用USB控制器。
- 随机数（Random）


  - [`CONFIG_PSA_CSPRNG_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CSPRNG_GENERATOR)
- 设置（Settings）


  - [`CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION)
  - [`CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION_VALUE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION_VALUE_SIZE)
- 命令行（Shell）


  - [shell_readline()](../shell_core_reference/P001_Shell核心接口.md#ga05b2eb80f3484216ef2e1d4bf9492453)用于读取用户输入。（[用户输入（User Input）](https://docs.zephyrproject.org/latest/services/shell/index.html#shell-readline)）
- 步进电机（Stepper）


  - [`stepper_ctrl_configure_ramp()`](https://docs.zephyrproject.org/latest/doxygen/html/group__stepper__ctrl.html#gae0ebe9949b9fe2bda51c4dc9d537cac5)
- 系统功能（Sys）


  - [`COND_CASE_1`](../util_reference/P001_通用工具公共接口.md#ga0325a11d188ce0d7f2fddc4b74947478)
- 时间工具（Timeutil）


  - [`CONFIG_TIMEUTIL_APPLY_SKEW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMEUTIL_APPLY_SKEW)
- 用户空间（Userspace）


  - [`k_object_access_check()`](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga2c25103810b5e06fdde8355134bed46c)
  - [`k_mem_domain_deinit()`](../memory_domain_reference/P001_内存域接口.md#gaca2e3ca494fe9b7d90b5b7567eb8f18c)
- 实用工具（Utilities）


  - 一致开销字节填充（COBS）流式处理支持。


    - [`cobs_decoder`](https://docs.zephyrproject.org/latest/doxygen/html/structcobs__decoder.html)
    - [`cobs_decoder_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga49fa5a2c541ac72c2a0fe89971bec38d)
    - [`cobs_decoder_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga16669d639b1bdf7bc4a90190530ec2d9)
    - [`cobs_decoder_close()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gac50b6fd7bf9943429a4c0706350fcd76)
    - [`cobs_encoder`](https://docs.zephyrproject.org/latest/doxygen/html/structcobs__encoder.html)
    - [`cobs_encoder_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gafebbd3ea1b058cf7834dd534048602fb)
    - [`cobs_encoder_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga88a7600ca21e3a160ed8354a5af0987b)
    - [`cobs_encoder_close()`](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga0b6ad6f90e70629f143c65f8dbe76a33)
  - 不相交集合（Disjoint Set）支持：[sys_set_node](../unionfind_reference/P002_并查集节点.md)、[sys_set_makeset()](../unionfind_reference/P001_并查集公共接口.md#gae88559a39874fcdc4f8a4a1aa09cfaaa)、[sys_set_find()](../unionfind_reference/P001_并查集公共接口.md#ga2dd615047d421a97a8cc1ff412cf024d)及[sys_set_union()](../unionfind_reference/P001_并查集公共接口.md#gadc4cda883c44c79e3a143a8d5585c011)。
- 视频（Video）


  - [`CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE)
  - [`CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION)
  - [`CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION_NAME)
  - [`video_transform_cap()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__caps.html#ga3d2d1692e4adab02948b11f38407610f)
  - [`VIDEO_PIX_FMT_SBGGR8P16`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabb167fd4b58db338de823dc285e62342)
  - [`VIDEO_PIX_FMT_SGBRG8P16`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga07b22957c7fdc64fd3089fbcb811d599)
  - [`VIDEO_PIX_FMT_SGRBG8P16`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4df33d1a41c2dbdc16c19113be13760b)
  - [`VIDEO_PIX_FMT_SRGGB8P16`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab471cd15aa874a5deadf7b54b826a90e)
  - [`VIDEO_PIX_FMT_Y8P16`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad40f2d8628a39f0d87d5f0a337d7f8c4)
  - [`VIDEO_FMT_IS_SEMI_PLANAR`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga236286b6c75a3dac10f7d82347dfdd9b)
  - `VIDEO_FMT_IS_PLANAR`
  - [`VIDEO_FMT_IS_GRAYSCALE`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7793e9ac7b592429b0dac4da4ead3674)
  - [`VIDEO_FMT_IS_BAYER`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae46d2e9dc794ebb59e2809187754f978)
  - [`VIDEO_FMT_IS_RGB`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae95d61e79e7a102eedba629e4d26cf5d)
  - [`VIDEO_FMT_IS_YUV`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3bac0f45c04fea1d141b65a1d7edb267)
  - [`VIDEO_FMT_IS_MIPI_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga81623ba4831653e1805018ec822f2ef1)
  - [`VIDEO_FMT_IS_PADDED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafdb3d79c7df1881b3946260e191e3cad)
  - [`VIDEO_FMT_IS_SEMI_PLANAR`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga236286b6c75a3dac10f7d82347dfdd9b)
  - [`VIDEO_FMT_IS_FULL_PLANAR`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5fe20fff04af51e514eebc07bed44745)
  - [`VIDEO_FOREACH_BAYER`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacaf01a28e346128216eaaec08591403b)
  - [`VIDEO_FOREACH_BAYER_PADDED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaec20e32bf0da102bafc033ac2e48b8b5)
  - [`VIDEO_FOREACH_BAYER_MIPI_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga22517dda8497ba924ba8bffeaad0c67c)
  - [`VIDEO_FOREACH_BAYER_NON_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga275ba44fc86f0916a9b2a9f7915c0cfe)
  - [`VIDEO_FOREACH_GRAYSCALE`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2cc6468e655d039ba07f624b032d3765)
  - [`VIDEO_FOREACH_GRAYSCALE_NON_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5e694f4181c9f861a1f9603075e20ceb)
  - [`VIDEO_FOREACH_GRAYSCALE_PADDED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga1580b8c54fa57958ebfb573a4a138b9c)
  - [`VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4580c65a689a43878c18e0dc985e52f5)
  - [`VIDEO_FOREACH_RGB`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8f1ce8a81f2aea6386a5168c9e1ed939)
  - [`VIDEO_FOREACH_RGB_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadec2c5cf7e59f4092eef6930580d93f0)
  - [`VIDEO_FOREACH_RGB_NON_PACKED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf667895d82c3dd5b6a4ec8e9e98dbd0a)
  - [`VIDEO_FOREACH_RGB_ALPHA`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacc88a5297ba55a0216e72de6fe087005)
  - [`VIDEO_FOREACH_RGB_PADDED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga34ee863f07f90bd14ccfe5b9c1058539)
  - [`VIDEO_FOREACH_YUV`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga95b3d15b30a04e432543a250339cde93)
  - [`VIDEO_FOREACH_YUV_NON_PLANAR`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8de7c85dd4b32fa406aa121a3ee7f519)
  - [`VIDEO_FOREACH_YUV_SEMI_PLANAR`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac7378ac0dcd5d2afeba4def9cab509f0)
  - [`VIDEO_FOREACH_YUV_FULL_PLANAR`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac71db00c78d16191a6d613ca190a9ede)
  - [`VIDEO_FOREACH_COMPRESSED`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2b2310e1eee22f0e4c28d870e251ecc7)
  - [`video_import_buffer()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#gaa65b69cdc4271a07ad26c4850ff96e45)
- Zephyr消息总线（Zbus）

  > - [`CONFIG_ZBUS_ASYNC_LISTENER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_ASYNC_LISTENER)
  > - [`CONFIG_ZBUS_ASYNC_LISTENER_EXEC_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_ASYNC_LISTENER_EXEC_TIMEOUT)
  > - [`CONFIG_ZBUS_PROXY_AGENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT)
  > - [`CONFIG_ZBUS_PROXY_AGENT_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT_IPC)
  > - [`ZBUS_ASYNC_LISTENER_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#gafe019ce850055a1af70fff20b7126ae5)
  > - [`ZBUS_ASYNC_LISTENER_DEFINE_WITH_ENABLE`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga03e97ece295770b84c97f1ccb2d4875a)
  > - [`ZBUS_PROXY_AGENT_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent.html#ga7e7053ab642e15e577e36bbc5109baac)
  > - [`ZBUS_PROXY_ADD_CHAN`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent.html#gae349b82cf348987e97cc070a7aaeaa58)
  > - [`ZBUS_SHADOW_CHAN_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent.html#ga8da82a59ccd656c4e051a4cadedb4d1c)
  > - [`ZBUS_SHADOW_CHAN_DEFINE_WITH_ID`](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent.html#ga7278f78eb7e250aa730f88db8ac6714c)
  > - [zbus_chan_from_name()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga4c9ca845c43d6f15ae7c8c10c7667d12)：根据名称字符串获取Zbus通道引用。
  > - [zbus_async_listener_set_work_queue()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga549a7a10d4535c6c6448776157e636f6)：设置异步监听器观察者使用的工作队列。
  > - [zbus_chan_pub_stats_msg_age()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga4d674705c121fcd6a573c7c6d9ea7397)：获取距最近一次发布经过的毫秒数，即消息年龄（Message Age）。

<a id="new-boards"></a>

<a id="boards-added-in-zephyr-4-4"></a>

## 新增开发板（New Boards）


- Adafruit Industries, LLC

  > - [RP2040 Prop-Maker Feather](../boards_adafruit_feather_and_grand_central/P005_RP2040_Prop-Maker_Feather.md#adafruit_feather_propmaker_rp2040)开发板（adafruit_feather_propmaker_rp2040）
  > - [RP2040 Scorpio Feather](../boards_adafruit_feather_and_grand_central/P008_RP2040_Scorpio_Feather.md#adafruit_feather_scorpio_rp2040)开发板（adafruit_feather_scorpio_rp2040）
- Advanced Micro Devices（AMD）, Inc.

  > - AMD Versal Gen 2 APU 开发板（Development Board）（versal2_apu）（[AMD Versal第二代APU开发板（Gen 2 Development Board）](../boards_amd/P006_AMD_Versal_Gen_2_APU_Development_Board.md#versal2_apu)）
  > - AMD Versal APU 开发板（Development Board）（versal_apu）（[AMD Versal应用处理单元开发板（APU Development Board）](../boards_amd/P008_AMD_Versal_APU_Development_Board.md#versal_apu)）
  > - [AMD Versal RPU Cortex-R5](../boards_amd/P009_AMD_Versal_RPU_Cortex-R5.md#versal_rpu)开发板（versal_rpu）
- 安信可（Ai-Thinker Co., Ltd.）

  > - Ai-Thinker M61-32S 开发板（Development Board）（ai_m61_32s_kit）（[安信可Ai-Thinker M61-32S开发板（Development Board）](../boards_aesc_aithinker_alientek/P004_Ai-Thinker_M61-32S_development_board.md#ai_m61_32s_kit)）
- 正点原子（Alientek）

  > - [DNESP32S3B](../boards_aesc_aithinker_alientek/P011_DNESP32S3B.md#dnesp32s3b)开发板（dnesp32s3b）
- Alif Semiconductor

  > - Alif Ensemble E1C 开发套件（Development Kit）（ensemble_e1c_dk）（[Alif Ensemble E1C开发套件（Development Kit）](../boards_alif_ambiq/P003_Alif_Ensemble_E1C_Development_Kit.md#ensemble_e1c_dk)）
  > - Alif Ensemble E8 开发套件（Development Kit）（ensemble_e8_dk）（[Alif Ensemble E8开发套件（Development Kit）](../boards_alif_ambiq/P006_Alif_Ensemble_E8_Development_Kit.md#ensemble_e8_dk)）
- Analog Devices, Inc.

  > - [EVAL-ADIN2111D1Z](../boards_adi_ethernet_platforms/P005_EVAL-ADIN2111D1Z.md#adi_eval_adin2111d1z)开发板（adi_eval_adin2111d1z）
- Arm公司（ARM Ltd.）

  > - BASE RevC 2xAEM架构包络模型（Architectural Envelope Model）固定虚拟平台（Fixed Virtual Platform）（fvp_base_revc_2xaem）（[BASE RevC 2xAEM架构包络模型固定虚拟平台（Architectural Envelope Model / Fixed Virtual Platform）](../boards_arm/P001_BASE_RevC_2xAEM_Architectural_Envelope_Model_Fixed_Virtual_Platform.md#fvp_base_revc_2xaem)）
- 黑莓有限公司（BlackBerry Limited）

  > - [QNX虚拟机监控器虚拟机（QNX Hypervisor Virtual Machine）](../boards_bouffalo_qnx_bliiot_blues/P006_QNX_Hypervisor_Virtual_Machine.md#qnxhv_vm)（qnxhv_vm）
- 博流（南京）有限公司（Bouffalo Lab）

  > - [Bouffalo Lab BL706-IoT-DVK](../boards_bouffalo_qnx_bliiot_blues/P003_Bouffalo_Lab_BL706-IoT-DVK.md#bl706_iot_dvk)开发板（bl706_iot_dvk）
- Cadence Design Systems Inc.公司

  > - Cadence SweRV开发板（cdns_swerv）
- Chengdu Heltec Automation Technology Co., Ltd.（成都惠利特自动化科技有限公司）

  > - [WiFi LoRa 32 (V3)](../boards_gd_to_iar/P028_WiFi_LoRa_32_V3.md#heltec_wifi_lora32_v3)开发板（heltec_wifi_lora32_v3）
  > - [Wireless Tracker (V1.1)](../boards_gd_to_iar/P030_Wireless_Tracker_V1.1.md#heltec_wireless_tracker)开发板（heltec_wireless_tracker）
- Cirrus Logic, Inc.公司

  > - [CRD40L50-POC-Q](../boards_cdac_to_cthings/P008_CRD40L50-POC-Q.md#crd40l50)开发板（crd40l50）
- Cytron Technologies公司

  > - [Cytron Maker Nano RP2040](../boards_cypress_to_dragino/P005_Cytron_Maker_Nano_RP2040.md#maker_nano_rp2040)开发板（maker_nano_rp2040）
  > - [Cytron Maker Pi RP2040](../boards_cypress_to_dragino/P006_Cytron_Maker_Pi_RP2040.md#maker_pi_rp2040)开发板（maker_pi_rp2040）
  > - [Cytron Maker Uno RP2040](../boards_cypress_to_dragino/P007_Cytron_Maker_Uno_RP2040.md#maker_uno_rp2040)开发板（maker_uno_rp2040）
  > - [Motion 2350 Pro](https://docs.zephyrproject.org/latest/boards/cytron/motion_2350_pro/doc/index.html#motion_2350_pro)开发板（motion_2350_pro）
- DFRobot

  > - [DFRobot Beetle ESP32-C3](../boards_cypress_to_dragino/P008_DFRobot_Beetle_ESP32-C3.md#beetle_esp32c3)开发板（beetle_esp32c3）
  > - [Beetle RP2350](../boards_cypress_to_dragino/P010_Beetle_RP2350.md#beetle_rp2350)开发板（beetle_rp2350）
- 义隆微电子（Elan Microelectronic Corp.）

  > - [ELAN EM32F967](../boards_ebyte_to_enjoydigital/P009_ELAN_EM32F967.md#32f967_dv)开发板（32f967_dv）
- 乐鑫信息科技（Espressif Systems）

  > - [ESP32-C5-DevKitC-1](../boards_espressif/P021_ESP32-C5-DevKitC-1.md#esp32c5_devkitc)开发板（esp32c5_devkitc）
  > - [ESP Thread边界路由器／ZigBee网关（Border Router / Gateway）](../boards_espressif/P033_ESP_Thread_Border_Router_ZigBee_Gateway.md#esp_threadbr)（esp_threadbr）
- Ezurio

  > - [Lyra 24 P10 DVK](../boards_eurovibes_ezurio/P013_Lyra_24_P10_DVK.md#lyra_24_dvk_p10)开发板（lyra_24_dvk_p10）
  > - [Lyra 24 P20 DVK](../boards_eurovibes_ezurio/P014_Lyra_24_P20_DVK.md#lyra_24_dvk_p20)开发板（lyra_24_dvk_p20）
  > - [Lyra 24 P20RF DVK](../boards_eurovibes_ezurio/P015_Lyra_24_P20RF_DVK.md#lyra_24_dvk_p20rf)开发板（lyra_24_dvk_p20rf）
  > - [Lyra 24 S10 DVK](../boards_eurovibes_ezurio/P016_Lyra_24_S10_DVK.md#lyra_24_dvk_s10)开发板（lyra_24_dvk_s10）
  > - [Lyra P DVK](../boards_eurovibes_ezurio/P017_Lyra_P_DVK.md#lyra_dvk_p)开发板（lyra_dvk_p）
  > - [Lyra S DVK](../boards_eurovibes_ezurio/P018_Lyra_S_DVK.md#lyra_dvk_s)开发板（lyra_dvk_s）
  > - [RM1261 DVK](../boards_eurovibes_ezurio/P021_RM1261_DVK.md#rm126x_dvk_rm1261)开发板（rm126x_dvk_rm1261）
  > - [RM1262 DVK](../boards_eurovibes_ezurio/P022_RM1262_DVK.md#rm126x_dvk_rm1262)开发板（rm126x_dvk_rm1262）
- FocalTech Systems Co., Ltd.（敦泰电子）

  > - FocalTech FT9001 评估板（Evaluation Board）（ft9001_eval）（[FocalTech FT9001评估板（Evaluation Board）](../boards_fanke_to_gardena/P013_FocalTech_FT9001_Evaluation_Board.md#ft9001_eval)）
- Framework Computer, Inc.

  > - [Framework LED矩阵（LED Matrix）](../boards_fanke_to_gardena/P014_Framework_LED_Matrix.md#framework_ledmatrix)开发板（framework_ledmatrix）
  > - [Framework Laptop 16键盘（Keyboard）](../boards_fanke_to_gardena/P016_Framework_Laptop_16_Keyboard.md#framework_laptop16_keyboard)开发板（framework_laptop16_keyboard）
- 英飞凌科技（Infineon Technologies）

  > - PSOC™ 4100S Max 先驱套件（Pioneer Kit）（cy8ckit_041s_max）（[PSOC 4100S Max先锋套件（Pioneer Kit）](../boards_infineon_innblue/P001_PSOC_4100S_Max_pioneer_kit.md#cy8ckit_041s_max)）
  > - [CY8CPROTO-041TP](../boards_infineon_innblue/P006_CY8CPROTO-041TP.md#cy8cproto_041tp)开发板（cy8cproto_041tp）
  > - T2G Body High 评估套件（Evaluation Kit）（kit_t2g_b_h_evk）（[T2G Body High评估套件（Evaluation Kit）](../boards_infineon_innblue/P016_T2G_Body_High_Evaluation_Kit.md#kit_t2g_b_h_evk)）
  > - T2G Body High Lite 评估套件（Evaluation Kit）（kit_t2g_b_h_lite）（[T2G Body High Lite评估套件（Evaluation Kit）](../boards_infineon_innblue/P017_T2G_Body_High_Lite_Evaluation_Kit.md#kit_t2g_b_h_lite)）
- 英特尔公司（Intel Corporation）

  > - [Wildcat Lake CRB](../boards_intel_ite/P021_Wildcat_Lake_CRB.md#intel_wcl_crb)开发板（intel_wcl_crb）
- Longan Labs公司（Shenzhen Longan Technology Co., Ltd.）

  > - [CANBed RP2040](https://docs.zephyrproject.org/latest/boards/longan/canbed_rp2040/doc/index.html#canbed_rp2040)开发板（canbed_rp2040）
- M5Stack

  > - [NanoC6](../boards_lilygo_to_m5stack/P026_NanoC6.md#m5stack_nanoc6)开发板（m5stack_nanoc6）
- 制造商：Makerbase Co., Ltd.

  > - [MKS CANable V1.0](../boards_madmachine_to_mediatek/P005_MKS_CANable_V1.0.md#mks_canable_v10)开发板（mks_canable_v10）
- 联发科技（MediaTek Inc.）

  > - MT8365 ADSP开发板（mt8365）
- 微芯科技（Microchip Technology Inc.）

  > - [PIC32CM PL10 Curiosity Nano](../boards_microchip/P019_PIC32CM_PL10_Curiosity_Nano.md#pic32cm_pl10_cnano)开发板（pic32cm_pl10_cnano）
  > - [PIC32CX SG41 Curiosity Ultra](../boards_microchip/P021_PIC32CX_SG41_Curiosity_Ultra.md#pic32cx_sg41_cult)开发板（pic32cx_sg41_cult）
  > - [PIC32CZ CA90 Curiosity Ultra](../boards_microchip/P024_PIC32CZ_CA90_Curiosity_Ultra.md#pic32cz_ca90_cult)开发板（pic32cz_ca90_cult）
  > - [PIC64GX1000 Curiosity kit](../boards_microchip/P025_PIC64GX1000_Curiosity_kit.md#pic64gx_curiosity_kit)开发板（pic64gx_curiosity_kit）
  > - [SAM E54 Curiosity Ultra](../boards_microchip/P026_SAM_E54_Curiosity_Ultra.md#sam_e54_cult)开发板（sam_e54_cult）
- Nordic Semiconductor

  > - [nRF54L15 TAG](../boards_nordic/P013_nRF54L15_TAG.md#nrf54l15tag)开发板（nrf54l15tag）
  > - [nRF7120 DK](../boards_nordic/P017_nRF7120_DK.md#nrf7120dk)开发板（nrf7120dk）
- 新唐科技（Nuvoton Technology Corporation）

  > - [NUMAKER NUGESTUREAI M55M1](../boards_norik_to_nuvoton/P014_NUMAKER_NUGESTUREAI_M55M1.md#numaker_gai_m55m1)开发板（numaker_gai_m55m1）
- 恩智浦半导体（NXP Semiconductors）

  > - [FRDM-iMXRT1186](../boards_nxp_frdm_imx_kinetis/P004_FRDM-iMXRT1186.md#frdm_imxrt1186)开发板（frdm_imxrt1186）
  > - [FRDM-KE16Z](../boards_nxp_frdm_imx_kinetis/P011_FRDM-KE16Z.md#frdm_ke16z)开发板（frdm_ke16z）
  > - [FRDM-MCXA577](../boards_nxp_frdm_mcx_rw/P004_FRDM-MCXA577.md#frdm_mcxa577)开发板（frdm_mcxa577）
  > - [FRDM-MCXL255](../boards_nxp_frdm_mcx_rw/P012_FRDM-MCXL255.md#frdm_mcxl255)开发板（frdm_mcxl255）
  > - [FRDM-MCXW70](../boards_nxp_frdm_mcx_rw/P016_FRDM-MCXW70.md#frdm_mcxw70)开发板（frdm_mcxw70）
  > - [S32K5XXCVB](../boards_nxp_remaining/P012_S32K5XXCVB.md#s32k5xxcvb)开发板（s32k5xxcvb）
- 其他（Others）

  > - [DOIT ESP32-DevKit-V1](../boards_other_vendors/P007_DOIT_ESP32-DevKit-V1.md#doit_esp32_devkit_v1)开发板（doit_esp32_devkit_v1）
  > - ESP32-C3 开发板（Development Board） (LCKFB)（esp32c3_lckfb）（[LCKFB ESP32-C3开发板](../boards_other_vendors/P008_ESP32-C3_Development_Board_LCKFB.md#esp32c3_lckfb)）
- PCB Cupid

  > - [Glyph-C3](../boards_panasonic_particle_pcbcupid_peregrine/P014_Glyph-C3.md#glyph_c3)开发板（glyph_c3）
  > - [Glyph-H2](../boards_panasonic_particle_pcbcupid_peregrine/P016_Glyph-H2.md#glyph_h2)开发板（glyph_h2）
- PHYTEC

  > - [phyBOARD-Atlas i.MX RT1170](../boards_phytec/P002_phyBOARD-Atlas_i.MX_RT1170.md#phyboard_atlas)开发板（phyboard_atlas）
- Pimoroni Ltd.

  > - [Pimoroni Tiny 2040](../boards_pimoroni_radxa/P003_Pimoroni_Tiny_2040.md#tiny2040)开发板（tiny2040）
- QEMU模拟器

  > - OpenRISC 1000的QEMU仿真（QEMU Emulation）（qemu_or1k）（[QEMU仿真：OpenRISC 1000](../qemu_other_reference/P003_QEMU_OpenRISC_1000仿真开发板.md#qemu_or1k)）
- Qualcomm Technologies, Inc

  > - QCC744M 评估套件（Evaluation Kit）（qcc744m_evk）（[QCC744M评估套件（Evaluation Kit）](../boards_pimoroni_radxa/P010_QCC744M_Evaluation_Kit.md#qcc744m_evk)）
- RAKwireless Technology Limited

  > - [RAK11160](../boards_rak_raspberry_raytac/P002_RAK11160.md#rak11160)开发板（rak11160）
- Realtek Semiconductor Corp.

  > - RTL8721F 评估板（Evaluation Board）（rtl8721f_evb）（[RTL8721F评估板（Evaluation Board）](../boards_realtek_ruiside_sifive/P003_RTL8721F_Evaluation_Board.md#rtl8721f_evb)）
  > - RTL872xD 评估板（Evaluation Board）（rtl872xd_evb）（[RTL872xD评估板（Evaluation Board）](../boards_realtek_ruiside_sifive/P004_RTL872xD_Evaluation_Board.md#rtl872xd_evb)）
  > - RTL8721Dx 评估板（Evaluation Board）（rtl872xda_evb）（[RTL8721Dx评估板（Evaluation Board）](../boards_realtek_ruiside_sifive/P005_RTL8721Dx_Evaluation_Board.md#rtl872xda_evb)）
  > - RTL8752H 评估板（Evaluation Board）（rtl8752h_evb）（[RTL8752H评估板（Evaluation Board）](../boards_realtek_ruiside_sifive/P006_RTL8752H_Evaluation_Board.md#rtl8752h_evb)）
  > - RTL87x2G Model A 评估板（Evaluation Board）（rtl87x2g_evb_a）（[RTL87x2G Model A评估板（Evaluation Board）](../boards_realtek_ruiside_sifive/P007_RTL87x2G_Model_A_Evaluation_Board.md#rtl87x2g_evb_a)）
  > - RTS5817 MAA 评估板（Evaluation Board）（rts5817_maa_evb）（[RTS5817 MAA评估板（Evaluation Board）](../boards_realtek_ruiside_sifive/P008_RTS5817_MAA_Evaluation_Board.md#rts5817_maa_evb)）
- 瑞萨电子（Renesas Electronics Corporation）

  > - [RA8D1人工智能套件开发平台（AI Kit Development Platform）](../boards_renesas_ra/P001_RA8D1_AI_Kit_Development_Platform.md#aik_ra8d1)（aik_ra8d1）
  > - [CPKCOR RA8D1B开发板](../boards_renesas_ra/P002_CPKCOR_RA8D1B_board.md#cpkcor_ra8d1b)（cpkcor_ra8d1b）
  > - RA8T2 评估套件（Evaluation Kit）（ek_ra8t2）（[RA8T2评估套件](../boards_renesas_ra/P025_RA8T2_Evaluation_Kit.md#ek_ra8t2)）
  > - RA0E1 快速原型板（Fast Prototype Board）（fpb_ra0e1）（[RA0E1快速原型板（Fast Prototype Board）](../boards_renesas_rx_rz/P004_RA0E1_Fast_Prototype_Board.md#fpb_ra0e1)）
  > - RA8E1 MCU系列快速原型板（Fast Prototyping Board）（fpb_ra8e1）（[RA8E1 MCU组快速原型板](../boards_renesas_rx_rz/P008_Fast_Prototyping_Board_for_RA8E1_MCU_Group.md#fpb_ra8e1)）
  > - [RX140快速原型板](../boards_renesas_rx_rz/P009_Fast_Prototyping_Board_for_RX140.md#fpb_rx140)（Fast Prototyping Board）（fpb_rx140）
  > - RX14T 快速原型板（Fast Prototyping Board）（fpb_rx14t）（[RX14T快速原型板](../boards_renesas_rx_rz/P010_RX14T_Fast_Prototyping_Board.md#fpb_rx14t)）
  > - RX14T 电机控制板（Motor Control Board）（mcb_rx14t）（[RX14T电机控制板（Motor Control Board）](../boards_renesas_rx_rz/P013_RX14T_Motor_Control_Board.md#mcb_rx14t)）
  > - RA4T1 电机控制套件（Motor Control Kit）（mck_ra4t1）（[RA4T1电机控制套件（Motor Control Kit）](../boards_renesas_rx_rz/P015_RA4T1_Motor_Control_Kit.md#mck_ra4t1)）
  > - [瑞萨RX140入门套件](../boards_renesas_rx_rz/P022_Renesas_Starter_Kit_for_RX140.md#rsk_rx140)（Renesas Starter Kit）（rsk_rx140）
  > - RZ/G3E 评估板套件（Evaluation Board Kit）（rzg3e_smarc）（[RZ/G3E评估板套件](../boards_renesas_rx_rz/P030_RZ_G3E_Evaluation_Board_Kit.md#rzg3e_smarc)）
  > - RZ/N2H 评估板套件（Evaluation Board Kit）（rzn2h_evb）（[RZ/N2H评估板套件](../boards_renesas_rx_rz/P032_RZ_N2H_Evaluation_Board_Kit.md#rzn2h_evb)）
  > - RZ/T2H 评估板套件（Evaluation Board Kit）（rzt2h_evb）（[RZ/T2H评估板套件](../boards_renesas_rx_rz/P034_RZ_T2H_Evaluation_Board_Kit.md#rzt2h_evb)）
- Retronix Technology Inc.

  > - [Sparrow Hawk R-Car V4H SBC](../boards_retronix_sifli/P002_Sparrow_Hawk_R-Car_V4H_SBC.md#sparrowhawk_rcar_v4h)开发板（sparrowhawk_rcar_v4h）
- Seeed Technology Co., Ltd

  > - [reTerminal E1002](../boards_seeed/P005_reTerminal_E1002.md#reterminal_e1002)开发板（reterminal_e1002）
  > - [XIAO RP2350](../boards_seeed/P022_XIAO_RP2350.md#xiao_rp2350)开发板（xiao_rp2350）
- Shenzhen Holyiot Technology Co., Ltd.

  > - [21014 Module](../boards_gd_to_iar/P032_21014_Module.md#holyiot_21014)开发板（holyiot_21014）
  > - [HOLYIOT 25008](../boards_gd_to_iar/P033_HOLYIOT_25008.md#holyiot_25008)开发板（holyiot_25008）
- Shenzhen Sipeed Technology Co., Ltd.

  > - [Sipeed M0S Dock](../boards_sipeed_sparkfun/P005_Sipeed_M0S_Dock.md#maix_m0s_dock)开发板（maix_m0s_dock）
- 深圳迅龙软件有限公司（Shenzhen Xunlong Software CO.,Limited）

  > - [Orange Pi Zero](../boards_waveshare_tail/P052_Orange_Pi_Zero.md#opi_zero)开发板（opi_zero）
  > - [Orange Pi 5 Ultra RK3588](../boards_waveshare_tail/P054_Orange_Pi_5_Ultra_RK3588.md#orangepi_5_ultra_rk3588)开发板（orangepi_5_ultra_rk3588）
- 芯科科技（Silicon Laboratories）

  > - [EFM32 Tiny Gecko (EFM32TG-STK3300)](../boards_silabs/P061_EFM32_Tiny_Gecko_EFM32TG-STK3300.md#efm32tg_stk3300)开发板（efm32tg_stk3300）
  > - EFR32xG28 探索套件（Explorer Kit） (xG28-EK2705A)（xg28_ek2705a）（[EFR32xG28探索套件，xG28-EK2705A](../boards_silabs/P021_EFR32xG28_Explorer_Kit_xG28-EK2705A.md#xg28_ek2705a)）
  > - SiWx917 Wi-Fi 6 and 低功耗蓝牙（Bluetooth LE） SoC 8 MB Flash 无线电板（Radio Board） (SiWx91x-RB4338A)（siwx917_rb4338a）（[SiWx917 Wi-Fi 6与低功耗蓝牙SoC 8 MB闪存无线电板，SiWx91x-RB4338A](../boards_silabs/P025_SiWx917_Wi-Fi_6_and_Bluetooth_LE_SoC_8_MB_Flash_Radio_Board_SiWx91x-RB4338A.md#siwx917_rb4338a)）
  > - SiWx917 Wi-Fi 6 and 低功耗蓝牙（Bluetooth LE） 8 MB Flash + 8 MB外部PSRAM 无线电板（Radio Board） (SiWx91x-RB4342A)（siwx917_rb4342a）（[SiWx917 Wi-Fi 6与低功耗蓝牙8 MB闪存、8 MB外部PSRAM无线电板，SiWx91x-RB4342A](../boards_silabs/P026_SiWx917_Wi-Fi_6_and_Bluetooth_LE_8_MB_Flash_8_MB_ext_PSRAM_Radio_Board_SiWx91x-RB4342A.md#siwx917_rb4342a)）
- Soldered Electronics

  > - [Inkplate 6Color](../boards_sipeed_sparkfun/P016_Inkplate_6Color.md#inkplate_6color)开发板（inkplate_6color）
- Space Cubics Inc.

  > - [SC-OBC Module V1](../boards_retronix_sifli/P010_SC-OBC_Module_V1.md#scobc_v1)开发板（scobc_v1）
- SparkFun Electronics

  > - Sparkfun RP2040 mikroBUS 开发板（Development Board）（sparkfun_rp2040_mikrobus）（[SparkFun RP2040 mikroBUS开发板](../boards_sipeed_sparkfun/P022_Sparkfun_RP2040_mikroBUS_Development_Board.md#sparkfun_rp2040_mikrobus)）
- 意法半导体（STMicroelectronics）

  > - [Nucleo C542RC开发板](../boards_st_nucleo/P004_Nucleo_C542RC.md#nucleo_c542rc)（nucleo_c542rc）
  > - [Nucleo C562RE开发板](../boards_st_nucleo/P005_Nucleo_C562RE.md#nucleo_c562re)（nucleo_c562re）
  > - [Nucleo C5A3ZG开发板](../boards_st_nucleo/P006_Nucleo_C5A3ZG.md#nucleo_c5a3zg)（nucleo_c5a3zg）
  > - [Nucleo U3C5ZI Q开发板](../boards_st_nucleo/P068_Nucleo_U3C5ZI_Q.md#nucleo_u3c5zi_q)（nucleo_u3c5zi_q）
  > - [Nucleo WBA25CE1开发板](../boards_st_nucleo/P076_Nucleo_WBA25CE1.md#nucleo_wba25ce1)（nucleo_wba25ce1）
  > - [STM32H5F5J-DK Discovery](../boards_st_discovery_eval/P034_STM32H5F5J-DK_Discovery.md#stm32h5f5j_dk)开发板（stm32h5f5j_dk）
  > - STM32MP215F-DK 评估板（Evaluation Board）（stm32mp215f_dk）（[STM32MP215F-DK评估板（Evaluation Board）](../boards_st_discovery_eval/P049_STM32MP215F-DK_Evaluation_Board.md#stm32mp215f_dk)）
- Synaptics

  > - [SR100 RDK](../boards_starfive_trenz/P006_SR100_RDK.md#sr100_rdk)开发板（sr100_rdk）
- 德州仪器（Texas Instruments）

  > - AM62L TMDS62LEVM 评估模块（Evaluation Module，EVM）（am62l_evm）（[AM62L TMDS62LEVM评估模块（EVM）](../boards_ti/P002_AM62L_TMDS62LEVM_evaluation_module_EVM.md#am62l_evm)）
  > - [CC1312R1 LaunchXL](../boards_ti/P003_CC1312R1_LaunchXL.md#cc1312r1_launchxl)开发板（cc1312r1_launchxl）
- Third Reality, Inc.

  > - ThirdReality精简版温湿度传感器（Temperature and Humidity Sensor Lite）（3r_tnh_sensor_lite）（[ThirdReality温湿度传感器Lite（Temperature and Humidity Sensor Lite）](../boards_starfive_trenz/P015_ThirdReality_Temperature_and_Humidity_Sensor_Lite.md#3r_tnh_sensor_lite)）
- u-blox

  > - [EVK-NINA-B5-MCXW716C](../boards_ublox_misc/P015_EVK-NINA-B5-MCXW716C.md#ubx_evkninab5)开发板（ubx_evkninab5）
- Vicharak

  > - [Shrike-lite](../boards_ublox_misc/P035_Shrike-lite.md#shrike_lite)开发板（shrike_lite）
- VIEWE Display Co., Ltd.

  > - [VIEWE UEDX24320028E-WB-A](../boards_ublox_misc/P038_VIEWE_UEDX24320028E-WB-A.md#uedx24320028e_wb_a)开发板（uedx24320028e_wb_a）
- Waveshare Electronics微雪电子

  > - [ESP32-S3-GEEK](../boards_waveshare_tail/P008_ESP32-S3-GEEK.md#esp32s3_geek)开发板（esp32s3_geek）
  > - [ESP32-S3-RLCD-4.2](../boards_waveshare_tail/P010_ESP32-S3-RLCD-4.2.md#esp32s3_rlcd_4_2)开发板（esp32s3_rlcd_4_2）
  > - [RP2350-Zero](../boards_waveshare_tail/P020_RP2350-Zero.md#rp2350_zero)开发板（rp2350_zero）
- WeAct Studio

  > - [CAN485 DevBoard V1](../boards_weact/P007_CAN485_DevBoard_V1.md#can485dbv1)开发板（can485dbv1）
  > - [WeAct RP2350B Core](../boards_weact/P018_WeAct_RP2350B_Core.md#rp2350b_core)开发板（rp2350b_core）
  > - STM32G0B1 核心板（Core Board）（weact_stm32g0b1_core）（[STM32G0B1核心板](../boards_weact/P022_STM32G0B1_Core_Board.md#weact_stm32g0b1_core)）
- WEMOS Electronics

  > - [Wemos Lolin32 Lite](../boards_ublox_misc/P045_Wemos_Lolin32_Lite.md#lolin32_lite)开发板（lolin32_lite）
- WinChipHead

  > - [WCH CH32V307V-EVT-R1](../boards_waveshare_tail/P030_WCH_CH32V307V-EVT-R1.md#ch32v307v_evt_r1)开发板（ch32v307v_evt_r1）

<a id="new-shields"></a>

<a id="shields-added-in-zephyr-4-4"></a>

## 新增扩展板（New Shields）


- [Adafruit FeatherWing 128×64 OLED扩展板（Shield）](../boards_shields/P016_Adafruit_FeatherWing_128x64_OLED_Shield.md#adafruit-featherwing-128x64-oled)
- [Adafruit HTS221扩展板（Shield）](../boards_shields/P019_Adafruit_HTS221_Shield.md#adafruit-hts221)
- [Adafruit INA3221扩展板（Shield）](../boards_shields/P023_Adafruit_INA3221_Shield.md#adafruit-ina3221)
- [Adafruit MAX17048扩展板（Shield）](../boards_shields/P030_Adafruit_MAX17048_Shield.md#adafruit-max17048)
- [Adafruit MCP4728四路DAC扩展板（Quad DAC Shield）](../boards_shields/P031_Adafruit_MCP4728_Quad_DAC_Shield.md#adafruit-mcp4728)
- [Analog Devices EVAL-CN0391-ARDZ扩展板](../boards_shields/P070_EVAL-CN0391-ARDZ.md#eval-cn0391-ardz)
- [Arduino Modulino磁保持继电器模块（Latch Relay）](../boards_shields/P048_Arduino_Modulino_Latch_Relay.md#arduino-modulino-latch-relay)
- [ESP Thread边界路由器／Zigbee网关以太网扩展板（BR / GW Ethernet）](../boards_espressif/P033_ESP_Thread_Border_Router_ZigBee_Gateway.md#esp-threadbr-ethernet)
- [Microchip RNBD451附加板（Add-on Board）](../boards_shields/P088_RNBD451_Add-on_Board.md#rnbd451-add-on-shield)
- [MikroElektronika三轴Accel 4 Click加速度计扩展板](../boards_shields/P092_MikroElektronika_3_axis_Accel_4_Click.md#mikroe-accel4-click-shield)
- [MikroElektronika CAN FD 6 Click扩展板](../boards_shields/P097_MikroElektronika_CAN_FD_6_Click.md#mikroe-can-fd-6-click-shield)
- [MikroElektronika EEPROM 13 Click存储扩展板](../boards_shields/P099_MikroElektronika_EEPROM_13_Click.md#mikroe-eeprom-13-click-shield)
- [MikroElektronika Flash 5 Click闪存扩展板](../boards_shields/P103_MikroElektronika_Flash_5_Click.md#mikroe-flash-5-click-shield)
- [MikroElektronika Flash 6 Click闪存扩展板](../boards_shields/P104_MikroElektronika_Flash_6_Click.md#mikroe-flash-6-click-shield)
- [MikroElektronika Flash 8 Click闪存扩展板](../boards_shields/P105_MikroElektronika_Flash_8_Click.md#mikroe-flash-8-click-shield)
- [MikroElektronika LTE IoT 7 Click蜂窝通信扩展板](../boards_shields/P112_MikroElektronika_LTE_IoT_7_Click.md#mikroe-lte-iot7-click-shield)
- [MikroElektronika MCP251x Click扩展板（Shields）](../boards_shields/P113_MikroElektronika_MCP251x_Click_shields.md#mikroe-mcp251x-click-shield)
- [MikroElektronika MCP251xFD Click扩展板（Shields）](../boards_shields/P114_MikroElektronika_MCP251xFD_Click_shields.md#mikroe-mcp251xfd-click-shield)
- [MikroElektronika RS485 Isolator 5 Click隔离扩展板](../boards_shields/P117_MikroElektronika_RS485_Isolator_5_Click.md#mikroe-rs485-isolator-5-click-shield)
- [MikroElektronika Temp&Hum Click温湿度扩展板](../boards_shields/P121_MikroElektronika_Temp_Hum_Click.md#mikroe-temp-hum-click-shield)
- [Nordic Semiconductor nRF7002 EB II扩展板](../boards_shields/P131_nRF7002_EB_II.md#nrf7002eb2)
- [NXP S32K5XX-MB扩展板（Shield）](../boards_shields/P140_NXP_S32K5XX-MB_Shield.md#nxp-s32k5xx-mb)
- [树莓派摄像头模块2（Raspberry Pi Camera Module 2）](../boards_shields/P148_Raspberry_Pi_Camera_Module_2.md#raspberry-pi-camera-module-2)
- [Renesas AIK OV2640摄像头扩展板（Camera Shield）](../boards_shields/P149_Renesas_AIK_OV2640_Camera_Shield.md#renesas-aik-ov2640-cam)
- [Seeed Studio XIAO 24 GHz毫米波传感器（mmWave Sensor）](../boards_shields/P165_Seeed_Studio_24GHz_mmWave_Sensor_for_XIAO.md#seeed-xiao-hsp24)
- [Semtech SX1261MB2BAS LoRa扩展板（Shield）](../boards_shields/P167_Semtech_SX1261MB2BAS_LoRa_Shield.md#semtech-sx1261mb2bas)
- [意法半导体（ST Microelectronics）B-DSI-MB1314扩展板](../boards_shields/P182_ST_B-DSI-MB1314.md#st-b-dsi-mb1314)
- [意法半导体（ST Microelectronics）ST87MXX扩展板（Shield）](../boards_shields/P179_ST87MXX_shield.md#st87mxx-generic)
- [意法半导体（ST Microelectronics）X-NUCLEO-IKS5A1：微机电系统（MEMS）惯性与环境多传感器扩展板](../boards_shields/P214_X-NUCLEO-IKS5A1_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md#x-nucleo-iks5a1)
- [WIZnet W5500以太网扩展板（Ethernet Shield）](../boards_shields/P200_WIZnet_W5500_Ethernet_Shield.md#wiznet-w5500)
- [ZHAW Luma Matrix矩阵扩展板（Shield）](../boards_shields/P219_ZHAW_Luma_Matrix_Shield.md#zhaw-lumamatrix)

<a id="new-drivers"></a>

## 新增驱动（New Drivers）


- 模数转换器（ADC）

  > - [bflb,adc](../hardware/P886_BouffaloLab模数转换器绑定.md#dtbinding-bflb-adc)（[GitHub #98624](https://github.com/zephyrproject-rtos/zephyr/issues/98624)）
  > - [infineon,sar-adc](../hardware/P882_InfineonSAR模数转换器绑定.md#dtbinding-infineon-sar-adc)（[GitHub #103453](https://github.com/zephyrproject-rtos/zephyr/issues/103453)）
  > - [maxim,max2253x](../hardware/P936_MAX2253x模数转换器绑定.md#dtbinding-maxim-max2253x)（[GitHub #102115](https://github.com/zephyrproject-rtos/zephyr/issues/102115)）
  > - [microchip,adc-g1](../hardware/P859_MicrochipG1模数转换器绑定.md#dtbinding-microchip-adc-g1)（[GitHub #99966](https://github.com/zephyrproject-rtos/zephyr/issues/99966)）
  > - [microchip,mcp3221](../hardware/P939_MCP3221模数转换器绑定.md#dtbinding-microchip-mcp3221)（[GitHub #105751](https://github.com/zephyrproject-rtos/zephyr/issues/105751)）
  > - [renesas,ra-adc12](../hardware/P868_RenesasRAADC12绑定.md#dtbinding-renesas-ra-adc12)（[GitHub #95710](https://github.com/zephyrproject-rtos/zephyr/issues/95710)）
  > - [renesas,ra-adc16](../hardware/P869_RenesasRAADC16绑定.md#dtbinding-renesas-ra-adc16)（[GitHub #95710](https://github.com/zephyrproject-rtos/zephyr/issues/95710)）
  > - [renesas,rz-adc-e](../hardware/P872_RenesasRZADCE绑定.md#dtbinding-renesas-rz-adc-e)（[GitHub #100575](https://github.com/zephyrproject-rtos/zephyr/issues/100575)）
  > - [renesas,rza2m-adc](../hardware/P874_RenesasRZA2M模数转换器绑定.md#dtbinding-renesas-rza2m-adc)（[GitHub #100637](https://github.com/zephyrproject-rtos/zephyr/issues/100637)）
  > - [sifli,sf32lb-gpadc](../hardware/P898_SiFliSF32LB通用模数转换器绑定.md#dtbinding-sifli-sf32lb-gpadc)（[GitHub #99460](https://github.com/zephyrproject-rtos/zephyr/issues/99460)）
  > - [ti,ads7950](../hardware/P968_ADS7950模数转换器绑定.md#dtbinding-ti-ads7950)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7951](../hardware/P969_ADS7951模数转换器绑定.md#dtbinding-ti-ads7951)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7952](../hardware/P970_ADS7952模数转换器绑定.md#dtbinding-ti-ads7952)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7953](../hardware/P971_ADS7953模数转换器绑定.md#dtbinding-ti-ads7953)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7954](../hardware/P972_ADS7954模数转换器绑定.md#dtbinding-ti-ads7954)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7955](../hardware/P973_ADS7955模数转换器绑定.md#dtbinding-ti-ads7955)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7956](../hardware/P974_ADS7956模数转换器绑定.md#dtbinding-ti-ads7956)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7957](../hardware/P975_ADS7957模数转换器绑定.md#dtbinding-ti-ads7957)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7958](../hardware/P976_ADS7958模数转换器绑定.md#dtbinding-ti-ads7958)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7959](../hardware/P977_ADS7959模数转换器绑定.md#dtbinding-ti-ads7959)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7960](../hardware/P978_ADS7960模数转换器绑定.md#dtbinding-ti-ads7960)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
  > - [ti,ads7961](../hardware/P979_ADS7961模数转换器绑定.md#dtbinding-ti-ads7961)（[GitHub #101660](https://github.com/zephyrproject-rtos/zephyr/issues/101660)）
- ARM 架构（ARM Architecture）

  > - [arm,axi-timing-adapter](../arm_timing_ethosu_control_binding_reference/P001_arm_axi-timing-adapter.md#std-dtcompatible-arm-axi-timing-adapter)（[GitHub #100356](https://github.com/zephyrproject-rtos/zephyr/issues/100356)）
  > - [nordic,nrf-pwr-antswc](../arm_nordic_nxp_control_binding_reference/P001_nordic_nrf-pwr-antswc.md#std-dtcompatible-nordic-nrf-pwr-antswc)（[GitHub #101199](https://github.com/zephyrproject-rtos/zephyr/issues/101199)）
  > - [nordic,nrf-tampc](../arm_nordic_nxp_control_binding_reference/P006_nordic_nrf-tampc.md#std-dtcompatible-nordic-nrf-tampc)（[GitHub #99295](https://github.com/zephyrproject-rtos/zephyr/issues/99295)）
- 音频（Audio）

  > - [awinic,aw88298](../audio_pdm_codec_binding_reference/P002_awinic_aw88298.md#std-dtcompatible-awinic-aw88298)（[GitHub #97006](https://github.com/zephyrproject-rtos/zephyr/issues/97006)）
  > - [infineon,pdm](../audio_pdm_codec_binding_reference/P009_infineon_pdm.md#std-dtcompatible-infineon-pdm)（[GitHub #104698](https://github.com/zephyrproject-rtos/zephyr/issues/104698)）
  > - [sifli,sf32lb-audcodec](../audio_pdm_codec_binding_reference/P016_sifli_sf32lb-audcodec.md#std-dtcompatible-sifli-sf32lb-audcodec)（[GitHub #98701](https://github.com/zephyrproject-rtos/zephyr/issues/98701)）
  > - [zephyr,pdm-dmic](../audio_stm32_ti_wolfson_binding_reference/P016_zephyr_pdm-dmic.md#std-dtcompatible-zephyr-pdm-dmic)（[GitHub #99351](https://github.com/zephyrproject-rtos/zephyr/issues/99351)）
- 生物识别（Biometrics）

  > - [adh-tech,gt5x](../gnss_fingerprint_binding_reference/P001_adh-tech_gt5x.md#std-dtcompatible-adh-tech-gt5x)（[GitHub #100139](https://github.com/zephyrproject-rtos/zephyr/issues/100139)）
  > - [zephyr,biometrics-emul](../hardware/P532_生物识别仿真设备绑定.md#dtbinding-zephyr-biometrics-emul)（[GitHub #100139](https://github.com/zephyrproject-rtos/zephyr/issues/100139)）
  > - [zhiantec,zfm-x0](../gnss_fingerprint_binding_reference/P002_zhiantec_zfm-x0.md#std-dtcompatible-zhiantec-zfm-x0)（[GitHub #100139](https://github.com/zephyrproject-rtos/zephyr/issues/100139)）
- 蓝牙（Bluetooth）

  > - bflb,bl70x-bt-hci（[GitHub #104346](https://github.com/zephyrproject-rtos/zephyr/issues/104346)）
  > - [infineon,bt-hci-uart](../bluetooth_vendor_hci_binding_reference/P006_infineon_bt-hci-uart.md#std-dtcompatible-infineon-bt-hci-uart)（[GitHub #103871](https://github.com/zephyrproject-rtos/zephyr/issues/103871)）
  > - [realtek,bee-bt-hci](../bluetooth_vendor_hci_binding_reference/P011_realtek_bee-bt-hci.md#std-dtcompatible-realtek-bee-bt-hci)（[GitHub #104580](https://github.com/zephyrproject-rtos/zephyr/issues/104580)）
  > - [sifli,sf32lb-mailbox](../bluetooth_vendor_hci_binding_reference/P014_sifli_sf32lb-mailbox.md#std-dtcompatible-sifli-sf32lb-mailbox)（[GitHub #96692](https://github.com/zephyrproject-rtos/zephyr/issues/96692)）
- 控制器局域网（CAN）

  > - [infineon,can](../can_adi_atmel_nxp_binding_reference/P007_infineon_can.md#std-dtcompatible-infineon-can)（[GitHub #105471](https://github.com/zephyrproject-rtos/zephyr/issues/105471)）
  > - [infineon,canfd-controller](../can_adi_atmel_nxp_binding_reference/P008_infineon_canfd-controller.md#std-dtcompatible-infineon-canfd-controller)（[GitHub #105471](https://github.com/zephyrproject-rtos/zephyr/issues/105471)）
- 充电器（Charger）

  > - [nordic,npm10xx-charger](../charger_binding_reference/P003_nordic_npm10xx-charger.md#std-dtcompatible-nordic-npm10xx-charger)（[GitHub #105564](https://github.com/zephyrproject-rtos/zephyr/issues/105564)）
  > - [ti,bq25186](../charger_binding_reference/P015_ti_bq25186.md#std-dtcompatible-ti-bq25186)（[GitHub #97157](https://github.com/zephyrproject-rtos/zephyr/issues/97157)）
  > - [ti,bq25188](../charger_binding_reference/P016_ti_bq25188.md#std-dtcompatible-ti-bq25188)（[GitHub #97157](https://github.com/zephyrproject-rtos/zephyr/issues/97157)）
  > - [zephyr,charger-gpio](../charger_binding_reference/P019_zephyr_charger-gpio.md#std-dtcompatible-zephyr-charger-gpio)（[GitHub #103112](https://github.com/zephyrproject-rtos/zephyr/issues/103112)）
- 时钟控制（Clock Control）

  > - [alif,clockctrl](../clock_adi_atmel_bflb_binding_reference/P006_alif_clockctrl.md#std-dtcompatible-alif-clockctrl)（[GitHub #101244](https://github.com/zephyrproject-rtos/zephyr/issues/101244)）
  > - [bflb,bl70x_l-clock-controller](../clock_adi_atmel_bflb_binding_reference/P018_bflb_bl70x_l-clock-controller.md#std-dtcompatible-bflb-bl70x_l-clock-controller)（[GitHub #104625](https://github.com/zephyrproject-rtos/zephyr/issues/104625)）
  > - [bflb,bl70x_l-dll](../clock_adi_atmel_bflb_binding_reference/P019_bflb_bl70x_l-dll.md#std-dtcompatible-bflb-bl70x_l-dll)（[GitHub #104625](https://github.com/zephyrproject-rtos/zephyr/issues/104625)）
  > - [bflb,f32k](../clock_adi_atmel_bflb_binding_reference/P022_bflb_f32k.md#std-dtcompatible-bflb-f32k)（[GitHub #104738](https://github.com/zephyrproject-rtos/zephyr/issues/104738)）
  > - [bflb,pll](../clock_adi_atmel_bflb_binding_reference/P025_bflb_pll.md#std-dtcompatible-bflb-pll)（[GitHub #104738](https://github.com/zephyrproject-rtos/zephyr/issues/104738)）
  > - [bflb,root-clk](../clock_esp_infineon_microchip_binding_reference/P001_bflb_root-clk.md#std-dtcompatible-bflb-root-clk)（[GitHub #104738](https://github.com/zephyrproject-rtos/zephyr/issues/104738)）
  > - [elan,em32-ahb](../clock_esp_infineon_microchip_binding_reference/P002_elan_em32-ahb.md#std-dtcompatible-elan-em32-ahb)（[GitHub #97843](https://github.com/zephyrproject-rtos/zephyr/issues/97843)）
  > - [elan,em32-apb](../clock_esp_infineon_microchip_binding_reference/P003_elan_em32-apb.md#std-dtcompatible-elan-em32-apb)（[GitHub #97843](https://github.com/zephyrproject-rtos/zephyr/issues/97843)）
  > - [focaltech,ft9001-cpm](../clock_esp_infineon_microchip_binding_reference/P005_focaltech_ft9001-cpm.md#std-dtcompatible-focaltech-ft9001-cpm)（[GitHub #95959](https://github.com/zephyrproject-rtos/zephyr/issues/95959)）
  > - [microchip,pic32cm-jh-clock](../clock_microchip_pic32_binding_reference/P007_microchip_pic32cm-jh-clock.md#std-dtcompatible-microchip-pic32cm-jh-clock)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-fdpll](../clock_microchip_pic32_binding_reference/P008_microchip_pic32cm-jh-fdpll.md#std-dtcompatible-microchip-pic32cm-jh-fdpll)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-gclkgen](../clock_microchip_pic32_binding_reference/P009_microchip_pic32cm-jh-gclkgen.md#std-dtcompatible-microchip-pic32cm-jh-gclkgen)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-gclkperiph](../clock_microchip_pic32_binding_reference/P010_microchip_pic32cm-jh-gclkperiph.md#std-dtcompatible-microchip-pic32cm-jh-gclkperiph)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-mclkcpu](../clock_microchip_pic32_binding_reference/P011_microchip_pic32cm-jh-mclkcpu.md#std-dtcompatible-microchip-pic32cm-jh-mclkcpu)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-mclkperiph](../clock_microchip_pic32_binding_reference/P012_microchip_pic32cm-jh-mclkperiph.md#std-dtcompatible-microchip-pic32cm-jh-mclkperiph)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-osc32k](../clock_microchip_pic32_binding_reference/P013_microchip_pic32cm-jh-osc32k.md#std-dtcompatible-microchip-pic32cm-jh-osc32k)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-osc48m](../clock_microchip_pic32_binding_reference/P014_microchip_pic32cm-jh-osc48m.md#std-dtcompatible-microchip-pic32cm-jh-osc48m)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-rtc](../clock_microchip_pic32_binding_reference/P015_microchip_pic32cm-jh-rtc.md#std-dtcompatible-microchip-pic32cm-jh-rtc)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-xosc](../clock_microchip_pic32_binding_reference/P016_microchip_pic32cm-jh-xosc.md#std-dtcompatible-microchip-pic32cm-jh-xosc)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-jh-xosc32k](../clock_microchip_pic32_binding_reference/P017_microchip_pic32cm-jh-xosc32k.md#std-dtcompatible-microchip-pic32cm-jh-xosc32k)（[GitHub #97160](https://github.com/zephyrproject-rtos/zephyr/issues/97160)）
  > - [microchip,pic32cm-pl-clock](../clock_microchip_pic32_binding_reference/P018_microchip_pic32cm-pl-clock.md#std-dtcompatible-microchip-pic32cm-pl-clock)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-gclkgen](../clock_microchip_pic32_binding_reference/P019_microchip_pic32cm-pl-gclkgen.md#std-dtcompatible-microchip-pic32cm-pl-gclkgen)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-gclkperiph](../clock_microchip_pic32_binding_reference/P020_microchip_pic32cm-pl-gclkperiph.md#std-dtcompatible-microchip-pic32cm-pl-gclkperiph)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-mclkcpu](../clock_microchip_pic32_binding_reference/P021_microchip_pic32cm-pl-mclkcpu.md#std-dtcompatible-microchip-pic32cm-pl-mclkcpu)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-mclkperiph](../clock_microchip_pic32_binding_reference/P022_microchip_pic32cm-pl-mclkperiph.md#std-dtcompatible-microchip-pic32cm-pl-mclkperiph)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-osc32k](../clock_microchip_pic32_binding_reference/P023_microchip_pic32cm-pl-osc32k.md#std-dtcompatible-microchip-pic32cm-pl-osc32k)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-oschf](../clock_microchip_pic32_binding_reference/P024_microchip_pic32cm-pl-oschf.md#std-dtcompatible-microchip-pic32cm-pl-oschf)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-rtc](../clock_microchip_pic32_binding_reference/P025_microchip_pic32cm-pl-rtc.md#std-dtcompatible-microchip-pic32cm-pl-rtc)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cm-pl-xosc32k](../clock_microchip_pic32_sam_binding_reference/P001_microchip_pic32cm-pl-xosc32k.md#std-dtcompatible-microchip-pic32cm-pl-xosc32k)（[GitHub #104337](https://github.com/zephyrproject-rtos/zephyr/issues/104337)）
  > - [microchip,pic32cz-ca-clock](../clock_microchip_pic32_sam_binding_reference/P012_microchip_pic32cz-ca-clock.md#std-dtcompatible-microchip-pic32cz-ca-clock)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-dfll48m](../clock_microchip_pic32_sam_binding_reference/P013_microchip_pic32cz-ca-dfll48m.md#std-dtcompatible-microchip-pic32cz-ca-dfll48m)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-dpll](../clock_microchip_pic32_sam_binding_reference/P014_microchip_pic32cz-ca-dpll.md#std-dtcompatible-microchip-pic32cz-ca-dpll)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-gclkgen](../clock_microchip_pic32_sam_binding_reference/P015_microchip_pic32cz-ca-gclkgen.md#std-dtcompatible-microchip-pic32cz-ca-gclkgen)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-gclkperiph](../clock_microchip_pic32_sam_binding_reference/P016_microchip_pic32cz-ca-gclkperiph.md#std-dtcompatible-microchip-pic32cz-ca-gclkperiph)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-mclkdomain](../clock_microchip_pic32_sam_binding_reference/P017_microchip_pic32cz-ca-mclkdomain.md#std-dtcompatible-microchip-pic32cz-ca-mclkdomain)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-mclkperiph](../clock_microchip_pic32_sam_binding_reference/P018_microchip_pic32cz-ca-mclkperiph.md#std-dtcompatible-microchip-pic32cz-ca-mclkperiph)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-rtc](../clock_microchip_pic32_sam_binding_reference/P019_microchip_pic32cz-ca-rtc.md#std-dtcompatible-microchip-pic32cz-ca-rtc)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-xosc](../clock_microchip_pic32_sam_binding_reference/P020_microchip_pic32cz-ca-xosc.md#std-dtcompatible-microchip-pic32cz-ca-xosc)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [microchip,pic32cz-ca-xosc32k](../clock_microchip_pic32_sam_binding_reference/P021_microchip_pic32cz-ca-xosc32k.md#std-dtcompatible-microchip-pic32cz-ca-xosc32k)（[GitHub #101934](https://github.com/zephyrproject-rtos/zephyr/issues/101934)）
  > - [nordic,nrf71-hfxo](../clock_sam_nordic_binding_reference/P030_nordic_nrf71-hfxo.md#std-dtcompatible-nordic-nrf71-hfxo)（[GitHub #103349](https://github.com/zephyrproject-rtos/zephyr/issues/103349)）
  > - [nordic,nrf71-lfxo](../clock_nordic_nuvoton_nxp_binding_reference/P001_nordic_nrf71-lfxo.md#std-dtcompatible-nordic-nrf71-lfxo)（[GitHub #101199](https://github.com/zephyrproject-rtos/zephyr/issues/101199)）
  > - [realtek,ameba-rcc](../clock_nxp_pico_realtek_renesas_binding_reference/P021_realtek_ameba-rcc.md#std-dtcompatible-realtek-ameba-rcc)（[GitHub #104843](https://github.com/zephyrproject-rtos/zephyr/issues/104843)）
  > - [realtek,bee-cctl](../clock_nxp_pico_realtek_renesas_binding_reference/P022_realtek_bee-cctl.md#std-dtcompatible-realtek-bee-cctl)（[GitHub #102691](https://github.com/zephyrproject-rtos/zephyr/issues/102691)）
  > - [realtek,rts5817-clock](../clock_nxp_pico_realtek_renesas_binding_reference/P023_realtek_rts5817-clock.md#std-dtcompatible-realtek-rts5817-clock)（[GitHub #91486](https://github.com/zephyrproject-rtos/zephyr/issues/91486)）
  > - [renesas,r8a779g0-cpg-mssr](../clock_nxp_pico_realtek_renesas_binding_reference/P027_renesas_r8a779g0-cpg-mssr.md#std-dtcompatible-renesas-r8a779g0-cpg-mssr)（[GitHub #97783](https://github.com/zephyrproject-rtos/zephyr/issues/97783)）
  > - [st,stm32c5-rcc](../timer_reference/P180_STM32C5复位与时钟控制绑定.md#dtbinding-st-stm32c5-rcc)（[GitHub #105577](https://github.com/zephyrproject-rtos/zephyr/issues/105577)）
  > - [st,stm32c5-xsik-clock](../timer_reference/P166_STM32C5派生时钟绑定.md#dtbinding-st-stm32c5-xsik-clock)（[GitHub #105577](https://github.com/zephyrproject-rtos/zephyr/issues/105577)）
  > - [st,stm32fx-pll-clock](../timer_reference/P128_STM32Fx锁相环时钟绑定.md#dtbinding-st-stm32fx-pll-clock)（[GitHub #100757](https://github.com/zephyrproject-rtos/zephyr/issues/100757)）
  > - [syna,sr100-clock](../clock_silabs_ti_xilinx_binding_reference/P018_syna_sr100-clock.md#std-dtcompatible-syna-sr100-clock)（[GitHub #100172](https://github.com/zephyrproject-rtos/zephyr/issues/100172)）
  > - [ti,k2g-sci-clk](../clock_silabs_ti_xilinx_binding_reference/P024_ti_k2g-sci-clk.md#std-dtcompatible-ti-k2g-sci-clk)（[GitHub #90216](https://github.com/zephyrproject-rtos/zephyr/issues/90216)）
- 比较器（Comparator）

  > - [microchip,ac-g1-comparator](../hardware/P756_Microchip模拟比较器通道绑定.md#dtbinding-microchip-ac-g1-comparator)（[GitHub #99155](https://github.com/zephyrproject-rtos/zephyr/issues/99155)）
  > - [nxp,acomp](../hardware/P742_NXP模拟比较器绑定.md#dtbinding-nxp-acomp)（[GitHub #100818](https://github.com/zephyrproject-rtos/zephyr/issues/100818)）
  > - [nxp,hscmp](../hardware/P744_NXP高速比较器绑定.md#dtbinding-nxp-hscmp)（[GitHub #100629](https://github.com/zephyrproject-rtos/zephyr/issues/100629)）
  > - [nxp,lpcmp](../hardware/P747_NXP低功耗比较器绑定.md#dtbinding-nxp-lpcmp)（[GitHub #100998](https://github.com/zephyrproject-rtos/zephyr/issues/100998)）
- 计数器（Counter）

  > - [bflb,rtc](../counter_binding_reference/P012_bflb_rtc.md#std-dtcompatible-bflb-rtc)（[GitHub #104739](https://github.com/zephyrproject-rtos/zephyr/issues/104739)）
  > - [bflb,timer](../counter_binding_reference/P014_bflb_timer.md#std-dtcompatible-bflb-timer)（[GitHub #104739](https://github.com/zephyrproject-rtos/zephyr/issues/104739)）
  > - [bflb,timer-channel](../counter_binding_reference/P013_bflb_timer-channel.md#std-dtcompatible-bflb-timer-channel)（[GitHub #104739](https://github.com/zephyrproject-rtos/zephyr/issues/104739)）
  > - [microchip,rtc-g1-counter](../microchip_soc_counter_binding_reference/P007_microchip_rtc-g1-counter.md#std-dtcompatible-microchip-rtc-g1-counter)（[GitHub #102163](https://github.com/zephyrproject-rtos/zephyr/issues/102163)）
  > - [microchip,sam-pit64b-counter](../microchip_soc_counter_binding_reference/P008_microchip_sam-pit64b-counter.md#std-dtcompatible-microchip-sam-pit64b-counter)（[GitHub #93806](https://github.com/zephyrproject-rtos/zephyr/issues/93806)）
  > - [microchip,tc-g1](../microchip_soc_counter_binding_reference/P010_microchip_tc-g1.md#std-dtcompatible-microchip-tc-g1)（[GitHub #100070](https://github.com/zephyrproject-rtos/zephyr/issues/100070)）
  > - [microchip,tc-g1-counter](../microchip_soc_counter_binding_reference/P009_microchip_tc-g1-counter.md#std-dtcompatible-microchip-tc-g1-counter)（[GitHub #101941](https://github.com/zephyrproject-rtos/zephyr/issues/101941)）
  > - [microchip,tc-g2-counter](../microchip_soc_counter_binding_reference/P011_microchip_tc-g2-counter.md#std-dtcompatible-microchip-tc-g2-counter)（[GitHub #93401](https://github.com/zephyrproject-rtos/zephyr/issues/93401)）
  > - [microchip,tcc-g1-counter](../microchip_soc_counter_binding_reference/P012_microchip_tcc-g1-counter.md#std-dtcompatible-microchip-tcc-g1-counter)（[GitHub #100745](https://github.com/zephyrproject-rtos/zephyr/issues/100745)）
  > - [microcrystal,rv3032-counter](../microchip_soc_counter_binding_reference/P015_microcrystal_rv3032-counter.md#std-dtcompatible-microcrystal-rv3032-counter)（[GitHub #98918](https://github.com/zephyrproject-rtos/zephyr/issues/98918)）
  > - [nuvoton,npck-lct](../microchip_soc_counter_binding_reference/P018_nuvoton_npck-lct.md#std-dtcompatible-nuvoton-npck-lct)（[GitHub #98548](https://github.com/zephyrproject-rtos/zephyr/issues/98548)）
  > - [nuvoton,npcx-lct-base](../nxp_nuvoton_counter_binding_reference/P001_nuvoton_npcx-lct-base.md#std-dtcompatible-nuvoton-npcx-lct-base)（[GitHub #98548](https://github.com/zephyrproject-rtos/zephyr/issues/98548)）
  > - [nuvoton,npcx-lct-v1](../nxp_nuvoton_counter_binding_reference/P002_nuvoton_npcx-lct-v1.md#std-dtcompatible-nuvoton-npcx-lct-v1)（[GitHub #98548](https://github.com/zephyrproject-rtos/zephyr/issues/98548)）
  > - [nuvoton,npcx-lct-v2](../nxp_nuvoton_counter_binding_reference/P003_nuvoton_npcx-lct-v2.md#std-dtcompatible-nuvoton-npcx-lct-v2)（[GitHub #98548](https://github.com/zephyrproject-rtos/zephyr/issues/98548)）
  > - [nxp,imx-gpt](../nxp_nuvoton_counter_binding_reference/P004_nxp_imx-gpt.md#std-dtcompatible-nxp-imx-gpt)（[GitHub #101040](https://github.com/zephyrproject-rtos/zephyr/issues/101040)）
  > - [raspberrypi,pico-pit](../renesas_realtek_counter_binding_reference/P007_raspberrypi_pico-pit.md#std-dtcompatible-raspberrypi-pico-pit)（[GitHub #85618](https://github.com/zephyrproject-rtos/zephyr/issues/85618)）
  > - [raspberrypi,pico-pit-channel](../renesas_realtek_counter_binding_reference/P006_raspberrypi_pico-pit-channel.md#std-dtcompatible-raspberrypi-pico-pit-channel)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
  > - [realtek,bee-counter-timer](../renesas_realtek_counter_binding_reference/P011_realtek_bee-counter-timer.md#std-dtcompatible-realtek-bee-counter-timer)（[GitHub #104805](https://github.com/zephyrproject-rtos/zephyr/issues/104805)）
  > - [renesas,rza2m-ostm-counter](../stm32_ti_xilinx_counter_binding_reference/P001_renesas_rza2m-ostm-counter.md#std-dtcompatible-renesas-rza2m-ostm-counter)（[GitHub #100934](https://github.com/zephyrproject-rtos/zephyr/issues/100934)）
  > - [silabs,burtc-counter](../stm32_ti_xilinx_counter_binding_reference/P003_silabs_burtc-counter.md#std-dtcompatible-silabs-burtc-counter)（[GitHub #102272](https://github.com/zephyrproject-rtos/zephyr/issues/102272)）
  > - [silabs,protimer](../stm32_ti_xilinx_counter_binding_reference/P004_silabs_protimer.md#std-dtcompatible-silabs-protimer)（[GitHub #103428](https://github.com/zephyrproject-rtos/zephyr/issues/103428)）
  > - [silabs,timer-counter](../stm32_ti_xilinx_counter_binding_reference/P005_silabs_timer-counter.md#std-dtcompatible-silabs-timer-counter)（[GitHub #103885](https://github.com/zephyrproject-rtos/zephyr/issues/103885)）
- 中央处理器（CPU）

  > - [adi,max32-rv32](../cpu_arm_riscv_binding_reference/P002_adi_max32-rv32.md#std-dtcompatible-adi-max32-rv32)（[GitHub #97309](https://github.com/zephyrproject-rtos/zephyr/issues/97309)）
  > - [arm,cortex-a320](../cpu_arm_riscv_binding_reference/P006_arm_cortex-a320.md#std-dtcompatible-arm-cortex-a320)（[GitHub #96852](https://github.com/zephyrproject-rtos/zephyr/issues/96852)）
  > - [arm,cortex-a510](../cpu_arm_riscv_binding_reference/P007_arm_cortex-a510.md#std-dtcompatible-arm-cortex-a510)（[GitHub #96852](https://github.com/zephyrproject-rtos/zephyr/issues/96852)）
  > - [arm,cortex-a7](../cpu_arm_riscv_binding_reference/P011_arm_cortex-a7.md#std-dtcompatible-arm-cortex-a7)（[GitHub #101582](https://github.com/zephyrproject-rtos/zephyr/issues/101582)）
  > - [arm,cortex-a9](../cpu_arm_riscv_binding_reference/P016_arm_cortex-a9.md#std-dtcompatible-arm-cortex-a9)（[GitHub #101582](https://github.com/zephyrproject-rtos/zephyr/issues/101582)）
  > - [cdns,swerv,s400](../cpu_cortex_xtensa_binding_reference/P017_cdns_swerv_s400.md#std-dtcompatible-cdns-swerv-s400)（[GitHub #102288](https://github.com/zephyrproject-rtos/zephyr/issues/102288)）
  > - [cdns,swerv,s420](../cpu_cortex_xtensa_binding_reference/P018_cdns_swerv_s420.md#std-dtcompatible-cdns-swerv-s420)（[GitHub #102288](https://github.com/zephyrproject-rtos/zephyr/issues/102288)）
  > - [intel,wildcat-lake](../cpu_vendor_multiarc_binding_reference/P014_intel_wildcat-lake.md#std-dtcompatible-intel-wildcat-lake)（[GitHub #99205](https://github.com/zephyrproject-rtos/zephyr/issues/99205)）
  > - [riscv](../cpu_vendor_multiarc_binding_reference/P034_riscv.md#std-dtcompatible-riscv)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
  > - [spinalhdl,vexriscv](../cpu_vendor_multiarc_binding_reference/P046_spinalhdl_vexriscv.md#std-dtcompatible-spinalhdl-vexriscv)（[GitHub #97925](https://github.com/zephyrproject-rtos/zephyr/issues/97925)）
- 循环冗余校验（CRC）

  > - [nxp,crc](../crc_clock_monitor_binding_reference/P006_nxp_crc.md#std-dtcompatible-nxp-crc)（[GitHub #100875](https://github.com/zephyrproject-rtos/zephyr/issues/100875)）
  > - [nxp,lpc-crc](../crc_clock_monitor_binding_reference/P007_nxp_lpc-crc.md#std-dtcompatible-nxp-lpc-crc)（[GitHub #101528](https://github.com/zephyrproject-rtos/zephyr/issues/101528)）
  > - [sifli,sf32lb-crc](../crc_clock_monitor_binding_reference/P009_sifli_sf32lb-crc.md#std-dtcompatible-sifli-sf32lb-crc)（[GitHub #98997](https://github.com/zephyrproject-rtos/zephyr/issues/98997)）
  > - [silabs,gpcrc](../crc_clock_monitor_binding_reference/P010_silabs_gpcrc.md#std-dtcompatible-silabs-gpcrc)（[GitHub #104471](https://github.com/zephyrproject-rtos/zephyr/issues/104471)）
  > - [st,stm32-crc](../crc_clock_monitor_binding_reference/P011_st_stm32-crc.md#std-dtcompatible-st-stm32-crc)（[GitHub #105302](https://github.com/zephyrproject-rtos/zephyr/issues/105302)）
- 密码学加速器（Cryptographic Accelerator）

  > - [bflb,sec-eng-aes](../crypto_aes_sha_ccm_binding_reference/P004_bflb_sec-eng-aes.md#std-dtcompatible-bflb-sec-eng-aes)（[GitHub #104371](https://github.com/zephyrproject-rtos/zephyr/issues/104371)）
  > - [bflb,sec-eng-sha](../crypto_aes_sha_ccm_binding_reference/P005_bflb_sec-eng-sha.md#std-dtcompatible-bflb-sec-eng-sha)（[GitHub #104371](https://github.com/zephyrproject-rtos/zephyr/issues/104371)）
  > - [bflb,sec-eng-trng](../crypto_aes_sha_ccm_binding_reference/P006_bflb_sec-eng-trng.md#std-dtcompatible-bflb-sec-eng-trng)（[GitHub #104349](https://github.com/zephyrproject-rtos/zephyr/issues/104349)）
  > - [microchip,aes-g1](../crypto_aes_sha_ccm_binding_reference/P017_microchip_aes-g1.md#std-dtcompatible-microchip-aes-g1)（[GitHub #105389](https://github.com/zephyrproject-rtos/zephyr/issues/105389)）
  > - [microchip,sha-g1-crypto](../crypto_aes_sha_ccm_binding_reference/P018_microchip_sha-g1-crypto.md#std-dtcompatible-microchip-sha-g1-crypto)（[GitHub #98894](https://github.com/zephyrproject-rtos/zephyr/issues/98894)）
  > - [nxp,s32-crypto-hse-mu](../crypto_secure_engine_st_ti_binding_reference/P005_nxp_s32-crypto-hse-mu.md#std-dtcompatible-nxp-s32-crypto-hse-mu)（[GitHub #79351](https://github.com/zephyrproject-rtos/zephyr/issues/79351)）
  > - [raspberrypi,pico-sha256](../crypto_secure_engine_st_ti_binding_reference/P006_raspberrypi_pico-sha256.md#std-dtcompatible-raspberrypi-pico-sha256)（[GitHub #85036](https://github.com/zephyrproject-rtos/zephyr/issues/85036)）
  > - [sifli,sf32lb-crypto](../crypto_secure_engine_st_ti_binding_reference/P011_sifli_sf32lb-crypto.md#std-dtcompatible-sifli-sf32lb-crypto)（[GitHub #100583](https://github.com/zephyrproject-rtos/zephyr/issues/100583)）
- 数模转换器（DAC）

  > - [microchip,dac-g1](../hardware/P776_MicrochipG1数模转换器绑定.md#dtbinding-microchip-dac-g1)（[GitHub #101431](https://github.com/zephyrproject-rtos/zephyr/issues/101431)）
  > - [nxp,hpdac](../hardware/P767_NXPHPDAC数模转换器绑定.md#dtbinding-nxp-hpdac)（[GitHub #104642](https://github.com/zephyrproject-rtos/zephyr/issues/104642)）
  > - [ti,dac5311](../hardware/P807_DAC5311数模转换器绑定.md#dtbinding-ti-dac5311)（[GitHub #90811](https://github.com/zephyrproject-rtos/zephyr/issues/90811)）
  > - [ti,dac6311](../hardware/P811_DAC6311数模转换器绑定.md#dtbinding-ti-dac6311)（[GitHub #90811](https://github.com/zephyrproject-rtos/zephyr/issues/90811)）
  > - [ti,dac7311](../hardware/P814_DAC7311数模转换器绑定.md#dtbinding-ti-dac7311)（[GitHub #90811](https://github.com/zephyrproject-rtos/zephyr/issues/90811)）
  > - [ti,dac8311](../hardware/P816_DAC8311数模转换器绑定.md#dtbinding-ti-dac8311)（[GitHub #90811](https://github.com/zephyrproject-rtos/zephyr/issues/90811)）
  > - [ti,dac8411](../hardware/P817_DAC8411数模转换器绑定.md#dtbinding-ti-dac8411)（[GitHub #90811](https://github.com/zephyrproject-rtos/zephyr/issues/90811)）
  > - [zephyr,dac-emul](../hardware/P527_DAC仿真设备绑定.md#dtbinding-zephyr-dac-emul)（[GitHub #100306](https://github.com/zephyrproject-rtos/zephyr/issues/100306)）
- 磁盘（Disk）

  > - [zephyr,ftl-dhara](../storage_filesystem_binding_reference/P001_zephyr_ftl-dhara.md#std-dtcompatible-zephyr-ftl-dhara)（[GitHub #100858](https://github.com/zephyrproject-rtos/zephyr/issues/100858)）
- 显示（Display）

  > - [eink,ac057tc1](../display_adi_chipone_eink_binding_reference/P011_eink_ac057tc1.md#std-dtcompatible-eink-ac057tc1)（[GitHub #104142](https://github.com/zephyrproject-rtos/zephyr/issues/104142)）
  > - [ilitek,ili9163c](../display_ilitek_matrix_nxp_binding_reference/P002_ilitek_ili9163c.md#std-dtcompatible-ilitek-ili9163c)（[GitHub #104071](https://github.com/zephyrproject-rtos/zephyr/issues/104071)）
  > - [nxp,imx-lcdifv2](../display_ilitek_matrix_nxp_binding_reference/P019_nxp_imx-lcdifv2.md#std-dtcompatible-nxp-imx-lcdifv2)（[GitHub #103646](https://github.com/zephyrproject-rtos/zephyr/issues/103646)）
  > - [qemu,ramfb](../display_panel_renesas_sharp_binding_reference/P005_qemu_ramfb.md#std-dtcompatible-qemu-ramfb)（[GitHub #103887](https://github.com/zephyrproject-rtos/zephyr/issues/103887)）
  > - [sifli,sf32lb-lcdc](../display_panel_renesas_sharp_binding_reference/P016_sifli_sf32lb-lcdc.md#std-dtcompatible-sifli-sf32lb-lcdc)（[GitHub #99549](https://github.com/zephyrproject-rtos/zephyr/issues/99549)）
  > - [sitronix,st7586s](../display_sinowealth_sitronix_solomon_binding_reference/P008_sitronix_st7586s.md#std-dtcompatible-sitronix-st7586s)（[GitHub #103296](https://github.com/zephyrproject-rtos/zephyr/issues/103296)）
  > - [solomon,ssd1325](../compatible_binding_reference/P066_solomon_ssd1325.md#std-dtcompatible-solomon-ssd1325)（[GitHub #102128](https://github.com/zephyrproject-rtos/zephyr/issues/102128)）
  > - [waveshare,dsi2dpi](../display_st_ultrachip_zephyr_binding_reference/P010_waveshare_dsi2dpi.md#std-dtcompatible-waveshare-dsi2dpi)（[GitHub #100140](https://github.com/zephyrproject-rtos/zephyr/issues/100140)）
- 直接存储器访问（DMA）

  > - [infineon,dmac](../intel_microchip_dma_binding_reference/P001_infineon_dmac.md#std-dtcompatible-infineon-dmac)（[GitHub #101583](https://github.com/zephyrproject-rtos/zephyr/issues/101583)）
  > - [microchip,dmac-g1-dma](../intel_microchip_dma_binding_reference/P013_microchip_dmac-g1-dma.md#std-dtcompatible-microchip-dmac-g1-dma)（[GitHub #96300](https://github.com/zephyrproject-rtos/zephyr/issues/96300)）
  > - [microchip,dmac-g2-dma](../intel_microchip_dma_binding_reference/P014_microchip_dmac-g2-dma.md#std-dtcompatible-microchip-dmac-g2-dma)（[GitHub #104404](https://github.com/zephyrproject-rtos/zephyr/issues/104404)）
  > - [nxp,4ch-dma](../intel_microchip_dma_binding_reference/P018_nxp_4ch-dma.md#std-dtcompatible-nxp-4ch-dma)（[GitHub #97841](https://github.com/zephyrproject-rtos/zephyr/issues/97841)）
- 错误检测与纠正（EDAC）

  > - [nxp,eim](../edac_syscon_binding_reference/P002_nxp_eim.md#std-dtcompatible-nxp-eim)（[GitHub #94111](https://github.com/zephyrproject-rtos/zephyr/issues/94111)）
  > - [nxp,erm](../edac_syscon_binding_reference/P003_nxp_erm.md#std-dtcompatible-nxp-erm)（[GitHub #94111](https://github.com/zephyrproject-rtos/zephyr/issues/94111)）
- 以太网（Ethernet）

  > - [davicom,dm9051](../ethernet_mac_mdio_binding_reference/P007_davicom_dm9051.md#std-dtcompatible-davicom-dm9051)（[GitHub #104715](https://github.com/zephyrproject-rtos/zephyr/issues/104715)）
  > - [ethernet-phy-fixed-link](../ethernet_nxp_phy_binding_reference/P018_ethernet-phy-fixed-link.md#std-dtcompatible-ethernet-phy-fixed-link)（[GitHub #100454](https://github.com/zephyrproject-rtos/zephyr/issues/100454)）
  > - [maxlinear,gpy111](../ethernet_nxp_phy_binding_reference/P020_maxlinear_gpy111.md#std-dtcompatible-maxlinear-gpy111)（[GitHub #100995](https://github.com/zephyrproject-rtos/zephyr/issues/100995)）
  > - [microchip,lan8742](../ethernet_phy_renesas_rockchip_binding_reference/P003_microchip_lan8742.md#std-dtcompatible-microchip-lan8742)（[GitHub #96134](https://github.com/zephyrproject-rtos/zephyr/issues/96134)）
  > - [motorcomm,yt8521](../ethernet_phy_renesas_rockchip_binding_reference/P007_motorcomm_yt8521.md#std-dtcompatible-motorcomm-yt8521)（[GitHub #97535](https://github.com/zephyrproject-rtos/zephyr/issues/97535)）
  > - [motorcomm,yt8531](../ethernet_phy_renesas_rockchip_binding_reference/P008_motorcomm_yt8531.md#std-dtcompatible-motorcomm-yt8531)（[GitHub #104945](https://github.com/zephyrproject-rtos/zephyr/issues/104945)）
  > - [nxp,t1s-phy](../ethernet_phy_renesas_rockchip_binding_reference/P009_nxp_t1s-phy.md#std-dtcompatible-nxp-t1s-phy)（[GitHub #105033](https://github.com/zephyrproject-rtos/zephyr/issues/105033)）
  > - [renesas,ra-eswm](../ethernet_phy_renesas_rockchip_binding_reference/P015_renesas_ra-eswm.md#std-dtcompatible-renesas-ra-eswm)（[GitHub #100995](https://github.com/zephyrproject-rtos/zephyr/issues/100995)）
  > - [renesas,ra-ethernet-rmac](../ethernet_phy_renesas_rockchip_binding_reference/P016_renesas_ra-ethernet-rmac.md#std-dtcompatible-renesas-ra-ethernet-rmac)（[GitHub #100995](https://github.com/zephyrproject-rtos/zephyr/issues/100995)）
  > - [renesas,ra-mdio-rmac](../ethernet_mdio_microchip_binding_reference/P005_renesas_ra-mdio-rmac.md#std-dtcompatible-renesas-ra-mdio-rmac)（[GitHub #100995](https://github.com/zephyrproject-rtos/zephyr/issues/100995)）
  > - [st,stm32h5-ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P010_st_stm32h5-ethernet.md#std-dtcompatible-st-stm32h5-ethernet)（[GitHub #100910](https://github.com/zephyrproject-rtos/zephyr/issues/100910)）
  > - [st,stm32mp13-ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P012_st_stm32mp13-ethernet.md#std-dtcompatible-st-stm32mp13-ethernet)（[GitHub #96134](https://github.com/zephyrproject-rtos/zephyr/issues/96134)）
  > - [wch,ethernet](../ethernet_synopsys_st_xilinx_binding_reference/P016_wch_ethernet.md#std-dtcompatible-wch-ethernet)（[GitHub #101390](https://github.com/zephyrproject-rtos/zephyr/issues/101390)）
  > - wch,ethernet-controller（[GitHub #101390](https://github.com/zephyrproject-rtos/zephyr/issues/101390)）
  > - wch,mdio（[GitHub #101390](https://github.com/zephyrproject-rtos/zephyr/issues/101390)）
  > - [wiznet,w6100](../ethernet_synopsys_st_xilinx_binding_reference/P019_wiznet_w6100.md#std-dtcompatible-wiznet-w6100)（[GitHub #101753](https://github.com/zephyrproject-rtos/zephyr/issues/101753)）
  > - xlnx,xps-ethernetlite-1.00.a（[GitHub #95073](https://github.com/zephyrproject-rtos/zephyr/issues/95073)）
  > - xlnx,xps-ethernetlite-1.00.a-mac（[GitHub #95073](https://github.com/zephyrproject-rtos/zephyr/issues/95073)）
  > - xlnx,xps-ethernetlite-1.00.a-mdio（[GitHub #103944](https://github.com/zephyrproject-rtos/zephyr/issues/103944)）
  > - xlnx,xps-ethernetlite-3.00.a（[GitHub #95073](https://github.com/zephyrproject-rtos/zephyr/issues/95073)）
  > - xlnx,xps-ethernetlite-3.00.a-mac（[GitHub #95073](https://github.com/zephyrproject-rtos/zephyr/issues/95073)）
  > - xlnx,xps-ethernetlite-3.00.a-mdio（[GitHub #103944](https://github.com/zephyrproject-rtos/zephyr/issues/103944)）
- 固件（Firmware）

  > - [arm,scmi-smc](../hardware/P601_SCMI安全调用传输绑定.md#dtbinding-arm-scmi-smc)（[GitHub #103584](https://github.com/zephyrproject-rtos/zephyr/issues/103584)）
  > - [arm,scmi-system](../hardware/P607_SCMI系统电源协议绑定.md#dtbinding-arm-scmi-system)（[GitHub #99037](https://github.com/zephyrproject-rtos/zephyr/issues/99037)）
  > - [qemu,fw-cfg-ioport](../hardware/P609_QEMU固件配置端口绑定.md#dtbinding-qemu-fw-cfg-ioport)（[GitHub #103717](https://github.com/zephyrproject-rtos/zephyr/issues/103717)）
  > - [qemu,fw-cfg-mmio](../hardware/P610_QEMU固件配置内存映射绑定.md#dtbinding-qemu-fw-cfg-mmio)（[GitHub #103717](https://github.com/zephyrproject-rtos/zephyr/issues/103717)）
- 闪存控制器（Flash Controller）

  > - [nxp,c40-flash-controller](../flash_nuvoton_nxp_renesas_binding_reference/P008_nxp_c40-flash-controller.md#std-dtcompatible-nxp-c40-flash-controller)（[GitHub #97401](https://github.com/zephyrproject-rtos/zephyr/issues/97401)）
  > - [renesas,rza2m-qspi-spibsc](../flash_renesas_st_ti_binding_reference/P004_renesas_rza2m-qspi-spibsc.md#std-dtcompatible-renesas-rza2m-qspi-spibsc)（[GitHub #102175](https://github.com/zephyrproject-rtos/zephyr/issues/102175)）
  > - [st,stm32c5-flash-controller](../flash_renesas_st_ti_binding_reference/P015_st_stm32c5-flash-controller.md#std-dtcompatible-st-stm32c5-flash-controller)（[GitHub #105577](https://github.com/zephyrproject-rtos/zephyr/issues/105577)）
- 电量计（Fuel Gauge）

  > - [hycon,hy4245](../fuel_gauge_binding_reference/P003_hycon_hy4245.md#std-dtcompatible-hycon-hy4245)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
- 全球导航卫星系统（GNSS）

  > - [globaltop,pa6h](../gnss_fingerprint_binding_reference/P004_globaltop_pa6h.md#std-dtcompatible-globaltop-pa6h)（[GitHub #104789](https://github.com/zephyrproject-rtos/zephyr/issues/104789)）
- 通用输入输出（GPIO）

  > - [elan,em32-gpio](../gpio_connectors_bflb_esp_binding_reference/P018_elan_em32-gpio.md#std-dtcompatible-elan-em32-gpio)（[GitHub #97843](https://github.com/zephyrproject-rtos/zephyr/issues/97843)）
  > - espressif,esp-threadbr-header（[GitHub #99704](https://github.com/zephyrproject-rtos/zephyr/issues/99704)）
  > - [infineon,cyw43-gpio](../gpio_connectors_bflb_esp_binding_reference/P030_infineon_cyw43-gpio.md#std-dtcompatible-infineon-cyw43-gpio)（[GitHub #104728](https://github.com/zephyrproject-rtos/zephyr/issues/104728)）
  > - [infineon,shared-gpio](../gpio_infineon_intel_ite_microchip_binding_reference/P002_infineon_shared-gpio.md#std-dtcompatible-infineon-shared-gpio)（[GitHub #105081](https://github.com/zephyrproject-rtos/zephyr/issues/105081)）
  > - [microchip,xpro-header](../gpio_microchip_nordic_nuvoton_binding_reference/P005_microchip_xpro-header.md#std-dtcompatible-microchip-xpro-header)（[GitHub #98043](https://github.com/zephyrproject-rtos/zephyr/issues/98043)）
  > - [nordic,expansion-board-header](../gpio_microchip_nordic_nuvoton_binding_reference/P009_nordic_expansion-board-header.md#std-dtcompatible-nordic-expansion-board-header)（[GitHub #104138](https://github.com/zephyrproject-rtos/zephyr/issues/104138)）
  > - [nxp,sc18is606-gpio](../gpio_nxp_expanders_binding_reference/P027_nxp_sc18is606-gpio.md#std-dtcompatible-nxp-sc18is606-gpio)（[GitHub #100743](https://github.com/zephyrproject-rtos/zephyr/issues/100743)）
  > - [realtek,ameba-gpio](../gpio_raspberrypi_renesas_binding_reference/P010_realtek_ameba-gpio.md#std-dtcompatible-realtek-ameba-gpio)（[GitHub #78036](https://github.com/zephyrproject-rtos/zephyr/issues/78036)）
  > - [realtek,bee-gpio](../gpio_raspberrypi_renesas_binding_reference/P011_realtek_bee-gpio.md#std-dtcompatible-realtek-bee-gpio)（[GitHub #102691](https://github.com/zephyrproject-rtos/zephyr/issues/102691)）
  > - [renesas,rz-gpio-common](../gpio_raspberrypi_renesas_binding_reference/P022_renesas_rz-gpio-common.md#std-dtcompatible-renesas-rz-gpio-common)（[GitHub #101256](https://github.com/zephyrproject-rtos/zephyr/issues/101256)）
  > - [renesas,rz-gpio-common-v2](../gpio_raspberrypi_renesas_binding_reference/P020_renesas_rz-gpio-common-v2.md#std-dtcompatible-renesas-rz-gpio-common-v2)（[GitHub #101256](https://github.com/zephyrproject-rtos/zephyr/issues/101256)）
  > - [renesas,rz-gpio-common-v3](../gpio_raspberrypi_renesas_binding_reference/P021_renesas_rz-gpio-common-v3.md#std-dtcompatible-renesas-rz-gpio-common-v3)（[GitHub #104804](https://github.com/zephyrproject-rtos/zephyr/issues/104804)）
  > - [solderedelectronics,easyc-connector](../gpio_silabs_st_connectors_binding_reference/P022_solderedelectronics_easyc-connector.md#std-dtcompatible-solderedelectronics-easyc-connector)（[GitHub #104919](https://github.com/zephyrproject-rtos/zephyr/issues/104919)）
- 触觉反馈（Haptics）

  > - cirrus,cs40l5x（[GitHub #100042](https://github.com/zephyrproject-rtos/zephyr/issues/100042)）
- 硬件信息（Hardware Information）

  > - [microchip,hwinfo-g1](../hwinfo_binding_reference/P005_microchip_hwinfo-g1.md#std-dtcompatible-microchip-hwinfo-g1)（[GitHub #100147](https://github.com/zephyrproject-rtos/zephyr/issues/100147)）
  > - [nxp,rcm-hwinfo](../hwinfo_binding_reference/P012_nxp_rcm-hwinfo.md#std-dtcompatible-nxp-rcm-hwinfo)（[GitHub #102490](https://github.com/zephyrproject-rtos/zephyr/issues/102490)）
  > - [nxp,sim-uuid](../hwinfo_binding_reference/P014_nxp_sim-uuid.md#std-dtcompatible-nxp-sim-uuid)（[GitHub #102490](https://github.com/zephyrproject-rtos/zephyr/issues/102490)）
- 硬件自旋锁（Hardware Spinlock）

  > - [nxp,sema42](../intercore_reference/P011_NXP硬件信号量设备树绑定.md#dtbinding-nxp-sema42)（[GitHub #101499](https://github.com/zephyrproject-rtos/zephyr/issues/101499)）
- 集成电路间总线（I2C）

  > - [bflb,i2c](../i2c_adi_atmel_esp_binding_reference/P012_bflb_i2c.md#std-dtcompatible-bflb-i2c)（[GitHub #98364](https://github.com/zephyrproject-rtos/zephyr/issues/98364)）
  > - [microchip,sercom-g1-i2c](../i2c_infineon_ite_nordic_binding_reference/P012_microchip_sercom-g1-i2c.md#std-dtcompatible-microchip-sercom-g1-i2c)（[GitHub #98385](https://github.com/zephyrproject-rtos/zephyr/issues/98385)）
  > - [renesas,rza2m-riic](../i2c_nxp_pico_renesas_binding_reference/P019_renesas_rza2m-riic.md#std-dtcompatible-renesas-rza2m-riic)（[GitHub #100513](https://github.com/zephyrproject-rtos/zephyr/issues/100513)）
  > - [sifli,sf32lb-i2c](../i2c_stm32_ti_mux_binding_reference/P003_sifli_sf32lb-i2c.md#std-dtcompatible-sifli-sf32lb-i2c)（[GitHub #96316](https://github.com/zephyrproject-rtos/zephyr/issues/96316)）
- 集成电路间音频总线（I2S）

  > - [adi,max32-i2s](../i2s_binding_reference/P001_adi_max32-i2s.md#std-dtcompatible-adi-max32-i2s)（[GitHub #91508](https://github.com/zephyrproject-rtos/zephyr/issues/91508)）
  > - [infineon,i2s](../i2s_binding_reference/P004_infineon_i2s.md#std-dtcompatible-infineon-i2s)（[GitHub #100606](https://github.com/zephyrproject-rtos/zephyr/issues/100606)）
- 输入（Input）

  > - [adafruit,seesaw-gamepad](../input_adc_touch_matrix_binding_reference/P001_adafruit_seesaw-gamepad.md#std-dtcompatible-adafruit-seesaw-gamepad)（[GitHub #105508](https://github.com/zephyrproject-rtos/zephyr/issues/105508)）
  > - [bflb,irx](../input_adc_touch_matrix_binding_reference/P006_bflb_irx.md#std-dtcompatible-bflb-irx)（[GitHub #100600](https://github.com/zephyrproject-rtos/zephyr/issues/100600)）
  > - [chipsemi,chsc6540](../input_adc_touch_matrix_binding_reference/P008_chipsemi_chsc6540.md#std-dtcompatible-chipsemi-chsc6540)（[GitHub #104710](https://github.com/zephyrproject-rtos/zephyr/issues/104710)）
  > - [focaltech,ft6146](../input_adc_touch_matrix_binding_reference/P015_focaltech_ft6146.md#std-dtcompatible-focaltech-ft6146)（[GitHub #96330](https://github.com/zephyrproject-rtos/zephyr/issues/96330)）
  > - [hynitron,cst8xx](../input_adc_touch_matrix_binding_reference/P020_hynitron_cst8xx.md#std-dtcompatible-hynitron-cst8xx)（[GitHub #105348](https://github.com/zephyrproject-rtos/zephyr/issues/105348)）
  > - [nxp,tsi-input](../input_keyboard_optical_ctsu_binding_reference/P011_nxp_tsi-input.md#std-dtcompatible-nxp-tsi-input)（[GitHub #103116](https://github.com/zephyrproject-rtos/zephyr/issues/103116)）
  > - [parade,tma525b](../input_keyboard_optical_ctsu_binding_reference/P012_parade_tma525b.md#std-dtcompatible-parade-tma525b)（[GitHub #101254](https://github.com/zephyrproject-rtos/zephyr/issues/101254)）
  > - [realtek,bee-keyscan](../input_keyboard_optical_ctsu_binding_reference/P016_realtek_bee-keyscan.md#std-dtcompatible-realtek-bee-keyscan)（[GitHub #105110](https://github.com/zephyrproject-rtos/zephyr/issues/105110)）
  > - [wch,ch9350l](../input_touch_lvgl_gesture_binding_reference/P012_wch_ch9350l.md#std-dtcompatible-wch-ch9350l)（[GitHub #101976](https://github.com/zephyrproject-rtos/zephyr/issues/101976)）
- 中断控制器（Interrupt Controller）

  > - [adi,max32-rv32-intc](../soc_interrupt_binding_reference/P001_adi_max32-rv32-intc.md#std-dtcompatible-adi-max32-rv32-intc)（[GitHub #97309](https://github.com/zephyrproject-rtos/zephyr/issues/97309)）
  > - [cdns,swerv-pic](../riscv_interrupt_binding_reference/P009_cdns_swerv-pic.md#std-dtcompatible-cdns-swerv-pic)（[GitHub #102288](https://github.com/zephyrproject-rtos/zephyr/issues/102288)）
  > - [microchip,aic-g1-intc](../infineon_microchip_interrupt_binding_reference/P005_microchip_aic-g1-intc.md#std-dtcompatible-microchip-aic-g1-intc)（[GitHub #101016](https://github.com/zephyrproject-rtos/zephyr/issues/101016)）
  > - [microchip,eic-g1-intc](../infineon_microchip_interrupt_binding_reference/P007_microchip_eic-g1-intc.md#std-dtcompatible-microchip-eic-g1-intc)（[GitHub #100928](https://github.com/zephyrproject-rtos/zephyr/issues/100928)）
  > - [nxp,gint](../nxp_interrupt_binding_reference/P001_nxp_gint.md#std-dtcompatible-nxp-gint)（[GitHub #100240](https://github.com/zephyrproject-rtos/zephyr/issues/100240)）
  > - [opencores,or1k-pic-level](../soc_interrupt_binding_reference/P012_opencores_or1k-pic-level.md#std-dtcompatible-opencores-or1k-pic-level)（[GitHub #98160](https://github.com/zephyrproject-rtos/zephyr/issues/98160)）
  > - [renesas,rx-grp-intc](../renesas_interrupt_binding_reference/P001_renesas_rx-grp-intc.md#std-dtcompatible-renesas-rx-grp-intc)（[GitHub #96451](https://github.com/zephyrproject-rtos/zephyr/issues/96451)）
  > - [renesas,rz-icu-v2](../renesas_interrupt_binding_reference/P005_renesas_rz-icu-v2.md#std-dtcompatible-renesas-rz-icu-v2)（[GitHub #104804](https://github.com/zephyrproject-rtos/zephyr/issues/104804)）
  > - [renesas,rz-intc-v2](../renesas_interrupt_binding_reference/P007_renesas_rz-intc-v2.md#std-dtcompatible-renesas-rz-intc-v2)（[GitHub #101256](https://github.com/zephyrproject-rtos/zephyr/issues/101256)）
  > - [renesas,rz-tint](../renesas_interrupt_binding_reference/P009_renesas_rz-tint.md#std-dtcompatible-renesas-rz-tint)（[GitHub #101256](https://github.com/zephyrproject-rtos/zephyr/issues/101256)）
  > - [riscv,aplic](../interrupt_fabric_binding_reference/P007_riscv_aplic.md#std-dtcompatible-riscv-aplic)（[GitHub #104730](https://github.com/zephyrproject-rtos/zephyr/issues/104730)）
  > - [riscv,imsic](../interrupt_fabric_binding_reference/P008_riscv_imsic.md#std-dtcompatible-riscv-imsic)（[GitHub #102055](https://github.com/zephyrproject-rtos/zephyr/issues/102055)）
- 发光二极管（LED）

  > - [issi,is31fl3197](../led_issi_nordic_nxp_binding_reference/P007_issi_is31fl3197.md#std-dtcompatible-issi-is31fl3197)（[GitHub #96821](https://github.com/zephyrproject-rtos/zephyr/issues/96821)）
  > - [sct,sct2024](../led_sct_ti_xpowers_binding_reference/P001_sct_sct2024.md#std-dtcompatible-sct-sct2024)（[GitHub #98698](https://github.com/zephyrproject-rtos/zephyr/issues/98698)）
- 远距离无线通信（LoRa）

  > - [semtech,llcc68](../lora_ieee802154_binding_reference/P018_semtech_llcc68.md#std-dtcompatible-semtech-llcc68)（[GitHub #100705](https://github.com/zephyrproject-rtos/zephyr/issues/100705)）
  > - [semtech,sx1268](../lora_ieee802154_binding_reference/P022_semtech_sx1268.md#std-dtcompatible-semtech-sx1268)（[GitHub #100705](https://github.com/zephyrproject-rtos/zephyr/issues/100705)）
  > - [semtech,sx1278](../lora_ieee802154_binding_reference/P025_semtech_sx1278.md#std-dtcompatible-semtech-sx1278)（[GitHub #100705](https://github.com/zephyrproject-rtos/zephyr/issues/100705)）
- 邮箱（Mailbox）

  > - [adi,mbox-max32-sema](../intercore_reference/P032_ADI硬件信号量邮箱绑定.md#dtbinding-adi-mbox-max32-sema)（[GitHub #104547](https://github.com/zephyrproject-rtos/zephyr/issues/104547)）
  > - [raspberrypi,pico-mbox](../intercore_reference/P050_Pico邮箱绑定.md#dtbinding-raspberrypi-pico-mbox)（[GitHub #94502](https://github.com/zephyrproject-rtos/zephyr/issues/94502)）
  > - [xlnx,mbox-versal-ipi-mailbox](../intercore_reference/P057_Versal核间中断邮箱绑定.md#dtbinding-xlnx-mbox-versal-ipi-mailbox)（[GitHub #92768](https://github.com/zephyrproject-rtos/zephyr/issues/92768)）
- 管理组件传输协议（MCTP）

  > - [zephyr,mctp-i3c-controller](../lin_dali_mctp_sensor_bus_binding_reference/P008_zephyr_mctp-i3c-controller.md#std-dtcompatible-zephyr-mctp-i3c-controller)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
  > - [zephyr,mctp-i3c-endpoint](../lin_dali_mctp_sensor_bus_binding_reference/P009_zephyr_mctp-i3c-endpoint.md#std-dtcompatible-zephyr-mctp-i3c-endpoint)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
  > - [zephyr,mctp-i3c-target](../lin_dali_mctp_sensor_bus_binding_reference/P010_zephyr_mctp-i3c-target.md#std-dtcompatible-zephyr-mctp-i3c-target)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
- 存储器控制器（Memory Controller）

  > - [adi,max32-backup-sram](../memory_controller_hyperbus_smc_binding_reference/P001_adi_max32-backup-sram.md#std-dtcompatible-adi-max32-backup-sram)（[GitHub #104528](https://github.com/zephyrproject-rtos/zephyr/issues/104528)）
- 多功能设备（MFD）

  > - [adi,max2221x](../hardware/P697_MAX2221x多功能设备绑定.md#dtbinding-adi-max2221x)（[GitHub #97584](https://github.com/zephyrproject-rtos/zephyr/issues/97584)）
  > - [microcrystal,rv3032-mfd](../hardware/P712_RV3032多功能设备绑定.md#dtbinding-microcrystal-rv3032-mfd)（[GitHub #98918](https://github.com/zephyrproject-rtos/zephyr/issues/98918)）
  > - [nordic,npm10xx](../hardware/P684_nPM10xx多功能设备绑定.md#dtbinding-nordic-npm10xx)（[GitHub #105447](https://github.com/zephyrproject-rtos/zephyr/issues/105447)）
- MIPI显示总线接口（MIPI DBI）

  > - [bflb,dbi](../mipi_dbi_dsi_binding_reference/P001_bflb_dbi.md#std-dtcompatible-bflb-dbi)（[GitHub #98752](https://github.com/zephyrproject-rtos/zephyr/issues/98752)）
  > - [espressif,esp32-lcd-cam-mipi-dbi](../mipi_dbi_dsi_binding_reference/P002_espressif_esp32-lcd-cam-mipi-dbi.md#std-dtcompatible-espressif-esp32-lcd-cam-mipi-dbi)（[GitHub #99863](https://github.com/zephyrproject-rtos/zephyr/issues/99863)）
  > - [raspberrypi,pico-mipi-dbi-pio](../mipi_dbi_dsi_binding_reference/P006_raspberrypi_pico-mipi-dbi-pio.md#std-dtcompatible-raspberrypi-pico-mipi-dbi-pio)（[GitHub #91350](https://github.com/zephyrproject-rtos/zephyr/issues/91350)）
  > - [sifli,sf32lb-lcdc-mipi-dbi](../mipi_dbi_dsi_binding_reference/P008_sifli_sf32lb-lcdc-mipi-dbi.md#std-dtcompatible-sifli-sf32lb-lcdc-mipi-dbi)（[GitHub #99549](https://github.com/zephyrproject-rtos/zephyr/issues/99549)）
- 其他绑定（Miscellaneous）

  > - [adi,max2221x-misc](../misc_adi_nordic_binding_reference/P001_adi_max2221x-misc.md#std-dtcompatible-adi-max2221x-misc)（[GitHub #97584](https://github.com/zephyrproject-rtos/zephyr/issues/97584)）
  > - [espressif,esp32-lcd-cam](../misc_adi_nordic_binding_reference/P007_espressif_esp32-lcd-cam.md#std-dtcompatible-espressif-esp32-lcd-cam)（[GitHub #99863](https://github.com/zephyrproject-rtos/zephyr/issues/99863)）
  > - [nordic,axon](../misc_adi_nordic_binding_reference/P012_nordic_axon.md#std-dtcompatible-nordic-axon)（[GitHub #102160](https://github.com/zephyrproject-rtos/zephyr/issues/102160)）
  > - [raspberrypi,pico-sio](../misc_nxp_renesas_zephyr_binding_reference/P013_raspberrypi_pico-sio.md#std-dtcompatible-raspberrypi-pico-sio)（[GitHub #94502](https://github.com/zephyrproject-rtos/zephyr/issues/94502)）
  > - [renesas,ra-drw](../misc_nxp_renesas_zephyr_binding_reference/P015_renesas_ra-drw.md#std-dtcompatible-renesas-ra-drw)（[GitHub #97163](https://github.com/zephyrproject-rtos/zephyr/issues/97163)）
  > - [renesas,ra-sau](../misc_nxp_renesas_zephyr_binding_reference/P019_renesas_ra-sau.md#std-dtcompatible-renesas-ra-sau)（[GitHub #102379](https://github.com/zephyrproject-rtos/zephyr/issues/102379)）
  > - [renesas,ra-sau-channel](../misc_nxp_renesas_zephyr_binding_reference/P018_renesas_ra-sau-channel.md#std-dtcompatible-renesas-ra-sau-channel)（[GitHub #102379](https://github.com/zephyrproject-rtos/zephyr/issues/102379)）
  > - [skyworks,sky13348](../misc_nxp_renesas_zephyr_binding_reference/P032_skyworks_sky13348.md#std-dtcompatible-skyworks-sky13348)（[GitHub #102321](https://github.com/zephyrproject-rtos/zephyr/issues/102321)）
  > - [st,stm32-npu-cache](../misc_nxp_renesas_zephyr_binding_reference/P036_st_stm32-npu-cache.md#std-dtcompatible-st-stm32-npu-cache)（[GitHub #102232](https://github.com/zephyrproject-rtos/zephyr/issues/102232)）
- 调制解调器（Modem）

  > - [st,st87mxx](../modem_sierra_telit_ublox_binding_reference/P002_st_st87mxx.md#std-dtcompatible-st-st87mxx)（[GitHub #100366](https://github.com/zephyrproject-rtos/zephyr/issues/100366)）
- 多位串行外设接口（Multi-Bit SPI）

  > - [st,stm32-ospi-controller](../mspi_binding_reference/P012_st_stm32-ospi-controller.md#std-dtcompatible-st-stm32-ospi-controller)（[GitHub #96670](https://github.com/zephyrproject-rtos/zephyr/issues/96670)）
  > - [st,stm32-qspi-controller](../mspi_binding_reference/P013_st_stm32-qspi-controller.md#std-dtcompatible-st-stm32-qspi-controller)（[GitHub #96670](https://github.com/zephyrproject-rtos/zephyr/issues/96670)）
  > - [st,stm32-xspi-controller](../mspi_binding_reference/P014_st_stm32-xspi-controller.md#std-dtcompatible-st-stm32-xspi-controller)（[GitHub #96670](https://github.com/zephyrproject-rtos/zephyr/issues/96670)）
- 存储技术设备（MTD）

  > - [jedec,spi-nand](../mtd_microchip_nordic_nxp_binding_reference/P001_jedec_spi-nand.md#std-dtcompatible-jedec-spi-nand)（[GitHub #100845](https://github.com/zephyrproject-rtos/zephyr/issues/100845)）
  > - [mxicy,mx25u](../mtd_microchip_nordic_nxp_binding_reference/P007_mxicy_mx25u-mspi.md#std-dtcompatible-mxicy-mx25u)（[GitHub #104357](https://github.com/zephyrproject-rtos/zephyr/issues/104357)）
  > - [netsol,s3axx04](../mtd_microchip_nordic_nxp_binding_reference/P009_netsol_s3axx04.md#std-dtcompatible-netsol-s3axx04)（[GitHub #97867](https://github.com/zephyrproject-rtos/zephyr/issues/97867)）
  > - [nxp,c40-flash](../mtd_microchip_nordic_nxp_binding_reference/P015_nxp_c40-flash.md#std-dtcompatible-nxp-c40-flash)（[GitHub #97401](https://github.com/zephyrproject-rtos/zephyr/issues/97401)）
  > - [nxp,imx-flexspi-is66wvs8m8](../mtd_microchip_nordic_nxp_binding_reference/P020_nxp_imx-flexspi-is66wvs8m8.md#std-dtcompatible-nxp-imx-flexspi-is66wvs8m8)（[GitHub #100976](https://github.com/zephyrproject-rtos/zephyr/issues/100976)）
  > - [nxp,s32-xspi-device](../mtd_nxp_st_ti_partition_binding_reference/P006_nxp_s32-xspi-device.md#std-dtcompatible-nxp-s32-xspi-device)（[GitHub #101487](https://github.com/zephyrproject-rtos/zephyr/issues/101487)）
  > - [nxp,s32-xspi-hyperram](../mtd_nxp_st_ti_partition_binding_reference/P007_nxp_s32-xspi-hyperram.md#std-dtcompatible-nxp-s32-xspi-hyperram)（[GitHub #101487](https://github.com/zephyrproject-rtos/zephyr/issues/101487)）
  > - [zephyr,mapped-partition](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)（[GitHub #104398](https://github.com/zephyrproject-rtos/zephyr/issues/104398)）
- 运算放大器（OPAMP）

  > - [st,stm32-opamp](../hardware/P733_STM32运算放大器绑定.md#dtbinding-st-stm32-opamp)（[GitHub #99181](https://github.com/zephyrproject-rtos/zephyr/issues/99181)）
  > - [st,stm32g4-opamp](../hardware/P734_STM32G4运算放大器绑定.md#dtbinding-st-stm32g4-opamp)（[GitHub #99181](https://github.com/zephyrproject-rtos/zephyr/issues/99181)）
- 一次性可编程存储器（OTP Memory）

  > - [nxp,ocotp](../otp_binding_reference/P004_nxp_ocotp.md#std-dtcompatible-nxp-ocotp)（[GitHub #103089](https://github.com/zephyrproject-rtos/zephyr/issues/103089)）
  > - [sifli,sf32lb-efuse](../otp_binding_reference/P008_sifli_sf32lb-efuse.md#std-dtcompatible-sifli-sf32lb-efuse)（[GitHub #101926](https://github.com/zephyrproject-rtos/zephyr/issues/101926)）
  > - [st,stm32-bsec](../otp_binding_reference/P009_st_stm32-bsec.md#std-dtcompatible-st-stm32-bsec)（[GitHub #102403](https://github.com/zephyrproject-rtos/zephyr/issues/102403)）
  > - [st,stm32-nvm-otp](../otp_binding_reference/P010_st_stm32-nvm-otp.md#std-dtcompatible-st-stm32-nvm-otp)（[GitHub #102976](https://github.com/zephyrproject-rtos/zephyr/issues/102976)）
  > - [zephyr,otp-emul](../hardware/P534_OTP仿真设备绑定.md#dtbinding-zephyr-otp-emul)（[GitHub #101292](https://github.com/zephyrproject-rtos/zephyr/issues/101292)）
- 性能状态（P-state）

  > - [nxp,mcxn-pstate](../power_state_wakeup_binding_reference/P002_nxp_mcxn-pstate.md#std-dtcompatible-nxp-mcxn-pstate)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
- 引脚控制（Pin Control）

  > - [alif,pinctrl](../pinctrl_adi_ambiq_arm_binding_reference/P003_alif_pinctrl.md#std-dtcompatible-alif-pinctrl)（[GitHub #101244](https://github.com/zephyrproject-rtos/zephyr/issues/101244)）
  > - [brcm,bcm2711-pinctrl](../pinctrl_adi_ambiq_arm_binding_reference/P017_brcm_bcm2711-pinctrl.md#std-dtcompatible-brcm-bcm2711-pinctrl)（[GitHub #101008](https://github.com/zephyrproject-rtos/zephyr/issues/101008)）
  > - [nxp,s32k5-pinctrl](../pinctrl_nxp_pico_binding_reference/P020_nxp_s32k5-pinctrl.md#std-dtcompatible-nxp-s32k5-pinctrl)（[GitHub #100803](https://github.com/zephyrproject-rtos/zephyr/issues/100803)）
  > - [realtek,ameba-pinctrl](../pinctrl_renesas_silabs_binding_reference/P002_realtek_ameba-pinctrl.md#std-dtcompatible-realtek-ameba-pinctrl)（[GitHub #78036](https://github.com/zephyrproject-rtos/zephyr/issues/78036)）
  > - [realtek,bee-pinctrl](../pinctrl_renesas_silabs_binding_reference/P003_realtek_bee-pinctrl.md#std-dtcompatible-realtek-bee-pinctrl)（[GitHub #102691](https://github.com/zephyrproject-rtos/zephyr/issues/102691)）
  > - [realtek,rts5817-pinctrl](../pinctrl_renesas_silabs_binding_reference/P004_realtek_rts5817-pinctrl.md#std-dtcompatible-realtek-rts5817-pinctrl)（[GitHub #91486](https://github.com/zephyrproject-rtos/zephyr/issues/91486)）
  > - [renesas,ra0-pinctrl-pfs](../pinctrl_renesas_silabs_binding_reference/P007_renesas_ra0-pinctrl-pfs.md#std-dtcompatible-renesas-ra0-pinctrl-pfs)（[GitHub #102379](https://github.com/zephyrproject-rtos/zephyr/issues/102379)）
  > - [st,stm32h5-pinctrl](../pinctrl_stm32_ti_xilinx_binding_reference/P006_st_stm32h5-pinctrl.md#std-dtcompatible-st-stm32h5-pinctrl)（[GitHub #105856](https://github.com/zephyrproject-rtos/zephyr/issues/105856)）
  > - [syna,sr100-pinctrl](../pinctrl_stm32_ti_xilinx_binding_reference/P008_syna_sr100-pinctrl.md#std-dtcompatible-syna-sr100-pinctrl)（[GitHub #100172](https://github.com/zephyrproject-rtos/zephyr/issues/100172)）
- 电源管理 CPU 操作（Power Management CPU Operations）

  > - [arm,fvp-pwrc](../power_state_wakeup_binding_reference/P003_arm_fvp-pwrc.md#std-dtcompatible-arm-fvp-pwrc)（[GitHub #96852](https://github.com/zephyrproject-rtos/zephyr/issues/96852)）
- 电源管理（Power Management）

  > - [bflb,power-controller](../power_control_binding_reference/P002_bflb_power-controller.md#std-dtcompatible-bflb-power-controller)（[GitHub #102063](https://github.com/zephyrproject-rtos/zephyr/issues/102063)）
  > - [st,stm32-dualreg-pwr](../stm32_soc_power_binding_reference/P007_st_stm32-dualreg-pwr.md#std-dtcompatible-st-stm32-dualreg-pwr)（[GitHub #99171](https://github.com/zephyrproject-rtos/zephyr/issues/99171)）
  > - [st,stm32-iocell](../stm32_soc_power_binding_reference/P008_st_stm32-iocell.md#std-dtcompatible-st-stm32-iocell)（[GitHub #100539](https://github.com/zephyrproject-rtos/zephyr/issues/100539)）
  > - [st,stm32h5-iocell](../stm32_soc_power_binding_reference/P013_st_stm32h5-iocell.md#std-dtcompatible-st-stm32h5-iocell)（[GitHub #104599](https://github.com/zephyrproject-rtos/zephyr/issues/104599)）
  > - [st,stm32h7-pwr](../stm32_soc_power_binding_reference/P014_st_stm32h7-pwr.md#std-dtcompatible-st-stm32h7-pwr)（[GitHub #99171](https://github.com/zephyrproject-rtos/zephyr/issues/99171)）
  > - [st,stm32h7rs-pwr](../stm32_soc_power_binding_reference/P015_st_stm32h7rs-pwr.md#std-dtcompatible-st-stm32h7rs-pwr)（[GitHub #99171](https://github.com/zephyrproject-rtos/zephyr/issues/99171)）
  > - [st,stm32u5-pwr](../stm32_soc_power_binding_reference/P016_st_stm32u5-pwr.md#std-dtcompatible-st-stm32u5-pwr)（[GitHub #100319](https://github.com/zephyrproject-rtos/zephyr/issues/100319)）
  > - [st,stm32wba-pwr](../stm32_soc_power_binding_reference/P018_st_stm32wba-pwr.md#std-dtcompatible-st-stm32wba-pwr)（[GitHub #105279](https://github.com/zephyrproject-rtos/zephyr/issues/105279)）
- 电源域（Power Domain）

  > - [arm,scmi-power-domain](../hardware/P613_SCMI电源域绑定.md#dtbinding-arm-scmi-power-domain)（[GitHub #102370](https://github.com/zephyrproject-rtos/zephyr/issues/102370)）
- PS/2 接口（PS/2）

  > - [ite,it51xxx-ps2](../lin_dali_mctp_sensor_bus_binding_reference/P011_ite_it51xxx-ps2.md#std-dtcompatible-ite-it51xxx-ps2)（[GitHub #102790](https://github.com/zephyrproject-rtos/zephyr/issues/102790)）
- 脉宽调制（PWM）

  > - [adi,max2221x-pwm](../pwm_adi_esp_infineon_binding_reference/P002_adi_max2221x-pwm.md#std-dtcompatible-adi-max2221x-pwm)（[GitHub #97584](https://github.com/zephyrproject-rtos/zephyr/issues/97584)）
  > - [bflb,pwm-1](../pwm_adi_esp_infineon_binding_reference/P010_bflb_pwm-1.md#std-dtcompatible-bflb-pwm-1)（[GitHub #99195](https://github.com/zephyrproject-rtos/zephyr/issues/99195)）
  > - [bflb,pwm-2](../pwm_adi_esp_infineon_binding_reference/P011_bflb_pwm-2.md#std-dtcompatible-bflb-pwm-2)（[GitHub #99195](https://github.com/zephyrproject-rtos/zephyr/issues/99195)）
  > - [elan,em32-pwm](../pwm_adi_esp_infineon_binding_reference/P012_elan_em32-pwm.md#std-dtcompatible-elan-em32-pwm)（[GitHub #97843](https://github.com/zephyrproject-rtos/zephyr/issues/97843)）
  > - [microchip,tc-g1-pwm](../pwm_intel_microchip_nxp_binding_reference/P010_microchip_tc-g1-pwm.md#std-dtcompatible-microchip-tc-g1-pwm)（[GitHub #100070](https://github.com/zephyrproject-rtos/zephyr/issues/100070)）
  > - [renesas,rza2m-gpt-pwm](../pwm_stm32_ti_generic_binding_reference/P003_renesas_rza2m-gpt-pwm.md#std-dtcompatible-renesas-rza2m-gpt-pwm)（[GitHub #100932](https://github.com/zephyrproject-rtos/zephyr/issues/100932)）
  > - [sifli,sf32lb-atim-pwm](../pwm_stm32_ti_generic_binding_reference/P005_sifli_sf32lb-atim-pwm.md#std-dtcompatible-sifli-sf32lb-atim-pwm)（[GitHub #100137](https://github.com/zephyrproject-rtos/zephyr/issues/100137)）
  > - [sifli,sf32lb-gpt-pwm](../pwm_stm32_ti_generic_binding_reference/P006_sifli_sf32lb-gpt-pwm.md#std-dtcompatible-sifli-sf32lb-gpt-pwm)（[GitHub #99362](https://github.com/zephyrproject-rtos/zephyr/issues/99362)）
- 稳压器（Regulator）

  > - [arduino,modulino-latch-relay](../hardware/P673_Arduino_Modulino锁存继电器绑定.md#dtbinding-arduino-modulino-latch-relay)（[GitHub #104466](https://github.com/zephyrproject-rtos/zephyr/issues/104466)）
  > - [bflb,aon-regulator](../hardware/P646_Bouffalo_AON稳压器绑定.md#dtbinding-bflb-aon-regulator)（[GitHub #102063](https://github.com/zephyrproject-rtos/zephyr/issues/102063)）
  > - [bflb,rt-regulator](../hardware/P647_Bouffalo_RT稳压器绑定.md#dtbinding-bflb-rt-regulator)（[GitHub #102063](https://github.com/zephyrproject-rtos/zephyr/issues/102063)）
  > - [bflb,soc-regulator](../hardware/P648_Bouffalo_SoC稳压器绑定.md#dtbinding-bflb-soc-regulator)（[GitHub #102063](https://github.com/zephyrproject-rtos/zephyr/issues/102063)）
  > - [espressif,esp32-regulator](../hardware/P649_ESP32稳压器绑定.md#dtbinding-espressif-esp32-regulator)（[GitHub #105076](https://github.com/zephyrproject-rtos/zephyr/issues/105076)）
  > - [nordic,npm10xx-regulator](../hardware/P660_nPM10xx稳压器绑定.md#dtbinding-nordic-npm10xx-regulator)（[GitHub #105562](https://github.com/zephyrproject-rtos/zephyr/issues/105562)）
  > - [nordic,vregusb-regulator](../hardware/P645_Nordic_USB稳压器绑定.md#dtbinding-nordic-vregusb-regulator)（[GitHub #97642](https://github.com/zephyrproject-rtos/zephyr/issues/97642)）
  > - [st,stm32-vrefbuf](../hardware/P638_STM32参考电压缓冲器绑定.md#dtbinding-st-stm32-vrefbuf)（[GitHub #99304](https://github.com/zephyrproject-rtos/zephyr/issues/99304)）
  > - [ti,tps55287](../hardware/P666_TPS55287稳压器绑定.md#dtbinding-ti-tps55287)（[GitHub #98662](https://github.com/zephyrproject-rtos/zephyr/issues/98662)）
- 复位控制器（Reset Controller）

  > - [focaltech,ft9001-cpm-rctl](../reset_controller_binding_reference/P002_focaltech_ft9001-cpm-rctl.md#std-dtcompatible-focaltech-ft9001-cpm-rctl)（[GitHub #95959](https://github.com/zephyrproject-rtos/zephyr/issues/95959)）
  > - [realtek,rts5817-reset](../reset_controller_binding_reference/P013_realtek_rts5817-reset.md#std-dtcompatible-realtek-rts5817-reset)（[GitHub #91486](https://github.com/zephyrproject-rtos/zephyr/issues/91486)）
  > - [syna,sr100-reset](../reset_controller_binding_reference/P018_syna_sr100-reset.md#std-dtcompatible-syna-sr100-reset)（[GitHub #100172](https://github.com/zephyrproject-rtos/zephyr/issues/100172)）
- 随机数生成器（RNG）

  > - [gd,gd32-trng](../rng_binding_reference/P008_gd_gd32-trng.md#std-dtcompatible-gd-gd32-trng)（[GitHub #101559](https://github.com/zephyrproject-rtos/zephyr/issues/101559)）
  > - [microchip,trng-g1-entropy](../rng_binding_reference/P010_microchip_trng-g1-entropy.md#std-dtcompatible-microchip-trng-g1-entropy)（[GitHub #99183](https://github.com/zephyrproject-rtos/zephyr/issues/99183)）
  > - [raspberrypi,pico-rng](../soc_rng_binding_reference/P001_raspberrypi_pico-rng.md#std-dtcompatible-raspberrypi-pico-rng)（[GitHub #83346](https://github.com/zephyrproject-rtos/zephyr/issues/83346)）
  > - [renesas,ra-rsip-e50d-trng](../soc_rng_binding_reference/P004_renesas_ra-rsip-e50d-trng.md#std-dtcompatible-renesas-ra-rsip-e50d-trng)（[GitHub #100995](https://github.com/zephyrproject-rtos/zephyr/issues/100995)）
  > - [sifli,sf32lb-trng](../soc_rng_binding_reference/P012_sifli_sf32lb-trng.md#std-dtcompatible-sifli-sf32lb-trng)（[GitHub #98467](https://github.com/zephyrproject-rtos/zephyr/issues/98467)）
  > - [ti,mspm0-trng](../soc_rng_binding_reference/P019_ti_mspm0-trng.md#std-dtcompatible-ti-mspm0-trng)（[GitHub #94733](https://github.com/zephyrproject-rtos/zephyr/issues/94733)）
  > - [wch,rng](../soc_rng_binding_reference/P020_wch_rng.md#std-dtcompatible-wch-rng)（[GitHub #101390](https://github.com/zephyrproject-rtos/zephyr/issues/101390)）
- 实时时钟（RTC）

  > - [adi,max31331](../rtc_binding_reference/P001_adi_max31331.md#std-dtcompatible-adi-max31331)（[GitHub #100508](https://github.com/zephyrproject-rtos/zephyr/issues/100508)）
  > - [maxim,ds1302](../rtc_binding_reference/P010_maxim_ds1302.md#std-dtcompatible-maxim-ds1302)（[GitHub #103964](https://github.com/zephyrproject-rtos/zephyr/issues/103964)）
  > - [microchip,rtc-g1](../rtc_binding_reference/P015_microchip_rtc-g1.md#std-dtcompatible-microchip-rtc-g1)（[GitHub #99144](https://github.com/zephyrproject-rtos/zephyr/issues/99144)）
  > - [microchip,rtc-g2](../rtc_binding_reference/P016_microchip_rtc-g2.md#std-dtcompatible-microchip-rtc-g2)（[GitHub #99889](https://github.com/zephyrproject-rtos/zephyr/issues/99889)）
  > - [nxp,rtc-jdp](../soc_rtc_binding_reference/P001_nxp_rtc-jdp.md#std-dtcompatible-nxp-rtc-jdp)（[GitHub #98114](https://github.com/zephyrproject-rtos/zephyr/issues/98114)）
- SD 主机控制器（SDHC）

  > - [infineon,sdhc-sdio](../sdhc_binding_reference/P008_infineon_sdhc-sdio.md#std-dtcompatible-infineon-sdhc-sdio)（[GitHub #100644](https://github.com/zephyrproject-rtos/zephyr/issues/100644)）
  > - [litex,mmc](../sdhc_binding_reference/P010_litex_mmc.md#std-dtcompatible-litex-mmc)（[GitHub #93816](https://github.com/zephyrproject-rtos/zephyr/issues/93816)）
- 传感器（Sensors）

  > - [adi,ade7978](../sensor_adi_accel_bioz_binding_reference/P002_adi_ade7978.md#std-dtcompatible-adi-ade7978)（[GitHub #104030](https://github.com/zephyrproject-rtos/zephyr/issues/104030)）
  > - [adi,adt7410](../sensor_adi_accel_bioz_binding_reference/P006_adi_adt7410.md#std-dtcompatible-adi-adt7410)（[GitHub #105009](https://github.com/zephyrproject-rtos/zephyr/issues/105009)）
  > - [adi,adt7422](../sensor_adi_accel_bioz_binding_reference/P008_adi_adt7422.md#std-dtcompatible-adi-adt7422)（[GitHub #105009](https://github.com/zephyrproject-rtos/zephyr/issues/105009)）
  > - [adi,adxl355](../compatible_binding_reference/P003_adi_adxl355.md#std-dtcompatible-adi-adxl355)（[GitHub #103387](https://github.com/zephyrproject-rtos/zephyr/issues/103387)）
  > - [adi,max30210](../sensor_adi_accel_bioz_binding_reference/P024_adi_max30210.md#std-dtcompatible-adi-max30210)（[GitHub #100511](https://github.com/zephyrproject-rtos/zephyr/issues/100511)）
  > - [ams,as5048](../sensor_adi_accel_bioz_binding_reference/P027_ams_as5048.md#std-dtcompatible-ams-as5048)（[GitHub #100382](https://github.com/zephyrproject-rtos/zephyr/issues/100382)）
  > - [ams,as6221](../sensor_adi_accel_bioz_binding_reference/P030_ams_as6221.md#std-dtcompatible-ams-as6221)（[GitHub #94899](https://github.com/zephyrproject-rtos/zephyr/issues/94899)）
  > - [avia,hx711-spi](../sensor_ams_aosong_bosch_binding_reference/P022_avia_hx711-spi.md#std-dtcompatible-avia-hx711-spi)（[GitHub #104416](https://github.com/zephyrproject-rtos/zephyr/issues/104416)）
  > - [iclegend,s3km1110](../sensor_espressif_honeywell_invensense_binding_reference/P015_iclegend_s3km1110.md#std-dtcompatible-iclegend-s3km1110)（[GitHub #104279](https://github.com/zephyrproject-rtos/zephyr/issues/104279)）
  > - [invensense,icm45605](../compatible_binding_reference/P040_invensense_icm45605.md#std-dtcompatible-invensense-icm45605)（[GitHub #101061](https://github.com/zephyrproject-rtos/zephyr/issues/101061)）
  > - [invensense,icm45605s](../compatible_binding_reference/P041_invensense_icm45605s.md#std-dtcompatible-invensense-icm45605s)（[GitHub #101061](https://github.com/zephyrproject-rtos/zephyr/issues/101061)）
  > - [invensense,icm45686s](../compatible_binding_reference/P043_invensense_icm45686s.md#std-dtcompatible-invensense-icm45686s)（[GitHub #101061](https://github.com/zephyrproject-rtos/zephyr/issues/101061)）
  > - [invensense,icm45688p](../compatible_binding_reference/P044_invensense_icm45688p.md#std-dtcompatible-invensense-icm45688p)（[GitHub #101061](https://github.com/zephyrproject-rtos/zephyr/issues/101061)）
  > - [liteon,ltr553](../sensor_liteon_maxim_temperature_binding_reference/P006_liteon_ltr553.md#std-dtcompatible-liteon-ltr553)（[GitHub #101669](https://github.com/zephyrproject-rtos/zephyr/issues/101669)）
  > - [microcrystal,rv3032-temp](../sensor_microchip_nordic_nxp_binding_reference/P013_microcrystal_rv3032-temp.md#std-dtcompatible-microcrystal-rv3032-temp)（[GitHub #98918](https://github.com/zephyrproject-rtos/zephyr/issues/98918)）
  > - [nordic,npm10xx-adc](../sensor_microchip_nordic_nxp_binding_reference/P017_nordic_npm10xx-adc.md#std-dtcompatible-nordic-npm10xx-adc)（[GitHub #105597](https://github.com/zephyrproject-rtos/zephyr/issues/105597)）
  > - [nuvoton,npcx-adc-v2t](../sensor_microchip_nordic_nxp_binding_reference/P027_nuvoton_npcx-adc-v2t.md#std-dtcompatible-nuvoton-npcx-adc-v2t)（[GitHub #105006](https://github.com/zephyrproject-rtos/zephyr/issues/105006)）
  > - [nxp,mcux-qdc](../sensor_nxp_qdec_optical_binding_reference/P007_nxp_mcux-qdc.md#std-dtcompatible-nxp-mcux-qdc)（[GitHub #104880](https://github.com/zephyrproject-rtos/zephyr/issues/104880)）
  > - [nxp,tempsense](../sensor_nxp_qdec_optical_binding_reference/P014_nxp_tempsense.md#std-dtcompatible-nxp-tempsense)（[GitHub #101525](https://github.com/zephyrproject-rtos/zephyr/issues/101525)）
  > - [qst,qmi8658a](../sensor_realtek_rohm_sensirion_binding_reference/P001_qst_qmi8658a.md#std-dtcompatible-qst-qmi8658a)（[GitHub #104345](https://github.com/zephyrproject-rtos/zephyr/issues/104345)）
  > - [sensirion,stcc4](../sensor_realtek_rohm_sensirion_binding_reference/P027_sensirion_stcc4.md#std-dtcompatible-sensirion-stcc4)（[GitHub #104929](https://github.com/zephyrproject-rtos/zephyr/issues/104929)）
  > - [sifli,sf32lb-tsen](../sensor_realtek_rohm_sensirion_binding_reference/P030_sifli_sf32lb-tsen.md#std-dtcompatible-sifli-sf32lb-tsen)（[GitHub #99463](https://github.com/zephyrproject-rtos/zephyr/issues/99463)）
  > - [st,ism6hg256x](../compatible_binding_reference/P077_st_ism6hg256x.md#std-dtcompatible-st-ism6hg256x)（[GitHub #95802](https://github.com/zephyrproject-rtos/zephyr/issues/95802)）
  > - [st,lsm6dsv320x](../compatible_binding_reference/P095_st_lsm6dsv320x.md#std-dtcompatible-st-lsm6dsv320x)（[GitHub #95802](https://github.com/zephyrproject-rtos/zephyr/issues/95802)）
  > - [st,lsm6dsv80x](../compatible_binding_reference/P097_st_lsm6dsv80x.md#std-dtcompatible-st-lsm6dsv80x)（[GitHub #95802](https://github.com/zephyrproject-rtos/zephyr/issues/95802)）
  > - [ti,ina232](../sensor_st_ti_power_capacitance_binding_reference/P024_ti_ina232.md#std-dtcompatible-ti-ina232)（[GitHub #98791](https://github.com/zephyrproject-rtos/zephyr/issues/98791)）
  > - [ti,opt3004](../sensor_st_ti_power_capacitance_binding_reference/P030_ti_opt3004.md#std-dtcompatible-ti-opt3004)（[GitHub #99387](https://github.com/zephyrproject-rtos/zephyr/issues/99387)）
- 串行控制器（Serial Controller）

  > - [focaltech,ft9001-usart](../uart_espressif_infineon_microchip_binding_reference/P004_focaltech_ft9001-usart.md#std-dtcompatible-focaltech-ft9001-usart)（[GitHub #95959](https://github.com/zephyrproject-rtos/zephyr/issues/95959)）
  > - [microchip,dbgu-g1-uart](../uart_espressif_infineon_microchip_binding_reference/P018_microchip_dbgu-g1-uart.md#std-dtcompatible-microchip-dbgu-g1-uart)（[GitHub #101016](https://github.com/zephyrproject-rtos/zephyr/issues/101016)）
  > - [realtek,ameba-loguart](../uart_raspberrypi_realtek_renesas_binding_reference/P003_realtek_ameba-loguart.md#std-dtcompatible-realtek-ameba-loguart)（[GitHub #78036](https://github.com/zephyrproject-rtos/zephyr/issues/78036)）
  > - [realtek,bee-uart](../uart_raspberrypi_realtek_renesas_binding_reference/P004_realtek_bee-uart.md#std-dtcompatible-realtek-bee-uart)（[GitHub #102691](https://github.com/zephyrproject-rtos/zephyr/issues/102691)）
  > - [renesas,ra-uart-sau](../uart_raspberrypi_realtek_renesas_binding_reference/P007_renesas_ra-uart-sau.md#std-dtcompatible-renesas-ra-uart-sau)（[GitHub #102379](https://github.com/zephyrproject-rtos/zephyr/issues/102379)）
  > - [rpmsg-uart](../intercore_reference/P187_RPMsg串口设备树绑定.md#dtbinding-rpmsg-uart)（[GitHub #98463](https://github.com/zephyrproject-rtos/zephyr/issues/98463)）
- 串行外设接口（SPI）

  > - [bflb,spi](../spi_adi_atmel_esp_binding_reference/P010_bflb_spi.md#std-dtcompatible-bflb-spi)（[GitHub #94752](https://github.com/zephyrproject-rtos/zephyr/issues/94752)）
  > - [infineon,spi](../spi_adi_atmel_esp_binding_reference/P017_infineon_spi.md#std-dtcompatible-infineon-spi)（[GitHub #100644](https://github.com/zephyrproject-rtos/zephyr/issues/100644)）
  > - [microchip,sercom-g1-spi](../spi_microchip_nordic_nxp_binding_reference/P009_microchip_sercom-g1-spi.md#std-dtcompatible-microchip-sercom-g1-spi)（[GitHub #101864](https://github.com/zephyrproject-rtos/zephyr/issues/101864)）
  > - [realtek,rts5912-spi](../spi_flexspi_nxp_renesas_binding_reference/P014_realtek_rts5912-spi.md#std-dtcompatible-realtek-rts5912-spi)（[GitHub #96006](https://github.com/zephyrproject-rtos/zephyr/issues/96006)）
  > - [renesas,ra-spi-sci](../spi_flexspi_nxp_renesas_binding_reference/P016_renesas_ra-spi-sci.md#std-dtcompatible-renesas-ra-spi-sci)（[GitHub #97339](https://github.com/zephyrproject-rtos/zephyr/issues/97339)）
  > - [renesas,ra-spi-sci-b](../spi_flexspi_nxp_renesas_binding_reference/P015_renesas_ra-spi-sci-b.md#std-dtcompatible-renesas-ra-spi-sci-b)（[GitHub #95014](https://github.com/zephyrproject-rtos/zephyr/issues/95014)）
  > - [sensry,sy1xx-spi](../spi_stm32_ti_xilinx_binding_reference/P002_sensry_sy1xx-spi.md#std-dtcompatible-sensry-sy1xx-spi)（[GitHub #102323](https://github.com/zephyrproject-rtos/zephyr/issues/102323)）
  > - [sifli,sf32lb-spi](../spi_stm32_ti_xilinx_binding_reference/P004_sifli_sf32lb-spi.md#std-dtcompatible-sifli-sf32lb-spi)（[GitHub #97626](https://github.com/zephyrproject-rtos/zephyr/issues/97626)）
- 步进电机（Stepper）

  > - [adi,tmc50xx-stepper-ctrl](../stepper_binding_reference/P002_adi_tmc50xx-stepper-ctrl.md#std-dtcompatible-adi-tmc50xx-stepper-ctrl)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
  > - [adi,tmc50xx-stepper-driver](../stepper_binding_reference/P003_adi_tmc50xx-stepper-driver.md#std-dtcompatible-adi-tmc50xx-stepper-driver)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
  > - [adi,tmc51xx-stepper-ctrl](../stepper_binding_reference/P006_adi_tmc51xx-stepper-ctrl.md#std-dtcompatible-adi-tmc51xx-stepper-ctrl)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
  > - [adi,tmc51xx-stepper-driver](../stepper_binding_reference/P007_adi_tmc51xx-stepper-driver.md#std-dtcompatible-adi-tmc51xx-stepper-driver)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
  > - [adi,tmcm3216](../stepper_binding_reference/P011_adi_tmcm3216.md#std-dtcompatible-adi-tmcm3216)（[GitHub #104508](https://github.com/zephyrproject-rtos/zephyr/issues/104508)）
  > - [adi,tmcm3216-stepper-ctrl](../stepper_binding_reference/P009_adi_tmcm3216-stepper-ctrl.md#std-dtcompatible-adi-tmcm3216-stepper-ctrl)（[GitHub #104508](https://github.com/zephyrproject-rtos/zephyr/issues/104508)）
  > - [adi,tmcm3216-stepper-driver](../stepper_binding_reference/P010_adi_tmcm3216-stepper-driver.md#std-dtcompatible-adi-tmcm3216-stepper-driver)（[GitHub #104508](https://github.com/zephyrproject-rtos/zephyr/issues/104508)）
  > - [zephyr,fake-stepper-ctrl](../hardware/P547_伪步进电机控制器绑定.md#dtbinding-zephyr-fake-stepper-ctrl)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
  > - [zephyr,fake-stepper-driver](../hardware/P548_伪步进电机驱动器绑定.md#dtbinding-zephyr-fake-stepper-driver)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
  > - [zephyr,gpio-step-dir-stepper-ctrl](../stepper_binding_reference/P014_zephyr_gpio-step-dir-stepper-ctrl.md#std-dtcompatible-zephyr-gpio-step-dir-stepper-ctrl)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
  > - [zephyr,h-bridge-stepper-ctrl](../stepper_binding_reference/P015_zephyr_h-bridge-stepper-ctrl.md#std-dtcompatible-zephyr-h-bridge-stepper-ctrl)（[GitHub #101001](https://github.com/zephyrproject-rtos/zephyr/issues/101001)）
- 系统控制器（System Controller）

  > - [ti,control-module](../edac_syscon_binding_reference/P009_ti_control-module.md#std-dtcompatible-ti-control-module)（[GitHub #103330](https://github.com/zephyrproject-rtos/zephyr/issues/103330)）
- 定时器（Timer）

  > - [adi,max32-rv32-sys-timer](../system_timer_binding_reference/P001_adi_max32-rv32-sys-timer.md#std-dtcompatible-adi-max32-rv32-sys-timer)（[GitHub #97309](https://github.com/zephyrproject-rtos/zephyr/issues/97309)）
  > - [adi,max32-wut-timer](../system_timer_binding_reference/P003_adi_max32-wut-timer.md#std-dtcompatible-adi-max32-wut-timer)（[GitHub #104687](https://github.com/zephyrproject-rtos/zephyr/issues/104687)）
  > - [arm,armv7-timer](../arm_interrupt_timer_binding_reference/P009_ARMv7架构定时器.md#std-dtcompatible-arm-armv7-timer)（[GitHub #99675](https://github.com/zephyrproject-rtos/zephyr/issues/99675)）
  > - [infineon,cat1-lp-timer-pdl](../mcu_timer_binding_reference/P007_infineon_cat1-lp-timer-pdl.md#std-dtcompatible-infineon-cat1-lp-timer-pdl)（[GitHub #97831](https://github.com/zephyrproject-rtos/zephyr/issues/97831)）
  > - [infineon,lp-timer](../mcu_timer_binding_reference/P008_infineon_lp-timer.md#std-dtcompatible-infineon-lp-timer)（[GitHub #100644](https://github.com/zephyrproject-rtos/zephyr/issues/100644)）
  > - [realtek,bee-basic-timer](../microchip_nordic_nxp_realtek_timer_binding_reference/P009_realtek_bee-basic-timer.md#std-dtcompatible-realtek-bee-basic-timer)（[GitHub #104805](https://github.com/zephyrproject-rtos/zephyr/issues/104805)）
  > - [realtek,bee-enhanced-timer](../microchip_nordic_nxp_realtek_timer_binding_reference/P010_realtek_bee-enhanced-timer.md#std-dtcompatible-realtek-bee-enhanced-timer)（[GitHub #104805](https://github.com/zephyrproject-rtos/zephyr/issues/104805)）
  > - [realtek,bee-timer](../microchip_nordic_nxp_realtek_timer_binding_reference/P011_realtek_bee-timer.md#std-dtcompatible-realtek-bee-timer)（[GitHub #104805](https://github.com/zephyrproject-rtos/zephyr/issues/104805)）
  > - [renesas,rza2m-gpt](../renesas_timer_binding_reference/P010_renesas_rza2m-gpt.md#std-dtcompatible-renesas-rza2m-gpt)（[GitHub #100932](https://github.com/zephyrproject-rtos/zephyr/issues/100932)）
  > - [renesas,rza2m-ostm-timer](../renesas_timer_binding_reference/P011_renesas_rza2m-ostm-timer.md#std-dtcompatible-renesas-rza2m-ostm-timer)（[GitHub #100934](https://github.com/zephyrproject-rtos/zephyr/issues/100934)）
  > - [sifli,sf32lb-atim](../stm32_ti_silabs_timer_binding_reference/P001_sifli_sf32lb-atim.md#std-dtcompatible-sifli-sf32lb-atim)（[GitHub #100137](https://github.com/zephyrproject-rtos/zephyr/issues/100137)）
  > - [sifli,sf32lb-gptim](../stm32_ti_silabs_timer_binding_reference/P002_sifli_sf32lb-gptim.md#std-dtcompatible-sifli-sf32lb-gptim)（[GitHub #99362](https://github.com/zephyrproject-rtos/zephyr/issues/99362)）
- USB音频卸载（UAOL）

  > - [intel,adsp-uaol](../platform_rmt_openthread_binding_reference/P014_intel_adsp-uaol.md#std-dtcompatible-intel-adsp-uaol)（[GitHub #104137](https://github.com/zephyrproject-rtos/zephyr/issues/104137)）
  > - [intel,uaol-dai](../platform_rmt_openthread_binding_reference/P015_intel_uaol-dai.md#std-dtcompatible-intel-uaol-dai)（[GitHub #104137](https://github.com/zephyrproject-rtos/zephyr/issues/104137)）
- 通用串行总线（USB）

  > - [atmel,sam-udp](../usb_controller_binding_reference/P003_atmel_sam-udp.md#std-dtcompatible-atmel-sam-udp)（[GitHub #102041](https://github.com/zephyrproject-rtos/zephyr/issues/102041)）
  > - [bflb,udc-1](../usb_controller_binding_reference/P007_bflb_udc-1.md#std-dtcompatible-bflb-udc-1)（[GitHub #104244](https://github.com/zephyrproject-rtos/zephyr/issues/104244)）
  > - [nordic,nrf-usbhs-wrapper](../usb_soc_binding_reference/P002_nordic_nrf-usbhs-wrapper.md#std-dtcompatible-nordic-nrf-usbhs-wrapper)（[GitHub #97642](https://github.com/zephyrproject-rtos/zephyr/issues/97642)）
  > - [nuvoton,numaker-hsusbd](../usb_soc_binding_reference/P004_nuvoton_numaker-hsusbd.md#std-dtcompatible-nuvoton-numaker-hsusbd)（[GitHub #95709](https://github.com/zephyrproject-rtos/zephyr/issues/95709)）
- USB Type-C 接口（USB Type-C）

  > - [zephyr,usb-c-pwrctrl](../usbc_tcpc_binding_reference/P009_zephyr_usb-c-pwrctrl.md#std-dtcompatible-zephyr-usb-c-pwrctrl)（[GitHub #103883](https://github.com/zephyrproject-rtos/zephyr/issues/103883)）
- 视频（Video）

  > - [arducam,mega](../video_camera_endpoint_binding_reference/P002_arducam_mega.md#std-dtcompatible-arducam-mega)（[GitHub #96234](https://github.com/zephyrproject-rtos/zephyr/issues/96234)）
  > - [himax,hm0360](../video_camera_endpoint_binding_reference/P006_himax_hm0360.md#std-dtcompatible-himax-hm0360)（[GitHub #94904](https://github.com/zephyrproject-rtos/zephyr/issues/94904)）
  > - [ovti,ov5642](../video_camera_endpoint_binding_reference/P015_ovti_ov5642.md#std-dtcompatible-ovti-ov5642)（[GitHub #97106](https://github.com/zephyrproject-rtos/zephyr/issues/97106)）
  > - [ovti,ov7675](../video_camera_endpoint_binding_reference/P017_ovti_ov7675.md#std-dtcompatible-ovti-ov7675)（[GitHub #96319](https://github.com/zephyrproject-rtos/zephyr/issues/96319)）
  > - [sony,imx219](../video_st_sony_emulation_binding_reference/P001_sony_imx219.md#std-dtcompatible-sony-imx219)（[GitHub #101754](https://github.com/zephyrproject-rtos/zephyr/issues/101754)）
- 唤醒控制器（Wakeup Controller）

  > - [nxp,llwu](../power_state_wakeup_binding_reference/P006_nxp_llwu.md#std-dtcompatible-nxp-llwu)（[GitHub #100559](https://github.com/zephyrproject-rtos/zephyr/issues/100559)）
- 看门狗（Watchdog）

  > - [adi,max42500-watchdog](../watchdog_binding_reference/P002_adi_max42500-watchdog.md#std-dtcompatible-adi-max42500-watchdog)（[GitHub #102929](https://github.com/zephyrproject-rtos/zephyr/issues/102929)）
  > - [bflb,wdt](../watchdog_binding_reference/P010_bflb_wdt.md#std-dtcompatible-bflb-wdt)（[GitHub #104243](https://github.com/zephyrproject-rtos/zephyr/issues/104243)）
  > - [microchip,wdt-g1](../soc_pmic_watchdog_binding_reference/P010_microchip_wdt-g1.md#std-dtcompatible-microchip-wdt-g1)（[GitHub #101335](https://github.com/zephyrproject-rtos/zephyr/issues/101335)）
  > - [realtek,rts5817-watchdog](../realtek_renesas_silabs_watchdog_binding_reference/P003_realtek_rts5817-watchdog.md#std-dtcompatible-realtek-rts5817-watchdog)（[GitHub #91486](https://github.com/zephyrproject-rtos/zephyr/issues/91486)）
- 无线局域网（Wi-Fi）

  > - [nordic,nrf7120-wifi](../wifi_nordic_nxp_simulation_binding_reference/P008_nordic_nrf7120-wifi.md#std-dtcompatible-nordic-nrf7120-wifi)（[GitHub #104055](https://github.com/zephyrproject-rtos/zephyr/issues/104055)）
- 扩展串行外设接口（XSPI）

  > - [nxp,s32-xspi](../qspi_ospi_xspi_binding_reference/P014_nxp_s32-xspi.md#std-dtcompatible-nxp-s32-xspi)（[GitHub #101487](https://github.com/zephyrproject-rtos/zephyr/issues/101487)）
  > - [nxp,s32-xspi-sfp-frad](../qspi_ospi_xspi_binding_reference/P012_nxp_s32-xspi-sfp-frad.md#std-dtcompatible-nxp-s32-xspi-sfp-frad)（[GitHub #101487](https://github.com/zephyrproject-rtos/zephyr/issues/101487)）
  > - [nxp,s32-xspi-sfp-mdad](../qspi_ospi_xspi_binding_reference/P013_nxp_s32-xspi-sfp-mdad.md#std-dtcompatible-nxp-s32-xspi-sfp-mdad)（[GitHub #101487](https://github.com/zephyrproject-rtos/zephyr/issues/101487)）
  > - [st,stm32-xspim](../qspi_ospi_xspi_binding_reference/P017_st_stm32-xspim.md#std-dtcompatible-st-stm32-xspim)（[GitHub #104943](https://github.com/zephyrproject-rtos/zephyr/issues/104943)）

<a id="new-samples"></a>

## 新增示例（New Samples）


- 六自由度设备FIFO流式采集（6DoF Device FIFO Streaming），原名stream_fifo。（[六自由度设备FIFO流式采集（6dof Device FIFO Streaming）](../sensors/P013_六自由度FIFO流式读取示例.md#6dof_fifo_stream)）
- [通用三轴加速度计流式采集（Generic 3-Axis Accelerometer Streaming）](../sensors/P011_三轴加速度计流式读取示例.md#accel_stream)，原名accel_polling。
- [通用模数转换器数据流（Generic ADC Stream）](../hardware/P441_ADC通用流示例.md#adc_stream)
- [OpenAMP数字信号处理器非对称多处理示例（DSP AMP Sample）](../board_samples/P078_DSP非对称多处理OpenAMP通信.md#amp_talk)
- [AT 命令客户端（AT Command Client）](../driver_samples/P019_AT命令客户端示例.md#at_client)
- [博流（Bouffalolab）GPIO FIFO／线输出UART示例（Wire Out UART）](../driver_samples/P052_Bouffalolab_GPIO_FIFO串口示例.md#bflb-bl61x-wo-uart)
- [外围设备警报通知服务（Peripheral ANS）](../bluetooth_samples/P046_警报通知外设.md#ble_peripheral_ans)
- [经过时间服务（Elapsed Time Service，ETS）外围设备](../bluetooth_samples/P049_经过时间服务外设.md#ble_peripheral_ets)
- [外围设备通用访问配置文件（GAP）服务自定义实现](../bluetooth_samples/P050_自定义GAP服务.md#ble_peripheral_gap_svc)
- [高级音频分发配置文件接收端（A2DP Sink）](../bluetooth_samples/P083_A2DP接收端.md#bluetooth_a2dp_sink)
- [高级音频分发配置文件发送端（A2DP Source）](../bluetooth_samples/P084_A2DP音频源.md#bluetooth_a2dp_source)
- [L2CAP面向连接通道接收方（Connection Oriented Channels，Acceptor）](../bluetooth_samples/P009_L2CAP信道接受端.md#bluetooth_l2cap_coc_acceptor)
- [L2CAP面向连接通道发起方（Connection Oriented Channels，Initiator）](../bluetooth_samples/P010_L2CAP信道发起端.md#bluetooth_l2cap_coc_initiator)
- [bridge](../networking/P113_以太网桥示例.md#bridge)
- [按钮中断（Button Interrupt）](../driver_samples/P002_GPIO按钮中断示例.md#button_interrupt)
- [脉宽调制捕获（PWM Capture）](../hardware/P169_PWM输入捕获示例.md#capture)
- [受限应用协议上传（CoAP Upload）](../networking/P071_CoAP上传示例.md#coap-upload)
- [音频编解码器（Audio Codec）](../driver_samples/P027_音频编解码器示例.md#codec)
- [按需CPU调频（On-demand CPU frequency scaling）](../power/P019_按需CPU调频示例.md#cpu_freq_on_demand)
- [基于调度压力的CPU调频（Pressure-based CPU Frequency Scaling）](../power/P020_压力CPU调频示例.md#cpu_freq_pressure)
- [循环冗余校验驱动（Cyclic Redundancy Check Drivers，CRC）](../hardware/P042_CRC校验示例.md#crc_drivers)
- [循环冗余校验子系统（CRC Subsys）](../data_utilities/P002_CRC子系统示例.md#crc_subsys)
- [CS40L5x触觉反馈驱动（Haptic Driver）](../hardware/P161_CS40L5x触觉驱动示例.md#cs40l5x)
- [设备空闲电源管理（Device Idle Power Management）](../power/P049_设备空闲电源管理示例.md#device_pm)
- [分布式交换机架构（DSA / Distributed Switch Architecture）](../networking/P123_DSA分布式交换机示例.md#dsa)
- [脉宽调制事件（PWM Event）](../hardware/P170_PWM事件示例.md#event)
- [EXT2文件系统fstab示例](../storage/P081_Ext2挂载表示例.md#ext2-fstab)
- [指纹传感器（Fingerprint Sensor）](../driver_samples/P032_指纹传感器示例.md#fingerprint-sensor)
- [ESP32上的Flash处理器间消息（IPM）示例](../intercore_reference/P078_ESP32闪存IPM示例.md#flash-ipm)
- [FRDM-MCXA156低功耗DAC、运算放大器及低功耗ADC示例（lpdac / opamp / lpadc）](../hardware/P099_FRDM模拟信号链示例.md#frdm_mcxa156_lpdac_opamp_lpadc)
- [文件传输协议客户端Shell示例（FTP Client Shell Sample）](../networking/P076_FTP客户端示例.md#ftp-client)
- [HL78xx调制解调器驱动入门（Hello hl78xx Modem Driver）](../driver_samples/P020_HL78xx调制解调器示例.md#hello_hl78xx)
- [硬件自旋锁（HWSPINLOCK）](../intercore_reference/P013_硬件自旋锁驱动示例.md#hwspinlock)
- [插桩（Instrumentation）](../observability/P019_函数插桩示例.md#instrumentation)
- [IS31FL319x红绿蓝发光二极管（RGB LED）](../hardware/P188_IS31FL319x三色LED示例.md#is31fl319x)
- [时延监测客户端（Latmon Client）](../networking/P095_Latmon客户端示例.md#latmon-client)
- [低功耗GPIO唤醒（LP GPIO Wakeup）](../board_samples/P104_低功耗核GPIO唤醒.md#lp-gpio-wakeup)
- [低功耗定时器唤醒（LP Timer Wakeup）](../board_samples/P106_低功耗核定时器唤醒.md#lp-timer-wakeup)
- [MAX32664C与MAX86141传感器集线器（Sensor Hub）](../sensors/P081_MAX32664C与MAX86141传感器集线器示例.md#max32664c)
- [管理组件传输协议I2C GPIO端点节点示例（MCTP I2C GPIO Endpoint Node Sample）](../basic_samples/P052_MCTPI2C端点示例.md#mctp_i2c_bus_endpoint)
- 通过I2C与GPIO传输的PMCI MCTP示例（mctp_i2c_bus_owner）
- [管理组件传输协议I3C端点节点示例（MCTP I3C Endpoint Node Sample）](../basic_samples/P054_MCTPI3C端点示例.md#mctp_i3c_bus_endpoint)
- 通过I3C传输的PMCI MCTP示例（mctp_i3c_bus_owner）
- [管理组件传输协议USB端点节点示例（MCTP USB Endpoint Node Sample）](../usb/P191_MCTPUSB端点示例.md#mctp-usb-endpoint)
- [消息队列（Message Queue）](../basic_samples/P026_消息队列示例.md#msg_queue)
- [MTCH9010液体泄漏检测器测试平台（Liquid Leak Detector Testbench）](../sensors/P076_MTCH9010液体泄漏检测示例.md#mtch9010)
- [MIDI2网络传输（Network Transport）](../networking/P219_MIDI2网络传输示例.md#netmidi2)
- [nRF时钟控制（Clock Control）](../timer_reference/P116_nRF时钟控制示例.md#nrf_clock_control)
- [OCPP充电点（Charge Point）](../networking/P182_OCPP充电桩示例.md#ocpp)
- [运算放大器（Operational Amplifier，OPAMP）输出测量示例](../hardware/P092_运算放大器输出测量示例.md#opamp_output_measure)
- [OpenThread边界路由器（Border Router）](../networking/P173_OpenThread边界路由器.md#openthread-border-router)
- [Pico W的Wi-Fi与LED示例](../board_samples/P050_Pico_W的WiFi与LED.md#pico-w-wifi-led)
- [生产者与消费者（Producer / Consumer）](../basic_samples/P045_实时IO生产者消费者示例.md#producer_consumer)
- [服务质量（Quality of Service）](../networking/P122_以太网服务质量示例.md#quality-of-service)
- [红黑树数据结构（Red-Black Tree Data Structure）](../basic_samples/P033_红黑树示例.md#red-black-tree)
- [稳压器Shell示例（Regulator Shell Sample）](../power/P076_稳压器命令行示例.md#regulator_shell)
- [使用比较器的瑞萨低电压检测示例（Low-voltage Detection）](../board_samples/P046_Renesas低电压检测.md#renesas_lvd)
- [RTK0EG0019B01002BJ电容触摸应用扩展板（Capacitive Touch Application Shield）](../shield_samples/P007_Renesas电容触摸扩展板.md#rtk0eg0019b01002bj)
- [Iclegend S3KM1110毫米波传感器](../sensors/P067_S3KM1110毫米波传感器示例.md#s3km1110)
- [系统控制与管理接口平台交互（SCMI Platform Interaction）](../hardware/P599_SCMI平台交互示例.md#scmi)
- [SCT2024 LED控制器（LED Controller）](../hardware/P199_SCT2024发光二极管示例.md#sct2024)
- [devmem load Shell命令示例](../interaction/P012_内存加载Shell示例.md#shell-devmem-load)
- [STM32 PWM主模式（Master Mode）](../board_samples/P005_STM32的PWM主模式.md#stm32_pwm_mastermode)
- [10BASE-T1S测试（OA_TC6）](../networking/P125_10BASE-T1S测试示例.md#t1s)
- [TMCM-3216步进电机（Stepper）](../hardware/P167_TMCM3216步进电机示例.md#tmcm3216)
- [基础USB-C双角色端口（DRP）](../usb/P010_USBC双电源角色示例.md#usb-c-drp)
- [USB主机UVC摄像头（USB Host UVC Camera）](../usb/P125_USB主机摄像头示例.md#usb-host-uvc)
- [VEML6046 RGBIR颜色传感器（Color Sensor）](../sensors/P062_VEML6046颜色传感器示例.md#veml6046)
- [virtiofs文件系统（Filesystem）](../storage/P030_Virtiofs文件系统示例.md#virtiofs)
- [WireGuard虚拟专用网络（VPN）](../networking/P211_WireGuard虚拟专用网示例.md#wireguard-vpn)
- [Zbus异步监听器（Async Listeners）](../zbus_samples/P005_异步监听器.md#zbus-async-listeners)
- [Zbus代理与进程间通信（Proxy Agent - IPC）](../zbus_samples/P013_跨核代理.md#zbus-proxy-agent-ipc)
- [Zephyr基准测试示例（Benchmark Sample）](../testing/P008_基准测试示例.md#ztest_benchmark)

<a id="devicetree"></a>

## 设备树（Devicetree）


- 迁移指南：[设备树（Devicetree）](../releases_guides/P006_迁移到Zephyr_4.4.md#migration-4-4-devicetree)
- 新增遍历reg属性的宏。（[GitHub #104223](https://github.com/zephyrproject-rtos/zephyr/issues/104223)）


  - [`DT_FOREACH_REG`](../dt_reg_reference/P001_设备树寄存器属性宏.md#gae43b5601701f53e1cf637fa985dca613)
  - [`DT_FOREACH_REG_SEP`](../dt_reg_reference/P001_设备树寄存器属性宏.md#gaf37a613ce652b5060df85e6a3c7e87d7)
  - [`DT_FOREACH_REG_VARGS`](../dt_reg_reference/P001_设备树寄存器属性宏.md#ga19b6ffbc2702dbf3140e774b524aac7d)
  - [`DT_FOREACH_REG_SEP_VARGS`](../dt_reg_reference/P001_设备树寄存器属性宏.md#ga19898e7348160246a0ee3f16c09c75b2)
  - 各宏均有按实例编号操作的变体，例如[DT_INST_FOREACH_REG](../dt_instance_reference/P001_设备树驱动实例宏.md#gab67721b2b1d405adb980e3dcff17ef61)。
- *-map相关属性定义（[GitHub #87595](https://github.com/zephyrproject-rtos/zephyr/issues/87595)）为连接节点（Nexus Nodes）及说明符映射（Specifier Mappings）提供原生支持。详情见设备树规范（Devicetree Specification）v0.4第2.5节。
- 新增[zephyr,mapped-partition](../mtd_nxp_st_ti_partition_binding_reference/P023_zephyr_mapped-partition.md#std-dtcompatible-zephyr-mapped-partition)绑定及相关API，用于内存映射Flash分区，作为现有[fixed-partitions](../hardware/P568_固定分区绑定.md#dtbinding-fixed-partitions)绑定的后继。
- 绑定不再允许为status、#address-cells及#size-cells属性指定任何默认值。
- [`DT_CHILD_BY_UNIT_ADDR_INT`](../dt_identity_reference/P001_设备树节点标识宏.md#ga3ebb396be1ef1bc6d6ab1414efbf8001)
- [`DT_INST_CHILD_BY_UNIT_ADDR_INT`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga5afddd3216367030d78efd9f03db9945)

<a id="kconfig"></a>

## Kconfig配置系统


- 新增预处理函数dt_highest_controller_irq_number。（[GitHub #104819](https://github.com/zephyrproject-rtos/zephyr/issues/104819)）

<a id="kernel"></a>

## 内核（Kernel）


- 移除自Zephyr 4.2.0起弃用的CONFIG_SCHED_DUMB及CONFIG_WAITQ_DUMB选项。
- 通过[CONFIG_SYS_HEAP_HARDENING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_HEAP_HARDENING)新增分级堆加固（Heap Hardening）：基础、中等、完整及极限级（Basic / Moderate / Full / Extreme）。为[sys_heap_alloc()](../lowheap_reference/P001_底层堆分配接口.md#ga6b8bdf02c9be5576fddbe711904a3aad)及[sys_heap_free()](../lowheap_reference/P001_底层堆分配接口.md#gab654da64adf74e67ae12f263eb420560)逐级增加运行时损坏检测，包括重复释放检测、相邻块一致性检查及可选的逐块哨兵值（Canaries）。（[GitHub #104999](https://github.com/zephyrproject-rtos/zephyr/issues/104999)）
- [基于作用域的清理辅助机制（Scope-based Cleanup Helpers）](https://docs.zephyrproject.org/latest/kernel/cleanup.html#cleanup-api)


  - [`SCOPE_VAR_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga4faf2c585a3fa2ce28480a5e2805ca8b)
  - [`SCOPE_GUARD_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#gab584b9adf45e13376c0f8e0b817a6213)
  - [`SCOPE_DEFER_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga07847cc6bb3cd5f63b4d05e084eb9203)
  - [`scope_var`](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga62362f13860dbea4361e7cf149801d3f)
  - [`scope_var_init`](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga096c421f2ba9d7acd68039d493a80b63)
  - [`scope_guard`](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga3905160905199178d29b66084f237f4e)
  - [`scope_defer`](https://docs.zephyrproject.org/latest/doxygen/html/group__cleanup__interface.html#ga5ea0ef9eed956fa112b069d87f8b05e5)

<a id="libraries-subsystems"></a>

## 库与子系统（Libraries / Subsystems）


- LoRa无线通信／LoRa广域网（LoRaWAN）

  > - [`lora_airtime()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaedf7847838b1e2b83bde8fc7bf735cf6)
  > - LoRa API新增信道活动检测（Channel Activity Detection，CAD）支持：[lora_cad()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga497bf93cfe42ce6a6d48a4b463b52c21)及[lora_cad_async()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga35e79551b8cdb160e74d3759a76f2db4)。CAD参数与发送前监听（LBT）模式通过[lora_modem_config](https://docs.zephyrproject.org/latest/doxygen/html/structlora__modem__config.html)配置。
  > - 新增[lora_recv_duty_cycle()](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5d1802eed6067734ca45c70e3114b272)，支持由硬件驱动的无线唤醒（Wake-on-radio），通过接收占空比循环实现。
- Mbed TLS密码与TLS库


  - 新增[CONFIG_MBEDTLS_VERSION_C](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_VERSION_C)，简化Mbed TLS版本信息导出。启用后，可使用mbedtls_version_get_number()。
  - Mbed TLS升级到4.1.0。此后，该仓库仅包含TLS及X.509，密码支持移至TF-PSA-Crypto。后者作为新的West模块引入，基于上游1.1.0版本。两个项目的发行说明如下：


    - [https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-4.1.0](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-4.1.0)
    - [https://github.com/Mbed-TLS/TF-PSA-Crypto/releases/tag/tf-psa-crypto-1.1.0](https://github.com/Mbed-TLS/TF-PSA-Crypto/releases/tag/tf-psa-crypto-1.1.0)
- Zephyr消息总线（Zbus）

  > - 新增异步监听器（Async Listener）支持。异步监听器在工作队列上下文中执行，而非发布者线程中；无需专门的订阅者线程，即可实现非阻塞操作。
  > - 新增[Zbus异步监听器（Async Listeners）](../zbus_samples/P005_异步监听器.md#zbus-async-listeners)示例。
  > - 新增实验性代理通信（Proxy-agent Communication），支持IPC后端，用于跨域转发通道数据。
  > - 新增Zbus代理与IPC示例（Proxy Agent - IPC）。（[Zbus代理与进程间通信（Proxy Agent - IPC）](../zbus_samples/P013_跨核代理.md#zbus-proxy-agent-ipc)）
  > - 新增[zbus_chan_from_name()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga4c9ca845c43d6f15ae7c8c10c7667d12)，根据名称字符串获取Zbus通道。
  > - 新增[zbus_async_listener_set_work_queue()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga549a7a10d4535c6c6448776157e636f6)，设置异步监听器的工作队列。
  > - 新增[zbus_chan_pub_stats_msg_age()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga4d674705c121fcd6a573c7c6d9ea7397)，获取距最近一次发布经过的毫秒数，即消息年龄。
  > - 澄清观察者优先级（Observer Priority）文档，并修正拼写及语法。
  > - 更新文档中的观察者类型示意图。
  > - 过滤不支持对称多处理（SMP）的测试。

<a id="other-notable-changes"></a>

## 其他主要变更（Other Notable Changes）


- TF-M从2.2.0更新到2.2.2，发行说明见：


  - [https://trustedfirmware-m.readthedocs.io/en/tf-mv2.2.2/releases/2.2.1.html](https://trustedfirmware-m.readthedocs.io/en/tf-mv2.2.2/releases/2.2.1.html)
  - [https://trustedfirmware-m.readthedocs.io/en/tf-mv2.2.2/releases/2.2.2.html](https://trustedfirmware-m.readthedocs.io/en/tf-mv2.2.2/releases/2.2.2.html)
- TF-M非安全（NS）接口头文件现在经zephyr_interface CMake库自动提供给非安全应用，无需显式链接tfm_api。
- NXP SoC的DTSI文件已重组，移入dts/arm/nxp下按系列划分的子目录。
- 原生模拟器（Native Simulator）：基于native_sim的目标现在支持交叉编译。（[GitHub #100182](https://github.com/zephyrproject-rtos/zephyr/issues/100182)）（[原生模拟器（Native Simulator，native_sim）](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)；[cross-compiled](../native_reference/P003_POSIX架构交叉编译.md#posix-arch-cross-compile)）

## 译注

本页按对应版本的官方发行说明翻译；“新增”“弃用”“当前”等描述均以该版本为背景。安全编号、开发板目标、设备树compatible、代码和源码路径保留原始标识；不会将原文中的历史保密期说明作为当前状态承诺。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [UM11732.pdf](https://www.nxp.com/docs/en/user-manual/UM11732.pdf)：HTTP Error 404: Not Found。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Zephyr 4.3 发行说明](P003_Zephyr_4.3_发行说明.md) · [本模块主线目录](../reading/releases_notes.md) · [全部主线](../reading/README.md) · [下一篇：Zephyr 4.5 工作草案 发行说明](P005_Zephyr_4.5_工作草案_发行说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P003_Zephyr_4.3_发行说明.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_Zephyr_4.5_工作草案_发行说明.md)

</details>

<!-- reading-navigation:end -->
