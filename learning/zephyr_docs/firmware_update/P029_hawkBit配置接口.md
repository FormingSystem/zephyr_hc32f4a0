---
id: learning.zephyr-docs.firmware_update.fwapi-hawkbit__config
title: hawkBit配置接口
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第29章\_hawkBit配置接口

原文：[group__hawkbit__config](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html)。读取日期：2026-10-13，`latest`。

## 29.1\_配置接口与结构

hawkBit配置 **应用程序编程接口（Application Programming Interface，API）**声明在头文件 [`zephyr/mgmt/hawkbit/config.h`](https://docs.zephyrproject.org/latest/doxygen/html/config_8h.html) 中。结构体 [`hawkbit_runtime_config`](https://docs.zephyrproject.org/latest/doxygen/html/structhawkbit__runtime__config.html) 保存服务器地址、主机名、端口、认证令牌和安全凭据标记，字段详见[运行时配置结构](P032_hawkBit运行时配置结构.md)。

**直接设备集成（Direct Device Integration，DDI）**安全令牌供服务器认证；**传输层安全（Transport Layer Security，TLS）**标记通过类型 [`sec_tag_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3) 标识TLS凭据集合，本身不是证书内容。下列 `static inline` 声明表示头文件中的静态内联辅助函数，签名与原文保持一致。

## 29.2\_整体设置与读取

函数 [`hawkbit_set_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5e6a1e2e49b75a44a9f13f059ed7d3f6) 设置服务器配置，参数 `config` 指向要设置的配置结构：

```c
int hawkbit_set_config(struct hawkbit_runtime_config *config);
```

成功返回0；查询正在运行时返回稍后重试错误常量 `-EAGAIN`；配置参数无效时返回错误常量 `-EINVAL`。

函数 [`hawkbit_get_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaae46014585251b53afe726d42475d739) 返回配置结构值：

```c
struct hawkbit_runtime_config hawkbit_get_config(void);
```

> 译注：结构中含有字符指针，返回结构值不等于自动深拷贝其字符串。原参考没有授予调用者释放这些字符串或不受限制修改内部状态的权限，应经设置接口更新配置。

## 29.3\_设置主机名、地址和端口

函数 [`hawkbit_set_server_domain()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga2c6aa606a003b34538b521fda77af903) 设置服务器主机名，参数 `domain_str` 为要设置的主机名字符串：

```c
static inline int hawkbit_set_server_domain(char *domain_str);
```

成功返回0；字符串长度与 `server_domain` 要求不符时返回 `-EINVAL`；查询正在运行时返回 `-EAGAIN`。

函数 [`hawkbit_set_server_addr()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa49efdafe94e1d36a537aff962df41d5) 设置服务器地址，参数 `addr_str` 为地址字符串：

```c
static inline int hawkbit_set_server_addr(char *addr_str);
```

成功返回0，查询进行中返回 `-EAGAIN`，配置参数无效返回 `-EINVAL`。

函数 [`hawkbit_set_server_port()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga78ef6a168132940040ad04498f0b462d) 设置服务器端口，参数 `port` 为端口值：

```c
static inline int hawkbit_set_server_port(uint16_t port);
```

原参考列出的返回值为成功0，以及查询进行中的 `-EAGAIN`。

## 29.4\_设置安全令牌和TLS标记

函数 [`hawkbit_set_ddi_security_token()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa2799669246cc817bb8e294a8fbfb3d2) 设置安全令牌，参数 `token` 为令牌字符串：

```c
static inline int hawkbit_set_ddi_security_token(char *token);
```

成功返回0，查询正在运行时返回 `-EAGAIN`。

函数 [`hawkbit_set_tls_tag()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5c73e9ba4dd9788e22fdb11f1f2b81ee) 设置TLS凭据标记，参数 `tag` 为标记值：

```c
static inline int hawkbit_set_tls_tag(sec_tag_t tag);
```

成功返回0，查询正在运行时返回 `-EAGAIN`。以上返回列表按原文逐项保留，不另行推断其他未记录错误。

## 29.5\_逐项读取配置

下列五个函数均无参数，分别返回对应配置值。字符指针的所有权边界仍应遵循库实现，不因返回类型是 `char *` 就自行释放。

```c
static inline char *hawkbit_get_server_addr(void);
static inline char *hawkbit_get_server_domain(void);
static inline uint16_t hawkbit_get_server_port(void);
static inline char *hawkbit_get_ddi_security_token(void);
static inline sec_tag_t hawkbit_get_tls_tag(void);
```

| 函数 | 返回含义 |
| --- | --- |
| [`hawkbit_get_server_addr()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gacbbaed38e2ace7d8dcc78e40b286b5e9) | 服务器地址。 |
| [`hawkbit_get_server_domain()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gafd9f30b2acab65c34bcb5edaa3da8738) | 服务器主机名。 |
| [`hawkbit_get_server_port()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga3674fc406aa20fe4770ff0c729817b7c) | 服务器端口。 |
| [`hawkbit_get_ddi_security_token()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gadc4aea2dac4915a434a10e6e055f54f7) | 安全令牌。 |
| [`hawkbit_get_tls_tag()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga694e5f4fbcae451eb90a019f6d1f3b81) | TLS凭据标记。 |

## 29.6\_动作编号与轮询间隔

函数 [`hawkbit_get_action_id()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga0ca5f633e902137ecda068ab312d52db) 取得hawkBit **动作编号（Action ID）**，返回有符号32位整数：

```c
int32_t hawkbit_get_action_id(void);
```

函数 [`hawkbit_get_poll_interval()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga46c56cee1a89abd81a328ef3f91648bb) 取得 **轮询间隔（Poll Interval）**，返回无符号32位整数：

```c
uint32_t hawkbit_get_poll_interval(void);
```

原参考未在此处写单位。**译注：**本地自动处理器将该返回值传给 `K_SECONDS()`，即按秒使用；不要与UpdateHub示例中按分钟配置的轮询间隔混淆。

[上一章：hawkBit自动处理接口](P028_hawkBit自动处理接口.md) · [下一章：hawkBit事件接口](P030_hawkBit事件接口.md) · [返回大纲](大纲.md)
