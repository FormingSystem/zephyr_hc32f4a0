---
id: learning.zephyr-docs.kconfig-reference.page-192
title: "`drivers/wifi`配置项参考（5/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第192章\_`drivers/wifi`配置项参考（5/7）

本章翻译官方 Kconfig 数据库中 `drivers/wifi` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NXP_WIFI_SMOKE_TESTS"></a>

## 192.1 `CONFIG_NXP_WIFI_SMOKE_TESTS`

**提示（Prompt）**：冒烟测试（Smoke Tests）

**说明（Help）**

此选项用于 Wi-Fi 驱动开发时的冒烟测试（smoke test）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_NET_SHELL
CONFIG_KERNEL_SHELL
CONFIG_SHELL_BACKEND_TELNET
CONFIG_SHELL_TELNET_SUPPORT_COMMAND
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1224)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SHELL)、[`CONFIG_KERNEL_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_KERNEL_SHELL)、[`CONFIG_SHELL_BACKEND_TELNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_TELNET_SUPPORT_COMMAND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_TELNET_SUPPORT_COMMAND)。

<a id="CONFIG_NXP_WIFI_SM_IP_ADDRESS"></a>

## 192.2 `CONFIG_NXP_WIFI_SM_IP_ADDRESS`

**提示（Prompt）**：NXP 站点模式（Station mode）的 IP 地址

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SM_IP_STATIC && CONFIG_NXP_WIFI_SMOKE_TESTS && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1265)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 冒烟测试（Smoke Tests）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SM_IP_STATIC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SM_IP_STATIC)、[`CONFIG_NXP_WIFI_SMOKE_TESTS`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SMOKE_TESTS)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SM_IP_DHCP"></a>

## 192.3 `CONFIG_NXP_WIFI_SM_IP_DHCP`

**提示（Prompt）**：动态主机配置协议（DHCP）

**说明（Help）**

使用动态主机配置协议（DHCP）获取 IP 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1251)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 冒烟测试（Smoke Tests） → NXP SM IP 地址配置

<a id="CONFIG_NXP_WIFI_SM_IP_GATEWAY"></a>

## 192.4 `CONFIG_NXP_WIFI_SM_IP_GATEWAY`

**提示（Prompt）**：网关地址（Gateway Address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SM_IP_STATIC && CONFIG_NXP_WIFI_SMOKE_TESTS && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1268)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 冒烟测试（Smoke Tests）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SM_IP_STATIC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SM_IP_STATIC)、[`CONFIG_NXP_WIFI_SMOKE_TESTS`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SMOKE_TESTS)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SM_IP_MASK"></a>

## 192.5 `CONFIG_NXP_WIFI_SM_IP_MASK`

**提示（Prompt）**：网络掩码（Network Mask）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SM_IP_STATIC && CONFIG_NXP_WIFI_SMOKE_TESTS && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1271)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 冒烟测试（Smoke Tests）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SM_IP_STATIC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SM_IP_STATIC)、[`CONFIG_NXP_WIFI_SMOKE_TESTS`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SMOKE_TESTS)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SM_IP_STATIC"></a>

## 192.6 `CONFIG_NXP_WIFI_SM_IP_STATIC`

**提示（Prompt）**：静态（Static）

**说明（Help）**

设置静态 IP 地址（Static IP Address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1256)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 冒烟测试（Smoke Tests） → NXP SM IP 地址配置

<a id="CONFIG_NXP_WIFI_SOFTAP_DHCP_SERVER"></a>

## 192.7 `CONFIG_NXP_WIFI_SOFTAP_DHCP_SERVER`

**提示（Prompt）**：软件接入点（SoftAP）的 DHCP 服务器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_DHCPV4_SERVER
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:718`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L718)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 软件接入点（SoftAP）支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_DHCPV4_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4_SERVER)。

<a id="CONFIG_NXP_WIFI_SOFTAP_IP_ADDRESS"></a>

## 192.8 `CONFIG_NXP_WIFI_SOFTAP_IP_ADDRESS`

**提示（Prompt）**：NXP 软件接入点模式（SoftAP mode）的 IP 地址

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"192.168.10.1"
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:702`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L702)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 软件接入点（SoftAP）支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SOFTAP_IP_BASE"></a>

## 192.9 `CONFIG_NXP_WIFI_SOFTAP_IP_BASE`

**提示（Prompt）**：NXP 软件接入点（SoftAP）基地址

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"192.168.10.2"
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:714`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L714)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 软件接入点（SoftAP）支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SOFTAP_IP_GATEWAY"></a>

## 192.10 `CONFIG_NXP_WIFI_SOFTAP_IP_GATEWAY`

**提示（Prompt）**：网关地址（Gateway Address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"192.168.10.1"
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:706`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L706)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 软件接入点（SoftAP）支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SOFTAP_IP_MASK"></a>

## 192.11 `CONFIG_NXP_WIFI_SOFTAP_IP_MASK`

**提示（Prompt）**：网络掩码（Network Mask）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"255.255.255.0"
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:710`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L710)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 软件接入点（SoftAP）支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SOFTAP_SUPPORT"></a>

## 192.12 `CONFIG_NXP_WIFI_SOFTAP_SUPPORT`

**提示（Prompt）**：Wi-Fi 软件接入点（SoftAP）支持

**说明（Help）**

在 Wi-Fi 驱动中启用软件接入点（SoftAP）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_USAGE_MODE_AP || CONFIG_WIFI_USAGE_MODE_STA_AP
```

**主动选择（Selects）**

```text
CONFIG_WIFI_NM_HOSTAPD_AP if CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**弱选择（Implies）**

```text
CONFIG_WIFI_NM_HOSTAPD_WPS if CONFIG_WIFI_NM_HOSTAPD_AP && CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS
CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE if CONFIG_WIFI_NM_HOSTAPD_AP && CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:691`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L691)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_AP)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)、[`CONFIG_WIFI_NM_HOSTAPD_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_HOSTAPD_AP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_HOSTAPD_WPS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_HOSTAPD_WPS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS)、[`CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_HOSTAPD_CRYPTO_ENTERPRISE)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)。

<a id="CONFIG_NXP_WIFI_STA_AUTO_CONN"></a>

## 192.13 `CONFIG_NXP_WIFI_STA_AUTO_CONN`

**提示（Prompt）**：自动启动站点（STA）连接

**说明（Help）**

启用站点（Station）自动连接支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:520`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L520)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_STA_AUTO_PASSWORD"></a>

## 192.14 `CONFIG_NXP_WIFI_STA_AUTO_PASSWORD`

**提示（Prompt）**：NXP Wi-Fi 站点（STA）自动连接密码

**说明（Help）**

