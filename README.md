# sandbox-cdk-cognito-google-federation

CognitoでGoogle Federationを実現する環境をCDKで構築する検証。  
Amplifyで構築した環境をCDKで再構築してみた。

## 事前作業

### Python環境設定

```sh
$ python -m venv .venv
```

### 環境変数設定

`.env.{stage}`に以下の環境変数を設定する。

| 変数                        | 説明                                                                 |
|-----------------------------|----------------------------------------------------------------------|
| google_client_id            | GCPのOAuth2.0のクライアントID                                        |
| google_client_secret        | GCPのOAuth2.0のクライアントシークレット                              |
| web_client_callback_urls    | WebクライアントのOAuthコールバックURL(カンマ区切りで複数指定可能)    |
| web_client_logout_urls      | WebクライアントのOAuthログアウトURL(カンマ区切りで複数指定可能)      |
| mobile_client_callback_urls | MobileクライアントのOAuthコールバックURL(カンマ区切りで複数指定可能) |
| mobile_client_logout_urls   | MobileクライアントのOAuthログアウトURL(カンマ区切りで複数指定可能)   |

---

## 開発

### Python環境適用

```sh
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

### デプロイ

```sh
$ cdk deploy "*-cognito" --context stage=dev --require-approval never
```

### 削除

```sh
$ cdk destroy "*-cognito" --context stage=dev
```

---

## Google Cloud Plaform

### OAuth認証情報作成

- GCPにログイン
- OAuthクライアントを追加したいプロジェクトを選択
- 左上メニュー > APIとサービス > 認証情報
- 右ペイン上部の認証情報を作成 > OAuth クライアントID
  - アプリケーションの種類: Webアプリケーション
  - 名前: 任意
  - 承認済みのリダイレクト URI: `https://{project}-{stage}.auth.ap-northeast-1.amazoncognito.com/oauth2/idpresponse`
- 作成ボタンをクリックし、表示されるクライアントIDとクライアントシークレットをメモする。
  - この値を`.env.{stage}`に記載する。
