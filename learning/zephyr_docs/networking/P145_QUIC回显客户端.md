---
id: learning.zephyr-docs.networking.page-145
title: QUIC回显客户端
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/quic/echo_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第145章\_QUIC回显客户端

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/quic/echo_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Zephyr 的 `quic/echo_client` 示例实现使用 QUIC 协议的回显客户端（Echo Client），支持 IPv4、IPv6，并使用兼容 BSD 套接字（BSD Sockets）的 API。示例用于展示 QUIC API 与套接字服务（Socket Service）API 的用法。

套接字服务让一个线程监听多个阻塞套接字，在其中某个套接字出现活动时触发回调（Callback）。只需创建一个服务线程即可监视这组套接字，从而节省内存。

应用通过 QUIC 协议（[RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000.html)）提供服务。源码见 [samples/net/quic/echo_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/quic/echo_client)。

## 2. 前提（Requirements）

需具备以下两种环境之一：

- 按 [与主机系统联网](P007_与主机系统联网.md#networking-with-host) 配置的网络环境。
- 带有硬件网络接口的开发板。

## 3. 构建与运行（Building and Running）

以下是构建 Zephyr 版 `quic/echo_client` 的原文命令。前提是已经准备好所用版本的 Zephyr 工作区、工具链和对应板级网络支持；在 Zephyr 源码根目录的 Bash 终端执行，将 `<board_to_use>` 替换为实际板名。构建成功后，按该开发板的运行方式启动固件；失败时先处理构建错误。

```sh
west build -b <board_to_use> samples/net/quic/echo_client
```

示例启动后，尝试连接 `192.0.2.2` 或 `2001:db8::2` 的 `4422` 端口。

最简单的监听方式是使用 net-tools 项目中的回显服务端辅助脚本。下面保留原文命令；它们在取得相应文件的 net-tools 目录运行，`$` 是提示符。两行是 IPv4、IPv6 两种用法。

```sh
$ ./quic-echo-server.py --host 192.0.2.2 --certificate quic-ca-cert.pem --private-key quic-private-key.pem --max-stream-data 8192
$ ./quic-echo-server.py --host 2001:db8::1 --certificate quic-ca-cert.pem --private-key quic-private-key.pem
```

连接建立后，Zephyr 客户端检查收到的回显是否与发送给服务端的数据一致。原文说明 `quic-echo-server.py` 会在结束时打印统计信息（Statistics）。

### 3.1 原始命令与当前源码差异（译注）

官方 [客户端配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/quic/echo_client/prj.conf) 的本端 IPv6 地址是 `2001:db8::1`，对端是 `2001:db8::2`。原文辅助服务端第二行却监听 `2001:db8::1`，与默认对端地址不一致；保持默认配置时应监听主机侧的 `2001:db8::2`。网络地址是文档示例值，仍需按前提链接建立实际可达网络。

官方 [net-tools 辅助服务端](https://github.com/zephyrproject-rtos/net-tools/blob/master/quic-echo-server.py) 使用 `aioquic`，要求 `--certificate` 和 `--private-key`，并将 ALPN 设置为 `echo-quic`。本次核对的 net-tools 根目录没有原文命令中的 `quic-ca-cert.pem` 和 `quic-private-key.pem`；它们不能当作已随目录提供的文件。Zephyr 当前示例通过 [common.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/common/common.cmake) 从 `samples/net/common/quic_certs` 导入测试证书和密钥，客户端信任数据也来自该组测试材料。

下面是按当前源码补充的 IPv6 命令，和上面的原文命令分开。终端仍为 Bash，当前位置为官方 net-tools 根目录；所用 Python 环境必须已提供兼容该脚本的 `aioquic`。`ZEPHYR_BASE` 为所用 Zephyr 工具环境中的源码根变量，先核对它已经设置、下列官方测试文件真实存在，再执行；变量并非本译文新增的机器路径。若未设置，应先在自己的 Zephyr 工作区准备相应环境。命令中的路径随该变量解析，不要求任何盘符或用户名。

```sh
# Bash；当前位置：官方 net-tools 根目录。
# 前提：ZEPHYR_BASE 指向本次使用的 Zephyr 源码根；Python 已有 aioquic。
python3 quic-echo-server.py --host 2001:db8::2 \
    --certificate "${ZEPHYR_BASE:?请先在自己的工作区设置 ZEPHYR_BASE}/samples/net/common/quic_certs/quic_server_ec_cert.pem" \
    --private-key "$ZEPHYR_BASE/samples/net/common/quic_certs/quic_server_ec_key.pem" \
    --max-stream-data 8192 -d 1
```

IPv4 用法只需将监听地址改为 `192.0.2.2`。当前辅助脚本的统计通过 INFO 日志输出，而默认日志级别为 WARNING；上面 `-d 1` 使 INFO 可见，统计在连接终止事件中输出。启动后若不能监听，先检查主机是否具备该地址；握手失败则核对证书、信任、ALPN 与双方配置，不能把服务端启动等同于回显校验通过。

> 译注——测试配置：原文示例的当前 `prj.conf` 显式启用 [`CONFIG_TEST_RANDOM_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_QUIC_ALLOW_NON_CSPRNG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_ALLOW_NON_CSPRNG)，其源码注释限定为没有熵源的模拟平台协议测试。官方测试密钥和这种随机数配置不代表可用于产品的身份与随机性保障。本批仅核对文档和源码，没有安装依赖、运行网络辅助脚本、构建或进行实板测试。

## 4. 另见（See Also）

[QUIC 库（QUIC Library）API 参考](P147_QUIC完整API参考.md)。连接与流、凭据、ALPN、会话恢复及缓冲区配置说明见 [QUIC 传输接口](P143_QUIC传输接口.md)。


<a id="quic-client-echo"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P144_QUIC示例目录.md) · [返回大纲](大纲.md) · [下一章](P146_QUIC回显服务端.md)
