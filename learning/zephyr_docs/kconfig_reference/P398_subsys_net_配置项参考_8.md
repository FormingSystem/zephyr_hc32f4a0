---
id: learning.zephyr-docs.kconfig-reference.page-398
title: "`subsys/net`配置项参考（8/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第398章\_`subsys/net`配置项参考（8/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER"></a>

## 398.1 `CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER`

**提示（Prompt）**：在 DHCPv4 请求中发送供应商类别标识符（Vendor class identifier）

**说明（Help）**

启用后，网络协议栈会在 DHCPv4 请求的供应商类别标识符（Vendor class identifier）选项中包含指定字符串。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER_STRING"></a>

## 398.2 `CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER_STRING`

**提示（Prompt）**：供应商类别标识符（Vendor class identifier）

**说明（Help）**

要加入 DHCPv4 请求的供应商类别标识符（Vendor class identifier）选项的字符串。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER && CONFIG_NET_DHCPV4 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv4/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv4/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv4 客户端（Client） → 在 DHCPv4 请求中发送供应商类别标识符（Vendor class identifier）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV4_VENDOR_CLASS_IDENTIFIER)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6"></a>

## 398.3 `CONFIG_NET_DHCPV6`

**提示（Prompt）**：DHCPv6 客户端（Client）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_NET_UDP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)。

<a id="CONFIG_NET_DHCPV6_DECLINE_ON_DAD_FAILURE"></a>

## 398.4 `CONFIG_NET_DHCPV6_DECLINE_ON_DAD_FAILURE`

**提示（Prompt）**：重复地址检测（DAD）失败时发送 DHCPv6 Decline

**说明（Help）**

启用后，如果通过 DHCPv6 分配的地址未通过重复地址检测（Duplicate Address Detection，DAD），客户端会向服务器发送 Decline 报文（RFC 8415 第 18.2.8 节），移除发生冲突的地址，并重新开始协商。禁用时（默认行为），忽略 DHCPv6 地址的 DAD 失败，与此前的行为一致。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_DAD && CONFIG_NET_DHCPV6 && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT_EVENT_INFO
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_DAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_DAD)、[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT_EVENT_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_INFO)。

<a id="CONFIG_NET_DHCPV6_DNS_SERVER_VIA_INTERFACE"></a>

## 398.5 `CONFIG_NET_DHCPV6_DNS_SERVER_VIA_INTERFACE`

**提示（Prompt）**：将 DNS 服务器限定到对应的网络接口（Network interface）

**说明（Help）**

启用后，如果系统有多个网络接口且各接口均启用了 DHCP，则从某个接口收到的 DNS 服务器地址只分配给该接口。禁用时，执行 DNS 查询可以通过任意接口访问所有已配置的 DNS 服务器。例如，Wi-Fi 接口通过 DHCPv6 选项收到 DNS 服务器 `2001:db8::1:53`，以太网（Ethernet）接口收到 `2001:db8::2:53`。启用本选项后，DNS 解析器（Resolver）通过 Wi-Fi 接口发送查询时使用 `2001:db8::1:53`，通过以太网接口发送查询时使用 `2001:db8::2:53`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → 使用 DNS 递归名称服务器选项（DNS Recursive Name Server option）配置 DNS 解析器

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6_DUID_MAX_LEN"></a>

## 398.6 `CONFIG_NET_DHCPV6_DUID_MAX_LEN`

**提示（Prompt）**：DUID 最大长度（不含类型代码，Type code）

**说明（Help）**

设置 DHCP 唯一标识符（DHCP Unique Identifier，DUID）可使用的字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
22
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE"></a>