指定自动连接时使用的外部接入点（Access Point）口令（Passphrase）。默认仅支持预共享密钥（PSK）安全方式或开放式安全方式（open security）。长度范围为 8～64；开放式安全方式使用 0。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_STA_AUTO_CONN && CONFIG_NXP_WIFI_STA_AUTO_CONN && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:537`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L537)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → 自动启动站点（STA）连接

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_STA_AUTO_CONN`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_STA_AUTO_CONN)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_STA_AUTO_SSID"></a>

## 192.15 `CONFIG_NXP_WIFI_STA_AUTO_SSID`

**提示（Prompt）**：NXP Wi-Fi 站点（STA）自动连接的 SSID

**说明（Help）**

指定自动连接的外部接入点（Access Point）的服务集标识符（SSID）。最大长度为 32 个 ASCII 字符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_STA_AUTO_CONN && CONFIG_NXP_WIFI_STA_AUTO_CONN && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"myssid"
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:528`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L528)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持 → 自动启动站点（STA）连接

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_STA_AUTO_CONN`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_STA_AUTO_CONN)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_STA_RECONNECT"></a>

## 192.16 `CONFIG_NXP_WIFI_STA_RECONNECT`

**提示（Prompt）**：自动启动站点（STA）重连

**说明（Help）**

与当前关联的接入点（Access Point）断开连接时，启用站点（Station）自动重连支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:549`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L549)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_SUBSCRIBE_EVENT_SUPPORT"></a>

## 192.17 `CONFIG_NXP_WIFI_SUBSCRIBE_EVENT_SUPPORT`

**提示（Prompt）**：订阅固件事件（Subscribe event from firmware）

**说明（Help）**

打印从固件获取的订阅事件（subscribe event），供用户测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1096`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1096)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_SUPP_DEBUG"></a>

## 192.18 `CONFIG_NXP_WIFI_SUPP_DEBUG`

**提示（Prompt）**：认证客户端接口（Supplicant interface）调试

**说明（Help）**

启用认证客户端接口（supplicant interface）的调试信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1312`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1312)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG)。

<a id="CONFIG_NXP_WIFI_TC_RELOCATE"></a>

## 192.19 `CONFIG_NXP_WIFI_TC_RELOCATE`

**提示（Prompt）**：将数据流量 API 重定位到 RAM

**说明（Help）**

将 Wi-Fi 发送和接收 API 重定位（relocate）到 RAM，以提高数据吞吐量（throughput）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1175)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)。

<a id="CONFIG_NXP_WIFI_TIMER_DEBUG"></a>

## 192.20 `CONFIG_NXP_WIFI_TIMER_DEBUG`

**提示（Prompt）**：定时器（Timers）调试

**说明（Help）**

启用此选项以监视驱动的定时器活动（timer activity）。这些定时器通常用于处理 AMPDU 乱序数据包（out-of-order packet），也用于与命令超时相关的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1424`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1424)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_TSP"></a>

## 192.21 `CONFIG_NXP_WIFI_TSP`

**提示（Prompt）**：温度安全保护（Thermal Safeguard Protection）

**说明（Help）**

用于设置和获取温度安全保护（Thermal Safeguard Protection）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:987`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L987)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_TURBO_MODE"></a>

## 192.22 `CONFIG_NXP_WIFI_TURBO_MODE`

**提示（Prompt）**：加速模式（Turbo Mode）

**说明（Help）**

在 Wi-Fi 驱动中启用 WMM 加速模式（Turbo Mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_WMM && !CONFIG_NXP_88W8801 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:820`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L820)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_WMM`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_WMM)、[`CONFIG_NXP_88W8801`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_88W8801)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_TX_AMPDU_PROT_MODE"></a>

## 192.23 `CONFIG_NXP_WIFI_TX_AMPDU_PROT_MODE`

**提示（Prompt）**：TX AMPDU 保护模式（Protection Mode）支持

**说明（Help）**

启用 TX AMPDU 保护模式（protection mode）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:808`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L808)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_TX_PER_TRACK"></a>

## 192.24 `CONFIG_NXP_WIFI_TX_PER_TRACK`

**提示（Prompt）**：发送数据包错误跟踪（TX packet error tracking）

**说明（Help）**

用于跟踪发送数据包错误率（TX packet error ratio）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:857`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L857)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_TX_RX_HISTOGRAM"></a>

## 192.25 `CONFIG_NXP_WIFI_TX_RX_HISTOGRAM`

**提示（Prompt）**：发送／接收统计（TX/RX statistics）

**说明（Help）**

在 Wi-Fi 驱动中启用发送／接收统计（TX/RX statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_RW610 || CONFIG_NXP_IW610
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_NXP_IW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW610)。

<a id="CONFIG_NXP_WIFI_TX_RX_ZERO_COPY"></a>

## 192.26 `CONFIG_NXP_WIFI_TX_RX_ZERO_COPY`

**提示（Prompt）**：发送／接收数据包零内存复制（Zero memory copy TX/RX）

**说明（Help）**

在 Wi-Fi 驱动的数据路径（data path）中启用数据包零内存复制（zero memory copy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NXP_RW610 || CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER) && CONFIG_NXP_WIFI_WMM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SCATTER_GATHER_TRANSFER if !CONFIG_NXP_RW610
CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM if !CONFIG_NXP_RW610
```

**弱选择（Implies）**

```text
CONFIG_NET_IPV4_FRAGMENT
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:842`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L842)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER)、[`CONFIG_NXP_WIFI_WMM`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_WMM)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_SDHC_SCATTER_GATHER_TRANSFER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SCATTER_GATHER_TRANSFER)、[`CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_EXTRA_TX_PKT_HEADROOM)、[`CONFIG_NET_IPV4_FRAGMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_FRAGMENT)。

<a id="CONFIG_NXP_WIFI_TX_TASK_PRIO"></a>

## 192.27 `CONFIG_NXP_WIFI_TX_TASK_PRIO`

**提示（Prompt）**：Wi-Fi 驱动发送任务（TX task）优先级

**说明（Help）**

指定 Wi-Fi 驱动发送任务（TX task）的优先级。为获得更高吞吐量，最好使所有发送／接收任务（TX/RX tasks）具有相同优先级。不同任务之间的相对优先级已经过调优，需要保持与当前设置一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_WMM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 线程优先级配置

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_WMM`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_WMM)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_TX_TASK_STACK_SIZE"></a>

## 192.28 `CONFIG_NXP_WIFI_TX_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 驱动发送任务（TX task）栈大小

**说明（Help）**

指定 Wi-Fi 驱动发送任务（TX task）使用的栈大小（stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_WMM && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:446`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L446)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 驱动栈配置（Stack Configurations）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_WMM`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_WMM)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_UAP_DEBUG"></a>

