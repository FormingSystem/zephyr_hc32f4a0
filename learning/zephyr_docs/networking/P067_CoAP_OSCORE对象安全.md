---
id: learning.zephyr-docs.networking.page-67
title: CoAP_OSCORE对象安全
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap_oscore.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_CoAP_OSCORE对象安全

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap_oscore.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 67.1 概览（Overview）

Zephyr CoAP 库支持[RFC 8613](https://datatracker.ietf.org/doc/html/rfc8613.html)定义的受限 REST 环境对象安全（Object Security for Constrained RESTful Environments，OSCORE）。它使用 CBOR 对象签名与加密（CBOR Object Signing and Encryption，COSE）对 CoAP 消息提供端到端保护（End-to-End Protection）；CBOR 是简洁二进制对象表示（Concise Binary Object Representation）。

OSCORE 在应用层保护消息，提供以下能力：

| 能力 | 含义 |
| --- | --- |
| 保密性（Confidentiality） | 加密消息负载和敏感选项 |
| 完整性（Integrity） | 使用消息认证码（Message Authentication Code，MAC）认证消息 |
| 重放保护（Replay Protection） | 使用序列号防止重放攻击 |
| 代理友好（Proxy-friendly） | 外层选项仍可见，供代理路由 |

与数据报传输层安全（Datagram Transport Layer Security，DTLS）相比，OSCORE 的端到端安全可以在代理转换不同传输协议（UDP、TCP、HTTP）后继续保持。

## 67.2 配置（Configuration）

通过 [`CONFIG_COAP_OSCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE) 启用。它依赖 `uoscore-uedhoc` 模块及 PSA Crypto 支持：

```kconfig
CONFIG_COAP_OSCORE=y
CONFIG_UOSCORE=y
CONFIG_PSA_CRYPTO=y
```

`uoscore` 模块自动选择所需的 PSA 密码算法，例如 AES-CCM、HKDF-SHA256。

| 配置 | 作用 |
| --- | --- |
| [`CONFIG_COAP_OSCORE_MAX_CONTEXTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_MAX_CONTEXTS) | OSCORE 安全上下文最大数量 |
| [`CONFIG_COAP_OSCORE_EXCHANGE_CACHE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_EXCHANGE_CACHE_SIZE) | 每个服务跟踪的 OSCORE 交换数量 |
| [`CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS) | 交换记录的有效期，用于保护延后发送的独立响应；单位为毫秒 |
| [`CONFIG_COAP_OSCORE_CONTEXT_REUSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_CONTEXT_REUSE) | 支持设备重启后复用安全上下文 |
| [`CONFIG_COAP_OSCORE_MASTER_SECRET_MAX_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_MASTER_SECRET_MAX_LEN) | 主秘密的最大字节长度 |
| [`CONFIG_COAP_OSCORE_MASTER_SALT_MAX_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_MASTER_SALT_MAX_LEN) | 主盐值的最大字节长度 |

## 67.3 服务器用法（Server Usage）

使用 [`COAP_SERVICE_DEFINE_OSCORE`](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga306c2f205e9008a2bd3f1862f33460d8) 定义启用 OSCORE 的服务；若同时使用 DTLS，则使用 [`COAPS_SERVICE_DEFINE_OSCORE`](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gafbc0c4c98d1cefe0a77b4ffb28cefe88)。宏为每个服务静态分配交换缓存（Exchange Cache）。

安全上下文（Security Context）通过 Zephyr OSCORE API 单独创建并加入共享池；应用无需直接包含底层 `uoscore-uedhoc` 头文件。收到请求后，依据接收者标识（Recipient ID）和标识上下文（ID Context）匹配安全上下文，因此一个服务可服务多个客户端，每个客户端使用自己的上下文：

```c
#include <zephyr/net/coap_oscore.h>
#include <zephyr/net/coap_service.h>

static struct coap_oscore_context *my_oscore_ctx;

static uint16_t my_service_port = 5683;

/* Final argument "true" requires OSCORE for all requests. */
COAP_SERVICE_DEFINE_OSCORE(my_service, NULL, &my_service_port,
                           COAP_SERVICE_AUTOSTART, true);

int my_service_oscore_init(void)
{
    /* coap_oscore_context_add() copies the key material, so these
     * buffers need not outlive the call and can live on the stack.
     */
    const uint8_t master_secret[16] = { /* ... */ };
    const uint8_t master_salt[8] = { /* ... */ };
    const uint8_t sender_id[] = { /* ... */ };
    const uint8_t recipient_id[] = { /* ... */ };

    struct coap_oscore_init_params params = {
        .master_secret = master_secret,
        .master_secret_len = sizeof(master_secret),
        .sender_id = sender_id,
        .sender_id_len = sizeof(sender_id),
        .recipient_id = recipient_id,
        .recipient_id_len = sizeof(recipient_id),
        .master_salt = master_salt,
        .master_salt_len = sizeof(master_salt),
        .aead_alg = COAP_OSCORE_AEAD_AES_CCM_16_64_128,
        .hkdf = COAP_OSCORE_HKDF_SHA_256,
        .fresh_master_secret_salt = true,
    };

    /* Add the context to the shared pool once its key material is
     * available. Call once per client identity (Recipient ID).
     */
    return coap_oscore_context_add(&params, &my_oscore_ctx);
}
```

> 译注：省略号是密钥材料占位，不是可投入使用的密钥。`coap_oscore_context_add()` 会复制传入缓冲区，因此这些数组可放在栈上。`fresh_master_secret_salt=true` 声明的是每次启动使用新的主秘密／主盐组合；它不会自动把固定数组变成新密钥。使用可复用密钥时，须满足后面的持久化要求。

[`CONFIG_COAP_OSCORE_MAX_CONTEXTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_MAX_CONTEXTS) 控制同时可分配的上下文数量。通过 `coap_oscore_context_remove()` 释放上下文。上下文使用引用计数（Reference Counting）：仍有进行中的请求、活跃交换或观察者引用它时，函数返回 `-EAGAIN` 并保留上下文；这些引用释放后再重试移除。

服务通过 OSCORE 宏创建，且池中至少加入一个上下文后，处理行为如下。

### 接收请求（Incoming Requests）

服务器按 RFC 8613 第 8.2 节自动验证并解密受保护请求。资源处理函数收到解密后的 CoAP 消息，可看到内层选项（Inner Options）。

### 发送响应（Outgoing Responses）

服务器按 RFC 8613 第 8.3 节保护来自 OSCORE 交换的响应与通知。具体依据如下：

| 消息类型 | 匹配与保护依据 |
| --- | --- |
| 同步响应（Synchronous Response） | 请求处理期间生成，根据本服务交换缓存查找记录；匹配到记录时进行保护 |
| 观察通知（Observe Notification） | 使用观察者保存的 OSCORE 状态，状态持续到观察关系结束 |
| 延后／独立响应（Deferred／Separate Response） | 请求处理函数返回后生成，仍需根据本服务交换缓存查找记录 |

同步与独立响应使用的交换记录在 [`CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS) 后过期。混合服务（Mixed Service，同时服务 OSCORE 和普通客户端）在记录过期后发送这两类响应时，无法匹配 OSCORE 状态，将发送明文响应。

### 错误处理（Error Handling）

按照 RFC 8613 第 8.2 节，OSCORE 验证错误使用简单的 CoAP 响应发送，不再进行 OSCORE 处理：

| 错误 | 响应 |
| --- | --- |
| COSE 解码失败 | `4.02 Bad Option`，选项错误 |
| 找不到安全上下文 | `4.01 Unauthorized`，未授权 |
| 解密失败 | `4.00 Bad Request`，请求错误 |

### 强制保护与失败时拒绝（Required OSCORE / Fail-closed）

服务定义中的 `_oscore_required` 参数为 `true` 时，未受保护请求被拒绝，并返回 `4.01 Unauthorized`。

响应的 OSCORE 保护操作失败时，服务器不会改发明文。强制 OSCORE 的服务对于无法匹配任何 OSCORE 状态的输出响应，也直接丢弃。观察通知不会降级为明文。

混合服务有前述例外：同步或独立响应的交换缓存记录过期后，不能再匹配状态，因此不受保护地发送。实际主要影响独立响应，因为同步响应通常匹配的是处理请求时刚创建的记录。

## 67.4 已知限制（Known Limitations）

**混合服务中，过期交换可能导致明文响应。** 这同时适用于同步响应和延后发送的独立响应，超时时间由 [`CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_EXCHANGE_LIFETIME_MS) 控制。

官方原文要求：承载敏感数据的服务应设置为强制 OSCORE，例如使用 [`COAP_SERVICE_DEFINE_OSCORE`](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga306c2f205e9008a2bd3f1862f33460d8) 时传入 `_oscore_required=true`。这种服务拒绝未保护请求，也丢弃无法保护的响应，不会降级成明文。

## 67.5 安全上下文派生（Security Context Derivation）

按照 RFC 8613 第 3 节，上下文由少量参数派生。

| 参数 | 必选性与说明 |
| --- | --- |
| 主秘密（Master Secret） | 必需；共享秘密，AES-CCM-16-64-128 通常使用 16 字节 |
| 发送者标识（Sender ID） | 必需；发送者的唯一标识 |
| 接收者标识（Recipient ID） | 必需；接收者的唯一标识 |
| 主盐值（Master Salt） | 可选；提供额外熵，推荐使用，通常为 8 字节 |
| 标识上下文（ID Context） | 可选；额外的上下文标识 |
| 带关联数据的认证加密算法（Authenticated Encryption with Associated Data，AEAD） | 可选；默认 AES-CCM-16-64-128 |
| 密钥派生函数（Key Derivation Function，KDF） | 可选；默认 HKDF-SHA-256 |

这些参数通常通过设备配备阶段（Provisioning）配置的预共享密钥（Pre-shared Key），或基于 COSE 的临时 Diffie-Hellman 密钥交换（Ephemeral Diffie-Hellman Over COSE，EDHOC）建立。后者见 `uoscore-uedhoc` 模块。

## 67.6 安全事项（Security Considerations）

发送者序列号（Sender Sequence Number，SSN）对 AES-CCM-16-64-128 不得超过 `2^23-1`；原文说明 `uoscore` 强制执行此限制。

主秘密必须安全存储，例如放入安全存储，或通过 EDHOC 派生。

如果重启后复用同一主秘密，而非通过 EDHOC 等方式重新派生，则发送者序列号必须持久化到非易失性存储（Non-volatile Memory），防止随机数值（Nonce）复用破坏保密性和完整性。接收端的重放窗口（Replay Window）无需持久化：它保存在内存，重启后按 RFC 8613 附录 B.1.2 使用 Echo 选项重新同步。

> 源码核对译注：当前官方 [Kconfig.oscore](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig.oscore) 中，[`CONFIG_COAP_OSCORE_CONTEXT_REUSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE_CONTEXT_REUSE) 选择 `UOSCORE_NVM_SUPPORT`，通过 Zephyr 设置子系统（Settings Subsystem）持久化 SSN。应用仍须提供可工作的设置后端，例如存储分区及匹配的 [`CONFIG_SETTINGS_NVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_NVS)。当前 [`coap_oscore.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/coap_oscore.c) 在未启用复用支持且 `fresh_master_secret_salt=false` 时返回 `-ENOTSUP`。不能仅把布尔值改为 `true` 来规避持久化条件。

### 未启用 OSCORE 时的处理（Handling OSCORE When Not Supported）

[`CONFIG_COAP_OSCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE) 未启用，即 `CONFIG_COAP_OSCORE=n` 时，CoAP 协议栈按[RFC 7252](https://datatracker.ietf.org/doc/html/rfc7252.html)第 5.4.1 节对 OSCORE 选项执行失败时拒绝的行为：

| 收到的消息 | 服务器行为 |
| --- | --- |
| 带 OSCORE 选项的 CON 请求 | 返回 `4.02 Bad Option` |
| 带 OSCORE 选项的 NON 请求 | 静默丢弃 |
| 带 OSCORE 选项的响应 | CON 返回重置消息（Reset，RST）；NON／ACK 静默丢弃 |

CON 表示确认消息（Confirmable），NON 表示非确认消息（Non-confirmable），ACK 表示确认应答（Acknowledgement）。

## 67.7 API 参考（API Reference）

完整接口见[CoAP OSCORE API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html)，独立跟踪其翻译状态。本轮未生成或部署密钥、运行密码学测试、验证重启恢复或实际发送 OSCORE 报文。


<a id="oscore-support-rfc-8613"></a>
<a id="coap-oscore-interface"></a>
<a id="index-0"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="overview"></a>
<a id="index-1"></a>
<a id="configuration"></a>
<a id="server-usage"></a>
<a id="index-2"></a>
<a id="index-3"></a>
<a id="index-4"></a>
<a id="known-limitations"></a>
<a id="security-context-derivation"></a>
<a id="index-5"></a>
<a id="security-considerations"></a>
<a id="index-6"></a>
<a id="handling-oscore-when-not-supported"></a>
<a id="index-7"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CoAP服务器库](P066_CoAP服务器库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：LwM2M协议栈](P073_LwM2M协议栈.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P066_CoAP服务器库.md) · [返回大纲](大纲.md) · [下一章](P068_CoAP客户端示例.md)

</details>

<!-- reading-navigation:end -->
