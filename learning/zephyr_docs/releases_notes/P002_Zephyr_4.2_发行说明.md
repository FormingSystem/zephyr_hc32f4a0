---
id: learning.zephyr-docs.releases-notes.page-2
title: Zephyr 4.2 发行说明
kind: reference
status: maintained
domains: [zephyr, releases]
source_url: https://docs.zephyrproject.org/latest/releases/release-notes-4.2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="zephyr-4-2-0"></a>

<a id="zephyr-4-2"></a>

# 第2章\_Zephyr 4.2.0版本

原文：[官方页面](https://docs.zephyrproject.org/latest/releases/release-notes-4.2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Zephyr 4.2.0版本现已发布。

本版本的主要增强包括：

初步支持瑞萨RX（Renesas RX）

现在支持瑞萨RX架构，包括基于QEMU的开发板目标。（[开发板目标（Board Target）](../qemu_other_reference/P004_QEMU_Renesas_RX仿真开发板.md#qemu_rx)）

USB视频类驱动（USB Video Class Driver）

USB设备协议栈现在支持USB视频类（USB Video Class，UVC），可将摄像头及其他图像／视频源呈现为标准USB视频设备。入门可参考[USB视频摄像头（USB Video Webcam）](../usb/P124_USB视频摄像头示例.md#uvc)示例。

Twister功耗测试框架（Power Harness）

新增Twister测试框架，可测量被测设备（Device Under Test，DUT）的功耗，并确认其处于给定容差范围内。（[新Twister测试框架（Harness）](https://docs.zephyrproject.org/latest/develop/twister/harness/power.html#twister-power-harness)）

消息队列遥测传输协议MQTT 5.0

网络协议栈现在完整支持[MQTT 5.0](../networking/P059_MQTT客户端库.md#mqtt-socket-interface)协议。

经典蓝牙（Bluetooth Classic）改进

经典蓝牙协议栈现在支持免提配置文件（Hands-Free Profile，HFP）的音频网关（Audio Gateway，AG）及免提设备（Hands-Free，HF）角色。

Zephyr消息总线（Zbus）

[Zbus库](https://docs.zephyrproject.org/latest/services/zbus/index.html#zbus)随API v1.0.0发布进入稳定状态。

扩展开发板支持（Expanded Board Support）

本次发布新增96款开发板及22款扩展板（Shield）支持。（[新增开发板](#boards-added-in-zephyr-4-2)；[新增扩展板](#shields-added-in-zephyr-4-2)）

应用从Zephyr v4.1.0迁移到v4.2.0所需或建议的修改，见单独的[迁移指南（Migration Guide）](../releases_guides/P004_迁移到Zephyr_4.2.md#migration-4-2)。

以下各节按组件提供详细变更列表。

<a id="security-vulnerability-related"></a>

## 安全漏洞相关变更（Security Vulnerability Related）

本版本修复以下通用漏洞披露（CVE）项：


- <a id="index-0"></a>

  [CVE 2025-12890](https://www.cve.org/CVERecord?id=CVE-2025-12890)：[蓝牙外围设备错误处理格式异常的连接请求](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-8hrf-pfww-83v9)。
- <a id="index-1"></a>

  [CVE 2025-27809](https://www.cve.org/CVERecord?id=CVE-2025-27809)：[TLS客户端可能在不知情的情况下跳过服务器身份验证](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-03-1/)。
- <a id="index-2"></a>

  [CVE 2025-27810](https://www.cve.org/CVERecord?id=CVE-2025-27810)：[TLS握手可能被绕过身份验证](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-03-2/)。
- <a id="index-3"></a>

  [CVE 2025-2962](https://www.cve.org/CVERecord?id=CVE-2025-2962)：[dns_copy_qname中的无限循环](https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-2qp5-c2vq-g2ww)。
- <a id="index-4"></a>

  [CVE 2025-52496](https://www.cve.org/CVERecord?id=CVE-2025-52496)：[AESNI支持检测中的竞态条件](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-1/)（Race Condition）。
- <a id="index-5"></a>

  [CVE 2025-52497](https://www.cve.org/CVERecord?id=CVE-2025-52497)：[解析PEM加密材料时发生堆缓冲区下界越界读取](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-2/)（Heap Buffer Under-read）。
- <a id="index-6"></a>

  [CVE 2025-49600](https://www.cve.org/CVERecord?id=CVE-2025-49600)：[LMS验证中未检查返回值，可能绕过签名验证](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-3/)。
- <a id="index-7"></a>

  [CVE 2025-49601](https://www.cve.org/CVERecord?id=CVE-2025-49601)：[mbedtls_lms_import_public_key()中的越界读取](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-4/)。
- <a id="index-8"></a>

  [CVE 2025-49087](https://www.cve.org/CVERecord?id=CVE-2025-49087)：使用PKCS#7填充的分组密码解密中存在计时侧信道（Timing Side-channel）。（[使用PKCS#7填充的分组密码解密中的计时侧信道](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-5/)）
- <a id="index-9"></a>

  [CVE 2025-48965](https://www.cve.org/CVERecord?id=CVE-2025-48965)：[使用mbedtls_asn1_store_named_data()后发生空指针解引用](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-6/)。
- <a id="index-10"></a>

  [CVE 2025-47917](https://www.cve.org/CVERecord?id=CVE-2025-47917)：[mbedtls_x509_string_to_names()中易引起误解的内存管理行为](https://mbed-tls.readthedocs.io/en/latest/security-advisories/mbedtls-security-advisory-2025-06-7/)。
- <a id="index-11"></a>

  [CVE 2025-7403](https://www.cve.org/CVERecord?id=CVE-2025-7403)：原发行说明记载的保密期截至2025-09-05。

更多详细信息见：[https://docs.zephyrproject.org/latest/security/vulnerabilities.html](../security/P020_安全漏洞总览.md)。

<a id="api-changes"></a>

## API变更（API Changes）

<a id="removed-apis-and-options"></a>

### 已移除的API与选项（Removed APIs and Options）


- 移除已弃用的net_buf_put()及net_buf_get() API函数。
- 移除已弃用的include/zephyr/net/buf.h头文件。
- 移除Twister的--disable-unrecognized-section-test选项。相应测试已移除，该选项对应的行为已成为默认行为。
- 移除已弃用的键盘扫描（Kscan）子系统。
- 移除meas,ms5837，以[meas,ms5837-30ba](../sensor_microchip_nordic_nxp_binding_reference/P004_meas_ms5837-30ba.md#std-dtcompatible-meas-ms5837-30ba)及[meas,ms5837-02ba](../sensor_microchip_nordic_nxp_binding_reference/P003_meas_ms5837-02ba.md#std-dtcompatible-meas-ms5837-02ba)替代。
- 从[video_driver_api](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__driver__api.html)中移除get_ctrl驱动API。
- 移除CONFIG_I3C_USE_GROUP_ADDR及I3C设备的组地址（Group Address）支持。

<a id="deprecated-apis-and-options"></a>

### 已弃用的API与选项（Deprecated APIs and Options）


- 调度器Kconfig选项CONFIG_SCHED_DUMB及CONFIG_WAITQ_DUMB已重命名，原名称弃用；请改用[CONFIG_SCHED_SIMPLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SCHED_SIMPLE)及[CONFIG_WAITQ_SIMPLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WAITQ_SIMPLE)。
- 移除CONFIG_LWM2M_ENGINE_MESSAGE_HEADER_SIZE选项。所需头部空间应计入由[CONFIG_LWM2M_COAP_MAX_MSG_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_COAP_MAX_MSG_SIZE)设置的消息大小。尤其应确保CoAP块大小[CONFIG_LWM2M_COAP_BLOCK_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_COAP_BLOCK_SIZE)加上头部后，仍能容纳于配置的消息空间内。此前预留的头部空间为48字节。
- TLS凭据类型TLS_CREDENTIAL_SERVER_CERTIFICATE已重命名，原名称弃用；请改用[TLS_CREDENTIAL_PUBLIC_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8)。
- 弃用arduino_uno_r4_minima及arduino_uno_r4_wifi开发板目标，改用带修订版本的新arduino_uno_r4目标，即arduino_uno_r4@minima及arduino_uno_r4@wifi。
- 弃用esp32c6_devkitc开发板目标，重命名为esp32c6_devkitc/esp32c6/hpcore。
- 弃用xiao_esp32c6开发板目标，重命名为xiao_esp32c6/esp32c6/hpcore。
- 弃用CONFIG_HAWKBIT_DDI_NO_SECURITY选项，因为hawkBit服务器已在0.8.0版本移除匿名身份验证支持。
- 弃用CONFIG_BT_CONN_TX_MAX选项。待处理发送缓冲区数量现在与[CONFIG_BT_BUF_ACL_TX_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BUF_ACL_TX_COUNT)保持一致。
- 移除CONFIG_CRYPTO_TINYCRYPT_SHIM选项。它自Zephyr 4.0起弃用，此前已建议用户迁移到其他密码后端。
- 移除CONFIG_BT_MESH_USES_TINYCRYPT选项。它自Zephyr 4.0起弃用，此前已建议用户改用CONFIG_BT_MESH_USES_MBEDTLS_PSA或CONFIG_BT_MESH_USES_TFM_PSA。

<a id="stable-api-changes-in-this-release"></a>

### 本次发布的稳定API变更（Stable API Changes）


- net_mgmt事件处理函数[net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)及请求处理函数[net_mgmt_request_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga78b9302193bd0c5cc35d81d298a5eb6b)的API签名已更改：事件值类型从uint32_t改为uint64_t。

<a id="new-apis-and-options"></a>

### 新增API与选项（New APIs and Options）


- 架构（Architectures）


  - 从Zephyr中移除NIOS2架构。
  - `ARCH_HAS_VECTOR_TABLE_RELOCATION`
  - [CONFIG_SRAM_VECTOR_TABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SRAM_VECTOR_TABLE)从zephyr/Kconfig.zephyr移至zephyr/arch/Kconfig，并增加依赖条件。
- 蓝牙（Bluetooth）


  - 音频（Audio）


    - [`BT_BAP_ADV_PARAM_CONN_QUICK`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac290c620aa1861ea717dee37e1e83bfe)
    - [`BT_BAP_ADV_PARAM_CONN_REDUCED`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf1883b2596f793ef24913ef7f165c5dd)
    - [`BT_BAP_CONN_PARAM_SHORT_7_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga5d90920dfc8d554d0cd345edd0c36c66)
    - [`BT_BAP_CONN_PARAM_SHORT_10`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0469f86dc34ab738fbbcdf45cc105194)
    - [`BT_BAP_CONN_PARAM_RELAXED`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gad4a19588129f8cbf085dca166f0bc486)
    - [`BT_BAP_ADV_PARAM_BROADCAST_FAST`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf2e44d06b8b7aba57a80b1f04e65d7de)
    - [`BT_BAP_ADV_PARAM_BROADCAST_SLOW`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaa11e0195a02baa656085f305d911042d)
    - [`BT_BAP_PER_ADV_PARAM_BROADCAST_FAST`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#ga0f17a828720504892ff36447a4e3f7c3)
    - [`BT_BAP_PER_ADV_PARAM_BROADCAST_SLOW`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gaf71bf639a2fca0c4d5ab61bfd6354668)
    - [`bt_csip_set_member_set_size_and_rank()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gaef51ab05dbe9d8a69674f7020e8f837f)
    - [`bt_csip_set_member_get_info()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#gad80917089bc7e629cc3cb9d7fbf6cf45)
    - [`bt_bap_unicast_group_foreach_stream()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gad608ee07c8a50abf586a3bc31921f032)
    - [`bt_cap_unicast_group_create()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#gab49e8c2032a824516dc8d5f2f880dd8f)
    - [`bt_cap_unicast_group_reconfig()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c862b49aa1339225aeb05fad32c2f06)
    - [`bt_cap_unicast_group_add_streams()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga7b5d30c07e57f4db23f72836a3b12b2b)
    - [`bt_cap_unicast_group_delete()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga9af37b30b6c858c24892eb1739b5330a)
    - [`bt_cap_unicast_group_foreach_stream()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga6c13996298c3e3aa33eb40f74b7bfe44)
  - 主机（Host）


    - [`bt_le_get_local_features()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga650faa2a86f54499f4bc5a8657a55a87)
    - [`bt_le_bond_exists()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga309a67de79cc215db1d33251f267f361)
    - [`bt_br_bond_exists()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad88cf1dec20264f9bdde91571efe8dce)
    - [`bt_conn_lookup_addr_br()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga11ae1b656683cebe9db6a53e5166ad7a)
    - [`bt_conn_get_dst_br()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1b02a1ce8e48ad483d73d1efd803618c)
    - 低功耗蓝牙连接子速率（LE Connection Subrating）不再属于实验性功能。
    - [bt_unpair()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaceabbbe6e844650f791010e53c9df6a4)不再删除经典蓝牙绑定信息，新增[bt_br_unpair()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaccab07100ab64fd805fe1d468bc889ac)执行该操作。
    - [bt_foreach_bond()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad380b7f8984f8522c1b79f9bdc04905)不再查询经典蓝牙绑定信息，新增[bt_br_foreach_bond()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4c82193c50c616d9319c87ebcffabe66)执行该操作。
    - [bt_br_set_discoverable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae3376fdd364e9b9d6e304ec589ba00f5)新增limited参数，支持经典蓝牙的有限可发现模式（Limited Discoverable Mode）。
    - 启用经典蓝牙L2CAP重传及流量控制，包括[CONFIG_BT_L2CAP_RET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET)、[CONFIG_BT_L2CAP_FC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_FC)、[CONFIG_BT_L2CAP_ENH_RET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_ENH_RET)及[CONFIG_BT_L2CAP_STREAM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_STREAM)。
    - `bt_avrcp_get_cap()`
    - 改进经典蓝牙免提设备（HF），包括[CONFIG_BT_HFP_HF_CODEC_NEG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_CODEC_NEG)、[CONFIG_BT_HFP_HF_ECNR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ECNR)、[CONFIG_BT_HFP_HF_3WAY_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_3WAY_CALL)、[CONFIG_BT_HFP_HF_ECS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ECS)、[CONFIG_BT_HFP_HF_ECC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ECC)、[CONFIG_BT_HFP_HF_VOICE_RECG_TEXT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_VOICE_RECG_TEXT)、[CONFIG_BT_HFP_HF_ENH_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ENH_VOICE_RECG)、[CONFIG_BT_HFP_HF_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_VOICE_RECG)、[CONFIG_BT_HFP_HF_HF_INDICATORS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_HF_INDICATORS)、[CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY)及[CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY)。
    - 改进经典蓝牙免提音频网关（AG），包括[CONFIG_BT_HFP_AG_CODEC_NEG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_CODEC_NEG)、[CONFIG_BT_HFP_AG_ECNR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_ECNR)、[CONFIG_BT_HFP_AG_3WAY_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_3WAY_CALL)、[CONFIG_BT_HFP_AG_ECS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_ECS)、[CONFIG_BT_HFP_AG_ECC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_ECC)、[CONFIG_BT_HFP_AG_VOICE_RECG_TEXT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_VOICE_RECG_TEXT)、[CONFIG_BT_HFP_AG_ENH_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_ENH_VOICE_RECG)、[CONFIG_BT_HFP_AG_VOICE_TAG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_VOICE_TAG)、[CONFIG_BT_HFP_AG_HF_INDICATORS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_HF_INDICATORS)、[CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_HF_INDICATOR_ENH_SAFETY)、[CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_HF_INDICATOR_BATTERY)及[CONFIG_BT_HFP_AG_REJECT_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_REJECT_CALL)。
    - [bt_hfp_ag_cb](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__ag__cb.html)新增get_ongoing_call()回调。
    - [`bt_hfp_ag_ongoing_calls()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5614bf3f1de11959a0364f458523e06e)
    - 支持经典蓝牙L2CAP信令回显请求及响应（Echo Request / Response），包括[bt_l2cap_br_echo_cb](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__echo__cb.html)、[bt_l2cap_br_echo_cb_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga62c0115185f5026c1a842848dc5336ce)、[bt_l2cap_br_echo_cb_unregister()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga00ef7d0a42d8e544b195172af44b88b2)、[bt_l2cap_br_echo_req()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga3c6ad17ba18f5c00e39a379ed735de21)及[bt_l2cap_br_echo_rsp()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga8ebf537cc7e4c0a68a320f9c65c94b05)。
    - [`bt_a2dp_get_conn()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html#ga09470ceb08b66661d63c951736f34a5d)
    - [`bt_rfcomm_send_rpn_cmd()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gab38378db71d7f4631e47742ce4a5c59d)
- 构建系统（Build System）


  - 系统构建（Sysbuild）


    - Sysbuild使用[SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER)时，可通过SB_CONFIG_FIRMWARE_LOADER配置及选择固件加载器（Firmware Loader）镜像，例如用[SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR)选择SMP服务器。（[SMP服务器（Server）](../firmware_update/P022_SMP服务器示例.md#smp-svr)）
    - Sysbuild新增通过[SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD)启用单应用RAM加载的支持。
- 计数器（Counter）


  - [`counter_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__counter__interface.html#ga225705f1f6f3bef127de8ef84dcfba4e)
- 调试（Debug）


  - 核心转储（Core Dump）


    - ARM Cortex-M选择[CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN)时，默认启用[CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_THREAD_STACK_TOP)。
    - [`CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY)
    - [`CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_BACKEND_IN_MEMORY_SIZE)
- 显示（Display）

  > - 新增[display_clear()](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga62a6cd9e338aa07f789de60e64d3b3c4) API，以统一方式清除显示内容。
  > - 字符帧缓冲区（Character Frame Buffer，CFB）子系统现在可通过[cfb_draw_circle()](https://docs.zephyrproject.org/latest/doxygen/html/group__monochrome__character__framebuffer.html#ga2a87d5fd58bb7a56081668313f7038f6)绘制圆形。
- 集成电路间总线（I2C）


  - [i2c_configure_dt()](../hardware/P305_I2C公共接口.md#ga780c4b50a3dc89c01a98c432554c2795)。
  - [`I2C_DEVICE_DT_DEINIT_DEFINE`](../hardware/P305_I2C公共接口.md#ga831cf78c11ebfceb65315995504cb7fb)
  - [`I2C_DEVICE_DT_INST_DEINIT_DEFINE`](../hardware/P305_I2C公共接口.md#ga9c7a8248802760a2f9509e76377fb38a)
- 改进型集成电路间总线（I3C）


  - [`CONFIG_I3C_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I3C_MODE)
  - [`CONFIG_I3C_CONTROLLER_ROLE_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I3C_CONTROLLER_ROLE_ONLY)
  - [`CONFIG_I3C_TARGET_ROLE_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I3C_TARGET_ROLE_ONLY)
  - [`CONFIG_I3C_DUAL_ROLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I3C_DUAL_ROLE)
  - [`i3c_ccc_do_rstdaa()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac8bdf8d14db5e7fd06846637253cbb76)
- 内核（Kernel）

> - `K_TIMEOUT_ABS_SEC`
> - [`timespec_add()`](../timeutil_reference/P008_timespec时间工具接口.md#ga81026756e417d086b4f53306d04c8d10)
> - [`timespec_compare()`](../timeutil_reference/P008_timespec时间工具接口.md#gafa281a298f8b2f011875bb00094260fc)
> - [`timespec_equal()`](../timeutil_reference/P008_timespec时间工具接口.md#gaedc15d71f9eee8e243c070a3e07d919f)
> - [`timespec_is_valid()`](../timeutil_reference/P008_timespec时间工具接口.md#ga2426889e703021e8b6f8a0ccab885bb6)
> - [`timespec_negate()`](../timeutil_reference/P008_timespec时间工具接口.md#ga38216267ef6ca24e2b05d77104f5837a)
> - [`timespec_normalize()`](../timeutil_reference/P008_timespec时间工具接口.md#ga57f165604525ef6b680f646d97a38538)
> - [`timespec_from_timeout()`](../timeutil_reference/P002_时间表示接口.md#gab9b5ccdfd7abeaf7a05ebf273cb4d022)
> - [`timespec_to_timeout()`](../timeutil_reference/P002_时间表示接口.md#gab6b84a5c3f4fd24ab8f568f0626a0149)
> - [`k_heap_array_get()`](../heap_reference/P001_内核堆公共接口.md#ga3aa215396381e1513edf50bd9563dee5)


- 轻量多功能图形库（Light and Versatile Graphics Library，LVGL）

  > - LVGL模块同步到v9.3，包含多项上游改进及新功能。
  > - LVGL子系统现在支持同时使用多个显示器，并正确绑定输入设备与显示器。
  > - 为SSD1327、SSD1320、SSD1322及ST75256等显示器新增L8/Y8像素格式支持。
  > - [`CONFIG_LV_Z_COLOR_MONO_HW_INVERSION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_Z_COLOR_MONO_HW_INVERSION)
- LoRa广域网（LoRaWAN）

  > - [`lorawan_request_link_check()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaed19bb9c528f8f21104201fd0816e3a9)
- 管理（Management）


  - 微控制器管理（MCUmgr）


    - 镜像管理组（Image Management Group）通过[CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER)新增固件加载器支持。
    - 操作系统管理组（OS Group）的复位命令通过[CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE)新增可选启动模式，采用保留启动模式（Retention Boot Mode）机制。
- 网络（Networking）：


  - 受限应用协议（CoAP）


    - [`COAPS_SERVICE_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga1ec49f2bc2c378431c4721080a13d11d)
  - IPv4动态主机配置协议（DHCPv4）


    - [`CONFIG_NET_DHCPV4_INIT_REBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_INIT_REBOOT)
  - 域名系统（DNS）


    - [`dns_resolve_service()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)
    - [`dns_resolve_reconfigure_with_interfaces()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3d22eed1d6d017e5bd7a2344775d33b7)
  - 超文本传输协议（HTTP）


    - [`CONFIG_HTTP_SERVER_COMPRESSION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER_COMPRESSION)
  - 互联网协议第4版（IPv4）


    - [`CONFIG_NET_IPV4_MTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_MTU)
  - 轻量级机器到机器协议（LwM2M）


    - [`CONFIG_LWM2M_SERVER_BOOTSTRAP_ON_FAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_SERVER_BOOTSTRAP_ON_FAIL)
    - 实现大于、小于及步进观察属性（Greater Than / Less Than / Step Observe Attributes）的处理，见[CONFIG_LWM2M_MAX_NOTIFIED_NUMERICAL_RES_TRACKED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_MAX_NOTIFIED_NUMERICAL_RES_TRACKED)。
  - 其他（Misc）


    - [`net_if_oper_state_change_time()`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#gabae216ba527bdfcd945ef19fb48e56be)
  - 消息队列遥测传输协议（MQTT）


    - [`CONFIG_MQTT_VERSION_5_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_VERSION_5_0)
    - [`mqtt_transport.if_name`](https://docs.zephyrproject.org/latest/doxygen/html/structmqtt__transport.html#a7cfdf50105a275612dbda28e7c02808e)
  - OpenThread协议栈


    - OpenThread相关Kconfig选项从[subsys/net/l2/openthread/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/openthread/Kconfig)移至[modules/openthread/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig)。
    - 重构OpenThread网络API，见迁移指南的OpenThread章节。（[迁移指南（Migration Guide）](../releases_guides/P004_迁移到Zephyr_4.2.md#migration-4-2)）
    - [`CONFIG_OPENTHREAD_SYS_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SYS_INIT)
    - [`CONFIG_OPENTHREAD_SYS_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SYS_INIT_PRIORITY)
  - 简单网络时间协议（SNTP）


    - [`sntp_init_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gacd621da6168cf064d0bf6c370f6ca597)
    - [`sntp_send_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gab6adcd7259bdfa841b57e535c380508d)
    - [`sntp_read_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gac73db957041a6814abb286fd9143ddb5)
    - [`sntp_close_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__sntp.html#gaeb595e89c56fbb619010e3c8d7b2b5b1)
  - 套接字（Sockets）


    - [`CONFIG_NET_SOCKETS_INET_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_INET_RAW)
    - [`socket_offload_dns_enable()`](https://docs.zephyrproject.org/latest/doxygen/html/socket__offload_8h.html#a0d0123d234cd292282a272cb2e2eeb3c)
    - 新增套接字服务库（[Socket Services](../networking/P041_套接字服务.md#socket-service-interface)）的文档页。
    - 新增套接字选项（Socket Options）：


      - `IP_MULTICAST_LOOP`
      - `IPV6_MULTICAST_LOOP`
      - `TLS_CERT_VERIFY_RESULT`
  - 无线局域网（Wi-Fi）


    - [`CONFIG_WIFI_USAGE_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE)
    - Wi-Fi管理文档doc/connectivity/networking/api/wifi.rst新增章节，逐步介绍使用FreeRADIUS脚本生成Wi-Fi测试证书，便于用户在自己的测试环境中复现。
    - hostap进程间通信（IPC）机制从socketpair改为k_fifo。使用原生Wi-Fi协议栈时，根据启用的配置选项，可节省最多约6～8 kB内存。
  - 网络性能测试工具（zperf）


    - [`CONFIG_ZPERF_SESSION_PER_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZPERF_SESSION_PER_THREAD)
    - `zperf_upload_params.data_loader`
    - [`CONFIG_NET_ZPERF_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_SERVER)
- 高速外围组件互连（PCIe）

  > - [`CONFIG_NVME_PRP_PAGE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVME_PRP_PAGE_SIZE)
- 电源管理（Power Management）

  > - [`CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_USE_SYSTEM_WQ)
  > - [`CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ)
  > - [`CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ)
  > - [`CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_STACK_SIZE)
  > - [`CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_PRIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_PRIO)
  > - [`CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_INIT_PRIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_DEDICATED_WQ_INIT_PRIO)
  > - [`CONFIG_PM_DEVICE_RUNTIME_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME_ASYNC)
- 串行外设接口（SPI）


  - [`SPI_DEVICE_DT_DEINIT_DEFINE`](../hardware/P318_SPI公共接口.md#gaf98b0cb38cb316b9fe05146bba34126d)
  - [`SPI_DEVICE_DT_INST_DEINIT_DEFINE`](../hardware/P318_SPI公共接口.md#ga50cbb6845d230033f192f1e716fd9f2b)
- 传感器（Sensor）


  - [`sensor_value_to_deci()`](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabbcb8ad4b9484cba77ae65e2d3ba7457)
  - [`sensor_value_to_centi()`](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae812fb481bfe3a8053f0fc23f8617434)
- 步进电机（Stepper）


  - `stepper_stop()`
- 存储（Storage）


  - [`flash_area_copy()`](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa50bb1b455a9004f9c24e4af9fd74cd7)
- 系统功能（Sys）


  - [`util_eq()`](../util_reference/P001_通用工具公共接口.md#gaca458acb618a71bd95cb05fe8179d602)
  - [`util_memeq()`](../util_reference/P001_通用工具公共接口.md#gaccffc30e3554212d2cc3803c44cf86f8)
  - [`sys_clock_gettime()`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga92bad374219a4cd32299569c94907877)
  - [`sys_clock_settime()`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga297e885a8a95c762ae882e61f7d381b4)
  - [`sys_clock_nanosleep()`](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga01ca6f2ad006ed530ffec06c262ae380)
- 通用串行总线（USB）


  - `uvc_set_video_dev()`
- 固件更新服务（UpdateHub）


  - [`updatehub_report_error()`](https://docs.zephyrproject.org/latest/doxygen/html/group__updatehub.html#gaa3606855ac680341e7b568421562e165)
- 视频（Video）


  - [`video_api_ctrl_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga522b4027fc6f22bf59f4face3c97e303)
  - [`video_query_ctrl()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga8813a656a66adc6bfb10fb7f27194898)
  - [`video_print_ctrl()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga2bff04c6abc344350d6b0036289a701e)
  - [`video_api_selection_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gab4d2eb34f8ccc95fa6dcda7848f4408a)
  - [`video_set_selection()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga6ea31432d37e0f8f46e0f6c2690ee3e9)
  - [`video_get_selection()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__format.html#ga0c30d2802c82b28cbb5029e7bc52b5b4)
  - [video-sw-generator](../snippets/P005_视频软件发生器配置片段.md#snippet-video-sw-generator)
  - [`video_get_csi_link_freq()`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__control.html#ga41e450607b4dc062fac682728ec7a79d)
  - [`VIDEO_CID_LINK_FREQ`](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga2142e2819c445b70d82067a3cfb193c8)
  - [VIDEO_CID_AUTO_WHITE_BALANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga7e2ce049ed534e1c29ac47d33013e180)及BASE控制类别中的其他控制项。
  - [VIDEO_CID_EXPOSURE_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga036f78623bcae18ea9627d45d1209245)及CAMERA控制类别中的其他控制项。
  - [VIDEO_PIX_FMT_Y10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga0506f2c8aa1a82f02fc9383d99b43bc3)及Y12、Y14、Y16变体。
  - [VIDEO_PIX_FMT_SRGGB10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga604d2f3501407546aa924e2fdb37be2f)及12P、14P变体，覆盖全部4种拜耳（Bayer）排列。
  - [video_buffer.index](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__buffer.html#a84550afc674ad543c8c709d55ececda2)字段。
  - [video_ctrl_query.int_menu](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__ctrl__query.html#ad0d74a650e83dece50ca2d46d9e5c750)字段。
  - [VIDEO_MIPI_CSI2_DT_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html#ga59d6f35198b6412a9aa78c094ecfaa19)及其他MIPI标准值。
- Zephyr消息总线（ZBus）


  - Zbus随API v1.0.0发布进入稳定状态。
  - 运行时观察者（Runtime Observers）无需堆也可工作。现在可为其节点选择静态分配、动态分配或不分配。
  - 使用[CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE)的运行时观察者必须调用新函数[zbus_chan_add_obs_with_node()](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga6f2b8db3a13546e3d0fd095ff9cd37ba)。
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_DYNAMIC)
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_STATIC)
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_ALLOC_NONE)
  - [`CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_POOL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_RUNTIME_OBSERVERS_NODE_POOL_SIZE)

<a id="new-boards"></a>

<a id="boards-added-in-zephyr-4-2"></a>

## 新增开发板（New Boards）


- Adafruit Industries, LLC

  > - [Adafruit Feather ESP32S2](../boards_adafruit_feather_esp32_rp2040/P005_Adafruit_Feather_ESP32S2.md#adafruit_feather_esp32s2)开发板（adafruit_feather_esp32s2）
  > - [Adafruit Feather ESP32S2 TFT](../boards_adafruit_feather_esp32_rp2040/P006_Adafruit_Feather_ESP32S2_TFT.md#adafruit_feather_esp32s2_tft)开发板（adafruit_feather_esp32s2_tft）
  > - [Adafruit Feather ESP32S2 TFT Reverse](../boards_adafruit_feather_esp32_rp2040/P007_Adafruit_Feather_ESP32S2_TFT_Reverse.md#adafruit_feather_esp32s2_tft_reverse)开发板（adafruit_feather_esp32s2_tft_reverse）
  > - [Adafruit Feather ESP32S3](../boards_adafruit_feather_esp32_rp2040/P008_Adafruit_Feather_ESP32S3.md#adafruit_feather_esp32s3)开发板（adafruit_feather_esp32s3）
  > - [Adafruit Feather ESP32S3 TFT](../boards_adafruit_feather_esp32_rp2040/P009_Adafruit_Feather_ESP32S3_TFT.md#adafruit_feather_esp32s3_tft)开发板（adafruit_feather_esp32s3_tft）
  > - [Adafruit ESP32-S3 Reverse TFT Feather](../boards_adafruit_feather_esp32_rp2040/P010_Adafruit_ESP32-S3_Reverse_TFT_Feather.md#adafruit_feather_esp32s3_tft_reverse)开发板（adafruit_feather_esp32s3_tft_reverse）
- Advanced Micro Devices（AMD）, Inc.

  > - Versal 2 RPU 开发板（Development Board）（versal2_rpu）（[Versal 2实时处理单元开发板（RPU Development Board）](../boards_amd/P007_Versal_2_RPU_development_board.md#versal2_rpu)）
  > - Versal NET RPU 开发板（Development Board）（versalnet_rpu）（[Versal NET实时处理单元开发板（RPU Development Board）](../boards_amd/P011_Versal_NET_RPU_development_board.md#versalnet_rpu)）
- Aesc Silicon

  > - [ElemRV Flask-N](../boards_aesc_aithinker_alientek/P002_ElemRV_Flask-N.md#elemrv_flask_n)开发板（elemrv）
- 安信可（Ai-Thinker Co., Ltd.）

  > - Ai-Thinker WB2-12F 开发板（Development Board）（ai_wb2_12f_kit）（[安信可Ai-Thinker WB2-12F开发板（Development Board）](../boards_aesc_aithinker_alientek/P007_Ai-Thinker_WB2-12F_development_board.md#ai_wb2_12f_kit)）
- Ambiq Micro, Inc.

  > - Apollo510 SoC评估板（Evaluation Board）（apollo510_evb）（[Apollo510片上系统评估板（SoC Evaluation Board）](../boards_alif_ambiq/P013_Apollo510_SOC_Evaluation_Board.md#apollo510_evb)）
- Analog Devices, Inc.

  > - [MAX32657EVKIT](../boards_adi_max32_max78_sdp/P006_MAX32657EVKIT.md#max32657evkit)开发板（max32657evkit）
- Arduino

  > - [Arduino Nano Matter](../boards_arduino/P008_Arduino_Nano_Matter.md#arduino_nano_matter)开发板（arduino_nano_matter）
  > - [Arduino Portenta C33](../boards_arduino/P014_Arduino_Portenta_C33.md#arduino_portenta_c33)开发板（arduino_portenta_c33）
- Arm公司（ARM Ltd.）

  > - [MPS4 Corstone FVP](../boards_arm/P010_MPS4_Corstone_FVP.md#mps4)开发板（mps4）
- BeagleBoard.org基金会（Foundation）

  > - [PocketBeagle 2](../boards_beagle/P009_PocketBeagle_2.md#pocketbeagle_2)开发板（pocketbeagle_2）
- Blues Wireless

  > - [Cygnet](../boards_bouffalo_qnx_bliiot_blues/P009_Cygnet.md#cygnet)开发板（cygnet）
- 博流（南京）有限公司（Bouffalo Lab）

  > - BL604E IOT DVK 开发板（Development Board）（bl604e_iot_dvk）（[BL604E IOT DVK开发板（Development Board）](../boards_bouffalo_qnx_bliiot_blues/P001_BL604E_IOT_DVK_development_board.md#bl604e_iot_dvk)）
- Doctors of Intelligence & Technology

  > - DT-BL10 共存模块开发套件（Coexistence Module Development Kit）（dt_bl10_devkit）（[DT-BL10共存模块开发套件（Coexistence Module Development Kit）](../boards_cypress_to_dragino/P018_DT-BL10_coexistence_Module_Development_Kit.md#dt_bl10_devkit)）
- ENE Technology, Inc.公司

  > - [ENE KB1062_EVB](../boards_ebyte_to_enjoydigital/P021_ENE_KB1062_EVB.md#kb1062_evb)开发板（kb1062_evb）
- 乐鑫信息科技（Espressif Systems）

  > - [ESP32-DevKitC](../boards_espressif/P016_ESP32-DevKitC.md#esp32_devkitc)开发板（esp32_devkitc）
- Ezurio

  > - [BL54L15 DVK](../boards_eurovibes_ezurio/P004_BL54L15_DVK.md#bl54l15_dvk)开发板（bl54l15_dvk）
  > - `bl54l15u_dvk`
- FANKE Technology Co., Ltd.（反客科技）

  > - [FK743M5-XIH6](../boards_fanke_to_gardena/P002_FK743M5-XIH6.md#fk743m5_xih6)开发板（fk743m5_xih6）
- IAR Systems AB

  > - [STM32F429II-ACA](../boards_gd_to_iar/P038_STM32F429II-ACA.md#stm32f429ii_aca)开发板（stm32f429ii_aca）
- 英飞凌科技（Infineon Technologies）

  > - XMC7200 评估套件（Evaluation Kit）（kit_xmc72_evk）（[XMC7200评估套件（Evaluation Kit）](../boards_infineon_innblue/P019_XMC7200_Evaluation_Kit.md#kit_xmc72_evk)）
- 英特尔公司（Intel Corporation）

  > - [Bartlett Lake P CRB](../boards_intel_ite/P007_Bartlett_Lake_P_CRB.md#intel_btl_s_crb)开发板（intel_btl_s_crb）
- 联阳半导体（ITE Tech. Inc.）

  > - `it515xx_evb`
- KWS Computersysteme Gmbh

  > - [Pico2-SPE](../boards_jhoinrch_to_kws/P017_Pico2-SPE.md#pico2_spe)开发板（pico2_spe）
  > - [Pico-SPE](../boards_jhoinrch_to_kws/P018_Pico-SPE.md#pico_spe)开发板（pico_spe）
- 制造商：LilyGO（Shenzhen Xinyuan Electronic Technology Co., Ltd）

  > - [T-Dongle S3](../boards_lilygo_to_m5stack/P003_T-Dongle_S3.md#tdongle_s3)开发板（tdongle_s3）
  > - [TTGO TBeam](../boards_lilygo_to_m5stack/P008_TTGO_TBeam.md#ttgo_tbeam)开发板（ttgo_tbeam）
  > - [TTGO T-OI-PLUS](../boards_lilygo_to_m5stack/P009_TTGO_T-OI-PLUS.md#ttgo_toiplus)开发板（ttgo_toiplus）
  > - [T-Watch S3](../boards_lilygo_to_m5stack/P010_T-Watch_S3.md#twatch_s3)开发板（twatch_s3）
- M5Stack

  > - [Fire](../boards_lilygo_to_m5stack/P025_Fire.md#m5stack_fire)开发板（m5stack_fire）
- 微芯科技（Microchip Technology Inc.）

  > - [MEC17xxEVB ASSY6941](../boards_microchip/P012_MEC17xxEVB_ASSY6941.md#mec_assy6941)开发板（mec_assy6941）
  > - SAMA7G54 评估套件（Evaluation Kit）（sama7g54_ek）（[SAMA7G54评估套件](../boards_microchip/P030_SAMA7G54_Evaluation_Kit.md#sama7g54_ek)）
- MikroElektronika d.o.o.

  > - [MikroE Quail](../boards_mikroe_to_mxchip/P006_MikroE_Quail.md#mikroe_quail)开发板（mikroe_quail）
- Nordic Semiconductor

  > - [nRF54LM20 DK](../boards_nordic/P014_nRF54LM20_DK.md#nrf54lm20dk)开发板（nrf54lm20dk）
- 新唐科技（Nuvoton Technology Corporation）

  > - [NPCK3M8K_EVB](../boards_norik_to_nuvoton/P009_NPCK3M8K_EVB.md#npck3m8k_evb)开发板（npck3m8k_evb）
  > - [NUMAKER M55M1](../boards_norik_to_nuvoton/P020_NUMAKER_M55M1.md#numaker_m55m1)开发板（numaker_m55m1）
- 恩智浦半导体（NXP Semiconductors）

  > - [FRDM-MCXA153](../boards_nxp_frdm_mcx_rw/P001_FRDM-MCXA153.md#frdm_mcxa153)开发板（frdm_mcxa153）
  > - [i.MX943 EVK](../boards_nxp_imx_evk/P008_i.MX943_EVK.md#imx943_evk)开发板（imx943_evk）
  > - [MCX-N9XX-EVK](../boards_nxp_remaining/P003_MCX-N9XX-EVK.md#mcx_n9xx_evk)开发板（mcx_n9xx_evk）
  > - [S32K148EVB-Q176](../boards_nxp_remaining/P011_S32K148EVB-Q176.md#s32k148_evb)开发板（s32k148_evb）
- Octavo Systems LLC

  > - [OSD32MP1-BRK](../boards_octavo_olimex_openhw_openisa/P002_OSD32MP1-BRK.md#osd32mp1_brk)开发板（osd32mp1_brk）
- OpenHW Group

  > - Digilent CV32A6 基于Genesys 2开发板（cv32a6_genesys_2）（[Digilent Genesys 2上的CV32A6](../boards_octavo_olimex_openhw_openisa/P013_Digilent_CV32A6_on_Genesys_2.md#cv32a6_genesys_2)）
  > - Digilent CV64A6 基于Genesys 2开发板（cv64a6_genesys_2）（[Digilent Genesys 2上的CV64A6](../boards_octavo_olimex_openhw_openisa/P014_Digilent_CV64A6_on_Genesys_2.md#cv64a6_genesys_2)）
- Pimoroni Ltd.

  > - [Pimoroni Pico Plus2](../boards_pimoroni_radxa/P002_Pimoroni_Pico_Plus2.md#pico_plus2)开发板（pico_plus2）
- QEMU模拟器

  > - QEMU仿真： Renesas RX（qemu_rx）（[QEMU仿真：Renesas RX](../qemu_other_reference/P004_QEMU_Renesas_RX仿真开发板.md#qemu_rx)）
- Raytac Corporation

  > - [AN54LQ-DB-15](../boards_rak_raspberry_raytac/P015_AN54LQ-DB-15.md#raytac_an54lq_db_15)开发板（raytac_an54lq_db_15）
  > - [AN7002Q-DB-5340](../boards_rak_raspberry_raytac/P017_AN7002Q-DB-5340.md#raytac_an7002q_db)开发板（raytac_an7002q_db）
  > - [MDBT50Q-CX-40 Dongle](../boards_rak_raspberry_raytac/P019_MDBT50Q-CX-40_Dongle.md#raytac_mdbt50q_cx_40_dongle)开发板（raytac_mdbt50q_cx_40_dongle）
- 瑞萨电子（Renesas Electronics Corporation）

  > - RA8P1 评估套件（Evaluation Kit）（ek_ra8p1）（[RA8P1评估套件](../boards_renesas_ra/P024_RA8P1_Evaluation_Kit.md#ek_ra8p1)）
  > - 瑞萨入门套件（Renesas Starter Kit）： RX130（rsk_rx130）（[瑞萨RX130入门套件（Renesas Starter Kit）](../boards_renesas_rx_rz/P021_Renesas_Starter_Kit_for_RX130.md#rsk_rx130)）
  > - RZ/A2M 评估套件（Evaluation Kit）（rza2m_evk）（[RZ/A2M评估套件](../boards_renesas_rx_rz/P024_RZ_A2M_Evaluation_Kit.md#rza2m_evk)）
  > - RZ/A3UL SMARC 评估板套件（Evaluation Board Kit）（rza3ul_smarc）（[RZ/A3UL SMARC评估板套件](../boards_renesas_rx_rz/P026_RZ_A3UL_SMARC_Evaluation_Board_Kit.md#rza3ul_smarc)）
  > - RZ/G2L SMARC 评估板套件（Evaluation Board Kit）（rzg2l_smarc）（[RZ/G2L SMARC评估板套件](../boards_renesas_rx_rz/P027_RZ_G2L_SMARC_Evaluation_Board_Kit.md#rzg2l_smarc)）
  > - RZ/G2LC SMARC 评估板套件（Evaluation Board Kit）（rzg2lc_smarc）（[RZ/G2LC SMARC评估板套件](../boards_renesas_rx_rz/P028_RZ_G2LC_SMARC_Evaluation_Board_Kit.md#rzg2lc_smarc)）
  > - RZ/G2UL SMARC 评估板套件（Evaluation Board Kit）（rzg2ul_smarc）（[RZ/G2UL SMARC评估板套件](../boards_renesas_rx_rz/P029_RZ_G2UL_SMARC_Evaluation_Board_Kit.md#rzg2ul_smarc)）
  > - 瑞萨入门套件+（Renesas Starter Kit+）： RZ/N2L（rzn2l_rsk）（[瑞萨RZ/N2L入门套件Plus（Starter Kit+）](../boards_renesas_rx_rz/P033_Renesas_Starter_Kit_for_RZ_N2L.md#rzn2l_rsk)）
  > - 瑞萨入门套件+（Renesas Starter Kit+）： RZ/T2L（rzt2l_rsk）（[瑞萨RZ/T2L入门套件Plus](../boards_renesas_rx_rz/P035_Renesas_Starter_Kit_for_RZ_T2L.md#rzt2l_rsk)）
  > - 瑞萨入门套件+（Renesas Starter Kit+）： RZ/T2M（rzt2m_rsk）（[瑞萨RZ/T2M入门套件Plus](../boards_renesas_rx_rz/P036_Renesas_Starter_Kit_for_RZ_T2M.md#rzt2m_rsk)）
  > - RZ/V2H 评估板套件（Evaluation Board Kit）（rzv2h_evk）（[RZ/V2H评估板套件](../boards_renesas_rx_rz/P037_RZ_V2H_Evaluation_Board_Kit.md#rzv2h_evk)）
  > - RZ/V2L SMARC 评估板套件（Evaluation Board Kit）（rzv2l_smarc）（[RZ/V2L SMARC评估板套件](../boards_renesas_rx_rz/P038_RZ_V2L_SMARC_Evaluation_Board_Kit.md#rzv2l_smarc)）
  > - RZ/V2N 评估板套件（Evaluation Board Kit）（rzv2n_evk）（[RZ/V2N评估板套件](../boards_renesas_rx_rz/P039_RZ_V2N_Evaluation_Board_Kit.md#rzv2n_evk)）
- Seeed Technology Co., Ltd

  > - [XIAO MG24](../boards_seeed/P016_XIAO_MG24.md#xiao_mg24)开发板（xiao_mg24）
  > - [XIAO RA4M1](../boards_seeed/P020_XIAO_RA4M1.md#xiao_ra4m1)开发板（xiao_ra4m1）
- sensry.io

  > - Ganymed 入门套件（Starter Kit，SK）（ganymed_sk）（[Ganymed入门套件（Starter Kit，SK）](../boards_retronix_sifli/P021_Ganymed_Starter_Kit_SK.md#ganymed_sk)）
- 上海睿赛德电子科技有限公司（Shanghai Ruiside Electronic Technology Co., Ltd.）

  > - [ART-Pi2](../boards_realtek_ruiside_sifive/P011_ART-Pi2.md#art_pi2)开发板（art_pi2）
  > - RA8D1 视觉开发板（Vision Board）（ra8d1_vision_board）（[RA8D1 Vision Board视觉开发板](../boards_realtek_ruiside_sifive/P013_RA8D1_Vision_Board.md#ra8d1_vision_board)）
- 芯科科技（Silicon Laboratories）

  > - SiWx917 Wi-Fi 6 and 低功耗蓝牙（Bluetooth LE） 8 MB Flash + 8 MB外部PSRAM 无线电板（Radio Board） (SiWx91x-RB4342A)（siwx917_rb4342a）（[SiWx917 Wi-Fi 6与低功耗蓝牙8 MB闪存、8 MB外部PSRAM无线电板，SiWx91x-RB4342A](../boards_silabs/P026_SiWx917_Wi-Fi_6_and_Bluetooth_LE_8_MB_Flash_8_MB_ext_PSRAM_Radio_Board_SiWx91x-RB4342A.md#siwx917_rb4342a)）
  > - [EFR32xG21 2.4 GHz 20 dBm (SLWRB4180B)](../boards_silabs/P036_EFR32xG21_2.4_GHz_20_dBm_SLWRB4180B.md#slwrb4180b)开发板（slwrb4180b）
- Space Cubics, LLC公司

  > - [SC-OBC Module A1](../boards_retronix_sifli/P009_SC-OBC_Module_A1.md#scobc_a1)开发板（scobc_a1）
- 意法半导体（STMicroelectronics）

  > - [Nucleo F439ZI开发板](../boards_st_nucleo/P025_Nucleo_F439ZI.md#nucleo_f439zi)（nucleo_f439zi）
  > - [Nucleo U385RG Q开发板](../boards_st_nucleo/P067_Nucleo_U385RG_Q.md#nucleo_u385rg_q)（nucleo_u385rg_q）
  > - [Nucleo WBA65RI开发板](../boards_st_nucleo/P078_Nucleo_WBA65RI.md#nucleo_wba65ri)（nucleo_wba65ri）
  > - [STM32H757I Eval](../boards_st_discovery_eval/P039_STM32H757I_Eval.md#stm32h757i_eval)开发板（stm32h757i_eval）
  > - [STM32MP135F-DK Discovery](../boards_st_discovery_eval/P047_STM32MP135F-DK_Discovery.md#stm32mp135f_dk)开发板（stm32mp135f_dk）
  > - STM32MP257F-EV1 评估板（Evaluation Board）（stm32mp257f_ev1）（[STM32MP257F-EV1评估板（Evaluation Board）](../boards_st_discovery_eval/P051_STM32MP257F-EV1_Evaluation_Board.md#stm32mp257f_ev1)）
  > - STM32U5G9J 探索套件（Discovery Kit） 1（stm32u5g9j_dk1）（[STM32U5G9J探索套件1（Discovery Kit 1）](../boards_st_discovery_eval/P055_STM32U5G9J_Discovery_Kit_1.md#stm32u5g9j_dk1)）
  > - STM32U5G9J 探索套件（Discovery Kit）（stm32u5g9j_dk2）（[STM32U5G9J探索套件（Discovery Kit）](../boards_st_discovery_eval/P056_STM32U5G9J_Discovery_Kit.md#stm32u5g9j_dk2)）
- 德州仪器（Texas Instruments）

  > - [TI AM243x-EVM](../boards_ti/P001_TI_AM243x-EVM.md#am243x_evm)开发板（am243x_evm）
  > - [MSPM0G3507 Launchpad](../boards_ti/P018_MSPM0G3507_Launchpad.md#lp_mspm0g3507)开发板（lp_mspm0g3507）
  > - [SK-AM64](../boards_ti/P024_SK-AM64.md#sk_am64)开发板（sk_am64）
- u-blox

  > - [EVK-IRIS-W106-RW612](../boards_ublox_misc/P010_EVK-IRIS-W106-RW612.md#ubx_evk_iris_w1)开发板（ubx_evk_iris_w1）
- Variscite Ltd.

  > - [DART-MX8M-PLUS](../boards_ublox_misc/P025_DART-MX8M-PLUS.md#imx8mp_var_dart)开发板（imx8mp_var_dart）
  > - [VAR-SOM-MX8M-PLUS](../boards_ublox_misc/P026_VAR-SOM-MX8M-PLUS.md#imx8mp_var_som)开发板（imx8mp_var_som）
  > - [DART-MX93](../boards_ublox_misc/P027_DART-MX93.md#imx93_var_dart)开发板（imx93_var_dart）
  > - [VAR-SOM-MX93](../boards_ublox_misc/P028_VAR-SOM-MX93.md#imx93_var_som)开发板（imx93_var_som）
- Waveshare Electronics微雪电子

  > - [ESP32-S3-Matrix](../boards_waveshare_tail/P009_ESP32-S3-Matrix.md#esp32s3_matrix)开发板（esp32s3_matrix）
  > - [RP2040-Plus](../boards_waveshare_tail/P018_RP2040-Plus.md#rp2040_plus)开发板（rp2040_plus）
- WeAct Studio

  > - [BluePill Plus CH32V203](../boards_weact/P006_BluePill_Plus_CH32V203.md#bluepillplus_ch32v203)开发板（bluepillplus_ch32v203）
  > - STM32F446 核心板（Core Board） V1.1（weact_stm32f446_core）（[STM32F446核心板V1.1](../boards_weact/P020_STM32F446_Core_Board_V1.1.md#weact_stm32f446_core)）
- WinChipHead

  > - WCH CH32V003F4P6 开发板（Development Board）（ch32v003f4p6_dev_board）（[WCH CH32V003F4P6开发板](../boards_waveshare_tail/P024_WCH_CH32V003F4P6_Development_Board.md#ch32v003f4p6_dev_board)）
  > - [WCH CH32V006EVT](../boards_waveshare_tail/P025_WCH_CH32V006EVT.md#ch32v006evt)开发板（ch32v006evt）
  > - [WCH CH32V303VCT6_EVT](../boards_waveshare_tail/P028_WCH_CH32V303VCT6_EVT.md#ch32v303vct6_evt)开发板（ch32v303vct6_evt）
  > - [WCH LinkW](../boards_waveshare_tail/P032_WCH_LinkW.md#linkw)开发板（linkw）
- WIZnet Co., Ltd.

  > - [W5500-EVB-Pico2](../boards_waveshare_tail/P044_W5500-EVB-Pico2.md#w5500_evb_pico2)开发板（w5500_evb_pico2）
- Würth Elektronik GmbH.

  > - [Ophelia-IV EV](../boards_waveshare_tail/P036_Ophelia-IV_EV.md#ophelia4ev)开发板（ophelia4ev）

<a id="new-shields"></a>

<a id="shields-added-in-zephyr-4-2"></a>

### 新增扩展板（New Shields）


- [Arduino Giga显示扩展板（Display Shield）](../boards_shields/P046_Arduino_GIGA_Display_Shield.md#arduino-giga-display-shield)
- [Arduino Modulino按键模块（Buttons）](../boards_shields/P047_Arduino_Modulino_Buttons.md#arduino-modulino-buttons)
- [Arduino Modulino SmartLEDs扩展板](../boards_shields/P050_Arduino_Modulino_Pixels.md#arduino-modulino-pixels)
- [DVP 20引脚OV7670扩展板](../boards_shields/P061_DVP_20-pin_OV7670_Camera_Module.md#dvp-20pin-ov7670)
- [EVAL AD4052 ARDZ扩展板](../boards_shields/P065_EVAL-AD4052-ARDZ.md#eval-ad4052-ardz)
- [EVAL ADXL367 ARDZ扩展板](../boards_shields/P068_EVAL-ADXL367-ARDZ.md#eval-adxl367-ardz)
- [M5Stack Cardputer扩展板](../boards_shields/P082_M5Stack-Cardputer_base_shield.md#m5stack-cardputer)
- [MikroElektronika LTE IoT10 Click扩展板](../boards_shields/P111_MikroElektronika_LTE_IoT_10_Click.md#mikroe-lte-iot10-click-shield)
- [MikroElektronika Stepper 18 Click步进驱动扩展板](../boards_shields/P119_MikroElektronika_Stepper_18_Click.md#mikroe-stepper-18-click-shield)
- [MikroElektronika Stepper 19 Click步进驱动扩展板](../boards_shields/P120_MikroElektronika_Stepper_19_Click.md#mikroe-stepper-19-click-shield)
- [NPM2100评估套件（Evaluation Kit）](../boards_shields/P128_nPM2100_EK.md#npm2100-ek)
- [NXP ADTJA1101扩展板](../boards_shields/P133_NXP_ADTJA1101-RMII_Automotive_Ethernet_Adapter.md#nxp-adtja1101)
- [NXP M2 WiFi BT扩展板](../boards_shields/P137_NXP_M.2_Wi-Fi_and_BT_Shield.md#nxp-m2-wifi-bt)
- [OpenThread RCP Arduino扩展板](../boards_shields/P143_OpenThread_RCP_over_Arduino_header.md#openthread-rcp-arduino-shield)
- [RTK7 EKA6M3B00001BU扩展板](../boards_shields/P158_RTK7EKA6M3B00001BU_Display.md#rtk7eka6m3b00001bu)
- [RTKLCDPAR1S00001BE显示屏（Display）](../boards_shields/P160_RTKLCDPAR1S00001BE_Display.md#rtklcdpar1s00001be)
- [ST B-CAMS-IMX-MB1854摄像头模块](../boards_shields/P180_ST_B-CAMS-IMX-MB1854.md#st-b-cams-imx-mb1854)
- [ST MB1897摄像头模块（Camera Module）](../boards_shields/P186_ST_MB1897_CAM.md#st-mb1897-cam)
- [ST STM32F4DIS CAM扩展板](../boards_shields/P187_ST_STM32F4DIS-CAM.md#st-stm32f4dis-cam)
- [Waveshare Pico LCD 1.14扩展板](../boards_shields/P196_Waveshare_1.14inch_LCD_Display_Module_for_Raspberry_Pi_Pico.md#waveshare-pico-lcd-1-14)
- [Waveshare Pico OLED 1.3扩展板](../boards_shields/P197_Waveshare_1.3inch_OLED_Display_Module_for_Raspberry_Pi_Pico.md#waveshare-pico-oled-1-3)
- [X-Nucleo-GFX01M2](../boards_shields/P205_X-NUCLEO-GFX01M2_Display_expansion_board.md#x-nucleo-gfx01m2-shield)

<a id="new-drivers"></a>

## 新增驱动（New Drivers）


- 模数转换器（ADC）

  > - [`adi,ad4050-adc`](../hardware/P911_ADIAD4050模数转换器绑定.md#dtbinding-adi-ad4050-adc)
  > - [`adi,ad4052-adc`](../hardware/P912_ADIAD4052模数转换器绑定.md#dtbinding-adi-ad4052-adc)
  > - [`adi,ad4130-adc`](../hardware/P914_ADIAD4130模数转换器绑定.md#dtbinding-adi-ad4130-adc)
  > - [`ene,kb106x-adc`](../hardware/P887_ENEKB106x模数转换器绑定.md#dtbinding-ene-kb106x-adc)
  > - [`ite,it51xxx-adc`](../hardware/P890_ITEIT51xxx模数转换器绑定.md#dtbinding-ite-it51xxx-adc)
  > - [`microchip,mcp356xr`](../hardware/P940_MCP356xR模数转换器绑定.md#dtbinding-microchip-mcp356xr)
  > - [`realtek,rts5912-adc`](../hardware/P897_RealtekRTS5912模数转换器绑定.md#dtbinding-realtek-rts5912-adc)
  > - [`renesas,rz-adc`](../hardware/P873_RenesasRZ模数转换器绑定.md#dtbinding-renesas-rz-adc)
  > - [`silabs,siwx91x-adc`](../hardware/P902_SiliconLabsSiWx91x模数转换器绑定.md#dtbinding-silabs-siwx91x-adc)
  > - [`ti,am335x-adc`](../hardware/P904_TIAM335x模数转换器绑定.md#dtbinding-ti-am335x-adc)
  > - [`ti,cc23x0-adc`](../hardware/P906_TICC23x0模数转换器绑定.md#dtbinding-ti-cc23x0-adc)
  > - [`wch,adc`](../hardware/P909_沁恒模数转换器绑定.md#dtbinding-wch-adc)
- 音频（Audio）

  > - [`ambiq,pdm`](../audio_pdm_codec_binding_reference/P001_ambiq_pdm.md#std-dtcompatible-ambiq-pdm)
  > - [`maxim,max98091`](../audio_pdm_codec_binding_reference/P011_maxim_max98091.md#std-dtcompatible-maxim-max98091)
  > - [`ti,pcm1681`](../compatible_binding_reference/P098_ti_pcm1681.md#std-dtcompatible-ti-pcm1681)
  > - [`ti,tlv320aic3110`](../audio_stm32_ti_wolfson_binding_reference/P009_ti_tlv320aic3110.md#std-dtcompatible-ti-tlv320aic3110)
  > - [`wolfson,wm8962`](../audio_stm32_ti_wolfson_binding_reference/P013_wolfson_wm8962.md#std-dtcompatible-wolfson-wm8962)
- 辅助显示器（Auxiliary Display）

  > - [`gpio-7-segment`](../auxdisplay_iio_tach_binding_reference/P001_gpio-7-segment.md#std-dtcompatible-gpio-7-segment)
- 控制器局域网（CAN）

  > - [`adi,max32-can`](../can_adi_atmel_nxp_binding_reference/P001_adi_max32-can.md#std-dtcompatible-adi-max32-can)
  > - [`renesas,rz-canfd`](../can_nxp_renesas_stm32_ti_binding_reference/P010_renesas_rz-canfd.md#std-dtcompatible-renesas-rz-canfd)
  > - [`renesas,rz-canfd-global`](../can_nxp_renesas_stm32_ti_binding_reference/P009_renesas_rz-canfd-global.md#std-dtcompatible-renesas-rz-canfd-global)
- 充电器（Charger）

  > - [`ti,bq25713`](../charger_binding_reference/P017_ti_bq25713.md#std-dtcompatible-ti-bq25713)
  > - [`x-powers,axp2101-charger`](../charger_binding_reference/P018_x-powers_axp2101-charger.md#std-dtcompatible-x-powers-axp2101-charger)
- 时钟控制（Clock Control）

  > - [`bflb,bclk`](../clock_adi_atmel_bflb_binding_reference/P013_bflb_bclk.md#std-dtcompatible-bflb-bclk)
  > - [`bflb,bl60x-clock-controller`](../clock_adi_atmel_bflb_binding_reference/P014_bflb_bl60x-clock-controller.md#std-dtcompatible-bflb-bl60x-clock-controller)
  > - `bflb,bl60x-pll`
  > - `bflb,bl60x-root-clk`
  > - [`bflb,clock-controller`](../clock_adi_atmel_bflb_binding_reference/P021_bflb_clock-controller.md#std-dtcompatible-bflb-clock-controller)
  > - [`ite,it51xxx-ecpm`](../clock_esp_infineon_microchip_binding_reference/P013_ite_it51xxx-ecpm.md#std-dtcompatible-ite-it51xxx-ecpm)
  > - [`microchip,sam-pmc`](../clock_esp_infineon_microchip_binding_reference/P019_microchip_sam-pmc.md#std-dtcompatible-microchip-sam-pmc)
  > - [`microchip,sama7g5-sckc`](../clock_esp_infineon_microchip_binding_reference/P020_microchip_sama7g5-sckc.md#std-dtcompatible-microchip-sama7g5-sckc)
  > - [`nordic,nrf51-hfxo`](../clock_sam_nordic_binding_reference/P021_nordic_nrf51-hfxo.md#std-dtcompatible-nordic-nrf51-hfxo)
  > - [`nordic,nrf52-hfxo`](../clock_sam_nordic_binding_reference/P022_nordic_nrf52-hfxo.md#std-dtcompatible-nordic-nrf52-hfxo)
  > - [`nordic,nrf54l-hfxo`](../clock_sam_nordic_binding_reference/P028_nordic_nrf54l-hfxo.md#std-dtcompatible-nordic-nrf54l-hfxo)
  > - [`nordic,nrfs-audiopll`](../clock_nordic_nuvoton_nxp_binding_reference/P002_nordic_nrfs-audiopll.md#std-dtcompatible-nordic-nrfs-audiopll)
  > - [`renesas,rx-cgc-pclk`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P007_renesas_rx-cgc-pclk.md#std-dtcompatible-renesas-rx-cgc-pclk)
  > - [`renesas,rx-cgc-pclk-block`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P006_renesas_rx-cgc-pclk-block.md#std-dtcompatible-renesas-rx-cgc-pclk-block)
  > - [`renesas,rx-cgc-pll`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P008_renesas_rx-cgc-pll.md#std-dtcompatible-renesas-rx-cgc-pll)
  > - [`renesas,rx-cgc-root-clock`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P010_renesas_rx-cgc-root-clock.md#std-dtcompatible-renesas-rx-cgc-root-clock)
  > - [`renesas,rza2m-cpg`](../clock_renesas_rockchip_sifli_silabs_binding_reference/P018_renesas_rza2m-cpg.md#std-dtcompatible-renesas-rza2m-cpg)
  > - [`st,stm32mp13-cpu-clock-mux`](../timer_reference/P177_STM32MP13处理器时钟多路选择绑定.md#dtbinding-st-stm32mp13-cpu-clock-mux)
  > - [`st,stm32mp13-pll-clock`](../timer_reference/P156_STM32MP13锁相环时钟绑定.md#dtbinding-st-stm32mp13-pll-clock)
  > - [`st,stm32mp2-rcc`](../timer_reference/P182_STM32MP2复位与时钟控制绑定.md#dtbinding-st-stm32mp2-rcc)
  > - [`st,stm32u3-msi-clock`](../timer_reference/P159_STM32U3多速内部时钟绑定.md#dtbinding-st-stm32u3-msi-clock)
  > - [`ti,mspm0-clk`](../clock_silabs_ti_xilinx_binding_reference/P025_ti_mspm0-clk.md#std-dtcompatible-ti-mspm0-clk)
  > - [`ti,mspm0-osc`](../clock_silabs_ti_xilinx_binding_reference/P026_ti_mspm0-osc.md#std-dtcompatible-ti-mspm0-osc)
  > - [`ti,mspm0-pll`](../clock_silabs_ti_xilinx_binding_reference/P027_ti_mspm0-pll.md#std-dtcompatible-ti-mspm0-pll)
  > - [`wch,ch32v20x_30x-pll-clock`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/wch%2Cch32v20x_30x-pll-clock.html#std-dtcompatible-wch-ch32v20x_30x-pll-clock)
- 比较器（Comparator）

  > - [`ite,it51xxx-vcmp`](../hardware/P755_ITE电压比较器绑定.md#dtbinding-ite-it51xxx-vcmp)
  > - [`renesas,ra-acmphs`](../hardware/P749_RenesasRA高速模拟比较器绑定.md#dtbinding-renesas-ra-acmphs)
  > - [`renesas,ra-acmphs-global`](../hardware/P748_RenesasRA高速模拟比较器全局绑定.md#dtbinding-renesas-ra-acmphs-global)
- 计数器（Counter）

  > - [`adi,max32-wut`](../counter_binding_reference/P003_adi_max32-wut.md#std-dtcompatible-adi-max32-wut)
  > - [`espressif,esp32-counter`](../counter_binding_reference/P015_espressif_esp32-counter.md#std-dtcompatible-espressif-esp32-counter)
  > - [`ite,it51xxx-counter`](../microchip_soc_counter_binding_reference/P005_ite_it51xxx-counter.md#std-dtcompatible-ite-it51xxx-counter)
  > - [`ite,it8xxx2-counter`](../microchip_soc_counter_binding_reference/P006_ite_it8xxx2-counter.md#std-dtcompatible-ite-it8xxx2-counter)
  > - [`neorv32,gptmr`](../microchip_soc_counter_binding_reference/P016_neorv32_gptmr.md#std-dtcompatible-neorv32-gptmr)
  > - [`realtek,rts5912-timer`](../renesas_realtek_counter_binding_reference/P013_realtek_rts5912-timer.md#std-dtcompatible-realtek-rts5912-timer)
  > - [`ti,cc23x0-lgpt`](../stm32_ti_xilinx_counter_binding_reference/P008_ti_cc23x0-lgpt.md#std-dtcompatible-ti-cc23x0-lgpt)
  > - [`ti,cc23x0-rtc`](../stm32_ti_xilinx_counter_binding_reference/P009_ti_cc23x0-rtc.md#std-dtcompatible-ti-cc23x0-rtc)
  > - [`ti,mspm0-timer-counter`](../stm32_ti_xilinx_counter_binding_reference/P011_ti_mspm0-timer-counter.md#std-dtcompatible-ti-mspm0-timer-counter)
  > - [`wch,gptm`](../stm32_ti_xilinx_counter_binding_reference/P013_wch_gptm.md#std-dtcompatible-wch-gptm)
  > - [`zephyr,native-sim-counter`](../hardware/P550_主机原生计数器绑定.md#dtbinding-zephyr-native-sim-counter)
- 中央处理器（CPU）

  > - [`arm,cortex-r8`](../cpu_cortex_xtensa_binding_reference/P014_arm_cortex-r8.md#std-dtcompatible-arm-cortex-r8)
  > - [`intel,bartlett-lake`](../cpu_vendor_multiarc_binding_reference/P006_intel_bartlett-lake.md#std-dtcompatible-intel-bartlett-lake)
  > - [`openhwgroup,cva6`](../cpu_vendor_multiarc_binding_reference/P024_openhwgroup_cva6.md#std-dtcompatible-openhwgroup-cva6)
  > - [`renesas,rx`](../cpu_vendor_multiarc_binding_reference/P029_renesas_rx.md#std-dtcompatible-renesas-rx)
  > - [`wch,qingke-v4b`](../cpu_vendor_multiarc_binding_reference/P051_wch_qingke-v4b.md#std-dtcompatible-wch-qingke-v4b)
  > - [`wch,qingke-v4c`](../cpu_vendor_multiarc_binding_reference/P052_wch_qingke-v4c.md#std-dtcompatible-wch-qingke-v4c)
  > - [`wch,qingke-v4f`](../cpu_vendor_multiarc_binding_reference/P053_wch_qingke-v4f.md#std-dtcompatible-wch-qingke-v4f)
  > - [`zephyr,native-sim-cpu`](../hardware/P551_主机原生CPU绑定.md#dtbinding-zephyr-native-sim-cpu)
- 密码学加速器（Cryptographic Accelerator）

  > - [`ite,it51xxx-sha`](../crypto_aes_sha_ccm_binding_reference/P014_ite_it51xxx-sha.md#std-dtcompatible-ite-it51xxx-sha)
  > - [`realtek,rts5912-sha`](../crypto_secure_engine_st_ti_binding_reference/P009_realtek_rts5912-sha.md#std-dtcompatible-realtek-rts5912-sha)
  > - [`ti,cc23x0-aes`](../crypto_secure_engine_st_ti_binding_reference/P020_ti_cc23x0-aes.md#std-dtcompatible-ti-cc23x0-aes)
- 数模转换器（DAC）

  > - [`nxp,dac12`](../hardware/P765_NXPDAC12数模转换器绑定.md#dtbinding-nxp-dac12)
  > - [`ti,dac161s997`](../hardware/P804_DAC161S997数模转换器绑定.md#dtbinding-ti-dac161s997)
- 调试（Debug）

  > - [`silabs,pti`](../debug_binding_reference/P006_Silicon_Labs数据包跟踪绑定.md#std-dtcompatible-silabs-pti)
- 显示（Display）

  > - [`sinowealth,sh1122`](../compatible_binding_reference/P058_sinowealth_sh1122.md#std-dtcompatible-sinowealth-sh1122)
  > - [`sitronix,st75256`](../display_sinowealth_sitronix_solomon_binding_reference/P005_sitronix_st75256.md#std-dtcompatible-sitronix-st75256)
  > - [`sitronix,st7567`](../compatible_binding_reference/P059_sitronix_st7567.md#std-dtcompatible-sitronix-st7567)
  > - [`sitronix,st7701`](../display_sinowealth_sitronix_solomon_binding_reference/P009_sitronix_st7701.md#std-dtcompatible-sitronix-st7701)
  > - [`solomon,ssd1320`](../compatible_binding_reference/P065_solomon_ssd1320.md#std-dtcompatible-solomon-ssd1320)
  > - `solomon,ssd1327fb`
  > - [`solomon,ssd1331`](../display_solomon_oled_epd_binding_reference/P011_solomon_ssd1331.md#std-dtcompatible-solomon-ssd1331)
  > - [`solomon,ssd1351`](../display_solomon_oled_epd_binding_reference/P012_solomon_ssd1351.md#std-dtcompatible-solomon-ssd1351)
  > - [`solomon,ssd1363`](../compatible_binding_reference/P068_solomon_ssd1363.md#std-dtcompatible-solomon-ssd1363)
  > - [`zephyr,displays`](../display_st_ultrachip_zephyr_binding_reference/P011_zephyr_displays.md#std-dtcompatible-zephyr-displays)
- 直接存储器访问（DMA）

  > - `renesas,rz-dma`
  > - [`ti,cc23x0-dma`](../stm32_ti_xilinx_dma_binding_reference/P013_ti_cc23x0-dma.md#std-dtcompatible-ti-cc23x0-dma)
  > - [`wch,wch-dma`](../stm32_ti_xilinx_dma_binding_reference/P015_wch_wch-dma.md#std-dtcompatible-wch-wch-dma)
- 错误检测与纠正（EDAC）

  > - [`xlnx,zynqmp-ddrc-2.40a`](../edac_syscon_binding_reference/P005_xlnx_zynqmp-ddrc-2.40a.md#std-dtcompatible-xlnx-zynqmp-ddrc-2.40a)
- eSPI

  > - [`realtek,rts5912-espi`](../espi_binding_reference/P016_realtek_rts5912-espi.md#std-dtcompatible-realtek-rts5912-espi)
- 以太网（Ethernet）

  > - [`ethernet-phy`](../ethernet_nxp_phy_binding_reference/P019_ethernet-phy.md#std-dtcompatible-ethernet-phy)
  > - [`microchip,vsc8541`](../ethernet_phy_renesas_rockchip_binding_reference/P006_microchip_vsc8541.md#std-dtcompatible-microchip-vsc8541)
  > - [`nxp,netc-ptp-clock`](../ethernet_nxp_phy_binding_reference/P009_nxp_netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock)
  > - [`nxp,tja11xx`](../ethernet_nxp_phy_binding_reference/P013_nxp_tja11xx.md#std-dtcompatible-nxp-tja11xx)
  > - 引入st,stm32-ethernet-controller，便于与st,stm32-mdio互操作。
  > - [`st,stm32n6-ethernet`](../ethernet_synopsys_st_xilinx_binding_reference/P013_st_stm32n6-ethernet.md#std-dtcompatible-st-stm32n6-ethernet)
  > - [`ti,dp83867`](../ethernet_phy_renesas_rockchip_binding_reference/P014_ti_dp83867.md#std-dtcompatible-ti-dp83867)
  > - [`xlnx,axi-ethernet-1.00.a`](../ethernet_synopsys_st_xilinx_binding_reference/P021_xlnx_axi-ethernet-1.00.a.md#std-dtcompatible-xlnx-axi-ethernet-1.00.a)
- 固件（Firmware）

  > - [`nxp,scmi-cpu`](../hardware/P608_NXP%20SCMI处理器协议绑定.md#dtbinding-nxp-scmi-cpu)
  > - [`ti,k2g-sci`](../hardware/P612_TI%20K2G系统控制接口绑定.md#dtbinding-ti-k2g-sci)
- 闪存控制器（Flash Controller）

  > - [`realtek,rts5912-flash-controller`](../flash_nuvoton_nxp_renesas_binding_reference/P024_realtek_rts5912-flash-controller.md#std-dtcompatible-realtek-rts5912-flash-controller)
  > - [`renesas,ra-ospi-b-nor`](../flash_nuvoton_nxp_renesas_binding_reference/P030_renesas_ra-ospi-b-nor.md#std-dtcompatible-renesas-ra-ospi-b-nor)
  > - [`renesas,rx-flash`](../flash_renesas_st_ti_binding_reference/P001_renesas_rx-flash.md#std-dtcompatible-renesas-rx-flash)
  > - [`silabs,series2-flash-controller`](../flash_renesas_st_ti_binding_reference/P007_silabs_series2-flash-controller.md#std-dtcompatible-silabs-series2-flash-controller)
  > - [`st,stm32u3-flash-controller`](../flash_renesas_st_ti_binding_reference/P025_st_stm32u3-flash-controller.md#std-dtcompatible-st-stm32u3-flash-controller)
- 文件系统（File System）

  > - [`zephyr,fstab,fatfs`](../storage_filesystem_binding_reference/P005_zephyr_fstab_fatfs.md#std-dtcompatible-zephyr-fstab-fatfs)
- 电量计（Fuel Gauge）

  > - [`onnn,lc709203f`](../fuel_gauge_binding_reference/P005_onnn_lc709203f.md#std-dtcompatible-onnn-lc709203f)
  > - [`x-powers,axp2101-fuel-gauge`](../fuel_gauge_binding_reference/P011_x-powers_axp2101-fuel-gauge.md#std-dtcompatible-x-powers-axp2101-fuel-gauge)
- 全球导航卫星系统（GNSS）

  > - [`u-blox,f9p`](../gnss_fingerprint_binding_reference/P010_u-blox_f9p.md#std-dtcompatible-u-blox-f9p)
- 通用输入输出（GPIO）

  > - [`adi,max14915-gpio`](../gpio_adi_headers_ambiq_binding_reference/P005_adi_max14915-gpio.md#std-dtcompatible-adi-max14915-gpio)
  > - [`adi,max14917-gpio`](../gpio_adi_headers_ambiq_binding_reference/P007_adi_max14917-gpio.md#std-dtcompatible-adi-max14917-gpio)
  > - [`adi,max22199-gpio`](../gpio_adi_headers_ambiq_binding_reference/P010_adi_max22199-gpio.md#std-dtcompatible-adi-max22199-gpio)
  > - [`arducam,dvp-20pin-connector`](../gpio_adi_headers_ambiq_binding_reference/P021_arducam_dvp-20pin-connector.md#std-dtcompatible-arducam-dvp-20pin-connector)
  > - `bflb,gpio`
  > - [`ene,kb106x-gpio`](../gpio_connectors_bflb_esp_binding_reference/P019_ene_kb106x-gpio.md#std-dtcompatible-ene-kb106x-gpio)
  > - [`espressif,esp32-lpgpio`](../gpio_connectors_bflb_esp_binding_reference/P023_espressif_esp32-lpgpio.md#std-dtcompatible-espressif-esp32-lpgpio)
  > - [`ite,it51xxx-gpio`](../gpio_infineon_intel_ite_microchip_binding_reference/P007_ite_it51xxx-gpio.md#std-dtcompatible-ite-it51xxx-gpio)
  > - [`nordic,npm1304-gpio`](../gpio_microchip_nordic_nuvoton_binding_reference/P012_nordic_npm1304-gpio.md#std-dtcompatible-nordic-npm1304-gpio)
  > - [`nxp,lcd-pmod`](../gpio_nxp_expanders_binding_reference/P004_nxp_lcd-pmod.md#std-dtcompatible-nxp-lcd-pmod)
  > - [`raspberrypi,csi-connector`](../gpio_raspberrypi_renesas_binding_reference/P004_raspberrypi_csi-connector.md#std-dtcompatible-raspberrypi-csi-connector)
  > - [`raspberrypi,pico-gpio-port`](../gpio_raspberrypi_renesas_binding_reference/P005_raspberrypi_pico-gpio-port.md#std-dtcompatible-raspberrypi-pico-gpio-port)
  > - [`renesas,ra-parallel-graphics-header`](../gpio_raspberrypi_renesas_binding_reference/P016_renesas_ra-parallel-graphics-header.md#std-dtcompatible-renesas-ra-parallel-graphics-header)
  > - [`renesas,rx-gpio`](../gpio_raspberrypi_renesas_binding_reference/P019_renesas_rx-gpio.md#std-dtcompatible-renesas-rx-gpio)
  > - [`renesas,rza2m-gpio`](../gpio_raspberrypi_renesas_binding_reference/P027_renesas_rza2m-gpio.md#std-dtcompatible-renesas-rza2m-gpio)
  > - [`renesas,rza2m-gpio-int`](../gpio_raspberrypi_renesas_binding_reference/P026_renesas_rza2m-gpio-int.md#std-dtcompatible-renesas-rza2m-gpio-int)
  > - [`st,stm32mp2-gpio`](../gpio_silabs_st_connectors_binding_reference/P030_st_stm32mp2-gpio.md#std-dtcompatible-st-stm32mp2-gpio)
  > - [`ti,mspm0-gpio`](../gpio_ti_xilinx_sdl_binding_reference/P016_ti_mspm0-gpio.md#std-dtcompatible-ti-mspm0-gpio)
- IEEE 802.15.4 HDLC 无线协处理器接口（RCP Interface）

  > - [`spi,hdlc-rcp-if`](../network_radio_frontend_binding_reference/P004_spi_hdlc-rcp-if.md#std-dtcompatible-spi-hdlc-rcp-if)
- 集成电路间总线（I2C）

  > - [`cdns,i2c`](../i2c_adi_atmel_esp_binding_reference/P015_cdns_i2c.md#std-dtcompatible-cdns-i2c)
  > - [`ite,it51xxx-i2c`](../i2c_infineon_ite_nordic_binding_reference/P007_ite_it51xxx-i2c.md#std-dtcompatible-ite-it51xxx-i2c)
  > - [`litex,litei2c`](../i2c_infineon_ite_nordic_binding_reference/P010_litex_litei2c.md#std-dtcompatible-litex-litei2c)
  > - [`realtek,rts5912-i2c`](../i2c_nxp_pico_renesas_binding_reference/P011_realtek_rts5912-i2c.md#std-dtcompatible-realtek-rts5912-i2c)
  > - [`renesas,ra-i2c-sci-b`](../i2c_nxp_pico_renesas_binding_reference/P012_renesas_ra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b)
  > - [`renesas,rx-i2c`](../i2c_nxp_pico_renesas_binding_reference/P016_renesas_rx-i2c.md#std-dtcompatible-renesas-rx-i2c)
  > - [`renesas,rz-riic`](../i2c_nxp_pico_renesas_binding_reference/P018_renesas_rz-riic.md#std-dtcompatible-renesas-rz-riic)
  > - [`sensry,sy1xx-i2c`](../i2c_stm32_ti_mux_binding_reference/P001_sensry_sy1xx-i2c.md#std-dtcompatible-sensry-sy1xx-i2c)
  > - [`wch,i2c`](../i2c_stm32_ti_mux_binding_reference/P017_wch_i2c.md#std-dtcompatible-wch-i2c)
- 集成电路间音频总线（I2S）

  > - [`ambiq,i2s`](../i2s_binding_reference/P002_ambiq_i2s.md#std-dtcompatible-ambiq-i2s)
  > - [`nordic,nrf-tdm`](../i2s_binding_reference/P011_nordic_nrf-tdm.md#std-dtcompatible-nordic-nrf-tdm)
  > - [`renesas,ra-i2s-ssie`](../i2s_binding_reference/P014_renesas_ra-i2s-ssie.md#std-dtcompatible-renesas-ra-i2s-ssie)
  > - [`silabs,siwx91x-i2s`](../i2s_binding_reference/P015_silabs_siwx91x-i2s.md#std-dtcompatible-silabs-siwx91x-i2s)
  > - [`st,stm32-sai`](../i2s_binding_reference/P017_st_stm32-sai.md#std-dtcompatible-st-stm32-sai)
- 改进型集成电路间总线（I3C）

  > - [`ite,it51xxx-i3cm`](../i3c_smbus_binding_reference/P003_ite_it51xxx-i3cm.md#std-dtcompatible-ite-it51xxx-i3cm)
  > - [`ite,it51xxx-i3cs`](../i3c_smbus_binding_reference/P004_ite_it51xxx-i3cs.md#std-dtcompatible-ite-it51xxx-i3cs)
  > - [`renesas,ra-i3c`](../i3c_smbus_binding_reference/P008_renesas_ra-i3c.md#std-dtcompatible-renesas-ra-i3c)
- 低速率无线个域网（IEEE 802.15.4）

  > - [`espressif,esp32-ieee802154`](../lora_ieee802154_binding_reference/P004_espressif_esp32-ieee802154.md#std-dtcompatible-espressif-esp32-ieee802154)
- 输入（Input）

  > - [`arduino,modulino-buttons`](../input_adc_touch_matrix_binding_reference/P005_arduino_modulino-buttons.md#std-dtcompatible-arduino-modulino-buttons)
  > - [`ite,it51xxx-kbd`](../input_keyboard_optical_ctsu_binding_reference/P003_ite_it51xxx-kbd.md#std-dtcompatible-ite-it51xxx-kbd)
  > - [`realtek,rts5912-kbd`](../input_keyboard_optical_ctsu_binding_reference/P017_realtek_rts5912-kbd.md#std-dtcompatible-realtek-rts5912-kbd)
  > - [`st,stm32-tsc`](../input_touch_lvgl_gesture_binding_reference/P007_st_stm32-tsc.md#std-dtcompatible-st-stm32-tsc)
  > - [`tsc-keys`](../input_touch_lvgl_gesture_binding_reference/P010_tsc-keys.md#std-dtcompatible-tsc-keys)
  > - [`vishay,vs1838b`](../input_touch_lvgl_gesture_binding_reference/P011_vishay_vs1838b.md#std-dtcompatible-vishay-vs1838b)
- 中断控制器（Interrupt Controller）

  > - [`ite,it51xxx-intc`](../wakeup_interrupt_binding_reference/P001_ite_it51xxx-intc.md#std-dtcompatible-ite-it51xxx-intc)
  > - [`ite,it51xxx-wuc`](../wakeup_interrupt_binding_reference/P003_ite_it51xxx-wuc.md#std-dtcompatible-ite-it51xxx-wuc)
  > - [`ite,it51xxx-wuc-map`](../wakeup_interrupt_binding_reference/P002_ite_it51xxx-wuc-map.md#std-dtcompatible-ite-it51xxx-wuc-map)
  > - [`renesas,rx-icu`](../renesas_interrupt_binding_reference/P002_renesas_rx-icu.md#std-dtcompatible-renesas-rx-icu)
  > - [`riscv,clic`](../riscv_interrupt_binding_reference/P006_riscv_clic.md#std-dtcompatible-riscv-clic)
  > - [`wch,exti`](../mcu_external_interrupt_binding_reference/P005_wch_exti.md#std-dtcompatible-wch-exti)
- 发光二极管（LED）

  > - [`arduino,modulino-buttons-leds`](../led_issi_nordic_nxp_binding_reference/P001_arduino_modulino-buttons-leds.md#std-dtcompatible-arduino-modulino-buttons-leds)
  > - [`dac-leds`](../led_issi_nordic_nxp_binding_reference/P003_dac-leds.md#std-dtcompatible-dac-leds)
  > - [`nordic,npm1304-led`](../led_issi_nordic_nxp_binding_reference/P014_nordic_npm1304-led.md#std-dtcompatible-nordic-npm1304-led)
  > - [`x-powers,axp192-led`](../led_sct_ti_xpowers_binding_reference/P018_x-powers_axp192-led.md#std-dtcompatible-x-powers-axp192-led)
  > - [`x-powers,axp2101-led`](../led_sct_ti_xpowers_binding_reference/P019_x-powers_axp2101-led.md#std-dtcompatible-x-powers-axp2101-led)
- 灯带（LED Strip）

  > - `arduino,modulino-smartleds`
- 邮箱（Mailbox）

  > - [`arm,mhuv3`](../intercore_reference/P035_ArmMHUv3邮箱绑定.md#dtbinding-arm-mhuv3)
  > - [`renesas,rz-mhu-mbox`](../intercore_reference/P053_RenesasRZ邮箱绑定.md#dtbinding-renesas-rz-mhu-mbox)
  > - [`ti,secure-proxy`](../intercore_reference/P056_TI安全代理邮箱绑定.md#dtbinding-ti-secure-proxy)
- 管理数据输入输出（MDIO）

  > - [`xlnx,axi-ethernet-1.00.a-mdio`](../ethernet_mdio_microchip_binding_reference/P011_xlnx_axi-ethernet-1.00.a-mdio.md#std-dtcompatible-xlnx-axi-ethernet-1.00.a-mdio)
- 存储器控制器（Memory Controller）

  > - [`adi,max32-hpb`](../memory_controller_hyperbus_smc_binding_reference/P002_adi_max32-hpb.md#std-dtcompatible-adi-max32-hpb)
  > - [`realtek,rts5912-bbram`](../memory_controller_sdram_psram_binding_reference/P004_realtek_rts5912-bbram.md#std-dtcompatible-realtek-rts5912-bbram)
  > - [`silabs,siwx91x-qspi-memory`](../memory_controller_sdram_psram_binding_reference/P008_silabs_siwx91x-qspi-memory.md#std-dtcompatible-silabs-siwx91x-qspi-memory)
  > - [`st,stm32-xspi-psram`](../memory_controller_sdram_psram_binding_reference/P015_st_stm32-xspi-psram.md#std-dtcompatible-st-stm32-xspi-psram)
- 多功能设备（MFD）

  > - [`adi,maxq10xx`](../hardware/P719_MAXQ10xx多功能设备绑定.md#dtbinding-adi-maxq10xx)
  > - [`ambiq,iom`](../hardware/P699_Ambiq输入输出主控制器绑定.md#dtbinding-ambiq-iom)
  > - [`microchip,sam-flexcom`](../hardware/P701_SAM灵活通信接口绑定.md#dtbinding-microchip-sam-flexcom)
  > - [`nordic,npm1304`](../hardware/P686_nPM1304多功能设备绑定.md#dtbinding-nordic-npm1304)
  > - [`x-powers,axp2101`](../hardware/P692_AXP2101多功能设备绑定.md#dtbinding-x-powers-axp2101)
- MIPI显示总线接口（MIPI DBI）

  > - [`nxp,mipi-dbi-dcnano-lcdif`](../mipi_dbi_dsi_binding_reference/P004_nxp_mipi-dbi-dcnano-lcdif.md#std-dtcompatible-nxp-mipi-dbi-dcnano-lcdif)
- 其他绑定（Miscellaneous）

  > - [`ene,kb106x-gcfg`](../misc_adi_nordic_binding_reference/P004_ene_kb106x-gcfg.md#std-dtcompatible-ene-kb106x-gcfg)
  > - [`nordic,ironside-call`](../misc_adi_nordic_binding_reference/P013_nordic_ironside-call.md#std-dtcompatible-nordic-ironside-call)
  > - [`nordic,nrf-mpc`](../misc_adi_nordic_binding_reference/P019_nordic_nrf-mpc.md#std-dtcompatible-nordic-nrf-mpc)
  > - [`nxp,rtxxx-dsp-ctrl`](../misc_nxp_renesas_zephyr_binding_reference/P006_nxp_rtxxx-dsp-ctrl.md#std-dtcompatible-nxp-rtxxx-dsp-ctrl)
  > - [`renesas,ra-elc`](../misc_nxp_renesas_zephyr_binding_reference/P016_renesas_ra-elc.md#std-dtcompatible-renesas-ra-elc)
  > - [`renesas,ra-ulpt`](../misc_nxp_renesas_zephyr_binding_reference/P021_renesas_ra-ulpt.md#std-dtcompatible-renesas-ra-ulpt)
  > - [`renesas,rx-external-interrupt`](../misc_nxp_renesas_zephyr_binding_reference/P023_renesas_rx-external-interrupt.md#std-dtcompatible-renesas-rx-external-interrupt)
  > - [`renesas,rx-mtu`](../misc_nxp_renesas_zephyr_binding_reference/P024_renesas_rx-mtu.md#std-dtcompatible-renesas-rx-mtu)
  > - [`renesas,rx-sci`](../misc_nxp_renesas_zephyr_binding_reference/P026_renesas_rx-sci.md#std-dtcompatible-renesas-rx-sci)
  > - [`renesas,rz-sci`](../misc_nxp_renesas_zephyr_binding_reference/P029_renesas_rz-sci.md#std-dtcompatible-renesas-rz-sci)
  > - [`renesas,rz-sci-b`](../misc_nxp_renesas_zephyr_binding_reference/P028_renesas_rz-sci-b.md#std-dtcompatible-renesas-rz-sci-b)
  > - [`st,stm32n6-ramcfg`](../misc_nxp_renesas_zephyr_binding_reference/P038_st_stm32n6-ramcfg.md#std-dtcompatible-st-stm32n6-ramcfg)
- 调制解调器（Modem）

  > - [`quectel,eg800q`](../modem_fibocom_nordic_quectel_binding_reference/P015_quectel_eg800q.md#std-dtcompatible-quectel-eg800q)
  > - [`simcom,a76xx`](../modem_fibocom_nordic_quectel_binding_reference/P017_simcom_a76xx.md#std-dtcompatible-simcom-a76xx)
- 多位串行外设接口（Multi-Bit SPI）

  > - [`nordic,nrf-exmif`](../mspi_binding_reference/P006_nordic_nrf-exmif.md#std-dtcompatible-nordic-nrf-exmif)
  > - [`snps,designware-ssi`](../mspi_binding_reference/P009_snps_designware-ssi.md#std-dtcompatible-snps-designware-ssi)
- 存储技术设备（MTD）

  > - [`fixed-subpartitions`](../mtd_atmel_bouffalo_binding_reference/P013_fixed-subpartitions.md#std-dtcompatible-fixed-subpartitions)
  > - `jedec,mspi-nor`
  > - `mspi-aps-z8`
  > - `mspi-is25xX0xx`
  > - `renesas,ra-nv-code-flash`
  > - `renesas,ra-nv-data-flash`
  > - [`renesas,rx-nv-flash`](../mtd_nxp_st_ti_partition_binding_reference/P011_renesas_rx-nv-flash.md#std-dtcompatible-renesas-rx-nv-flash)
  > - [`ti,tmp11x-eeprom`](../mtd_nxp_st_ti_partition_binding_reference/P020_ti_tmp11x-eeprom.md#std-dtcompatible-ti-tmp11x-eeprom)
- 网络（Networking）

  > - [`nordic,nrf-nfct-v2`](../network_radio_frontend_binding_reference/P007_nordic_nrf-nfct-v2.md#std-dtcompatible-nordic-nrf-nfct-v2)
  > - [`silabs,siwx91x-nwp`](../network_radio_frontend_binding_reference/P015_silabs_siwx91x-nwp.md#std-dtcompatible-silabs-siwx91x-nwp)
- 八线SPI（Octal SPI）

  > - [`renesas,ra-ospi-b`](../qspi_ospi_xspi_binding_reference/P001_renesas_ra-ospi-b.md#std-dtcompatible-renesas-ra-ospi-b)
- 引脚控制（Pin Control）

  > - [`ambiq,apollo5-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P007_ambiq_apollo5-pinctrl.md#std-dtcompatible-ambiq-apollo5-pinctrl)
  > - [`arm,mps2-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P008_arm_mps2-pinctrl.md#std-dtcompatible-arm-mps2-pinctrl)
  > - [`arm,mps3-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P009_arm_mps3-pinctrl.md#std-dtcompatible-arm-mps3-pinctrl)
  > - [`arm,mps4-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P010_arm_mps4-pinctrl.md#std-dtcompatible-arm-mps4-pinctrl)
  > - [`arm,v2m_beetle-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P011_arm_v2m_beetle-pinctrl.md#std-dtcompatible-arm-v2m_beetle-pinctrl)
  > - [`bflb,pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P016_bflb_pinctrl.md#std-dtcompatible-bflb-pinctrl)
  > - [`ene,kb106x-pinctrl`](../pinctrl_adi_ambiq_arm_binding_reference/P020_ene_kb106x-pinctrl.md#std-dtcompatible-ene-kb106x-pinctrl)
  > - [`microchip,sama7g5-pinctrl`](../pinctrl_infineon_nordic_nxp_binding_reference/P007_microchip_sama7g5-pinctrl.md#std-dtcompatible-microchip-sama7g5-pinctrl)
  > - [`nuvoton,npcx-pinctrl-npckn`](../pinctrl_infineon_nordic_nxp_binding_reference/P014_nuvoton_npcx-pinctrl-npckn.md#std-dtcompatible-nuvoton-npcx-pinctrl-npckn)
  > - [`renesas,rx-pinctrl`](../pinctrl_renesas_silabs_binding_reference/P011_renesas_rx-pinctrl.md#std-dtcompatible-renesas-rx-pinctrl)
  > - [`renesas,rx-pinmux`](../pinctrl_renesas_silabs_binding_reference/P012_renesas_rx-pinmux.md#std-dtcompatible-renesas-rx-pinmux)
  > - [`renesas,rza-pinctrl`](../pinctrl_renesas_silabs_binding_reference/P013_renesas_rza-pinctrl.md#std-dtcompatible-renesas-rza-pinctrl)
  > - [`renesas,rza2m-pinctrl`](../pinctrl_renesas_silabs_binding_reference/P014_renesas_rza2m-pinctrl.md#std-dtcompatible-renesas-rza2m-pinctrl)
  > - [`renesas,rzn-pinctrl`](../pinctrl_renesas_silabs_binding_reference/P016_renesas_rzn-pinctrl.md#std-dtcompatible-renesas-rzn-pinctrl)
  > - [`renesas,rzt-pinctrl`](../pinctrl_renesas_silabs_binding_reference/P017_renesas_rzt-pinctrl.md#std-dtcompatible-renesas-rzt-pinctrl)
  > - [`renesas,rzv-pinctrl`](../pinctrl_renesas_silabs_binding_reference/P019_renesas_rzv-pinctrl.md#std-dtcompatible-renesas-rzv-pinctrl)
  > - [`st,stm32n6-pinctrl`](../pinctrl_stm32_ti_xilinx_binding_reference/P007_st_stm32n6-pinctrl.md#std-dtcompatible-st-stm32n6-pinctrl)
  > - [`ti,mspm0-pinctrl`](../pinctrl_stm32_ti_xilinx_binding_reference/P014_ti_mspm0-pinctrl.md#std-dtcompatible-ti-mspm0-pinctrl)
  > - [`wch,00x-afio`](../pinctrl_stm32_ti_xilinx_binding_reference/P016_wch_00x-afio.md#std-dtcompatible-wch-00x-afio)
  > - [`wch,20x_30x-afio`](../pinctrl_stm32_ti_xilinx_binding_reference/P017_wch_20x_30x-afio.md#std-dtcompatible-wch-20x_30x-afio)
- 电源管理（Power Management）

  > - [`infineon,cat1b-power`](../power_control_binding_reference/P003_infineon_cat1b-power.md#std-dtcompatible-infineon-cat1b-power)
  > - [`realtek,rts5912-ulpm`](../stm32_soc_power_binding_reference/P003_realtek_rts5912-ulpm.md#std-dtcompatible-realtek-rts5912-ulpm)
- 电源域（Power Domain）

  > - [`ti,sci-pm-domain`](../power_domain_binding_reference/P011_ti_sci-pm-domain.md#std-dtcompatible-ti-sci-pm-domain)
- 外设传感器接口（PSI5）

  > - [`nxp,s32-psi5`](../lin_dali_mctp_sensor_bus_binding_reference/P015_nxp_s32-psi5.md#std-dtcompatible-nxp-s32-psi5)
- 脉宽调制（PWM）

  > - [`arduino-header-pwm`](../pwm_adi_esp_infineon_binding_reference/P006_arduino-header-pwm.md#std-dtcompatible-arduino-header-pwm)
  > - [`ene,kb106x-pwm`](../pwm_adi_esp_infineon_binding_reference/P013_ene_kb106x-pwm.md#std-dtcompatible-ene-kb106x-pwm)
  > - [`ite,it51xxx-pwm`](../pwm_intel_microchip_nxp_binding_reference/P003_ite_it51xxx-pwm.md#std-dtcompatible-ite-it51xxx-pwm)
  > - [`neorv32,pwm`](../pwm_intel_microchip_nxp_binding_reference/P014_neorv32_pwm.md#std-dtcompatible-neorv32-pwm)
  > - [`realtek,rts5912-pwm`](../pwm_nxp_renesas_binding_reference/P017_realtek_rts5912-pwm.md#std-dtcompatible-realtek-rts5912-pwm)
  > - [`renesas,rx-mtu-pwm`](../pwm_nxp_renesas_binding_reference/P020_renesas_rx-mtu-pwm.md#std-dtcompatible-renesas-rx-mtu-pwm)
  > - [`silabs,letimer-pwm`](../pwm_stm32_ti_generic_binding_reference/P008_silabs_letimer-pwm.md#std-dtcompatible-silabs-letimer-pwm)
  > - [`silabs,siwx91x-pwm`](../pwm_stm32_ti_generic_binding_reference/P009_silabs_siwx91x-pwm.md#std-dtcompatible-silabs-siwx91x-pwm)
  > - [`silabs,timer-pwm`](../pwm_stm32_ti_generic_binding_reference/P010_silabs_timer-pwm.md#std-dtcompatible-silabs-timer-pwm)
  > - [`ti,mspm0-timer-pwm`](../pwm_stm32_ti_generic_binding_reference/P017_ti_mspm0-timer-pwm.md#std-dtcompatible-ti-mspm0-timer-pwm)
  > - [`wch,gptm-pwm`](../pwm_stm32_ti_generic_binding_reference/P019_wch_gptm-pwm.md#std-dtcompatible-wch-gptm-pwm)
- 稳压器（Regulator）

  > - [`nordic,npm1304-regulator`](../hardware/P663_nPM1304稳压器绑定.md#dtbinding-nordic-npm1304-regulator)
  > - [`x-powers,axp2101-regulator`](../hardware/P680_AXP2101稳压器绑定.md#dtbinding-x-powers-axp2101-regulator)
- 复位控制器（Reset Controller）

  > - [`microchip,mpfs-reset`](../reset_controller_binding_reference/P005_microchip_mpfs-reset.md#std-dtcompatible-microchip-mpfs-reset)
  > - [`reset-mmio`](../reset_controller_binding_reference/P014_reset-mmio.md#std-dtcompatible-reset-mmio)
- 随机数生成器（RNG）

  > - [`adi,maxq10xx-trng`](../rng_binding_reference/P002_adi_maxq10xx-trng.md#std-dtcompatible-adi-maxq10xx-trng)
  > - [`brcm,iproc-rng200`](../rng_binding_reference/P006_brcm_iproc-rng200.md#std-dtcompatible-brcm-iproc-rng200)
  > - [`virtio,device4`](../hardware/P586_VirtIO熵源设备绑定.md#dtbinding-virtio-device4)
  > - [`zephyr,native-sim-rng`](../hardware/P552_主机原生随机数绑定.md#dtbinding-zephyr-native-sim-rng)
- 实时时钟（RTC）

  > - [`nxp,pcf2123`](../microchip_microcrystal_nxp_rtc_binding_reference/P014_nxp_pcf2123.md#std-dtcompatible-nxp-pcf2123)
  > - [`realtek,rts5912-rtc`](../soc_rtc_binding_reference/P005_realtek_rts5912-rtc.md#std-dtcompatible-realtek-rts5912-rtc)
  > - [`silabs,siwx91x-rtc`](../soc_rtc_binding_reference/P012_silabs_siwx91x-rtc.md#std-dtcompatible-silabs-siwx91x-rtc)
- SD 主机控制器（SDHC）

  > - [`ambiq,sdio`](../sdhc_binding_reference/P002_ambiq_sdio.md#std-dtcompatible-ambiq-sdio)
  > - [`xlnx,versal-8.9a`](../sdhc_binding_reference/P021_xlnx_versal-8.9a.md#std-dtcompatible-xlnx-versal-8.9a)
- 传感器（Sensors）

  > - [`adi,ad2s1210`](../sensor_adi_accel_bioz_binding_reference/P001_adi_ad2s1210.md#std-dtcompatible-adi-ad2s1210)
  > - [`bosch,bmm350`](../compatible_binding_reference/P019_bosch_bmm350.md#std-dtcompatible-bosch-bmm350)
  > - [`brcm,afbr-s50`](../sensor_bosch_broadcom_espressif_binding_reference/P026_brcm_afbr-s50.md#std-dtcompatible-brcm-afbr-s50)
  > - [`everlight,als-pt19`](../sensor_espressif_honeywell_invensense_binding_reference/P002_everlight_als-pt19.md#std-dtcompatible-everlight-als-pt19)
  > - [`invensense,icm40627`](../sensor_espressif_honeywell_invensense_binding_reference/P019_invensense_icm40627-i2c.md#std-dtcompatible-invensense-icm40627)
  > - [`invensense,icm45686`](../compatible_binding_reference/P042_invensense_icm45686.md#std-dtcompatible-invensense-icm45686)
  > - [`invensense,icp201xx`](../compatible_binding_reference/P047_invensense_icp201xx.md#std-dtcompatible-invensense-icp201xx)
  > - [`liteon,ltr329`](../sensor_liteon_maxim_temperature_binding_reference/P005_liteon_ltr329.md#std-dtcompatible-liteon-ltr329)
  > - [`meas,ms5837-02ba`](../sensor_microchip_nordic_nxp_binding_reference/P003_meas_ms5837-02ba.md#std-dtcompatible-meas-ms5837-02ba)
  > - [`meas,ms5837-30ba`](../sensor_microchip_nordic_nxp_binding_reference/P004_meas_ms5837-30ba.md#std-dtcompatible-meas-ms5837-30ba)
  > - [`nordic,npm1304-charger`](../sensor_microchip_nordic_nxp_binding_reference/P019_nordic_npm1304-charger.md#std-dtcompatible-nordic-npm1304-charger)
  > - [`nxp,lpadc-temp40`](../sensor_nxp_qdec_optical_binding_reference/P005_nxp_lpadc-temp40.md#std-dtcompatible-nxp-lpadc-temp40)
  > - [`nxp,tpm-qdec`](../sensor_nxp_qdec_optical_binding_reference/P016_nxp_tpm-qdec.md#std-dtcompatible-nxp-tpm-qdec)
  > - [`peacefair,pzem004t`](../sensor_nxp_qdec_optical_binding_reference/P022_peacefair_pzem004t.md#std-dtcompatible-peacefair-pzem004t)
  > - [`pixart,paa3905`](../sensor_nxp_qdec_optical_binding_reference/P024_pixart_paa3905.md#std-dtcompatible-pixart-paa3905)
  > - [`pixart,paj7620`](../sensor_nxp_qdec_optical_binding_reference/P025_pixart_paj7620.md#std-dtcompatible-pixart-paj7620)
  > - [`pixart,pat9136`](../sensor_nxp_qdec_optical_binding_reference/P026_pixart_pat9136.md#std-dtcompatible-pixart-pat9136)
  > - [`pni,rm3100`](../compatible_binding_reference/P054_pni_rm3100.md#std-dtcompatible-pni-rm3100)
  > - [`rohm,bh1730`](../sensor_realtek_rohm_sensirion_binding_reference/P010_rohm_bh1730.md#std-dtcompatible-rohm-bh1730)
  > - [`rohm,bh1790`](../sensor_realtek_rohm_sensirion_binding_reference/P012_rohm_bh1790.md#std-dtcompatible-rohm-bh1790)
  > - [`st,lsm6dsv32x`](../compatible_binding_reference/P096_st_lsm6dsv32x.md#std-dtcompatible-st-lsm6dsv32x)
  > - [`st,lsm9ds1_mag`](../sensor_st_lsm_stm32_binding_reference/P026_st_lsm9ds1_mag.md#std-dtcompatible-st-lsm9ds1_mag)
  > - [`ti,tmp11x`](../sensor_ti_vishay_wurth_sensing_binding_reference/P009_ti_tmp11x.md#std-dtcompatible-ti-tmp11x)
  > - [`vishay,veml6031`](../sensor_ti_vishay_wurth_sensing_binding_reference/P014_vishay_veml6031.md#std-dtcompatible-vishay-veml6031)
  > - [`we,wsen-itds-2533020201601`](../compatible_binding_reference/P100_we_wsen-itds-2533020201601.md#std-dtcompatible-we-wsen-itds-2533020201601)
- 单边沿半字节传输（SENT）

  > - [`nxp,s32-sent`](../lin_dali_mctp_sensor_bus_binding_reference/P016_nxp_s32-sent.md#std-dtcompatible-nxp-s32-sent)
- 串行控制器（Serial Controller）

  > - [`aesc,uart`](../uart_adi_arm_atmel_binding_reference/P002_aesc_uart.md#std-dtcompatible-aesc-uart)
  > - [`ambiq,pl011-uart`](../uart_adi_arm_atmel_binding_reference/P005_ambiq_pl011-uart.md#std-dtcompatible-ambiq-pl011-uart)
  > - [`bflb,uart`](../uart_adi_arm_atmel_binding_reference/P013_bflb_uart.md#std-dtcompatible-bflb-uart)
  > - [`ene,kb106x-uart`](../uart_adi_arm_atmel_binding_reference/P019_ene_kb106x-uart.md#std-dtcompatible-ene-kb106x-uart)
  > - [`espressif,esp32-lpuart`](../uart_espressif_infineon_microchip_binding_reference/P001_espressif_esp32-lpuart.md#std-dtcompatible-espressif-esp32-lpuart)
  > - [`ite,it51xxx-uart`](../uart_espressif_infineon_microchip_binding_reference/P012_ite_it51xxx-uart.md#std-dtcompatible-ite-it51xxx-uart)
  > - [`nuvoton,npcx-uart-npckn`](../uart_microchip_nordic_nxp_binding_reference/P006_nuvoton_npcx-uart-npckn.md#std-dtcompatible-nuvoton-npcx-uart-npckn)
  > - [`renesas,rx-uart-sci`](../uart_raspberrypi_realtek_renesas_binding_reference/P013_renesas_rx-uart-sci.md#std-dtcompatible-renesas-rx-uart-sci)
  > - [`renesas,rx-uart-sci-qemu`](../uart_raspberrypi_realtek_renesas_binding_reference/P012_renesas_rx-uart-sci-qemu.md#std-dtcompatible-renesas-rx-uart-sci-qemu)
  > - [`renesas,rz-sci-b-uart`](../uart_raspberrypi_realtek_renesas_binding_reference/P014_renesas_rz-sci-b-uart.md#std-dtcompatible-renesas-rz-sci-b-uart)
  > - [`renesas,rz-sci-uart`](../uart_raspberrypi_realtek_renesas_binding_reference/P015_renesas_rz-sci-uart.md#std-dtcompatible-renesas-rz-sci-uart)
  > - [`renesas,rza2m-scif-uart`](../uart_raspberrypi_realtek_renesas_binding_reference/P017_renesas_rza2m-scif-uart.md#std-dtcompatible-renesas-rza2m-scif-uart)
  > - [`ti,mspm0-uart`](../uart_ti_wch_virtual_binding_reference/P002_ti_mspm0-uart.md#std-dtcompatible-ti-mspm0-uart)
  > - [`zephyr,native-pty-uart`](../uart_ti_wch_virtual_binding_reference/P013_zephyr_native-pty-uart.md#std-dtcompatible-zephyr-native-pty-uart)
  > - [`zephyr,uart-bridge`](../uart_ti_wch_virtual_binding_reference/P017_zephyr_uart-bridge.md#std-dtcompatible-zephyr-uart-bridge)
- 串行外设接口（SPI）

  > - [`cdns,spi`](../spi_adi_atmel_esp_binding_reference/P011_cdns_spi.md#std-dtcompatible-cdns-spi)
  > - [`ite,it51xxx-spi`](../spi_microchip_nordic_nxp_binding_reference/P001_ite_it51xxx-spi.md#std-dtcompatible-ite-it51xxx-spi)
  > - `microchip,mec5-qspi`
  > - [`renesas,rx-rspi`](../spi_flexspi_nxp_renesas_binding_reference/P019_renesas_rx-rspi.md#std-dtcompatible-renesas-rx-rspi)
  > - [`renesas,rz-rspi`](../spi_flexspi_nxp_renesas_binding_reference/P020_renesas_rz-rspi.md#std-dtcompatible-renesas-rz-rspi)
  > - [`silabs,gspi`](../spi_stm32_ti_xilinx_binding_reference/P006_silabs_gspi.md#std-dtcompatible-silabs-gspi)
  > - [`ti,cc23x0-spi`](../spi_stm32_ti_xilinx_binding_reference/P016_ti_cc23x0-spi.md#std-dtcompatible-ti-cc23x0-spi)
  > - [`wch,spi`](../spi_stm32_ti_xilinx_binding_reference/P019_wch_spi.md#std-dtcompatible-wch-spi)
- 步进电机（Stepper）

  > - [`adi,tmc51xx`](../compatible_binding_reference/P008_adi_tmc51xx.md#std-dtcompatible-adi-tmc51xx)
  > - [`allegro,a4979`](../stepper_binding_reference/P012_allegro_a4979.md#std-dtcompatible-allegro-a4979)
- 系统控制器（System Controller）

  > - [`bflb,efuse`](../otp_binding_reference/P002_bflb_efuse.md#std-dtcompatible-bflb-efuse)
- 转速计（Tachometer）

  > - [`ite,it51xxx-tach`](../auxdisplay_iio_tach_binding_reference/P015_ite_it51xxx-tach.md#std-dtcompatible-ite-it51xxx-tach)
  > - [`realtek,rts5912-tach`](../auxdisplay_iio_tach_binding_reference/P019_realtek_rts5912-tach.md#std-dtcompatible-realtek-rts5912-tach)
- Type-C端口控制器（TCPC）

  > - [`onnn,fusb307-tcpc`](../usbc_tcpc_binding_reference/P002_onnn_fusb307-tcpc.md#std-dtcompatible-onnn-fusb307-tcpc)
- 定时器（Timer）

  > - `infineon,cat1-lp-timer`
  > - [`ite,it51xxx-timer`](../mcu_timer_binding_reference/P010_ite_it51xxx-timer.md#std-dtcompatible-ite-it51xxx-timer)
  > - [`microchip,sam-pit64b`](../microchip_nordic_nxp_realtek_timer_binding_reference/P002_microchip_sam-pit64b.md#std-dtcompatible-microchip-sam-pit64b)
  > - [`renesas,ra-ulpt-timer`](../renesas_timer_binding_reference/P001_renesas_ra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer)
  > - [`renesas,rx-timer-cmt`](../renesas_timer_binding_reference/P004_renesas_rx-timer-cmt.md#std-dtcompatible-renesas-rx-timer-cmt)
  > - [`renesas,rx-timer-cmt-start-control`](../renesas_timer_binding_reference/P003_renesas_rx-timer-cmt-start-control.md#std-dtcompatible-renesas-rx-timer-cmt-start-control)
  > - [`renesas,rz-gtm-os-timer`](../renesas_timer_binding_reference/P007_renesas_rz-gtm-os-timer.md#std-dtcompatible-renesas-rz-gtm-os-timer)
  > - [`renesas,rza2m-ostm`](../renesas_timer_binding_reference/P012_renesas_rza2m-ostm.md#std-dtcompatible-renesas-rza2m-ostm)
  > - [`silabs,series2-letimer`](../stm32_ti_silabs_timer_binding_reference/P005_silabs_series2-letimer.md#std-dtcompatible-silabs-series2-letimer)
  > - [`silabs,series2-timer`](../stm32_ti_silabs_timer_binding_reference/P006_silabs_series2-timer.md#std-dtcompatible-silabs-series2-timer)
  > - [`ti,mspm0-timer`](../stm32_ti_silabs_timer_binding_reference/P015_ti_mspm0-timer.md#std-dtcompatible-ti-mspm0-timer)
- 通用串行总线（USB）

  > - [`adi,max32-usbhs`](../usb_controller_binding_reference/P001_adi_max32-usbhs.md#std-dtcompatible-adi-max32-usbhs)
  > - [`nxp,uhc-ehci`](../usb_soc_binding_reference/P009_nxp_uhc-ehci.md#std-dtcompatible-nxp-uhc-ehci)
  > - [`nxp,uhc-ip3516hs`](../usb_soc_binding_reference/P010_nxp_uhc-ip3516hs.md#std-dtcompatible-nxp-uhc-ip3516hs)
  > - [`nxp,uhc-khci`](../usb_soc_binding_reference/P011_nxp_uhc-khci.md#std-dtcompatible-nxp-uhc-khci)
  > - [`nxp,uhc-ohci`](../usb_soc_binding_reference/P012_nxp_uhc-ohci.md#std-dtcompatible-nxp-uhc-ohci)
  > - [`st,stm32n6-otghs`](../usb_stm32_audio_binding_reference/P008_st_stm32n6-otghs.md#std-dtcompatible-st-stm32n6-otghs)
  > - [`zephyr,uvc-device`](../usb/P126_USB视频设备绑定.md#std-dtcompatible-zephyr-uvc-device)
- 视频（Video）

  > - [`ovti,ov9655`](../video_camera_endpoint_binding_reference/P019_ovti_ov9655.md#std-dtcompatible-ovti-ov9655)
  > - [`sony,imx335`](../video_st_sony_emulation_binding_reference/P002_sony_imx335.md#std-dtcompatible-sony-imx335)
  > - [`st,mipid02`](../video_st_sony_emulation_binding_reference/P003_st_mipid02.md#std-dtcompatible-st-mipid02)
  > - [`st,stm32-dcmipp`](../video_st_sony_emulation_binding_reference/P005_st_stm32-dcmipp.md#std-dtcompatible-st-stm32-dcmipp)
  > - [`zephyr,video-sw-generator`](../video_st_sony_emulation_binding_reference/P011_zephyr_video-sw-generator.md#std-dtcompatible-zephyr-video-sw-generator)
- 虚拟输入输出（Virtio）

  > - [`virtio,mmio`](../hardware/P584_VirtIO_MMIO传输绑定.md#dtbinding-virtio-mmio)
  > - [`virtio,pci`](../hardware/P583_VirtIO_PCI传输绑定.md#dtbinding-virtio-pci)
- 看门狗（Watchdog）

  > - [`ene,kb106x-watchdog`](../watchdog_binding_reference/P011_ene_kb106x-watchdog.md#std-dtcompatible-ene-kb106x-watchdog)
  > - [`ite,it51xxx-watchdog`](../soc_pmic_watchdog_binding_reference/P005_ite_it51xxx-watchdog.md#std-dtcompatible-ite-it51xxx-watchdog)
  > - [`nordic,npm1304-wdt`](../soc_pmic_watchdog_binding_reference/P014_nordic_npm1304-wdt.md#std-dtcompatible-nordic-npm1304-wdt)
  > - [`nxp,ewm`](../nxp_nordic_nuvoton_watchdog_binding_reference/P007_nxp_ewm.md#std-dtcompatible-nxp-ewm)
  > - [`realtek,rts5912-watchdog`](../realtek_renesas_silabs_watchdog_binding_reference/P004_realtek_rts5912-watchdog.md#std-dtcompatible-realtek-rts5912-watchdog)
  > - [`renesas,ra-wdt`](../realtek_renesas_silabs_watchdog_binding_reference/P005_renesas_ra-wdt.md#std-dtcompatible-renesas-ra-wdt)
  > - [`silabs,siwx91x-wdt`](../realtek_renesas_silabs_watchdog_binding_reference/P012_silabs_siwx91x-wdt.md#std-dtcompatible-silabs-siwx91x-wdt)
  > - [`ti,cc23x0-wdt`](../stm32_ti_xilinx_watchdog_binding_reference/P004_ti_cc23x0-wdt.md#std-dtcompatible-ti-cc23x0-wdt)
  > - [`wch,iwdg`](../stm32_ti_xilinx_watchdog_binding_reference/P009_wch_iwdg.md#std-dtcompatible-wch-iwdg)
- 无线局域网（Wi-Fi）

  > - [`espressif,esp-hosted`](../wifi_esp_hosted_airoc_binding_reference/P008_espressif_esp-hosted.md#std-dtcompatible-espressif-esp-hosted)

<a id="new-samples"></a>

## 新增示例（New Samples）


- [音频输出非对称多处理（AMP）示例。](../board_samples/P075_DSP非对称多处理音频回环.md#amp_audio_loopback)
- [音频输出非对称多处理（AMP）示例。](../board_samples/P076_DSP非对称多处理音频输出.md#amp_audio_output)
- [Blinky闪灯非对称多处理（AMP）示例。](../board_samples/P077_DSP非对称多处理闪灯.md#amp_blinky)
- [邮箱mbox API非对称多处理（AMP）示例。](../intercore_reference/P031_RTxxx非对称多处理邮箱示例.md#amp_mbox)
- [辅助数字显示（Auxiliary Digits Display）](../hardware/P177_辅助数码显示示例.md#auxdisplay_digits)
- [BMG160三轴陀螺仪（3-axis Gyroscope）](../sensors/P038_BMG160三轴陀螺仪示例.md#bmg160)
- [超低功耗协处理器调试（Debug ULP）](../board_samples/P102_低功耗核调试.md#debug-ulp)
- [通用距离测量（Generic Distance Measurement）](../sensors/P018_距离传感器轮询示例.md#distance_polling)
- [超低功耗协处理器回显（Echo ULP）](../board_samples/P103_低功耗核串口回显.md#echo-ulp)
- [FatFs文件系统fstab示例](../storage/P082_FatFs挂载表示例.md#fatfs-fstab)
- [电量计（Fuel Gauge）](../driver_samples/P028_电量计示例.md#fuel_gauge)
- [心率传感器（Heart Rate Sensor）](../sensors/P080_心率传感器示例.md#heart_rate)
- [超低功耗协处理器中断（Interrupt ULP）](../board_samples/P105_主核中断低功耗核.md#interrupt-ulp)
- [通用光照传感器轮询（Generic Light Sensor Polling）](../sensors/P019_光照传感器轮询示例.md#light_sensor_polling)
- [LVGL多显示器（Multi-display）](../basic_samples/P070_LVGL多显示器示例.md#lvgl-multi-display)
- [最小堆数据结构（Min-Heap Data Structure）](../basic_samples/P032_最小堆示例.md#min-heap)
- [Ambiq MSPI时序扫描（Timing Scan）](../driver_samples/P025_Ambiq_MSPI时序扫描示例.md#mspi-timing-scan)
- [网络数据包过滤器（Network Packet Filter）](../networking/P202_网络数据包过滤示例.md#net-pkt-filter)
- [Nordic IronSide SE固件更新（Firmware Update）](../board_samples/P027_Nordic_IronSide_SE固件更新.md#nrf_ironside_update)
- [PAJ7620手势传感器（Gesture Sensor）](../sensors/P064_PAJ7620手势传感器示例.md#paj7620_gesture)
- [气压与温度传感器中断示例（Interrupt Example）](../sensors/P023_气压温度传感器中断示例.md#pressure_interrupt)
- [气压及温度传感器轮询示例](../sensors/P022_气压温度传感器轮询示例.md#pressure_polling)
- [外围传感器接口（PSI5）](../driver_samples/P038_PSI5接口示例.md#psi5)
- [瑞萨事件链接控制器（Renesas ELC）示例](../board_samples/P045_Renesas事件链接控制器.md#renesas-elc)
- [瑞萨比较器（Renesas Comparator）](../hardware/P098_Renesas比较器示例.md#renesas_comparator)
- [OpenAMP Linux Zephyr远程处理器消息（RPMsg）示例](../intercore_reference/P091_RenesasLinux与Zephyr通信示例.md#rz-openamp-linux-zephyr)
- [单边沿半字节传输接口（SENT）](../driver_samples/P039_SENT接口示例.md#sent)
- [SPI从机（SPIS）唤醒](../board_samples/P032_SPIS唤醒.md#spis-wakeup)
- [步进电机（Stepper）](../hardware/P165_通用步进电机示例.md#stepper)
- [通过数据就绪（Data Ready）触发器流式获取通用设备采样](../sensors/P014_数据就绪触发的传感器流示例.md#stream_drdy)
- [UART异步接口（ASYNC API）](../hardware/P349_UART异步API示例.md#uart_async)
- [USB CDC-ACM桥接（Bridge）](../usb/P056_CDCACM桥接示例.md#usb-cdc-acm-bridge)
- [通用唯一标识符（UUID）](../data_utilities/P015_UUID生成示例.md#uuid)
- [USB视频摄像头（USB Video Webcam）](../usb/P124_USB视频摄像头示例.md#uvc)
- [VEML6031高精度环境光传感器（High Accuracy Ambient Light Sensor）](../sensors/P061_VEML6031高精度环境光传感器示例.md#veml6031)

<a id="other-notable-changes"></a>

## 其他主要变更（Other Notable Changes）


- 新增Armv8.1-M内存保护单元（MPU）的特权禁止执行属性（Privileged Execute Never，PXN）支持。相应调整__ramfunc及__ram_text_reloc的MPU属性：启用CONFIG_ARM_MPU_PXN及CONFIG_USERSPACE编译时，为这些区域设置PXN。这会改变在这些区域执行代码的行为，因为设置PXN后，代码不能以特权模式执行。
- 移除Nucleo WBA52CG开发板（nucleo_wba52cg）支持，因为该板已不推荐用于新设计（Not Recommended for New Design，NRND），且STM32CubeWBA自1.1.0版本（2023年7月）起不再支持它。建议迁移到[Nucleo WBA55CG](../boards_st_nucleo/P077_Nucleo_WBA55CG.md#nucleo_wba55cg)（nucleo_wba55cg）。
- Mbed TLS从3.6.2更新到3.6.4。3.6.3及3.6.4发行说明如下：


  - 3.6.3发行说明：[https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.3](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.3)
  - 3.6.4发行说明：[https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.4](https://github.com/Mbed-TLS/mbedtls/releases/tag/mbedtls-3.6.4)
- TF-M从2.1.1更新到2.2.0。发行说明见：[https://trustedfirmware-m.readthedocs.io/en/latest/releases/2.2.0.html](https://trustedfirmware-m.readthedocs.io/en/latest/releases/2.2.0.html)。
- 所有带外部I2C连接器的开发板，例如Qwiic、Stemma及Grove，均改用zephyr_i2c设备树标签。由此可使用现有[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)构建功能west build --shield，将带连接器的I2C模块接到任何具有兼容I2C端口的开发板，无需受I2C连接器品牌限制。
- 撤销Nordic UART驱动接收器选项的弃用决定。使用额外TIMER外设计数接收字节的模式此前已弃用，例如原文写作CONFIG_CONFIG_UART_0_NRF_HW_ASYNC的选项；但后来发现，这种模式是唯一能在没有硬件流量控制（Hardware Flow Control）时可靠接收数据的模式，因此应保留。译注：原文配置名重复了CONFIG_前缀，此处保留其原始写法。

## 译注

本页按对应版本的官方发行说明翻译；“新增”“弃用”“当前”等描述均以该版本为背景。安全编号、开发板目标、设备树compatible、代码和源码路径保留原始标识；不会将原文中的历史保密期说明作为当前状态承诺。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Zephyr 3.7 发行说明](P001_Zephyr_3.7_发行说明.md) · [本模块主线目录](../reading/releases_notes.md) · [全部主线](../reading/README.md) · [下一篇：Zephyr 4.3 发行说明](P003_Zephyr_4.3_发行说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P001_Zephyr_3.7_发行说明.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_Zephyr_4.3_发行说明.md)

</details>

<!-- reading-navigation:end -->