## 398.7 `CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DHCPv6 客户端日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_DHCPV6 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_DHCPV6_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_DHCPV6_LOG_LEVEL_OFF
CONFIG_NET_DHCPV6_LOG_LEVEL_ERR
CONFIG_NET_DHCPV6_LOG_LEVEL_WRN
CONFIG_NET_DHCPV6_LOG_LEVEL_INF
CONFIG_NET_DHCPV6_LOG_LEVEL_DBG
CONFIG_NET_DHCPV6_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DHCPV6_LOG_LEVEL_DEFAULT`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_DHCPV6_LOG_LEVEL_OFF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_OFF)、[`CONFIG_NET_DHCPV6_LOG_LEVEL_ERR`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_ERR)、[`CONFIG_NET_DHCPV6_LOG_LEVEL_WRN`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_WRN)、[`CONFIG_NET_DHCPV6_LOG_LEVEL_INF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_INF)、[`CONFIG_NET_DHCPV6_LOG_LEVEL_DBG`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_DHCPV6_LOG_LEVEL_DBG"></a>

## 398.8 `CONFIG_NET_DHCPV6_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_LOG_LEVEL_DEFAULT"></a>

## 398.9 `CONFIG_NET_DHCPV6_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_LOG_LEVEL_ERR"></a>

## 398.10 `CONFIG_NET_DHCPV6_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_LOG_LEVEL_INF"></a>

## 398.11 `CONFIG_NET_DHCPV6_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_LOG_LEVEL_OFF"></a>

## 398.12 `CONFIG_NET_DHCPV6_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_LOG_LEVEL_WRN"></a>

## 398.13 `CONFIG_NET_DHCPV6_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 客户端日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_MAX_DOWNSTREAM"></a>

## 398.14 `CONFIG_NET_DHCPV6_MAX_DOWNSTREAM`

**提示（Prompt）**：前缀委派（Prefix delegation）允许的最大下游接口数

**说明（Help）**

请求路由器（Requesting router）可将获委派的前缀（IA_PD）进一步划分并分配到的下游接口的最大数量。`net_dhcpv6_params` 中列出的每个下游接口，都会分得从该委派前缀中划出的一个独立 `/64` 前缀。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6 && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS"></a>

## 398.15 `CONFIG_NET_DHCPV6_OPTION_DNS_ADDRESS`

**提示（Prompt）**：使用 DNS 递归名称服务器选项（DNS Recursive Name Server option）配置 DNS 解析器

**说明（Help）**

启用后，DHCPv6 客户端会向服务器请求 DNS 递归名称服务器选项（DNS Recursive Name Server option）；如果服务器提供该选项，则使用获取的信息配置 DNS 解析器（Resolver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6_SEND_RELEASE_ON_STOP"></a>

## 398.16 `CONFIG_NET_DHCPV6_SEND_RELEASE_ON_STOP`

**提示（Prompt）**：客户端停止时发送 DHCPv6 Release

**说明（Help）**

启用后，如果 DHCPv6 客户端停止时仍持有租约（Lease），就向服务器发送 Release 报文（RFC 8415 第 18.2.7 节），让服务器立即释放已分配的地址或前缀。禁用时（默认行为），直接放弃租约，等待服务器端的租约到期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6 && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6_SERVER"></a>

## 398.17 `CONFIG_NET_DHCPV6_SERVER`

**提示（Prompt）**：DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation）

**说明（Help）**

启用 DHCPv6 服务器，支持 RFC 8415 规定的 IPv6 非临时地址分配（IA_NA）和前缀委派（IA_PD）。服务器从配置的地址池或前缀池中，向请求的客户端或路由器分配地址或前缀。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_NET_UDP && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)。

<a id="CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE"></a>

