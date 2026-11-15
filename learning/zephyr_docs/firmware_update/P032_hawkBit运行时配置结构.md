---
id: learning.zephyr-docs.firmware_update.fwapi-runtime-config
title: hawkBit运行时配置结构
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第32章\_hawkBit运行时配置结构

原文：[structhawkbit__runtime__config](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html)。读取日期：2026-10-13，`latest`。

## 32.1\_运行时配置结构

结构体 [`hawkbit_runtime_config`](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html) 保存hawkBit运行时配置，声明来自头文件 [`zephyr/mgmt/hawkbit/config.h`](https://docs.zephyrproject.org/latest/doxygen/html/config_8h_source.html)。应用通过[配置接口](P029_hawkBit配置接口.md)设置或读取它。

这里 **传输层安全（Transport Layer Security，TLS）**用于安全连接，[`sec_tag_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3) 是标识TLS凭据的类型；**互联网协议（Internet Protocol，IP）**地址与域名均属于服务器寻址信息。安全令牌用于认证，凭据标记用于选择TLS凭据，两者不可互换。

## 32.2\_全部字段

下列为原文五个字段的类型、名字和说明：

| 类型与字段 | 含义 |
| --- | --- |
| `char *server_addr` | 服务器地址；原文括注为“启用Kconfig配置项 `CONFIG_HAWKBIT_USE_DOMAIN_NAME` 时为域名或IP地址”。 |
| `char *server_domain` | 服务器域名。 |
| `uint16_t server_port` | 服务器端口。 |
| `char *auth_token` | 安全令牌（Security Token）。 |
| `sec_tag_t tls_tag` | TLS凭据标记（TLS Tag）。 |

> 译注：保留原文 [`server_addr`](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#aee3966a3387498d726ca960663b0b291) 括注的条件表述；不要据此推断 [`server_domain`](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html#a3efc42d340461934b96a55ec6d5b91d2) 和地址字段可以在所有配置下随意互换。字符串内存的所有权、允许长度和更新条件由配置实现决定，本结构参考页没有额外规定。

原页面由 `zephyr/mgmt/hawkbit/config.h` 生成；它没有给出字段默认值、初始化例程或图片。

[上一章：UpdateHub接口](P031_UpdateHub接口.md) · [返回大纲](大纲.md)