## 192.29 `CONFIG_NXP_WIFI_UAP_DEBUG`

**提示（Prompt）**：Wi-Fi 驱动微型接入点（uAP）调试

**说明（Help）**

启用后打印与微型接入点（uAP）相关的日志，帮助开发者定位 uAP 问题。除其他日志外，还会打印 uAP 初始化和配置日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1334)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging） → Wi-Fi 额外调试选项

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_UAP_STA_MAC_ADDR_FILTER"></a>

## 192.30 `CONFIG_NXP_WIFI_UAP_STA_MAC_ADDR_FILTER`

**提示（Prompt）**：Wi-Fi 软件接入点（SoftAP）客户端允许／阻止列表

**说明（Help）**

允许或阻止允许列表（allowed list）中指定的 MAC 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if !CONFIG_NXP_WIFI_SLIM
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:723`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L723)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 软件接入点（SoftAP）支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_SLIM`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SLIM)。

<a id="CONFIG_NXP_WIFI_UAP_WORKAROUND_STICKY_TIM"></a>

## 192.31 `CONFIG_NXP_WIFI_UAP_WORKAROUND_STICKY_TIM`

**提示（Prompt）**：保持置位的 TIM（Sticky TIM）

**说明（Help）**

启用某个特定固件问题的规避措施（workaround）：该问题会导致站点（STA）处于 IEEE 节能模式（PS）时仍通过无线链路发送数据包。启用此项会采用保持 TIM 位的规避措施（sticky TIM bit workaround）。其缺点是微型接入点（uAP）的 STA 客户端将无法进入 IEEE PS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_SOFTAP_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:729`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L729)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 软件接入点（SoftAP）支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_SOFTAP_SUPPORT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_NXP_WIFI_SOFTAP_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_UNII4_BAND_SUPPORT"></a>

## 192.32 `CONFIG_NXP_WIFI_UNII4_BAND_SUPPORT`

**提示（Prompt）**：UNII4 支持

**说明（Help）**

用于启用或禁用 UNII4 信道（channels）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_5GHz_SUPPORT && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:920`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L920)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_5GHz_SUPPORT`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_5GHz_SUPPORT)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WAKE_TIMER_ENABLE"></a>

## 192.33 `CONFIG_NXP_WIFI_WAKE_TIMER_ENABLE`

**提示（Prompt）**：启用唤醒定时器（Wake Timer）

**说明（Help）**

在 Wi-Fi 驱动中启用持续 5 秒的唤醒定时器（wake timer）。启用后，设备从休眠中唤醒时，低功耗模式（low power mode）将被阻止 5 秒。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_HOST_SLEEP && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1150)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 主机睡眠（Host Sleep）

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_HOST_SLEEP`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_HOST_SLEEP)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WLAN_CALDATA_1ANT"></a>

## 192.34 `CONFIG_NXP_WIFI_WLAN_CALDATA_1ANT`

**提示（Prompt）**：单天线（One antenna）

**说明（Help）**

用于启用单天线（one antenna）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW610 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1048`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1048)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WLAN_CALDATA_1ANT_WITH_DIVERSITY"></a>

## 192.35 `CONFIG_NXP_WIFI_WLAN_CALDATA_1ANT_WITH_DIVERSITY`

**提示（Prompt）**：单天线分集（One antenna diversity）

**说明（Help）**

用于启用单天线分集（one antenna diversity）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW610 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1053`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1053)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WLAN_CALDATA_3ANT_DIVERSITY"></a>

## 192.36 `CONFIG_NXP_WIFI_WLAN_CALDATA_3ANT_DIVERSITY`

**提示（Prompt）**：三天线分集（Three antenna diversity）

**说明（Help）**

用于启用三天线分集（three antenna diversity）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_RW610 && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1058`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1058)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_RW610`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_RW610)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WLCMGR_DEBUG"></a>

## 192.37 `CONFIG_NXP_WIFI_WLCMGR_DEBUG`

**提示（Prompt）**：无线连接管理器（Wireless Connection Manager）

**说明（Help）**

启用 WLAN 连接管理器（Connection Manager）API 的调试信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:1318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L1318)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → 开发与调试（Development and Debugging）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WLCMGR_TASK_PRIO"></a>

## 192.38 `CONFIG_NXP_WIFI_WLCMGR_TASK_PRIO`

**提示（Prompt）**：无线连接管理器任务（wlcmgr task）优先级

**说明（Help）**

指定无线连接管理器任务（wlcmgr task）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:482`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L482)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 线程优先级配置

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WLCMGR_TASK_STACK_SIZE"></a>

## 192.39 `CONFIG_NXP_WIFI_WLCMGR_TASK_STACK_SIZE`

**提示（Prompt）**：无线连接管理器线程（wlcmgr thread）栈大小

**说明（Help）**

指定无线连接管理器任务（wlcmgr task）使用的栈大小（stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5120
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:434`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L434)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 驱动栈配置（Stack Configurations）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_NXP_WIFI_WLS"></a>

## 192.40 `CONFIG_NXP_WIFI_WLS`

**提示（Prompt）**：无线定位服务（Wireless Location Service）

**说明（Help）**

启用或禁用无线定位服务（Wireless Location Service，WLS）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NXP_WIFI_CSI && CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_NXP_IW61X && CONFIG_WIFI_NM_WPA_SUPPLICANT && !CONFIG_ARM64
```

**主动选择（Selects）**

```text
CONFIG_FPU
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:889`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L889)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NXP_WIFI_CSI`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_CSI)、[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_IW61X`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_IW61X)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_FPU`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU)。

<a id="CONFIG_NXP_WIFI_WMM"></a>

## 192.41 `CONFIG_NXP_WIFI_WMM`

**提示（Prompt）**：802.11 无线多媒体（WMM）支持

**说明（Help）**

