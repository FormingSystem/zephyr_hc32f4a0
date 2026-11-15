---
id: learning.zephyr-docs.kconfig-reference.page-333
title: "`subsys/canbus`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第333章\_`subsys/canbus`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/canbus` 的 23 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ISOTP"></a>

## 333.1 `CONFIG_ISOTP`

**提示（Prompt）**：ISO-TP 传输（ISO-TP Transport）

**说明（Help）**

为控制器局域网（CAN）启用 ISO-TP 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN
```

**主动选择（Selects）**

```text
CONFIG_NET_BUF
CONFIG_POLL
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_NET_BUF`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)。

<a id="CONFIG_ISOTP_A_TIMEOUT"></a>

## 333.2 `CONFIG_ISOTP_A_TIMEOUT`

**提示（Prompt）**：Ar 与 As 超时，单位为毫秒（sending and receiving timeout）

**说明（Help）**

As 为发送方发送超时（sender transmit timeout），Ar 为接收方发送超时（receiver transmit timeout）。ISO 15765-2：`1000ms`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[200, 10000]
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_BS_TIMEOUT"></a>

## 333.3 `CONFIG_ISOTP_BS_TIMEOUT`

**提示（Prompt）**：Bs 超时，单位为毫秒，即接收流控帧的超时（timeout for frame control）

**说明（Help）**

接收下一个流控帧（FC frame）的超时。ISO 15765-2：`1000ms`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[200, 10000]
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_BUF_TX_DATA_POOL_SIZE"></a>

## 333.4 `CONFIG_ISOTP_BUF_TX_DATA_POOL_SIZE`

**提示（Prompt）**：缓冲区分配来源内存池的大小（memory pool size）

**说明（Help）**

定义用于分配发送缓冲区的内存池（memory pool）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP_USE_TX_BUF && CONFIG_ISOTP
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 缓存发送写入（Buffer TX writes）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_USE_TX_BUF`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP_USE_TX_BUF)、[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_CR_TIMEOUT"></a>

## 333.5 `CONFIG_ISOTP_CR_TIMEOUT`

**提示（Prompt）**：Cr 超时，单位为毫秒，即连续帧超时（timeout for consecutive frames）

**说明（Help）**

Cr 为接收方连续帧超时（receiver consecutive frame timeout）。ISO 15765-2：`1000ms`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[200, 10000]
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_CUSTOM_FIXED_ADDR"></a>

## 333.6 `CONFIG_ISOTP_CUSTOM_FIXED_ADDR`

**提示（Prompt）**：使用不兼容 SAE J1939 的固定地址（fixed address not compatible with SAE J1939）

**说明（Help）**

允许使用另一种 CAN 帧标识符格式（frame ID format）。未设置时，ISO-TP 固定寻址（fixed addressing）使用 SAE J1939 标准。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS"></a>

## 333.7 `CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS`

**提示（Prompt）**：缓存发送上下文（Buffered TX contexts）

**说明（Help）**

启用发送上下文缓存（buffered sending contexts），使发送后无需继续管理数据的“发送即忘”（send and forget）方式成为可能。使用内存块池（memory slab）缓存上下文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_ENABLE_TX_PADDING"></a>

## 333.8 `CONFIG_ISOTP_ENABLE_TX_PADDING`

**提示（Prompt）**：发送消息填充（Padding for transmitted messages）

**说明（Help）**

如果 PDU 有效载荷（payload）未恰好填满 CAN 帧，则添加填充字节 `0xCC`，这是 Bosch 推荐的填充值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
y if CONFIG_ISOTP_REQUIRE_RX_PADDING
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)、[`CONFIG_ISOTP_REQUIRE_RX_PADDING`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP_REQUIRE_RX_PADDING)。

<a id="CONFIG_ISOTP_FIXED_ADDR_PRIO_MASK"></a>

## 333.9 `CONFIG_ISOTP_FIXED_ADDR_PRIO_MASK`

**提示（Prompt）**：固定寻址模式的优先级掩码（priority mask in fixed addressing mode）

**说明（Help）**

优先级地址掩码（Priority address mask）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
0x1C000000
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 固定地址定义（Fixed address definition）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_FIXED_ADDR_PRIO_POS"></a>

## 333.10 `CONFIG_ISOTP_FIXED_ADDR_PRIO_POS`

**提示（Prompt）**：固定寻址模式的优先级位置（priority position in fixed addressing mode）

**说明（Help）**

优先级地址的位位置（Priority address position in bits）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
26
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 固定地址定义（Fixed address definition）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_FIXED_ADDR_RX_MASK"></a>

## 333.11 `CONFIG_ISOTP_FIXED_ADDR_RX_MASK`

**提示（Prompt）**：匹配任意优先级和源地址的 CAN 接收过滤掩码（CAN filter RX mask, SA）

**说明（Help）**

CAN 接收过滤掩码（CAN filter RX mask）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
0x03FFFF00
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 固定地址定义（Fixed address definition）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_FIXED_ADDR_SA_MASK"></a>

## 333.12 `CONFIG_ISOTP_FIXED_ADDR_SA_MASK`

**提示（Prompt）**：提取固定源地址的掩码（fixed Source Address，SA mask）

**说明（Help）**

源地址掩码（Source address mask）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
0xFF
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 固定地址定义（Fixed address definition）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_FIXED_ADDR_SA_POS"></a>

## 333.13 `CONFIG_ISOTP_FIXED_ADDR_SA_POS`

**提示（Prompt）**：固定源地址位置（fixed Source Address，SA position）

**说明（Help）**

