---
id: learning.zephyr-docs.firmware_update.smp-group-9
title: Shell管理组
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/services/device_mgmt/smp_groups/smp_group_9.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第16章\_Shell管理组

原文：[Shell management](https://docs.zephyrproject.org/latest/services/device_mgmt/smp_groups/smp_group_9.html)。读取日期：2026-10-12，`latest`。

本章使用**简单管理协议（Simple Management Protocol，SMP）**；载荷采用**简洁二进制对象表示（Concise Binary Object Representation，CBOR）**。下列原文结构记号不是可以直接发送的 **JavaScript对象表示法（JavaScript Object Notation，JSON）**文本：`str` 为字符串，`uint` 为无符号整数，`int` 为整数，`bool` 为布尔值，`bstr` / `byte str` 为字节串，`opt` 表示可选。头字段 `OP` 为操作码，`Group ID` 为组标识，`Command ID` 为命令标识；0/1分别为读请求/响应，2/3分别为写请求/响应。

各命令的第2版组错误以 `err.group` 给出枚举 [`mcumgr_group_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga81f98b9a0c3810f7d607b783f8e259b5) 所属组、以 `err.rc` 给出非零组内错误码。第1版错误及第2版的通用SMP错误以顶层 `rc` 给出枚举 [`mcumgr_err_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5) 的非零错误码；成功时不必携带这些错误字段。后面保留每个命令的原始结构，通用编码规则见[SMP协议规范](P009_SMP协议规范.md)。

## 16.1\_经SMP执行命令

**命令解释器（Shell）**管理通过SMP把命令传给Zephyr的Shell子系统。组编号9，命令0是**命令行执行（Command Line Execute）**：执行效果类似在Shell中输入命令，但请求和响应都经过SMP传输。

## 16.2\_请求格式

请求头 `OP=2, Group ID=9, Command ID=0`：

```text
{
    (str)"argv"     : [
        (str)<cmd>
        (str,opt)<arg>
        ...
    ]
}
```

`argv` 是字符串数组，第一项 `<cmd>` 为待执行命令，后续 `<arg>` 为可选参数。

## 16.3\_响应与旧版返回码

响应头 `OP=3, Group ID=9, Command ID=0`，成功载荷为：

```text
{
    (str)"o"            : (str)
    (str)"ret"          : (int)
}
```

`o` 是命令输出字符串；`ret` 是Shell命令执行的返回码。它与下面MCUmgr自身的协议状态码属于不同层次。

失败响应（第2版组错误）：

```text
{
    (str)"err" : {
        (str)"group"    : (uint)
        (str)"rc"       : (uint)
    }
}
```

第1版错误或第2版通用SMP错误：

```text
{
    (str)"rc"       : (int)
}
```

字段的出现条件与本章开头相同。

**原文注意：**旧版Zephyr把 `rc` 同时用于MCUmgr状态和Shell命令返回码。Kconfig配置项 [`CONFIG_MCUMGR_GRP_SHELL_LEGACY_RC_RETURN_CODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_SHELL_LEGACY_RC_RETURN_CODE) 可以恢复这种旧行为，客户端解析时必须考虑固件配置。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：文件系统管理组](P015_文件系统管理组.md) · [本模块主线目录](../reading/firmware_update.md) · [全部主线](../reading/README.md) · [下一篇：枚举管理组](P017_枚举管理组.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：文件系统管理组](P015_文件系统管理组.md) · [下一章：枚举管理组](P017_枚举管理组.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