## 398.18 `CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DHCPv6 服务器日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_DHCPV6_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_OFF
CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_ERR
CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_WRN
CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_INF
CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DBG
CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_DHCPV6_SERVER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DEFAULT`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_OFF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_OFF)、[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_ERR`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_ERR)、[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_WRN`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_WRN)、[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_INF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_INF)、[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DBG`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DBG"></a>

## 398.19 `CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation） → DHCPv6 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DEFAULT"></a>

## 398.20 `CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation） → DHCPv6 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_ERR"></a>

## 398.21 `CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation） → DHCPv6 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_INF"></a>

## 398.22 `CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation） → DHCPv6 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_OFF"></a>

## 398.23 `CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation） → DHCPv6 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_WRN"></a>

## 398.24 `CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation） → DHCPv6 服务器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DHCPV6_SERVER_MAX_LEASES"></a>

## 398.25 `CONFIG_NET_DHCPV6_SERVER_MAX_LEASES`

**提示（Prompt）**：并发 DHCPv6 租约（Lease）的最大数量

**说明（Help）**

服务器可同时跟踪的客户端绑定（Client binding）的最大数量，使用静态分配的存储空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6_SERVER_PREFERRED_LIFETIME"></a>

## 398.26 `CONFIG_NET_DHCPV6_SERVER_PREFERRED_LIFETIME`

**提示（Prompt）**：租约的默认首选生存期（Preferred lifetime，秒）

**说明（Help）**

未通过 `net_dhcpv6_server_params` 覆盖时，为租出的地址或前缀通告的默认首选生存期（Preferred lifetime）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
43200
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DHCPV6_SERVER_VALID_LIFETIME"></a>

## 398.27 `CONFIG_NET_DHCPV6_SERVER_VALID_LIFETIME`

**提示（Prompt）**：租约的默认有效生存期（Valid lifetime，秒）

**说明（Help）**

未通过 `net_dhcpv6_server_params` 覆盖时，为租出的地址或前缀通告的默认有效生存期（Valid lifetime）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DHCPV6_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
86400
```

**定义位置（Location）**：[`subsys/net/lib/dhcpv6/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dhcpv6/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → DHCPv6 服务器（地址分配与前缀委派，Address assignment and prefix delegation）

**配置项引用（Symbol References）**：[`CONFIG_NET_DHCPV6_SERVER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DISABLE_ICMP_DESTINATION_UNREACHABLE"></a>

## 398.28 `CONFIG_NET_DISABLE_ICMP_DESTINATION_UNREACHABLE`

**提示（Prompt）**：禁用 ICMP 目的地不可达错误（Destination unreachable error）

**说明（Help）**

当未处于监听状态的端口收到数据包时，不生成 ICMP 目的地不可达错误（Destination unreachable error）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:1052`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L1052)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DSA"></a>

## 398.29 `CONFIG_NET_DSA`

**提示（Prompt）**：分布式交换架构支持（Distributed Switch Architecture）

**说明（Help）**

启用分布式交换架构（Distributed Switch Architecture，DSA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/dsa/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/dsa/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_DSA_LOG_LEVEL_CHOICE"></a>

## 398.30 `CONFIG_NET_DSA_LOG_LEVEL_CHOICE`

**提示（Prompt）**：分布式交换架构（DSA）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_DSA && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_DSA_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_DSA_LOG_LEVEL_OFF
CONFIG_NET_DSA_LOG_LEVEL_ERR
CONFIG_NET_DSA_LOG_LEVEL_WRN
CONFIG_NET_DSA_LOG_LEVEL_INF
CONFIG_NET_DSA_LOG_LEVEL_DBG
CONFIG_NET_DSA_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_DSA`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_DSA_LOG_LEVEL_DEFAULT`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_DSA_LOG_LEVEL_OFF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_OFF)、[`CONFIG_NET_DSA_LOG_LEVEL_ERR`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_ERR)、[`CONFIG_NET_DSA_LOG_LEVEL_WRN`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_WRN)、[`CONFIG_NET_DSA_LOG_LEVEL_INF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_INF)、[`CONFIG_NET_DSA_LOG_LEVEL_DBG`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_DSA_LOG_LEVEL_DBG"></a>

## 398.31 `CONFIG_NET_DSA_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DSA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture） → 分布式交换架构（DSA）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DSA_LOG_LEVEL_DEFAULT"></a>

## 398.32 `CONFIG_NET_DSA_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DSA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture） → 分布式交换架构（DSA）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DSA_LOG_LEVEL_ERR"></a>

## 398.33 `CONFIG_NET_DSA_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DSA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture） → 分布式交换架构（DSA）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DSA_LOG_LEVEL_INF"></a>

## 398.34 `CONFIG_NET_DSA_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DSA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture） → 分布式交换架构（DSA）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DSA_LOG_LEVEL_OFF"></a>

## 398.35 `CONFIG_NET_DSA_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DSA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture） → 分布式交换架构（DSA）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_DSA_LOG_LEVEL_WRN"></a>

## 398.36 `CONFIG_NET_DSA_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_DSA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 分布式交换架构支持（Distributed Switch Architecture） → 分布式交换架构（DSA）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_DSA_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DSA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ETHERNET_BRIDGE"></a>

## 398.37 `CONFIG_NET_ETHERNET_BRIDGE`

**提示（Prompt）**：以太网桥接（Ethernet bridging）支持

**说明（Help）**

启用以太网桥接（Ethernet bridging），使数据包能够在注册到同一网桥的接口之间透明转发。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_PROMISCUOUS_MODE
CONFIG_NET_L2_VIRTUAL
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PROMISCUOUS_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PROMISCUOUS_MODE)、[`CONFIG_NET_L2_VIRTUAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_VIRTUAL)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_COUNT"></a>

## 398.38 `CONFIG_NET_ETHERNET_BRIDGE_COUNT`

**提示（Prompt）**：网桥接口（Bridge interface）的最大数量

**说明（Help）**

要创建的网桥接口（Bridge interface）数量。每个网桥接口可以桥接两个或更多以太网接口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_ETH_INTERFACE_COUNT"></a>

## 398.39 `CONFIG_NET_ETHERNET_BRIDGE_ETH_INTERFACE_COUNT`

**提示（Prompt）**：共同桥接的以太网接口的最大数量

**说明（Help）**

每个网桥接口可以桥接的以太网（Ethernet）接口数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 32]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_FDB"></a>

## 398.40 `CONFIG_NET_ETHERNET_BRIDGE_FDB`

**提示（Prompt）**：转发数据库（Forwarding Database，FDB）表支持

**说明（Help）**

启用转发数据库（Forwarding Database，FDB）表支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_FDB_MAX_ENTRIES"></a>

## 398.41 `CONFIG_NET_ETHERNET_BRIDGE_FDB_MAX_ENTRIES`

**提示（Prompt）**：转发数据库（FDB）表项的最大数量

**说明（Help）**

支持的转发数据库（Forwarding Database，FDB）表项数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ETHERNET_BRIDGE_FDB && CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 转发数据库（Forwarding Database，FDB）表支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_FDB`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_FDB)、[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE"></a>

## 398.42 `CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：以太网桥接（Ethernet bridging）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_OFF
CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_ERR
CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_WRN
CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_INF
CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DBG
CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DEFAULT`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_OFF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_OFF)、[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_ERR`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_ERR)、[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_WRN`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_WRN)、[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_INF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_INF)、[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DBG`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DBG"></a>

## 398.43 `CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 以太网桥接（Ethernet bridging）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DEFAULT"></a>

## 398.44 `CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 以太网桥接（Ethernet bridging）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_ERR"></a>

## 398.45 `CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 以太网桥接（Ethernet bridging）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_INF"></a>

## 398.46 `CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 以太网桥接（Ethernet bridging）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_OFF"></a>

## 398.47 `CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 以太网桥接（Ethernet bridging）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_WRN"></a>

## 398.48 `CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 以太网桥接（Ethernet bridging）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_MAC"></a>

## 398.49 `CONFIG_NET_ETHERNET_BRIDGE_MAC`

**提示（Prompt）**：网桥接口的 MAC 地址来源（MAC address source）

**说明（Help）**

选择网桥接口的 MAC 地址，即链路地址（Link address），的分配方式。网桥接口可以拥有 IP 地址，并作为流量的接收终点或发送起点，因此需要 MAC 地址。如需完全自定义地址，应用也可在网桥接口处于关闭（down）状态时，对它调用 `net_if_set_link_addr()`；网桥接口不会自动启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_ETHERNET_BRIDGE_RANDOM_MAC
```

**可选项（Choices）**

```text
CONFIG_NET_ETHERNET_BRIDGE_RANDOM_MAC
CONFIG_NET_ETHERNET_BRIDGE_UNIQUE_MAC
CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_ETHERNET_BRIDGE_RANDOM_MAC`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_RANDOM_MAC)、[`CONFIG_NET_ETHERNET_BRIDGE_UNIQUE_MAC`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_UNIQUE_MAC)、[`CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_MAC_PREFIX"></a>

## 398.50 `CONFIG_NET_ETHERNET_BRIDGE_MAC_PREFIX`

**提示（Prompt）**：网桥 MAC 地址前缀（MAC address prefix）

**说明（Help）**

用于网桥接口的 MAC 地址前缀，由五个以冒号分隔的八位组（Octet）组成。网桥索引用作最后一个八位组。例如，前缀为 `02:00:00:00:00` 时，bridge0 的地址为 `02:00:00:00:00:00`，bridge1 的地址为 `02:00:00:00:00:01`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC && CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"02:00:00:00:00"
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC)、[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC"></a>

## 398.51 `CONFIG_NET_ETHERNET_BRIDGE_PREFIX_MAC`

**提示（Prompt）**：通过配置的前缀生成稳定 MAC 地址（Stable MAC address）

**说明（Help）**

在配置的五个八位组的 MAC 地址前缀后附加网桥索引，以生成稳定的 MAC 地址。重启后地址不变，因此对端缓存仍然有效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_MAC>
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 网桥接口的 MAC 地址来源（MAC address source）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_MAC`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_MAC)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_RANDOM_MAC"></a>

## 398.52 `CONFIG_NET_ETHERNET_BRIDGE_RANDOM_MAC`

**提示（Prompt）**：随机 MAC 地址（Random MAC Address）

**说明（Help）**

为每个网桥接口分配一个随机的本地管理 MAC 地址（Locally administered MAC address）。每次启动都会生成新地址，因此设备重启后，对端针对该网桥的 ARP 缓存或邻居缓存（Neighbor cache）会失效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_ETHERNET_BRIDGE_MAC>
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 网桥接口的 MAC 地址来源（MAC address source）

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE_MAC`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_MAC)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_SHELL"></a>