启用 802.11 无线多媒体（WMM）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_11AX
CONFIG_NXP_WIFI_11AC
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:776`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L776)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NXP_WIFI_11AX`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_WIFI_11AX)、[`CONFIG_NXP_WIFI_11AC`](P190_drivers_wifi_配置项参考_3.md#CONFIG_NXP_WIFI_11AC)。

<a id="CONFIG_NXP_WIFI_WMM_UAPSD"></a>

## 192.42 `CONFIG_NXP_WIFI_WMM_UAPSD`

**提示（Prompt）**：非调度自动节能传输模式（UAPSD mode）

**说明（Help）**

在 Wi-Fi 驱动中启用 WMM 非调度自动节能传输（UAPSD）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_NXP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/nxp/Kconfig.nxp:627`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/nxp/Kconfig.nxp#L627)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → NXP Wi-Fi 驱动支持 → Wi-Fi 站点（Station）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NXP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_RTK_AP_IPV4_ADDR"></a>

## 192.43 `CONFIG_RTK_AP_IPV4_ADDR`

**提示（Prompt）**：RTK 软件接入点（SoftAP）IPv4 地址

**说明（Help）**

分配给 RTK 软件接入点（SoftAP）接口的 IPv4 地址。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"192.168.43.1"
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_RTK_AP_IPV4_GATEWAY"></a>

## 192.44 `CONFIG_RTK_AP_IPV4_GATEWAY`

**提示（Prompt）**：RTK 软件接入点（SoftAP）IPv4 网关

**说明（Help）**

软件接入点（SoftAP）客户端使用的网关（gateway），通常为接入点（AP）本身。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"192.168.43.1"
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_RTK_AP_IPV4_NETMASK"></a>

## 192.45 `CONFIG_RTK_AP_IPV4_NETMASK`

**提示（Prompt）**：RTK 软件接入点（SoftAP）IPv4 网络掩码

**说明（Help）**

软件接入点（SoftAP）的 IPv4 地址所使用的网络掩码（netmask）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"255.255.255.0"
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_RTK_WIFI_AP_STA_MODE"></a>

## 192.46 `CONFIG_RTK_WIFI_AP_STA_MODE`

**提示（Prompt）**：接入点与站点并发模式（Concurrent AP and STA mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_RTK_WIFI_STA_AUTO_DHCPV4"></a>

## 192.47 `CONFIG_RTK_WIFI_STA_AUTO_DHCPV4`

**提示（Prompt）**：自动启动 DHCP4 协商（negotiation）

**说明（Help）**

Wi-Fi 驱动在连接后自动启动 DHCPV4 协商（negotiation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NET_IPV4 && CONFIG_WIFI_AMEBA && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Ameba 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_WIFI_AMEBA`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AMEBA)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_RX_AT_CMD_RING_BUF_SIZE"></a>

## 192.48 `CONFIG_ST67W611M1_RX_AT_CMD_RING_BUF_SIZE`

**提示（Prompt）**：接收 AT 命令环形缓冲区（RX AT command ring buffer）大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
768
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_RX_THREAD_PRIORITY"></a>

## 192.49 `CONFIG_ST67W611M1_RX_THREAD_PRIORITY`

**提示（Prompt）**：接收线程（RX thread）优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_RX_THREAD_STACK_SIZE"></a>

## 192.50 `CONFIG_ST67W611M1_RX_THREAD_STACK_SIZE`

**提示（Prompt）**：接收线程（RX thread）栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_SCAN_RESULT_MAX_NUMBER"></a>

## 192.51 `CONFIG_ST67W611M1_SCAN_RESULT_MAX_NUMBER`

**提示（Prompt）**：最大扫描结果数（scan results）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_SPI_PKT_MEM_SLAB_COUNT"></a>

## 192.52 `CONFIG_ST67W611M1_SPI_PKT_MEM_SLAB_COUNT`

**提示（Prompt）**：最大 SPI 数据包数（pkts）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_SPI_PROCESSOR_THREAD_PRIORITY"></a>

## 192.53 `CONFIG_ST67W611M1_SPI_PROCESSOR_THREAD_PRIORITY`

**提示（Prompt）**：处理 SPI 发送和接收传输（TX/RX transfers）的线程优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_SPI_PROCESSOR_THREAD_STACK_SIZE"></a>

## 192.54 `CONFIG_ST67W611M1_SPI_PROCESSOR_THREAD_STACK_SIZE`

**提示（Prompt）**：SPI 发送／接收传输线程（TX/RX transfer thread）栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_TX_AT_CMD_NET_BUF_POOL_COUNT"></a>

## 192.55 `CONFIG_ST67W611M1_TX_AT_CMD_NET_BUF_POOL_COUNT`

**提示（Prompt）**：AT 命令网络缓冲区池（net buf pool）中的缓冲区数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_TX_AT_CMD_NET_BUF_POOL_SIZE"></a>

## 192.56 `CONFIG_ST67W611M1_TX_AT_CMD_NET_BUF_POOL_SIZE`

**提示（Prompt）**：AT 命令网络缓冲区池（net buf pool）中的缓冲区大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_TX_AT_CMD_NET_PKT_SLAB_COUNT"></a>

## 192.57 `CONFIG_ST67W611M1_TX_AT_CMD_NET_PKT_SLAB_COUNT`

**提示（Prompt）**：可同时分配的 AT 命令 `net_pkt` 数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_WIFI_AUTO_CONNECT"></a>

## 192.58 `CONFIG_ST67W611M1_WIFI_AUTO_CONNECT`

**提示（Prompt）**：启动时自动连接已保存的接入点（access point）

**说明（Help）**

控制模块上电时的自动连接（auto-connect，`AT+CWAUTOCONN`）。启用后，模块在启动时会自动重新连接上一次配置的接入点（access point）。禁用此项可将连接管理交给 Wi-Fi 管理 API。仅当此设置与模块当前值不同时才写入，因为模块会将其持久保存到闪存（flash）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_WIFI_STA_SAP_MODE"></a>

## 192.59 `CONFIG_ST67W611M1_WIFI_STA_SAP_MODE`

**提示（Prompt）**：在站点模式（STA mode）之上启用软件接入点模式（SoftAP mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y if CONFIG_WIFI_USAGE_MODE_STA_AP
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_STA_AP`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_STA_AP)。

<a id="CONFIG_ST67W611M1_WORKQ_STACK_SIZE"></a>

## 192.60 `CONFIG_ST67W611M1_WORKQ_STACK_SIZE`

**提示（Prompt）**：驱动工作队列（work queue）栈大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_ST67W611M1_WORKQ_THREAD_PRIORITY"></a>

## 192.61 `CONFIG_ST67W611M1_WORKQ_THREAD_PRIORITY`

**提示（Prompt）**：工作队列线程（work queue thread）优先级

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ST67W611M1 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/wifi/st67w611m1/Kconfig.st67w611m1:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/st67w611m1/Kconfig.st67w611m1#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ST67W611M1 Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ST67W611M1`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ST67W611M1)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WHD_DISABLE_SDIO_PULLUP_DURING_SPI_SLEEP"></a>

## 192.62 `CONFIG_WHD_DISABLE_SDIO_PULLUP_DURING_SPI_SLEEP`

**提示（Prompt）**：在 SPI 休眠期间禁用 SDIO 上拉（pullups）

**说明（Help）**

当 SPI 总线被配置为休眠（sleep）时，清除 SDIO 上拉（pullups）。此选项默认为 `n`，因此默认启用 SDIO 上拉。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WHD_WIFI_COUNTRY"></a>

## 192.63 `CONFIG_WHD_WIFI_COUNTRY`

