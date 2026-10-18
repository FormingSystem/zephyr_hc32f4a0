---
id: learning.zephyr-docs.networking.page-164
title: WiFi凭据库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/wifi_credentials.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第164章\_WiFi凭据库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/wifi_credentials.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Wi-Fi 凭据库（Wi-Fi Credentials Library）用于加载和保存 Wi-Fi® 网络凭据（Credentials）。原文说明该库使用 Zephyr 设置子系统（Settings Subsystem）或平台安全架构（Platform Security Architecture，PSA）的内部可信存储（Internal Trusted Storage，ITS）保存凭据，同时在 RAM 中维护服务集标识符（Service Set Identifier，SSID）列表，以 SSID 为键提供类似字典的访问方式。

> 源码对照：这里“ITS”是原文说法。当前官方[PSA 后端实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/wifi_credentials_backend_psa.c)实际上使用 PSA Crypto 的持久密钥接口：以 `PSA_KEY_TYPE_RAW_DATA`、`PSA_KEY_LIFETIME_PERSISTENT` 和允许导出的属性导入凭据，通过 `psa_import_key()`、`psa_export_key()`、`psa_destroy_key()` 保存、读取和删除。不能据原文推断应用直接调用 ITS API；实际存储保护由所选 PSA 实现及平台配置决定。

## 2. 配置（Configuration）

启用 [`CONFIG_WIFI_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS) 使用该库。通过以下选项选择后端：

| 配置 | 原文说明 |
| --- | --- |
| [`CONFIG_WIFI_CREDENTIALS_BACKEND_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_BACKEND_PSA) | 包含 TF-M 分区、采用非最小 TF-M 配置档（Profile）的非安全目标（Non-Secure Target）的默认选择。 |
| [`CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_BACKEND_SETTINGS) | 安全目标（Secure Target）的默认选择。 |

> 译注：TF-M 是 Trusted Firmware-M。当前[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/Kconfig)首先在 `BUILD_WITH_TFM` 为真时默认选择 PSA，否则选择满足依赖的 Settings；静态凭据还有无存储后端。应以实际 Kconfig 依赖及最终配置为准，不将“安全／非安全”视为可脱离平台前提单独选择后端的开关。

[`CONFIG_WIFI_CREDENTIALS_MAX_ENTRIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_MAX_ENTRIES) 配置可保存网络的最大数量。IEEE 802.11 没有规定 SAE 密码的最大长度，可使用 [`CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH) 调整库中的默认上限。SAE 指对等实体同时认证（Simultaneous Authentication of Equals）。

## 3. 添加凭据（Adding Credentials）

使用 [`wifi_credentials_set_personal()`](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga28b13d11cca692921252e98788552957) 或 [`wifi_credentials_set_personal_struct()`](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga1b5525c7a6a7ca312236a2c674d94055) 添加凭据。前者根据给定字段构建内部结构体，后者直接接收该结构体。两次添加相同 SSID 时，新条目覆盖旧条目。

## 4. 查询凭据（Querying Credentials）

已知 SSID 时，通过 [`wifi_credentials_get_by_ssid_personal()`](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga548522fbc6b5fdcff4585c34f3565c82) 或 [`wifi_credentials_get_by_ssid_personal_struct()`](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3d83001e713206ec07f94996137537d5) 查询凭据。

使用 [`wifi_credentials_for_each_ssid()`](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3a5b20d07afc52cc452a9c55998ebcf7) 遍历所有已保存的凭据。遍历期间允许删除或覆盖条目，因为这些操作不会改变内部索引。

## 5. 删除凭据（Removing Credentials）

使用 [`wifi_credentials_delete_by_ssid()`](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga644d29db8091512a977f8e27b245975e) 删除指定 SSID 对应的凭据。

## 6. 命令行（Shell Commands）

`wifi cred` 是 Wi-Fi 命令行的扩展，通过以下子命令与凭据库交互：

| 子命令 | 说明 |
| --- | --- |
| `add` | 按下表参数向凭据存储添加网络。 |
| `delete <SSID>` | 从凭据存储删除网络。 |
| `list` | 列出凭据存储中的网络。 |
| `auto_connect` | 自动连接已保存的网络之一。 |

以下逐项保留原文 `add` 的全部参数和数值，并将网页中长选项前的排版破折号规范为可输入的两个连字符 `--`：

| 参数 | 说明 |
| --- | --- |
| `-s, --ssid "<SSID>"` | 必填，SSID。 |
| `-c, --channel` | 连接时需要扫描的信道；`0` 表示任意信道。 |
| `-b, --band` | 频段：`0` 为任意，`2` 为 2.4 GHz，`5` 为 5 GHz，`6` 为 6 GHz。 |
| `-p, --passphrase` | 口令，仅适用于受保护的 SSID。 |
| `-k, --key-mgmt` | 密钥管理类型：`0` None、`1` WPA2-PSK、`2` WPA2-PSK-256、`3` SAE-HNP、`4` SAE-H2E、`5` SAE-AUTO、`6` WAPI、`7` EAP-TLS、`8` WEP、`9` WPA-PSK、`10` WPA-Auto-Personal、`11` DPP。 |
| `-w, --ieee-80211w` | 管理帧保护（Management Frame Protection，MFP），可选但需指定安全类型：`0` 禁用、`1` 可选、`2` 必须启用。 |
| `-m, --bssid` | 接入点 MAC 地址，即基本服务集标识符（Basic Service Set Identifier，BSSID）。 |
| `-t, --timeout` | 超过该时间后，连接尝试应判定失败。 |
| `-a, --identity` | 企业模式身份。 |
| `-K, --key-passwd` | 企业模式私钥密码。 |
| `-h, --help` | 原文描述为打印 `connect` 命令帮助。 |

> 译注：这是官方页面所列参数，并非对所有版本命令行的保证。原表中的多余引号已去除；当前命令可用项以设备 `wifi cred add --help` 和官方[wifi_credentials_shell.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/wifi_credentials/wifi_credentials_shell.c)为准。特别是企业认证选项受构建配置控制，不能由表中出现这些参数推断企业凭据支持完整。

## 7. 限制（Limitations）

- IEEE 802.11 标准允许零长度 SSID，但此库不支持。
- Wi-Fi 保护访问（Wi-Fi Protected Access，WPA）企业模式凭据仅得到部分支持。
- 可存储网络的数量在编译时固定。

## 8. API 文档与相关示例

Zephyr 提供的接口概览和完整参考见[Wi-Fi 凭据库 API（Wi-Fi Credentials Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html)。该参考页与其子页单独跟踪，本章仅覆盖官方库指南。

相关示例：[通过低功耗蓝牙配置 Wi-Fi](P168_通过低功耗蓝牙配置WiFi.md#wifi-ble-provisioning)，展示通过 BLE 通用属性配置文件（Generic Attribute Profile，GATT）服务接收 Wi-Fi 凭据并连接接入点。


<a id="wi-fi-credentials-library"></a>
<a id="lib-wifi-credentials"></a>
<a id="contents"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="overview"></a>
<a id="configuration"></a>
<a id="adding-credentials"></a>
<a id="querying-credentials"></a>
<a id="removing-credentials"></a>
<a id="shell-commands"></a>
<a id="id1"></a>
<a id="limitations"></a>
<a id="api-documentation"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：WiFi管理接口](P163_WiFi管理接口.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：WiFi功能与密码原语映射](P165_WiFi功能与密码原语映射.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P163_WiFi管理接口.md) · [返回大纲](大纲.md) · [下一章](P165_WiFi功能与密码原语映射.md)

</details>

<!-- reading-navigation:end -->
