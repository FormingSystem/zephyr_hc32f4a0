---
id: learning.zephyr-docs.networking.page-146
title: QUIC回显服务端
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/quic/echo_service/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_QUIC回显服务端

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/quic/echo_service/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Zephyr 的 `quic/echo_service` 示例实现使用 QUIC 协议的回显服务端（Echo Server），支持 IPv4、IPv6，并使用兼容 BSD 套接字（BSD Sockets）的 API。示例用于展示 QUIC API 与套接字服务（Socket Service）API 的用法。

套接字服务让一个线程监听多个阻塞套接字，在其中出现活动时触发回调（Callback）。系统只需创建一个服务线程监视这组套接字，因而节省内存。

应用通过 QUIC 协议（[RFC 9000](https://datatracker.ietf.org/doc/html/rfc9000.html)）提供服务。源码见 [samples/net/quic/echo_service](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/quic/echo_service)。

## 2. 前提（Requirements）

需具备以下两种环境之一：

- 按 [与主机系统联网](P007_与主机系统联网.md#networking-with-host) 配置的网络环境。
- 带有硬件网络接口的开发板。

## 3. 构建与运行（Building and Running）

以下是构建 Zephyr 版 `quic/echo_service` 的原文命令。先准备所用版本的 Zephyr 工作区、工具链和对应板级网络支持；在 Zephyr 源码根目录的 Bash 终端执行，将 `<board_to_use>` 替换为实际板名。构建成功后按该板运行方式启动固件，失败时先解决构建错误。

```sh
west build -b <board_to_use> samples/net/quic/echo_service
```

示例启动后，等待发往 `192.0.2.1` 或 `2001:db8::1`、端口 `4422` 的连接。

最简单的连接方式是使用 net-tools 项目中的回显客户端辅助脚本。以下保留原文 IPv4、IPv6 两种调用；在官方 net-tools 根目录的 Bash 终端执行，`$` 是提示符，不属于命令内容。

```sh
$ ./quic-echo-client.py --host 192.0.2.1 --max-size 1280 --packets 1
$ ./quic-echo-client.py --host 2001:db8::1 --packets 10
```

连接建立后，应用回显发送给它的任意一行数据。`quic-echo-client.py` 在结束时打印统计信息（Statistics）。

### 3.1 辅助客户端与示例配置（译注）

官方 [辅助客户端](https://github.com/zephyrproject-rtos/net-tools/blob/master/quic-echo-client.py) 使用 `aioquic`，因此运行它的 Python 环境需要具备相应依赖；在脚本不可直接执行的环境中，可以用 `python3 quic-echo-client.py` 加相同参数调用。默认端口为 4422，ALPN 为 `echo-quic`。`--packets` 指测试生成并核对的应用载荷次数，不承诺等于线路上的 UDP 数据报数量；`--max-size` 限制测试载荷长度。QUIC 提供字节流，不保留应用每次发送的消息边界。

当前脚本默认走回显核对流程，成功时退出码为 0，核对失败时为 1；`--no-echo` 会改成只发送、不等待回显验证。若连接或校验失败，应返回检查双方地址、端口、网络可达性、ALPN 及证书配置，不能把握手成功单独当作数据回显成功。

当前辅助客户端把 `--insecure` 的默认值设为 `True`，并设置 `ssl.CERT_NONE`；**省略这个标志也不会恢复证书验证**。它用于协议回显测试，成功结果不等于完成了服务端身份认证。官方 [服务端配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/quic/echo_service/prj.conf) 同样显式启用测试随机数和 [`CONFIG_QUIC_ALLOW_NON_CSPRNG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC_ALLOW_NON_CSPRNG)，源码注释要求不要把这种没有密码学安全随机源的配置复制到产品中。

证书由官方 `samples/net/common/quic_certs` 提供，[common.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/common/common.cmake) 将 PEM 测试文件生成包含数据；[服务端源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/quic/echo_service/src/main.c) 注册证书、私钥并设置 `echo-quic` ALPN。这些是上游示例实现说明，不要求读者使用作者机器的目录。本批没有构建、运行辅助客户端或进行网络／硬件测试。

## 4. 另见（See Also）

[QUIC 库（QUIC Library）API 参考](P147_QUIC完整API参考.md)。连接套接字接受流的工作流程见 [QUIC 传输接口](P143_QUIC传输接口.md)，由 Zephyr 主动连接主机的另一种测试方向见 [QUIC 回显客户端](P145_QUIC回显客户端.md)。


<a id="quic-service-echo"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P145_QUIC回显客户端.md) · [返回大纲](大纲.md) · [下一章](P147_QUIC完整API参考.md)