源地址的位位置（Source address position in bits）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 固定地址定义（Fixed address definition）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_FIXED_ADDR_TA_MASK"></a>

## 333.14 `CONFIG_ISOTP_FIXED_ADDR_TA_MASK`

**提示（Prompt）**：提取固定目标地址的掩码（fixed Target Address，TA mask）

**说明（Help）**

目标地址掩码（Target address mask）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
0xFF00
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 固定地址定义（Fixed address definition）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_FIXED_ADDR_TA_POS"></a>

## 333.15 `CONFIG_ISOTP_FIXED_ADDR_TA_POS`

**提示（Prompt）**：固定目标地址位置（fixed Target Address，TA position）

**说明（Help）**

目标地址的位位置（Target address position in bits）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 固定地址定义（Fixed address definition）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_REQUIRE_RX_PADDING"></a>

## 333.16 `CONFIG_ISOTP_REQUIRE_RX_PADDING`

**提示（Prompt）**：要求接收消息带填充（Require padding for received messages）

**说明（Help）**

启用后，对于经典 CAN（classic CAN），单帧（SF）、流控帧（FC）和最后一个连续帧（CF）的数据长度码（DLC）必须始终表示 `8` 字节，发送设备必须填充未使用字节。此设置使实现能够符合 AUTOSAR 的 CAN 传输层规范（Specification of CAN Transport Layer）。默认情况下，接收的 CAN 帧无论是否填充均会被接受。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_RX_BUF_COUNT"></a>

## 333.17 `CONFIG_ISOTP_RX_BUF_COUNT`

**提示（Prompt）**：接收数据缓冲区数量（Number of data buffers for receiving data）

**说明（Help）**

每个数据缓冲区占用 `ISOTP_RX_BUF_SIZE` 加上较小的头部（`sizeof(struct net_buf)`）所对应的空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_RX_BUF_SIZE"></a>

## 333.18 `CONFIG_ISOTP_RX_BUF_SIZE`

**提示（Prompt）**：单个缓冲区数据块大小（Size of one buffer data block）

**说明（Help）**

定义池中单个数据块（block）的大小，块数量由 `ISOTP_RX_BUF_COUNT` 指定。为提高效率，应使用 `CAN_MAX_DLEN - 1` 的整数倍；对于经典 CAN 为 `8 - 1 = 7`，对于 CAN FD 为 `64 - 1 = 63`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
63 if CONFIG_CAN_FD_MODE
56
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)、[`CONFIG_CAN_FD_MODE`](P060_drivers_can_配置项参考.md#CONFIG_CAN_FD_MODE)。

<a id="CONFIG_ISOTP_RX_SF_FF_BUF_COUNT"></a>

## 333.19 `CONFIG_ISOTP_RX_SF_FF_BUF_COUNT`

**提示（Prompt）**：接收数据所用 SF 与 FF 缓冲区数量（SF and FF data buffers）

**说明（Help）**

此缓冲区用于首帧（first frames，FF）和单帧（single frames，SF）。它是额外缓冲区，因为必须在中断服务例程上下文（ISR context）首次接收前就绪，因此在绑定（binding）时分配。每个缓冲区占用 `CAN_MAX_DLEN - 1` 字节加上头部（`sizeof(struct net_buf)`）的空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_TX_BUF_COUNT"></a>

## 333.20 `CONFIG_ISOTP_TX_BUF_COUNT`

**提示（Prompt）**：发送数据缓冲区数量（Number of data buffers for sending data）

**说明（Help）**

每个数据缓冲区占用 `CONFIG_NET_BUF_DATA_SIZE` 加上较小头部（`sizeof(struct net_buf)`）所对应的空间。如果使用上下文缓冲区（context buffers），此处采用相同大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP_USE_TX_BUF && CONFIG_ISOTP
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 缓存发送写入（Buffer TX writes）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_USE_TX_BUF`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP_USE_TX_BUF)、[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_TX_CONTEXT_BUF_COUNT"></a>

## 333.21 `CONFIG_ISOTP_TX_CONTEXT_BUF_COUNT`

**提示（Prompt）**：发送数据所用上下文缓冲区数量（context buffers for sending data）

**说明（Help）**

定义分配这些缓冲区的内存块池（memory slab）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS && CONFIG_ISOTP
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport） → 缓存发送上下文（Buffered TX contexts）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS)、[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_USE_TX_BUF"></a>

## 333.22 `CONFIG_ISOTP_USE_TX_BUF`

**提示（Prompt）**：缓存发送写入（Buffer TX writes）

**说明（Help）**

将出站数据复制到网络缓冲区（net buffer），以便调用函数可以丢弃原数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<a id="CONFIG_ISOTP_WFTMAX"></a>

## 333.23 `CONFIG_ISOTP_WFTMAX`

**提示（Prompt）**：WFTmax：中止前允许的最大 WAIT 帧数（Max WAIT frames before aborting）

**说明（Help）**

定义中止传输前允许的最大等待帧（WAIT frames）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ISOTP
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 254]
```

**定义位置（Location）**：[`subsys/canbus/isotp/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/canbus/isotp/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 控制器局域网总线子系统（Controller Area Network，CAN bus subsystem） → ISO-TP 传输（ISO-TP Transport）

**配置项引用（Symbol References）**：[`CONFIG_ISOTP`](P333_subsys_canbus_配置项参考.md#CONFIG_ISOTP)。

<!-- kconfig-navigation -->

[上一章](P332_subsys_bluetooth_配置项参考_13.md) · [返回大纲](大纲.md) · [下一章](P334_subsys_console_配置项参考.md)