**提示（Prompt）**：Wi-Fi 国家／地区选项（country option）

**说明（Help）**

设置 Wi-Fi 初始化参数所使用的运行国家／地区（country）。有效选项见 `wifi-host-driver` 中的 `whd_country_code_t`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_AIROC && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"WHD_COUNTRY_UNITED_STATES" if CONFIG_CYW55572 || CONFIG_CYW55500
"WHD_COUNTRY_AUSTRALIA"
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_AIROC`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_AIROC)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_CYW55572`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55572)、[`CONFIG_CYW55500`](P188_drivers_wifi_配置项参考_1.md#CONFIG_CYW55500)。

<a id="CONFIG_WIFI"></a>

## 192.64 `CONFIG_WIFI`

**提示（Prompt）**：Wi-Fi 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/adafruit_winc1500/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_winc1500/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/wifi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_WIFI_AIROC"></a>

## 192.65 `CONFIG_WIFI_AIROC`

**提示（Prompt）**：Infineon AIROC 片上系统（SoC）Wi-Fi 支持

**说明（Help）**

启用英飞凌（Infineon）AIROC SoC 的 Wi-Fi 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AIROC_WIFI_ENABLED && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_THREAD_CUSTOM_DATA
CONFIG_NET_L2_ETHERNET
CONFIG_NET_L2_WIFI_MGMT
CONFIG_GPIO
CONFIG_WIFI_USE_NATIVE_NETWORKING
CONFIG_USE_INFINEON_ABSTRACTION_RTOS
```

**定义位置（Location）**：[`drivers/wifi/infineon/Kconfig.airoc:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/Kconfig.airoc#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_THREAD_CUSTOM_DATA`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_CUSTOM_DATA)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_USE_INFINEON_ABSTRACTION_RTOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_ABSTRACTION_RTOS)。

<a id="CONFIG_WIFI_AMEBA"></a>

## 192.66 `CONFIG_WIFI_AMEBA`

**提示（Prompt）**：Ameba 片上系统（SoC）Wi-Fi 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_WIFI_ENABLED && (CONFIG_ZEPHYR_HAL_REALTEK_MODULE_BLOBS || CONFIG_BUILD_ONLY_NO_BLOBS) && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_WIFI_USE_NATIVE_NETWORKING
CONFIG_NET_L2_ETHERNET
CONFIG_WIFI_NM
```

**定义位置（Location）**：[`drivers/wifi/ameba/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/ameba/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_REALTEK_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_REALTEK_MODULE_BLOBS)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_WIFI_NM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_REALTEK_MODULE_BLOBS`。

<a id="CONFIG_WIFI_BFLB"></a>

## 192.67 `CONFIG_WIFI_BFLB`

**提示（Prompt）**：博流（Bouffalo Lab）Wi-Fi 驱动

**说明（Help）**

启用使用 MACSW 二进制固件（blob）的博流（Bouffalo Lab）Wi-Fi 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_BFLB_WIFI6_ENABLED || DT_HAS_BFLB_WIFI4_ENABLED) && CONFIG_ZEPHYR_MBEDTLS_MODULE && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_NET_L2_ETHERNET
CONFIG_NET_L2_ETHERNET_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
CONFIG_HWINFO
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_BFLB_PHYRF
CONFIG_NET_SOCKETS
```

**定义位置（Location）**：[`drivers/wifi/bflb/Kconfig.bflb_wifi:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/Kconfig.bflb_wifi#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_MBEDTLS_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_MBEDTLS_MODULE)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_ETHERNET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_BFLB_PHYRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_PHYRF)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_MBEDTLS_MODULE`。

<a id="CONFIG_WIFI_BFLB_WIFI4"></a>

## 192.68 `CONFIG_WIFI_BFLB_WIFI4`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

wifi4 MACSW 二进制固件驱动（firmware blob driver，BL60x）的公共支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_WIFI4_ENABLED && CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BFLB_BL602_OS_SHIM
CONFIG_EVENTS
CONFIG_CRC
CONFIG_MBEDTLS_PSA_CRYPTO_C
CONFIG_PSA_WANT_KEY_TYPE_AES
CONFIG_PSA_WANT_ALG_CCM
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi4/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi4/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_BFLB_BL602_OS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_BL602_OS_SHIM)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_KEY_TYPE_AES)、[`CONFIG_PSA_WANT_ALG_CCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_CCM)。

<a id="CONFIG_WIFI_BFLB_WIFI4_RX_RING_CNT"></a>

## 192.69 `CONFIG_WIFI_BFLB_WIFI4_RX_RING_CNT`

**提示（Prompt）**：接收暂存环槽位数（RX staging ring slots）

**说明（Help）**

固件接收回调（RX callback）与 `net_pkt` 分配工作队列（allocation work queue）之间的暂存槽位数量；每个槽位为 1600 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_WIFI4_ENABLED && CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi4/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi4/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI4_SCAN_AP_MAX"></a>

## 192.70 `CONFIG_WIFI_BFLB_WIFI4_SCAN_AP_MAX`

**提示（Prompt）**：扫描结果缓存条目数（Scan result cache entries）

**说明（Help）**

扫描结果缓存（scan result cache）中保留的接入点（access point）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_WIFI4_ENABLED && CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi4/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi4/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI4_TASK_PRIORITY"></a>

## 192.71 `CONFIG_WIFI_BFLB_WIFI4_TASK_PRIORITY`

**提示（Prompt）**：Wi-Fi 固件任务（firmware task）优先级

**说明（Help）**

固件调度循环（firmware scheduler loop）的可抢占线程（preemptible thread）优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_WIFI4_ENABLED && CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi4/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi4/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI4_TASK_STACK_SIZE"></a>

## 192.72 `CONFIG_WIFI_BFLB_WIFI4_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 固件任务（firmware task）栈大小

**说明（Help）**

wifi4 固件调度器线程（firmware scheduler thread）的栈大小。二进制固件（blob）的内核队列和事件处理程序均在该线程中运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_WIFI4_ENABLED && CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi4/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi4/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI6"></a>

## 192.73 `CONFIG_WIFI_BFLB_WIFI6`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

wifi6 MACSW 二进制固件驱动（firmware blob driver，BL61x、BL616CL）的公共支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
DT_HAS_BFLB_WIFI6_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_BFLB_WL80211_SHIM
CONFIG_WIFI_NM_WPA_SUPPLICANT_AP
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_BFLB_WL80211_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_WL80211_SHIM)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_AP)。

<a id="CONFIG_WIFI_BFLB_WIFI6_BA_REORDER_BUF"></a>

## 192.74 `CONFIG_WIFI_BFLB_WIFI6_BA_REORDER_BUF`

