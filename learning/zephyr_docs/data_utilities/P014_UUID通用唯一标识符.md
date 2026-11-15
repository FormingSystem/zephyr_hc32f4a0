---
id: learning.zephyr-docs.data-utilities.page-14
title: UUID通用唯一标识符
kind: reference
status: maintained
domains: [zephyr, data, development]
source_url: https://docs.zephyrproject.org/latest/services/uuid/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_UUID通用唯一标识符

原文：[官方页面](https://docs.zephyrproject.org/latest/services/uuid/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 14.1\_概述

通用唯一标识符（Universally Unique Identifier，UUID），也称全局唯一标识符（Globally Unique Identifier，GUID），是128位标识符，设计目标是在不同空间与时间范围内保持唯一，由 [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562.html) 定义。

UUID子系统提供生成、解析和处理UUID的工具函数，支持生成版本4的随机UUID（UUIDv4）与版本5的基于名称UUID（Name-based UUID，UUIDv5）。

## 14.2\_使用接口

使用UUID API时，包含以下头文件：

```c
#include <zephyr/sys/uuid.h>
```

### 生成UUIDv4

UUIDv4基于随机数，因此需要熵生成器（Entropy Generator）。用 [`uuid_generate_v4()`](P023_UUID生成与转换接口.md#ga1e1e2f008f5ac3366bf474de27d42b66) 生成，并启用 [`CONFIG_UUID_V4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UUID_V4)：

```c
struct uuid my_uuid;
char uuid_str[UUID_STR_LEN];

int ret = uuid_generate_v4(&my_uuid);

if (ret != 0) {
    printk("Failed to generate UUID v4 (err %d)\n", ret);
    return ret;
}

ret = uuid_to_string(&my_uuid, uuid_str);
if (ret != 0) {
    printk("Failed to convert UUID to string (err %d)\n", ret);
    return ret;
}

 printk("UUID: %s\n", uuid_str);
```

译注：当前实现调用 `sys_rand_get()` 填充数据，再设置版本与变体（Variant）字段；随机源相关配置参阅[随机数指南](P006_随机数生成.md)。原文的唯一性是设计目标，不表示有限长度随机标识在数学上绝无碰撞（Collision）。`UUID_STR_LEN` 在当前头文件中为37，包含36个标准显示字符及末尾空字符。

### 生成UUIDv5

UUIDv5由命名空间UUID（Namespace UUID）及名称，即二进制数据（Binary Data）生成。使用 [`uuid_generate_v5()`](P023_UUID生成与转换接口.md#ga6f692b733f600e0346317f3d25d84409)，并启用 [`CONFIG_UUID_V5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UUID_V5)。

UUIDv5具有确定性（Determinism）：相同命名空间与名称总是得到相同UUID。

```c
struct uuid ns_uuid;
struct uuid my_uuid;
char uuid_str[UUID_STR_LEN];

/* Well-known namespace ID for URLs (RFC 9562) */
uuid_from_string("6ba7b811-9dad-11d1-80b4-00c04fd430c8", &ns_uuid);

const char *name = "https://zephyrproject.org/";
int ret = uuid_generate_v5(&ns_uuid, name, strlen(name), &my_uuid);

if (ret != 0) {
    printk("Failed to generate UUID v5 (err %d)\n", ret);
    return ret;
}

ret = uuid_to_string(&my_uuid, uuid_str);
if (ret != 0) {
    printk("Failed to convert UUID to string (err %d)\n", ret);
    return ret;
}

/* outputs: "UUID: abdb72b5-b342-5882-925b-4ce0e3cb4790" */
printk("UUID: %s\n", uuid_str);
```

代码注释译文：使用 RFC 9562 为URL规定的已知命名空间标识；示例输出为 `UUID: abdb72b5-b342-5882-925b-4ce0e3cb4790`。

译注：生成操作对传入名称的字节内容和长度计算，不会访问示例URL或自动规范化名称。示例的 `strlen(name)` 不含字符串末尾空字符。本批用主机标准库按相同命名空间与名称交叉计算，结果与原文一致；未运行Zephyr固件。原示例忽略了 `uuid_from_string()` 的返回值，处理外部输入时应先检查解析成功，再生成后续UUID。

## 14.3\_配置

相关配置项如下：

| 配置 | 用途 |
| --- | --- |
| [`CONFIG_UUID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UUID) | UUID库总开关 |
| [`CONFIG_UUID_V4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UUID_V4) | 版本4生成支持 |
| [`CONFIG_UUID_V5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UUID_V5) | 版本5生成支持 |
| [`CONFIG_UUID_BASE64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UUID_BASE64) | Base64表示转换支持 |

译注：当前官方Kconfig中，v4依赖 `ENTROPY_GENERATOR`；v5依赖 `PSA_WANT_ALG_SHA_1`，且限定 `!BUILD_WITH_TFM`；Base64支持依赖 `BASE64`。这些是所读取源码的配置条件，应与实际版本核对，不能只设置顶层符号就假定依赖满足。

## 14.4\_API参考

[UUID API参考](P023_UUID生成与转换接口.md)。


译注核对来源：[include/zephyr/sys/uuid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/uuid.h)、[lib/uuid/uuid.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/uuid.c)、[lib/uuid/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/Kconfig)。

本仓库的[对应源码](../../../include/zephyr/sys/uuid.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档；UUIDv5示例值另用主机标准库交叉计算，没有执行固件构建、烧录或硬件操作。

<a id="uuid"></a>
<a id="uuid-api"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="usage"></a>
<a id="generating-a-uuidv4"></a>
<a id="generating-a-uuidv5"></a>
<a id="configuration"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：二进制描述符](P010_二进制描述符.md) · [本模块主线目录](../reading/data_utilities.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P013_二进制描述符读取示例.md) · [返回大纲](大纲.md) · [下一章](P015_UUID生成示例.md)

</details>

<!-- reading-navigation:end -->