## 398.53 `CONFIG_NET_ETHERNET_BRIDGE_SHELL`

**提示（Prompt）**：以太网桥接管理命令行（Ethernet bridging management shell）

**说明（Help）**

启用用于交互式管理网桥配置的命令行工具（Shell utility）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SHELL
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SHELL)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_TXRX_DEBUG"></a>

## 398.54 `CONFIG_NET_ETHERNET_BRIDGE_TXRX_DEBUG`

**提示（Prompt）**：调试网桥接收和发送的数据包（Packet）

**说明（Help）**

启用后，打印接收和发送的网络数据包。这可能产生大量输出，因此默认禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG && CONFIG_NET_ETHERNET_BRIDGE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET_LOG_LEVEL_DBG)、[`CONFIG_NET_ETHERNET_BRIDGE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_ETHERNET_BRIDGE_UNIQUE_MAC"></a>

## 398.55 `CONFIG_NET_ETHERNET_BRIDGE_UNIQUE_MAC`

**提示（Prompt）**：从设备 ID 派生稳定 MAC 地址（Stable MAC address）

**说明（Help）**

从硬件设备 ID 派生稳定的本地管理 MAC 地址（Locally administered MAC address）。重启后地址保持不变，使对端缓存仍然有效。派生过程还混入网桥索引，让不同网桥接口获得不同地址。如果无法获取设备 ID，则回退到随机地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HWINFO && <choice CONFIG_NET_ETHERNET_BRIDGE_MAC>
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/bridge/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/bridge/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 以太网桥接（Ethernet bridging）支持 → 网桥接口的 MAC 地址来源（MAC address source）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_NET_ETHERNET_BRIDGE_MAC`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_ETHERNET_BRIDGE_MAC)。

<a id="CONFIG_NET_ETHERNET_FORWARD_UNRECOGNISED_ETHERTYPE"></a>

## 398.56 `CONFIG_NET_ETHERNET_FORWARD_UNRECOGNISED_ETHERTYPE`

**提示（Prompt）**：将无法识别 EtherType 的帧继续传入网络协议栈

**说明（Help）**