**提示（Prompt）**：每个块确认协定的重排序缓冲区深度（Block Ack reorder buffer depth per agreement）

**说明（Help）**

每个接收块确认重排序窗口（RX Block Ack reorder window）中的 MPDU 槽位数量。更深的缓冲区可在清空（flush）之前容忍更多乱序帧，但会消耗更多 WRAM；每个槽位保存一个 RX 描述符（descriptor）和 AMSDU 子帧（subframe）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
16 if CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK
12 if CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE
4
```

**取值范围（Ranges）**

```text
[4, 64]
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK)、[`CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE)。

<a id="CONFIG_WIFI_BFLB_WIFI6_BA_RX"></a>

## 192.75 `CONFIG_WIFI_BFLB_WIFI6_BA_RX`

**提示（Prompt）**：接收块确认协定数量（RX Block Ack agreements）

**说明（Help）**

与接入点（AP）协商的最大并发接收块确认会话数（RX Block Ack sessions）。更大的值允许并行的聚合数据流（aggregated streams），代价是额外的重排序缓冲区（reorder buffer）内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4 if CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK
2
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK)。

<a id="CONFIG_WIFI_BFLB_WIFI6_DEFAULT_COUNTRY"></a>

## 192.76 `CONFIG_WIFI_BFLB_WIFI6_DEFAULT_COUNTRY`

**提示（Prompt）**：默认监管国家／地区代码（regulatory country code）

**说明（Help）**

启动时用于射频校准（RF calibration）和 MAC 信道配置的 ISO/IEC 3166-1 两字母国家／地区代码（alpha-2 country code）。它必须与 `WL80211_COUNTRY_LIST` 表中的某个条目匹配。可在运行时通过 `wifi reg_domain` shell 命令更改。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
"US"
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK"></a>

## 192.77 `CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK`

**提示（Prompt）**：确认增强变体（ack）

**说明（Help）**

增强型块确认（Block Ack）和 A-MPDU 聚合（aggregation）变体。与 `default` 相比，它增加 BA 发送／接收协定数量（TX/RX agreement counts）和重排序缓冲区深度，从而提高大量帧聚合链路上的吞吐量。RAM 用量高于 `default`，但低于 `bridge`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT>
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动 → MACSW 固件变体（firmware variant）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT)。

<a id="CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE"></a>

## 192.78 `CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE`

**提示（Prompt）**：桥接变体（bridge）

**说明（Help）**

针对站点与接入点同时桥接（STA+AP bridging）的高吞吐量调优：64 个 TX1 描述符（相比之下原值为 32）、8K AMSDU（原值为 4K）、12 窗口块确认（block ack）和重排序缓冲区。与 `default` 相比，RAM 用量增加约 14 KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT>
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动 → MACSW 固件变体（firmware variant）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT)。

<a id="CONFIG_WIFI_BFLB_WIFI6_MACSW_COEX"></a>

## 192.79 `CONFIG_WIFI_BFLB_WIFI6_MACSW_COEX`

**提示（Prompt）**：共存变体（coex）

**说明（Help）**

在 `default` 固件基础上添加旧式 `coex_init`／`coex_event`／`coexist_event_*` 钩子 API（hook API），供厂商的 `components/wireless/coex/` 组件使用，以通过 TDMA 或 PTI 模式与 Thread／Zigbee 或 BR/EDR 进行仲裁（arbitration）。标准低功耗蓝牙（BLE）共存不需要此变体，`default` 变体内置的 PTA 已能处理该需求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT>
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动 → MACSW 固件变体（firmware variant）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT)。

<a id="CONFIG_WIFI_BFLB_WIFI6_MACSW_DEFAULT"></a>

## 192.80 `CONFIG_WIFI_BFLB_WIFI6_MACSW_DEFAULT`

**提示（Prompt）**：默认变体（default）

**说明（Help）**

适用于站点（STA）和轻量接入点（AP）使用场景的均衡配置。包含内置的数据包流量仲裁器（Packet Traffic Arbiter，PTA）共存管理器，在硬件层处理 BLE／BT 共存，并可直接与默认 BLE 控制器二进制固件（controller blob）配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT>
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动 → MACSW 固件变体（firmware variant）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT)。

<a id="CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT"></a>

## 192.81 `CONFIG_WIFI_BFLB_WIFI6_MACSW_VARIANT`

**提示（Prompt）**：MACSW 固件变体（firmware variant）

**说明（Help）**

选择 MACSW 下层 MAC 二进制固件变体（lower-MAC firmware blob variant）。所有变体使用相同的主机 API，仅编译时调优参数不同，例如 TX/RX 队列深度、AMSDU 大小和共存钩子（coex hooks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_BFLB_WIFI6_MACSW_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_BFLB_WIFI6_MACSW_DEFAULT
CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE
CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK
CONFIG_WIFI_BFLB_WIFI6_MACSW_COEX
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_BFLB_WIFI6_MACSW_DEFAULT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_DEFAULT)、[`CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_BRIDGE)、[`CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_ACK)、[`CONFIG_WIFI_BFLB_WIFI6_MACSW_COEX`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI6_MACSW_COEX)。

<a id="CONFIG_WIFI_BFLB_WIFI6_TASK_PRIORITY"></a>

## 192.82 `CONFIG_WIFI_BFLB_WIFI6_TASK_PRIORITY`

**提示（Prompt）**：Wi-Fi 任务（task）优先级

**说明（Help）**

Wi-Fi MACSW 事件循环（event loop）的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI6_TASK_STACK_SIZE"></a>

## 192.83 `CONFIG_WIFI_BFLB_WIFI6_TASK_STACK_SIZE`

**提示（Prompt）**：Wi-Fi 任务（task）栈大小

**说明（Help）**

Wi-Fi MACSW 任务线程（task thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI6_TX_MAX_PENDING"></a>

## 192.84 `CONFIG_WIFI_BFLB_WIFI6_TX_MAX_PENDING`

**提示（Prompt）**：最大在途发送数据包数（in-flight TX packets）

**说明（Help）**

限制同时排入固件发送路径（TX path）队列的数据包数量。达到此限制后，驱动在 `send()` 中阻塞，对 TCP 协议栈施加背压（backpressure），防止大批量传输期间耗尽 WRAM 堆（heap）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_BFLB_WIFI6_WRAM_HEAP_SIZE"></a>

## 192.85 `CONFIG_WIFI_BFLB_WIFI6_WRAM_HEAP_SIZE`

**提示（Prompt）**：WRAM 发送堆（TX heap）大小，单位为字节

**说明（Help）**

`wl80211_platform_malloc_wram()` 的堆大小。为确保 DMA 一致性（coherency），在不经过缓存的 WRAM 中分配。4 KB 可容纳两个并发的在途发送缓冲区（in-flight TX buffers）；单个完整 MTU 帧至少需要约 2 KB。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_BFLB && CONFIG_WIFI
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/wifi/bflb/wifi6/Kconfig:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/bflb/wifi6/Kconfig#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 博流（Bouffalo Lab）Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32"></a>

## 192.86 `CONFIG_WIFI_ESP32`

**提示（Prompt）**：ESP32 片上系统（SoC）Wi-Fi 支持

**说明（Help）**

启用 ESP32 SoC 的 Wi-Fi 支持。由于网络协议栈尚未考虑对称多处理（SMP），因此仅支持单核模式（single core mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_WIFI_ENABLED && (CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS || CONFIG_BUILD_ONLY_NO_BLOBS) && !CONFIG_SMP && CONFIG_WIFI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_THREAD_CUSTOM_DATA
CONFIG_EVENTS
CONFIG_NET_L2_WIFI_MGMT
CONFIG_NET_L2_ETHERNET
CONFIG_NET_L2_ETHERNET_MGMT
CONFIG_WIFI_USE_NATIVE_NETWORKING
CONFIG_MBEDTLS
CONFIG_PSA_CRYPTO
CONFIG_THREAD_STACK_INFO
CONFIG_DYNAMIC_THREAD
CONFIG_DYNAMIC_THREAD_ALLOC
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_THREAD_CUSTOM_DATA`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_CUSTOM_DATA)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_NET_L2_WIFI_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_L2_ETHERNET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_MGMT)、[`CONFIG_WIFI_USE_NATIVE_NETWORKING`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USE_NATIVE_NETWORKING)、[`CONFIG_MBEDTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS)、[`CONFIG_PSA_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_DYNAMIC_THREAD_ALLOC`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD_ALLOC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_ESPRESSIF_MODULE_BLOBS`。

<a id="CONFIG_WIFI_ESP32_MESH"></a>

## 192.87 `CONFIG_WIFI_ESP32_MESH`

**提示（Prompt）**：ESP Wi-Fi 网状网络（mesh）支持

**说明（Help）**

启用自组织多跳 Wi-Fi 网状网络协议栈（self-organizing multi-hop Wi-Fi mesh network stack）。每个节点同时以接入点（AP）和站点（station）模式运行 Wi-Fi：站点接口向上连接父节点，软件接入点（softAP）接口接受子节点。只有根节点（root node）可访问外部 IP 网络。ESP32-C2 和 ESP32-H2 不支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32C61) && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_ESP32_WIFI_SOFTAP_SUPPORT
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:501`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L501)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_ESP32_WIFI_SOFTAP_SUPPORT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SOFTAP_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32C61`。

