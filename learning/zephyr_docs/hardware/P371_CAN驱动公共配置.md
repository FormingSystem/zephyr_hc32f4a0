---
id: learning.zephyr-docs.hardware.canback-2
title: CAN驱动公共配置
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第371章\_CAN驱动公共配置

原文：[structcan__driver__config](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html)。读取日期：2026-10-13，`latest`。

## 371.1\_配置对象的首成员

[`can_driver_config`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html) 是所有控制器局域网（Controller Area Network，CAN）控制器驱动共用的配置结构，声明来自 `zephyr/drivers/can.h`。它应当是设备结构 `config` 字段所指对象的第一个成员。

收发器（Transceiver）与控制器共同决定速率范围；经典 CAN 与灵活数据速率 CAN（CAN with Flexible Data-Rate，CAN FD）的仲裁阶段（Arbitration Phase）使用公共初始速率和采样点，CAN FD 数据阶段（Data Phase）另有配置。

## 371.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a8e9f0ec132daf25a2e947478c0b952a3"></a>[`phy`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html#a8e9f0ec132daf25a2e947478c0b952a3) | `const struct device *` | 关联 CAN 收发器的设备结构指针，或 `NULL` |
| <a id="accc9f1b6202b2b30b60bbc890190d3c3"></a>[`min_bitrate`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html#accc9f1b6202b2b30b60bbc890190d3c3) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 控制器/收发器组合支持的最低比特率（Bitrate） |
| <a id="a420d9f8762ae332d4d78084dd74afa6e"></a>[`max_bitrate`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html#a420d9f8762ae332d4d78084dd74afa6e) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 控制器/收发器组合支持的最高比特率 |
| <a id="a6f4f050b5aeb8cd466a12d70c53e8423"></a>[`bitrate`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html#a6f4f050b5aeb8cd466a12d70c53e8423) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 经典 CAN / CAN FD 仲裁阶段初始比特率 |
| <a id="a2cd7693cd9acc0537a085cdc85688a96"></a>[`sample_point`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html#a2cd7693cd9acc0537a085cdc85688a96) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 仲裁阶段初始采样点（Sample Point），单位为千分比（Permille） |
| <a id="afa6cd8cb79ccad28ca86caec4d92cd85"></a>[`sample_point_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html#afa6cd8cb79ccad28ca86caec4d92cd85) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | CAN FD 数据阶段初始采样点，单位为千分比 |
| <a id="afd7a831b33b059f47dd867726e31e69b"></a>[`bitrate_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__config.html#afd7a831b33b059f47dd867726e31e69b) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | CAN FD 数据阶段初始比特率 |

`sample_point_data` 和 `bitrate_data` 仅在启用 Kconfig 配置项 [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE) 时可用。

---

[上一章：CAN驱动函数表](P370_CAN驱动函数表.md) · [下一章：CAN驱动公共数据](P372_CAN驱动公共数据.md) · [返回大纲](大纲.md)