启用后，以太网第二层（Ethernet L2）也会转交帧头中 EtherType 无法识别的帧。默认情况下，此类帧会在 L2 处理时被丢弃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_SOCKETS_PACKET
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_PACKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET)。

<a id="CONFIG_NET_GPTP"></a>

## 398.57 `CONFIG_NET_GPTP`

**提示（Prompt）**：IEEE 802.1AS（广义精确时间协议，gPTP）支持

**说明（Help）**

启用 gPTP 驱动，用于发送和接收 gPTP 数据包，以及处理网络数据包的时间戳（Timestamp）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_PRECISION_TIMING if CONFIG_NET_GPTP_USE_DEFAULT_CLOCK_UPDATE
CONFIG_PTP_CLOCK
CONFIG_NET_L2_PTP_TIMESTAMPING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PRECISION_TIMING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRECISION_TIMING)、[`CONFIG_NET_GPTP_USE_DEFAULT_CLOCK_UPDATE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_USE_DEFAULT_CLOCK_UPDATE)、[`CONFIG_PTP_CLOCK`](P141_drivers_ptp_clock_配置项参考.md#CONFIG_PTP_CLOCK)、[`CONFIG_NET_L2_PTP_TIMESTAMPING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP_TIMESTAMPING)。

<a id="CONFIG_NET_GPTP_ANNOUNCE_RECEIPT_TIMEOUT"></a>

## 398.58 `CONFIG_NET_GPTP_ANNOUNCE_RECEIPT_TIMEOUT`

**提示（Prompt）**：等待的通告间隔（Announce interval）数量

**说明（Help）**

定义连续多少个通告间隔（Announce interval）没有收到 Announce 报文后，就认定主时钟（Master）已停止发送 Announce 报文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_BMCA_PRIORITY1"></a>

## 398.59 `CONFIG_NET_GPTP_BMCA_PRIORITY1`

**提示（Prompt）**：最佳主时钟选择算法（BMCA）的 priority1 值

**说明（Help）**

本地时钟的 `priority1` 属性，用于最佳主时钟选择算法（Best Master Clock selection Algorithm，BMCA），值越小优先级越高。不具备最高主时钟（Grand Master，GM）能力的设备默认值为 255；具备 GM 能力的设备默认值为 248。有关 `priority1` 的详细说明，参见 IEEE 802.1AS 第 8.6.2.1 节。注意：如果系统不具备 GM 能力，则始终使用 255，忽略此设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
248 if CONFIG_NET_GPTP_GM_CAPABLE
255
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_GPTP_GM_CAPABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_GM_CAPABLE)。

<a id="CONFIG_NET_GPTP_BMCA_PRIORITY2"></a>

## 398.60 `CONFIG_NET_GPTP_BMCA_PRIORITY2`

**提示（Prompt）**：最佳主时钟选择算法（BMCA）的 priority2 值

**说明（Help）**

本地时钟的 `priority2` 属性，用于最佳主时钟选择算法（Best Master Clock selection Algorithm，BMCA），值越小优先级越高。默认值为 248。有关 `priority2` 的详细说明，参见 IEEE 802.1AS 第 8.6.2.5 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
248
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_CLOCK_ACCURACY"></a>

## 398.61 `CONFIG_NET_GPTP_CLOCK_ACCURACY`

**提示（Prompt）**：gPTP 时钟精度（Clock accuracy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0xfe
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_GM_CAPABLE"></a>

## 398.62 `CONFIG_NET_GPTP_GM_CAPABLE`

**提示（Prompt）**：IEEE 802.1AS 最高主时钟能力（GrandMaster capability）

**说明（Help）**

启用后，将整个系统标记为具备最高主时钟能力（Grand Master Capable）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_INIT_LOG_ANNOUNCE_ITV"></a>

## 398.63 `CONFIG_NET_GPTP_INIT_LOG_ANNOUNCE_ITV`

**提示（Prompt）**：以 2 为底的对数（Log2）设置初始通告间隔

**说明（Help）**

定义发送 Announce 报文的间隔。配置值按以下公式转换为纳秒：`nanoseconds = (10^9) * 2^(value)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_INIT_LOG_PDELAY_REQ_ITV"></a>

## 398.64 `CONFIG_NET_GPTP_INIT_LOG_PDELAY_REQ_ITV`

**提示（Prompt）**：以 2 为底的对数（Log2）设置初始路径延迟请求间隔

**说明（Help）**

定义发送路径延迟请求（Path Delay Request）的间隔。配置值按以下公式转换为纳秒：`nanoseconds = (10^9) * 2^(value)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_INIT_LOG_SYNC_ITV"></a>

## 398.65 `CONFIG_NET_GPTP_INIT_LOG_SYNC_ITV`

**提示（Prompt）**：以 2 为底的对数（Log2）设置初始同步间隔

**说明（Help）**

定义发送同步（Sync）报文的间隔。配置值按以下公式转换为纳秒：`nanoseconds = (10^9) * 2^(value)`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
-3
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_LOG_LEVEL_CHOICE"></a>