<a id="CONFIG_WIFI_ESP32_MESH_ALLOW_ROOT_CONFLICTS"></a>

## 192.88 `CONFIG_WIFI_ESP32_MESH_ALLOW_ROOT_CONFLICTS`

**提示（Prompt）**：允许一个网状网络（mesh network）中存在多个根节点（roots）

**说明（Help）**

允许同一个网状网络（mesh network）中多个根节点（root）共存。禁用时，检测到其他根节点的根节点会让出根角色，并以子节点身份重新加入树，因此同时启动的节点最终仍会收敛到单个根节点。仅与自动角色（auto role）有关。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:599`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L599)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32_MESH_ASSOC_EXPIRE"></a>

## 192.89 `CONFIG_WIFI_ESP32_MESH_ASSOC_EXPIRE`

**提示（Prompt）**：空闲子节点关联过期时间（Idle child association expiry），单位为秒

**说明（Help）**

节点在没有流量的情况下保留子节点关联（child association）多久才将其释放。子节点更换父节点后，原父节点会在过期前保留已经失效的关联，继续占用一个子节点槽位；当每个节点的连接数较少时，过长的过期时间可能阻碍树结构收敛。10 秒与禁用网状网络节能（mesh power save）时使用的值一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 60]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:569`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L569)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32_MESH_EVENT_HANDLERS"></a>

## 192.90 `CONFIG_WIFI_ESP32_MESH_EVENT_HANDLERS`

**提示（Prompt）**：已注册网状网络事件处理程序（mesh event handlers）的最大数量

**说明（Help）**

用于分发 Wi-Fi 和网状网络（mesh）事件的事件处理程序表（event handler table）大小。它必须同时容纳应用处理程序和 mesh 协议栈内部注册的处理程序，后者的数量无法由应用统计；超出此限制后注册的处理程序会被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
12
```

**取值范围（Ranges）**

```text
[4, 32]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:550`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L550)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32_MESH_FORCE_CHILD"></a>

## 192.91 `CONFIG_WIFI_ESP32_MESH_FORCE_CHILD`

**提示（Prompt）**：强制此节点保持为子节点（child），永不成为根节点（root）

**说明（Help）**

防止此节点成为根节点（root），使其始终作为子节点（child）连接到另一个节点。适用于使用固定根节点（fixed root）的场景，也适用于所有开发板都能接收到路由器信号的台架环境；否则每块板可能各自选举自己为根节点，而无法形成一棵树。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESP32_MESH_ROLE>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:644`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L644)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持 → 此节点的网状网络角色（Mesh role）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH_ROLE`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH_ROLE)。

<a id="CONFIG_WIFI_ESP32_MESH_FORCE_ROOT"></a>

## 192.92 `CONFIG_WIFI_ESP32_MESH_FORCE_ROOT`

**提示（Prompt）**：强制此节点作为根节点（fixed root，固定根节点）

**说明（Help）**

将此节点指定为网状网络（mesh）的固定根节点（fixed root）。它不参与选举，始终位于树的顶部。配置路由器后，它保留自组织行为（self-organized behavior），以关联路由器，并通过重连维持该上行链路；未配置路由器时则停止搜索父节点，因为此时没有可查找的父节点，且搜索会干扰其软件接入点（softAP）。子节点自动接入仍需要路由器：完全没有路由器的 mesh 必须为每个子节点显式指定父节点，而本驱动不会执行此操作。其他节点必须构建为固定子节点（`WIFI_ESP32_MESH_FORCE_CHILD`），使其接受指定的根节点，而不是自行选举。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESP32_MESH_ROLE>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:629`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L629)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持 → 此节点的网状网络角色（Mesh role）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH_ROLE`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH_ROLE)。

<a id="CONFIG_WIFI_ESP32_MESH_IP"></a>

## 192.93 `CONFIG_WIFI_ESP32_MESH_IP`

**提示（Prompt）**：通过网状网络承载 IP（IP over mesh）

**说明（Help）**

构建通过网状网络承载以太网（Ethernet-over-mesh）的网络接口，使 IP 在 mesh 传输之上运行。该接口以以太网帧作为 mesh 载荷（payload），使 Zephyr 网络协议栈的地址、DHCP、NAT 和套接字（sockets）功能无需修改即可在 mesh 上工作。未启用此选项时，mesh 仅通过 `esp_wifi_mesh_send()`／`esp_wifi_mesh_recv()` 承载应用数据。IP 层策略（地址、DHCP 服务器、NAT、路由）由应用负责，驱动仅提供传输接口（transport interface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_ETHERNET
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:654`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L654)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)。

