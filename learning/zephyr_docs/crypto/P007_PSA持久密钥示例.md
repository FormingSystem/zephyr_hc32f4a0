---
id: learning.zephyr-docs.crypto.page-7
title: PSA持久密钥示例
kind: reference
status: maintained
domains: [zephyr, crypto, security]
source_url: https://docs.zephyrproject.org/latest/samples/psa/persistent_key/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_PSA持久密钥示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/psa/persistent_key/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 7.1\_概述（Overview）

本示例演示 [PSA 密码学 API（PSA Crypto API）](P003_PSA密码学.md#psa-crypto) 中持久密钥（Persistent Key）的使用。

## 7.2\_要求（Requirements）

除了 PSA Crypto API，本示例还需要 [PSA 内部可信存储（Internal Trusted Storage，ITS）API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-internal-trusted-storage-api) 的实现，用于存放持久密钥。提供方可以是：

- [可信固件 M（Trusted Firmware-M，TF-M）](../tfm/P001_TFM可信固件入口.md#tfm)：适用于 `*/ns` [开发板目标（Board Targets）](../getting_started/P006_术语表.md#term-board-target)。
- [安全存储子系统（Secure Storage Subsystem）](../storage/P021_安全存储服务.md#secure-storage)：适用于其他开发板目标。

## 7.3\_构建（Building）

示例位于 [samples/psa/persistent_key](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/persistent_key)。

`tests.yaml` 定义了不同配置。可以根据 PSA ITS 提供方选择以下构建方式。

### 使用 TF-M

对于包含 TF-M 的开发板目标：

```shell
# From the root of the zephyr repository
west build -b <ns_board_target> -T sample.psa.persistent_key.tfm samples/psa/persistent_key
```

### 使用安全存储子系统

对于不含 TF-M 的开发板目标，如果目标具有熵驱动（Entropy Driver，推荐）：

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.persistent_key.secure_storage.entropy_driver samples/psa/persistent_key
```

也可以使用不安全熵源（Insecure Entropy Source，仅用于测试）：

```shell
# From the root of the zephyr repository
west build -b <board_target> -T sample.psa.persistent_key.secure_storage.entropy_not_secure samples/psa/persistent_key
```

以上命令中的英文注释表示从 Zephyr 仓库根目录执行。`<ns_board_target>` 与 `<board_target>` 是待替换的开发板目标占位符。

烧录方法见 [烧录：west flash](../west/P007_构建烧录与调试.md#west-flashing)。

译注（源码核对）：当前示例以 `ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_BEGIN` 作为固定密钥 ID，生成 256 位 AES 密钥，设置持久生存期（Persistent Lifetime）、加解密使用权限以及 CTR 算法。随后用 `psa_purge_key()` 清除易失内存中的密钥副本，再通过同一 ID 进行加解密并比较结果；最后调用 `psa_destroy_key()` 删除持久密钥。`purge` 与 `destroy` 的作用不同，示例没有真正复位设备，也不会在成功结束后留下该密钥。

译注：示例启动时也会尝试删除同一固定 ID 的已有密钥。将示例移入自己的应用时，应先核对密钥 ID 分配，不能把测试 ID 当成可与现有应用密钥任意复用的编号。

## 7.4\_API 参考（API Reference）

[PSA Crypto 密钥管理 API 参考](https://arm-software.github.io/psa-api/crypto/1.2/api/keys/index.html)。


译注核对来源：[samples/psa/persistent_key/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/persistent_key/src/main.c)、[samples/psa/persistent_key/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/persistent_key/prj.conf)、[samples/psa/persistent_key/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/psa/persistent_key/tests.yaml)。

本仓库的[对应源码](../../../samples/psa/persistent_key/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="persistent_key"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building"></a>
<a id="tab-0-0-0"></a>
<a id="tab-0-0-1"></a>
<a id="panel-0-0-0"></a>
<a id="panel-0-0-1"></a>
<a id="api-reference"></a>

[上一章](P006_PSA内部可信存储示例.md) · [返回大纲](大纲.md) · [下一章](P008_密码驱动通用接口.md)