## 398.66 `CONFIG_NET_GPTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：gPTP 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_GPTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_GPTP_LOG_LEVEL_OFF
CONFIG_NET_GPTP_LOG_LEVEL_ERR
CONFIG_NET_GPTP_LOG_LEVEL_WRN
CONFIG_NET_GPTP_LOG_LEVEL_INF
CONFIG_NET_GPTP_LOG_LEVEL_DBG
CONFIG_NET_GPTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_GPTP_LOG_LEVEL_DEFAULT`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_GPTP_LOG_LEVEL_OFF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_OFF)、[`CONFIG_NET_GPTP_LOG_LEVEL_ERR`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_ERR)、[`CONFIG_NET_GPTP_LOG_LEVEL_WRN`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_WRN)、[`CONFIG_NET_GPTP_LOG_LEVEL_INF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_INF)、[`CONFIG_NET_GPTP_LOG_LEVEL_DBG`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_GPTP_LOG_LEVEL_DBG"></a>

## 398.67 `CONFIG_NET_GPTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_GPTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持 → gPTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_GPTP_LOG_LEVEL_DEFAULT"></a>

## 398.68 `CONFIG_NET_GPTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_GPTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持 → gPTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_GPTP_LOG_LEVEL_ERR"></a>

## 398.69 `CONFIG_NET_GPTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_GPTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持 → gPTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_GPTP_LOG_LEVEL_INF"></a>

## 398.70 `CONFIG_NET_GPTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_GPTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持 → gPTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_GPTP_LOG_LEVEL_OFF"></a>

## 398.71 `CONFIG_NET_GPTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_GPTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持 → gPTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_GPTP_LOG_LEVEL_WRN"></a>

## 398.72 `CONFIG_NET_GPTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_GPTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持 → gPTP 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_GPTP_MONITOR_SYNC_STATUS"></a>

## 398.73 `CONFIG_NET_GPTP_MONITOR_SYNC_STATUS`

**提示（Prompt）**：监测实时同步状态（Real-time synchronization status）

**说明（Help）**

监测实时同步状态（Real-time synchronization status），包括同步偏移（Synchronization offset）、频率偏移（Frequency offset）等。启用后会持续打印消息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_NEIGHBOR_PROP_DELAY_THR"></a>

## 398.74 `CONFIG_NET_GPTP_NEIGHBOR_PROP_DELAY_THR`

**提示（Prompt）**：设置邻居传播延迟阈值（Neighbor propagation delay threshold，纳秒）

**说明（Help）**

以纳秒为单位定义邻居传播延迟阈值。如果传播时间超过该阈值，就认为端口不具备参与 IEEE 802.1AS 协议的能力。详见 IEEE 802.1AS 第 11.2.12.6 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
100000
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_NUM_PORTS"></a>

## 398.75 `CONFIG_NET_GPTP_NUM_PORTS`

**提示（Prompt）**：gPTP 端口数量（Number of ports）

**说明（Help）**

配置 gPTP 协议栈使用的端口数量。这里的端口（Port）与网络接口（Network interface）是同一概念。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_PATH_TRACE_ELEMENTS"></a>

## 398.76 `CONFIG_NET_GPTP_PATH_TRACE_ELEMENTS`

**提示（Prompt）**：要跟踪的路径跟踪元素（Path trace element）数量

**说明（Help）**

指定传递 Announce 报文的时间感知系统（Time-aware system）的数量。每个数组元素占用 8 字节。例如，设为 8 时，占用 `8 * 8 = 64` 字节内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_PROBE_CLOCK_SOURCE_ON_DEMAND"></a>

## 398.77 `CONFIG_NET_GPTP_PROBE_CLOCK_SOURCE_ON_DEMAND`

**提示（Prompt）**：按需探测时钟源（Clock source）

**说明（Help）**

当驱动未完整支持 `ClockSourceTime.invoke` 函数时，此项很有用。启用后，仅在实际需要时探测时钟源（Clock source），而不是每个时钟节拍（Tick）都更新。详见 IEEE 802.1AS-2011 第 9.2 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP_GM_CAPABLE && CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持 → IEEE 802.1AS 最高主时钟能力（GrandMaster capability）

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP_GM_CAPABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP_GM_CAPABLE)、[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_STACK_SIZE"></a>

## 398.78 `CONFIG_NET_GPTP_STACK_SIZE`

**提示（Prompt）**：gPTP 线程栈大小（Thread stack size）

**说明（Help）**

设置 gPTP 线程栈的大小，单位为字节。该线程负责处理 gPTP 状态机（State machine），系统中只有一个 gPTP 线程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_STATIC_TIME_RECEIVER"></a>

## 398.79 `CONFIG_NET_GPTP_STATIC_TIME_RECEIVER`

**提示（Prompt）**：静态时间接收端（Static timeReceiver）工作模式

**说明（Help）**

将每个 gPTP 端口作为静态配置的时间接收端（Time receiver）运行，适用于 IEEE 802.1AS 汽车应用配置文件（Automotive profile），即《AVnu Automotive Ethernet AVB Functional and Interoperability Specification》。该配置文件中的网桥采用静态端口角色：发送 Sync 和 Follow_Up，但不发送 Announce，因此最佳主时钟选择算法（BMCA）无法选出端口角色。启用此项后，绕过 BMCA 和全部 Announce 处理，将端口角色固定为时间接收端，即“slave”状态；强制 `asCapable` 为 true，使同步不依赖邻居 Pdelay 测量，因为网桥不必响应 Pdelay 请求；仅根据收到的 Sync 和 Follow_Up 报文校准本地时钟。这对应 linuxptp 的 ptp4l 汽车时间接收端配置：BMCA 为 `noop`，并采用 `clientOnly`、`inhibit_announce`、`asCapable` 为 `true` 和 `ignore_source_id`。即便设置了 `NET_GPTP_GM_CAPABLE`，设备也绝不会成为最高主时钟（Grandmaster），也不会发送 Sync 或 Announce 报文。在标准中，与这种禁用 BMCA 的方式对应的是 IEEE 802.1AS-2020 第 10.3.14 节的外部端口配置（External port configuration），它源自 IEEE 1588-2019 第 17.6.2 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_STATISTICS"></a>

## 398.80 `CONFIG_NET_GPTP_STATISTICS`

**提示（Prompt）**：收集 gPTP 统计信息（Statistics）

**说明（Help）**

需要收集 gPTP 统计信息（Statistics）时启用此项。必要时可在网络命令行（net-shell）中查看这些统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_SYNC_RECEIPT_TIMEOUT"></a>

## 398.81 `CONFIG_NET_GPTP_SYNC_RECEIPT_TIMEOUT`

**提示（Prompt）**：等待的同步间隔（Sync interval）数量

**说明（Help）**

定义连续多少个同步间隔（Sync interval）没有收到同步信息后，就认定主时钟（Master）已停止发送同步信息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_GPTP_USE_DEFAULT_CLOCK_UPDATE"></a>

## 398.82 `CONFIG_NET_GPTP_USE_DEFAULT_CLOCK_UPDATE`

**提示（Prompt）**：使用默认时钟更新函数（Clock update function）

**说明（Help）**

使用默认内部函数更新端口的本地时钟（Local clock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_GPTP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/gptp/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/gptp/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → IEEE 802.1AS（广义精确时间协议，gPTP）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_GPTP`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_GPTP)、[`CONFIG_NET_L2_ETHERNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_HEADERS_ALWAYS_CONTIGUOUS"></a>

## 398.83 `CONFIG_NET_HEADERS_ALWAYS_CONTIGUOUS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

这是一个隐藏选项，使用时务必极其谨慎。上游明确警告：启用该选项后，不接受相关缺陷报告（Bug report）！如果能够百分之百保证报头占用的内存始终连续，该选项可减少网络核心（net core）的栈占用和 ROM 占用。例如，仅使用 IPv4、启用 `NET_BUF_FIXED_DATA_SIZE` 且 `NET_BUF_DATA_SIZE` 为 128 时，可能满足这一条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:859`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L859)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_HOSTNAME"></a>

## 398.84 `CONFIG_NET_HOSTNAME`

**提示（Prompt）**：本设备的主机名（Hostname）

**说明（Help）**

该字符串应为有效的主机名（Hostname）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_HOSTNAME_ENABLE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"zephyr"
```

**定义位置（Location）**：[`subsys/net/Kconfig.hostname:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.hostname#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_ENABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_HOSTNAME_DYNAMIC"></a>

## 398.85 `CONFIG_NET_HOSTNAME_DYNAMIC`

**提示（Prompt）**：允许应用设置主机名（Hostname）

**说明（Help）**

启用 `net_hostname_set()` 函数。`NET_HOSTNAME` 用作默认主机名（Hostname）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_HOSTNAME_UNIQUE_UPDATE && CONFIG_NET_HOSTNAME_ENABLE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/Kconfig.hostname:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.hostname#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_UNIQUE_UPDATE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_UNIQUE_UPDATE)、[`CONFIG_NET_HOSTNAME_ENABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_HOSTNAME_ENABLE"></a>

## 398.86 `CONFIG_NET_HOSTNAME_ENABLE`

**提示（Prompt）**：为设备添加主机名（Hostname）

**说明（Help）**

例如，多播 DNS（mDNS）使用它来响应 `<hostname>.local` 形式的 mDNS 查询。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_POSIX_NETWORKING
```

**定义位置（Location）**：[`subsys/net/Kconfig.hostname:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.hostname#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_POSIX_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_NETWORKING)。

<a id="CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE"></a>

## 398.87 `CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE`

**提示（Prompt）**：主机名配置（Hostname configuration）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_HOSTNAME_ENABLE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_HOSTNAME_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_HOSTNAME_LOG_LEVEL_OFF
CONFIG_NET_HOSTNAME_LOG_LEVEL_ERR
CONFIG_NET_HOSTNAME_LOG_LEVEL_WRN
CONFIG_NET_HOSTNAME_LOG_LEVEL_INF
CONFIG_NET_HOSTNAME_LOG_LEVEL_DBG
CONFIG_NET_HOSTNAME_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_HOSTNAME_ENABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_HOSTNAME_LOG_LEVEL_DEFAULT`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_HOSTNAME_LOG_LEVEL_OFF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_OFF)、[`CONFIG_NET_HOSTNAME_LOG_LEVEL_ERR`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_ERR)、[`CONFIG_NET_HOSTNAME_LOG_LEVEL_WRN`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_WRN)、[`CONFIG_NET_HOSTNAME_LOG_LEVEL_INF`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_INF)、[`CONFIG_NET_HOSTNAME_LOG_LEVEL_DBG`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_HOSTNAME_LOG_LEVEL_DBG"></a>

## 398.88 `CONFIG_NET_HOSTNAME_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 主机名配置（Hostname configuration）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HOSTNAME_LOG_LEVEL_DEFAULT"></a>

## 398.89 `CONFIG_NET_HOSTNAME_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 主机名配置（Hostname configuration）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HOSTNAME_LOG_LEVEL_ERR"></a>

## 398.90 `CONFIG_NET_HOSTNAME_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 主机名配置（Hostname configuration）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HOSTNAME_LOG_LEVEL_INF"></a>

## 398.91 `CONFIG_NET_HOSTNAME_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 主机名配置（Hostname configuration）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HOSTNAME_LOG_LEVEL_OFF"></a>

## 398.92 `CONFIG_NET_HOSTNAME_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 主机名配置（Hostname configuration）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HOSTNAME_LOG_LEVEL_WRN"></a>

## 398.93 `CONFIG_NET_HOSTNAME_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 主机名配置（Hostname configuration）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HOSTNAME_MAX_LEN"></a>

## 398.94 `CONFIG_NET_HOSTNAME_MAX_LEN`

**提示（Prompt）**：允许的最大主机名长度（Hostname length）

**说明（Help）**

设置为主机名（Hostname）分配的字节数。禁用 `NET_HOSTNAME_ENABLE` 时，此项默认为 6，以容纳默认主机名 `zephyr`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
6 if !CONFIG_NET_HOSTNAME_ENABLE
63
```

**定义位置（Location）**：[`subsys/net/Kconfig.hostname:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.hostname#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_HOSTNAME_ENABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_ENABLE)。

<a id="CONFIG_NET_HOSTNAME_UNIQUE"></a>

## 398.95 `CONFIG_NET_HOSTNAME_UNIQUE`

**提示（Prompt）**：生成唯一主机名（Unique hostname）

**说明（Help）**

在 `NET_HOSTNAME` 后附加链路地址（Link address），以创建唯一主机名。例如，启用后主机名可能为 `zephyr00005e005357`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_HOSTNAME_ENABLE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/Kconfig.hostname:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.hostname#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_ENABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_HOSTNAME_UNIQUE_UPDATE"></a>

## 398.96 `CONFIG_NET_HOSTNAME_UNIQUE_UPDATE`

**提示（Prompt）**：更新唯一主机名（Unique hostname）

**说明（Help）**

在链路地址（Link address）改变时更新唯一主机名。此项默认禁用，即仅在启动时设置一次唯一主机名，此后不再更新。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_HOSTNAME_UNIQUE && CONFIG_NET_HOSTNAME_ENABLE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/Kconfig.hostname:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.hostname#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 生成唯一主机名（Unique hostname）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_UNIQUE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_UNIQUE)、[`CONFIG_NET_HOSTNAME_ENABLE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_HTTP_LOG_LEVEL_CHOICE"></a>

## 398.97 `CONFIG_NET_HTTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：HTTP 客户端库日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_HTTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_HTTP_LOG_LEVEL_OFF
CONFIG_NET_HTTP_LOG_LEVEL_ERR
CONFIG_NET_HTTP_LOG_LEVEL_WRN
CONFIG_NET_HTTP_LOG_LEVEL_INF
CONFIG_NET_HTTP_LOG_LEVEL_DBG
CONFIG_NET_HTTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_HTTP_LOG_LEVEL_DEFAULT`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_HTTP_LOG_LEVEL_OFF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_LOG_LEVEL_OFF)、[`CONFIG_NET_HTTP_LOG_LEVEL_ERR`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_ERR)、[`CONFIG_NET_HTTP_LOG_LEVEL_WRN`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_LOG_LEVEL_WRN)、[`CONFIG_NET_HTTP_LOG_LEVEL_INF`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_HTTP_LOG_LEVEL_INF)、[`CONFIG_NET_HTTP_LOG_LEVEL_DBG`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_HTTP_LOG_LEVEL_DBG"></a>

## 398.98 `CONFIG_NET_HTTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 客户端库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_LOG_LEVEL_DEFAULT"></a>

## 398.99 `CONFIG_NET_HTTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 客户端库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_HTTP_LOG_LEVEL_ERR"></a>

## 398.100 `CONFIG_NET_HTTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → HTTP 客户端库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_HTTP_LOG_LEVEL_CHOICE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HTTP_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P397_subsys_net_配置项参考_7.md) · [返回大纲](大纲.md) · [下一章](P399_subsys_net_配置项参考_9.md)
