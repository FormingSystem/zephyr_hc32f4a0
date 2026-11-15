---
id: learning.zephyr-docs.networking.page-42
title: TLS凭据Shell
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/tls_credentials_shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_TLS凭据Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/tls_credentials_shell.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 42.1 TLS 凭据命令行（TLS Credentials Shell）

TLS 凭据 Shell 提供命令行接口（Command-Line Interface），用于管理已安装的传输层安全（Transport Layer Security，TLS）凭据（Credential）。

## 42.2 命令（Commands）

### 缓存凭据：buf（Buffer Credential）

可以逐段向凭据缓冲区（Credential Buffer）追加数据，再使用[添加凭据（add）](#tls-credentials-shell-add-cred)命令保存。也可以清空缓冲区，或直接加载数据并以 `Ctrl + c` 结束。

向缓冲区追加 `<DATA>`：

```text
cred buf <DATA>
```

可以按需要重复执行，直到完整凭据都已写入缓冲区，然后用 `add` 命令存储。

直接向缓冲区加载 `<DATA>`：

```text
cred buf load
<DATA>
Ctrl + c
```

这里最后一行表示按下 Ctrl+C 结束输入，不是凭据内容。清空缓冲区：

```text
cred buf clear
```

| 参数 | 说明 |
| --- | --- |
| `<DATA>` | 要追加到缓冲区的文本数据，可以是文本，也可以是经过 Base64 编码的二进制数据。参见[添加凭据](#tls-credentials-shell-add-cred)及[存储／读取格式](#tls-credentials-shell-data-formats) |

### 添加凭据：add（Add Credential）

将 TLS 凭据加入凭据存储（Credential Store）。内容可以随 `cred add` 命令直接提供；没有直接提供时，从凭据缓冲区读取。

使用缓冲区中的数据：

```text
cred add <SECTAG> <TYPE> <BACKEND> <FORMAT>
```

在同一命令中直接提供数据：

```text
cred add <SECTAG> <TYPE> <BACKEND> <FORMAT> <DATA>
```

| 参数 | 说明 |
| --- | --- |
| `<SECTAG>` | 新凭据的安全标签（Security Tag，Sectag），可以是任意非负整数 |
| `<TYPE>` | 要添加的凭据类型，有效值见[凭据类型](#tls-credentials-shell-cred-types) |
| `<BACKEND>` | 保留参数，必须使用 `DEFAULT`，不区分大小写 |
| `<FORMAT>` | 提供数据的存储格式，有效值见[存储／读取格式](#tls-credentials-shell-data-formats) |
| `<DATA>` | 可选。提供后会以此作为凭据内容，取代缓冲区中的数据；可以是文本或经过 Base64 编码的二进制数据 |

### 删除凭据：del（Delete Credential）

从存储中删除指定凭据。若匹配的安全标签和类型存在，使用以下命令删除：

```text
cred del <SECTAG> <TYPE>
```

| 参数 | 说明 |
| --- | --- |
| `<SECTAG>` | 要删除凭据的安全标签，可以是任意非负整数 |
| `<TYPE>` | 要删除的凭据类型，有效值见[凭据类型](#tls-credentials-shell-cred-types) |

### 获取凭据内容：get（Get Credential Contents）

读取并打印指定凭据的内容。若匹配的安全标签和类型存在，使用：

```text
cred get <SECTAG> <TYPE> <FORMAT>
```

| 参数 | 说明 |
| --- | --- |
| `<SECTAG>` | 要读取凭据的安全标签，可以是任意非负整数 |
| `<TYPE>` | 要读取的凭据类型，有效值见[凭据类型](#tls-credentials-shell-cred-types) |
| `<FORMAT>` | 读取数据时采用的格式，有效值见[存储／读取格式](#tls-credentials-shell-data-formats) |

### 列出凭据：list（List Credentials）

列出凭据存储中的 TLS 凭据。列出全部可用凭据：

```text
cred list
```

列出指定安全标签的所有凭据：

```text
cred list <SECTAG>
```

列出指定类型的所有凭据：

```text
cred list any <TYPE>
```

同时按类型和安全标签筛选：

```text
cred list <SECTAG> <TYPE>
```

| 参数 | 说明 |
| --- | --- |
| `<SECTAG>` | 可选。指定后只列出该标签的凭据；传入 `any` 或省略表示允许任意标签，否则必须是非负整数 |
| `<TYPE>` | 可选。指定后只列出该类型；传入 `any` 或省略表示允许任意类型，否则使用[凭据类型](#tls-credentials-shell-cred-types)中的有效值 |

匹配的凭据按符合逗号分隔值（Comma-Separated Values，CSV）规范的格式输出：

```text
<SECTAG>,<TYPE>,<DIGEST>,<STATUS>
```

| 字段 | 含义 |
| --- | --- |
| `<SECTAG>` | 该凭据的安全标签，为非负整数 |
| `<TYPE>` | 该凭据类型的短代码（Short Code），见[凭据类型](#tls-credentials-shell-cred-types) |
| `<DIGEST>` | 表示凭据内容的摘要（Digest）字符串；具体算法可能因存储后端（Backend）而异。原文说明目前所有后端均采用原始凭据内容的 SHA256 哈希，再以 Base64 编码。因此，即使凭据实质相同，只要存储格式不同，摘要也可能不同 |
| `<STATUS>` | 生成该凭据摘要的状态码。成功为 `0`，否则为后端定义的负错误码；状态非零的行按错误格式打印 |

列表之后，打印找到的凭据数量：

```text
<N> credentials found.
```

其中 `<N>` 是找到的凭据数量，没有找到时为零。

## 42.3 凭据类型（Credential Types）

以下关键字不区分大小写，同一行的关键字是同类凭据的别名。

| 关键字 | 含义 |
| --- | --- |
| `CA_CERT`、`CA` | 可信证书颁发机构（Certificate Authority，CA）证书 |
| `SERVER_CERT`、`SELF_CERT`、`CLIENT_CERT`、`CLIENT`、`SELF`、`SERV` | 本端或服务器证书（Self or Server Certificate） |
| `PRIVATE_KEY`、`PK` | 私钥（Private Key） |
| `PRE_SHARED_KEY`、`PSK` | 预共享密钥（Pre-Shared Key，PSK） |
| `PRE_SHARED_KEY_ID`、`PSK_ID` | 预共享密钥标识（PSK ID） |

## 42.4 存储／读取格式（Storage/Retrieval Formats）

[tls_credentials 模块](P040_BSD套接字.md#sockets-tls-credentials-subsys)将存储的凭据视为任意二进制缓冲区。为方便在 Shell 中提供及读取这些缓冲区，命令行支持四种格式，关键字均不区分大小写。

这里的 NULL 终止符（NULL Terminator）表示字符串末尾的零字节。

| 格式 | 含义 | cred add 存储行为 | cred get 读取行为 |
| --- | --- | --- | --- |
| `BIN` | Shell 以 Base64 处理凭据，存储时不添加 NULL 终止符 | 把输入从 Base64 解码成原始二进制数据，不追加终止符 | 将已存储数据编码成 Base64 后打印 |
| `BINT` | Shell 以 Base64 处理凭据，存储时添加 NULL 终止符 | 从 Base64 解码成原始二进制数据，再追加 NULL 终止符后存储 | 先去掉 NULL 终止符，再编码成 Base64 后打印 |
| `STR` | Shell 以字面字符串（Literal String）处理凭据，不添加 NULL 终止符 | 按原样存储输入文本，不追加 NULL 终止符 | 以文本打印，不可打印字符显示为 `?` |
| `STRT` | Shell 以字面字符串处理凭据，添加 NULL 终止符 | 按原样存储输入文本，并追加 NULL 终止符 | 去掉 NULL 终止符后以文本打印，不可打印字符显示为 `?` |

Base64 可以表示任意二进制缓冲区，因此 `BIN` 可用于安装任意类型的凭据。另外三种格式用于简化特定场景。

安装可打印的预共享密钥时，用 `STR` 直接输入 PSK，无需先编码，并确保存储时不附加 NULL 终止符。

安装可辨别编码规则（Distinguished Encoding Rules，DER）格式的 X.509 证书，或不可打印的 PSK 等原始二进制凭据时，先将二进制数据编码为 Base64，再使用 `BIN`。

安装隐私增强邮件（Privacy-Enhanced Mail，PEM）格式的 X.509 证书或证书链（Certificate Chain）时，将完整 PEM 字符串编码为 Base64，包括换行及原文所称的 `----BEGIN X ----` / `----END X----` 标记，然后使用 `BINT`，以保证存储的字符串带有 NULL 终止符。原文说明，这是因为 Shell 不支持多行字符串；如果支持，便可以直接使用 `STRT`，不必进行 Base64 编码。也可以在 Base64 编码前手动把 NULL 终止符包含在数据中，然后用 `BIN`。

> 译注：上面的 BEGIN/END 文本沿用原文的泛指写法，并不是要求修改实际 PEM 文件中的分隔行。应保留实际证书的完整内容，包括真实的分隔行和换行。本章命令是官方交互语法，未在设备上安装、打印或删除任何凭据。


<a id="tls-credentials-shell"></a>
<a id="id1"></a>
<a id="commands"></a>
<a id="buffer-credential-buf"></a>
<a id="tls-credentials-shell-buf-cred"></a>
<a id="usage"></a>
<a id="arguments"></a>
<a id="add-credential-add"></a>
<a id="tls-credentials-shell-add-cred"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="delete-credential-del"></a>
<a id="tls-credentials-shell-del-cred"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="get-credential-contents-get"></a>
<a id="tls-credentials-shell-get-cred"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="list-credentials-list"></a>
<a id="tls-credentials-shell-list-cred"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="output"></a>
<a id="credential-types"></a>
<a id="tls-credentials-shell-cred-types"></a>
<a id="storage-retrieval-formats"></a>
<a id="tls-credentials-shell-data-formats"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：套接字服务](P041_套接字服务.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：HTTP客户端库](P049_HTTP客户端库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P041_套接字服务.md) · [返回大纲](大纲.md) · [下一章](P043_套接字服务回显示例.md)

</details>

<!-- reading-navigation:end -->