<a id="CONFIG_WIFI_ESP32_MESH_MAX_CONNECTIONS"></a>

## 192.94 `CONFIG_WIFI_ESP32_MESH_MAX_CONNECTIONS`

**提示（Prompt）**：每个节点最大直接子连接数的缓冲区上限（buffer ceiling）

**说明（Help）**

每个节点子节点扇出（child fan-out）的编译时上限：它在构建时决定路由表缓冲区（routing-table buffers）的大小，并限制 `esp_wifi_mesh_set_config()` 接受的 `max_connections` 字段，后者才是运行时实际采用的值。如果从未设置配置，`esp_wifi_mesh_start()` 会将 `max_connections` 默认设为此上限。此限制约束每个节点的扇出，而非整个网络的规模；超出此数量的节点会连接到下一层，因此网络仍可通过扩展树来增长。值越大，树越扁平，但每个节点需要更多 RAM 来容纳额外链路；值越小，树越深。每个直接链路都从系统堆（system heap）消耗 Wi-Fi 接收／发送缓冲区（RX/TX buffers），因此充当根节点或多个子节点中间枢纽的节点比叶节点需要更多堆空间。有关 `CONFIG_HEAP_MEM_POOL_SIZE` 的指导，参见示例的 `prj.conf`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:531`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L531)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32_MESH_MAX_LAYER"></a>

## 192.95 `CONFIG_WIFI_ESP32_MESH_MAX_LAYER`

**提示（Prompt）**：最大网状网络层数（树深度，tree depth）的缓冲区上限

**说明（Help）**

网状网络（mesh）树深度／层数（layers）的编译时上限：它在构建时决定路由表缓冲区（routing-table buffers）的大小，并限制 `esp_wifi_mesh_set_config()` 接受的 `num_layers` 字段，后者才是运行时实际采用的值。如果从未设置配置，`esp_wifi_mesh_start()` 会将 `num_layers` 默认设为此上限。根节点位于第 1 层，其直接子节点位于第 2 层，以此类推；若节点接入后所在层级超过运行时的 `num_layers`，接入会被拒绝。根节点上的路由表按整个子网络的规模分配，因此原文给出的最大节点数近似为 `MAX_LAYER * MAX_CONNECTIONS + 1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
25
```

**取值范围（Ranges）**

```text
[1, 25]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:516`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L516)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32_MESH_ROLE"></a>

## 192.96 `CONFIG_WIFI_ESP32_MESH_ROLE`

**提示（Prompt）**：此节点的网状网络角色（Mesh role）

**说明（Help）**

选择此节点在网状网络树（mesh tree）中确定自身位置的方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_ESP32_MESH_ROLE_AUTO
```

**可选项（Choices）**

```text
CONFIG_WIFI_ESP32_MESH_ROLE_AUTO
CONFIG_WIFI_ESP32_MESH_FORCE_ROOT
CONFIG_WIFI_ESP32_MESH_FORCE_CHILD
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:616`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L616)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_ESP32_MESH_ROLE_AUTO`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH_ROLE_AUTO)、[`CONFIG_WIFI_ESP32_MESH_FORCE_ROOT`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH_FORCE_ROOT)、[`CONFIG_WIFI_ESP32_MESH_FORCE_CHILD`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH_FORCE_CHILD)。

<a id="CONFIG_WIFI_ESP32_MESH_ROLE_AUTO"></a>

## 192.97 `CONFIG_WIFI_ESP32_MESH_ROLE_AUTO`

**提示（Prompt）**：自组织（Self-organized）：依据路由器可达性选举根节点

**说明（Help）**

默认的自组织行为（self-organized behavior）：节点进行扫描；如果能够到达路由器，就投票争取成为根节点（root），否则作为子节点（child）连接到范围内的一个 mesh 节点。选举需要路由器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_ESP32_MESH_ROLE>
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:622`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L622)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持 → 此节点的网状网络角色（Mesh role）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH_ROLE`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH_ROLE)。

<a id="CONFIG_WIFI_ESP32_MESH_SEND_BLOCK_TIME_MS"></a>

## 192.98 `CONFIG_WIFI_ESP32_MESH_SEND_BLOCK_TIME_MS`

**提示（Prompt）**：网状网络发送阻塞时间（Mesh send block time），单位为毫秒

**说明（Help）**

发生拥塞（congestion）时，`esp_wifi_mesh_send()` 在返回失败之前阻塞等待缓冲区空间的时长。较长时间允许突发流量逐步发送完成，避免丢帧；设为 `0` 时，没有可用缓冲区就立即失败。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
30000
```

**取值范围（Ranges）**

```text
[0, 60000]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:607`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L607)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32_MESH_START_TIMEOUT"></a>

## 192.99 `CONFIG_WIFI_ESP32_MESH_START_TIMEOUT`

**提示（Prompt）**：网状网络启动等待超时（Mesh-start wait timeout），单位为 ms

**说明（Help）**

`esp_wifi_mesh_start()` 在继续重新投递初始站点启动事件（station-start event）之前，等待 mesh 协议栈报告 `MESH_EVENT_STARTED` 的时间。事件到达时即结束等待；此值只是放弃等待并继续执行前的时间上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:560`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L560)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<a id="CONFIG_WIFI_ESP32_MESH_VOTE_PERCENTAGE"></a>

## 192.100 `CONFIG_WIFI_ESP32_MESH_VOTE_PERCENTAGE`

**提示（Prompt）**：根节点选举投票百分比阈值（Root election vote percentage threshold）

**说明（Help）**

自组织选举（self-organized election）中候选节点获准成为根节点（root）所需的票数百分比，以整数百分比表示，`100` 表示全票通过。仅与自动角色（auto role）有关。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_WIFI_ESP32_MESH && CONFIG_WIFI_ESP32 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`drivers/wifi/esp32/Kconfig.esp32:590`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/Kconfig.esp32#L590)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → ESP32 片上系统（SoC）Wi-Fi 支持 → ESP Wi-Fi 网状网络（mesh）支持

**配置项引用（Symbol References）**：[`CONFIG_WIFI_ESP32_MESH`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32_MESH)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)。

<!-- kconfig-navigation -->

[上一章](P191_drivers_wifi_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P193_drivers_wifi_配置项参考_6.md)
