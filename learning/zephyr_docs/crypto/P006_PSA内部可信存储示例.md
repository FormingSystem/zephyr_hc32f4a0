---
id: learning.zephyr-docs.crypto.page-6
title: PSA内部可信存储示例
kind: reference
status: maintained
domains: [zephyr, crypto, security]
source_url: https://docs.zephyrproject.org/latest/samples/psa/its/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_PSA内部可信存储示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/psa/its/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 6.1\_概述（Overview）

本示例演示如何使用[PSA 内部可信存储（Internal Trusted Storage，ITS）API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-internal-trusted-storage-api) 保存和读取持久数据。ITS 是 [PSA 安全存储（Secure Storage）API](https://arm-software.github.io/psa-api/storage/) 的组成部分。

## 6.2\_要求（Requirements）

要构建此示例，必须有可用的 PSA ITS API 实现。提供方可以是：

- [可信固件 M（Trusted Firmware-M，TF-M）](../tfm/P001_TFM可信固件入口.md#tfm)：适用于 `*/ns` [开发板目标（Board Targets）](../getting_started/P006_术语表.md#term-board-target)。
- [安全存储子系统（Secure Storage Subsystem）](../storage/P021_安全存储服务.md#secure-storage)：适用于其他开发板目标。

## 6.3\_构建（Building）

示例位于 [samples/psa/its](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/its)。

`tests.yaml` 定义了不同配置。可以根据 PSA ITS 提供方选择以下构建方式。

### 使用 TF-M

对于包含 TF-M 的开发板目标：

```shell
# From the root of the zephyr repository
west build -b <ns_board_target> -T sample.psa.its.tfm samples/psa/its
```

### 使用安全存储子系统

对于不含 TF-M 的开发板目标，如果目标具有熵驱动（Entropy Driver，推荐）：

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.its.secure_storage.entropy_driver samples/psa/its
```

也可以使用不安全熵源（Insecure Entropy Source，仅用于测试）：

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.its.secure_storage.entropy_not_secure samples/psa/its
```

以上命令中的英文注释表示从 Zephyr 仓库根目录执行。`<ns_board_target>` 与 `<board_target>` 是目标占位符，应替换为实际开发板目标。

烧录方法见 [烧录：west flash](../west/P007_构建烧录与调试.md#west-flashing)。

译注（源码核对）：示例使用数据 UID `1`，先写入数据，再从数据中点的偏移读取并比较，随后读取大小、容量与标志等元数据，最后删除该条目。它展示持久存储 API 的使用，但一次正常运行结束后不会保留该测试条目；此流程也没有执行断电后重启读回测试。安全存储实现的数据大小来自 `CONFIG_SECURE_STORAGE_ITS_MAX_DATA_SIZE`，其他情况下示例使用 128 字节。

## 6.4\_另请参阅（See Also）

[PSA 安全存储 API 参考](https://docs.zephyrproject.org/latest/doxygen/html/group__psa__secure__storage.html)。


译注核对来源：[samples/psa/its/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/its/src/main.c)、[samples/psa/its/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/its/prj.conf)、[samples/psa/its/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/its/tests.yaml)。

本仓库的[对应源码](../../../samples/psa/its/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="psa_its"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building"></a>
<a id="tab-0-0-0"></a>
<a id="tab-0-0-1"></a>
<a id="panel-0-0-0"></a>
<a id="panel-0-0-1"></a>
<a id="see-also"></a>

[上一章](P005_PSA示例目录.md) · [返回大纲](大纲.md) · [下一章](P007_PSA持久密钥示例.md)
