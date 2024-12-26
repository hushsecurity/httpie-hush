# httpie-hush

Hush OAuth 2 plugin for the `HTTPie <https://github.com/jkbr/httpie>` command line HTTP client.


## Installation

```bash
    $ pip install httpie-hush
```

You should now see `hush` under `--auth-type` in `$ http --help` output.


## Setup

```bash
    $ httpie-hush-setup
```

Configure Hush's auth plugin with your creds (saved in `~/.httpie/config.json`).  
The credentials can be either a username/password or an API Key ID/API Key Secret.

#### Notes:
- If username is not provided in conf file it will be searched at
  `HTTPIE_HUSH_USERNAME` envar
- If password is not provided in conf file it will be searched at
  `HTTPIE_HUSH_PASSWORD` envar
- If org shortname is not provided in conf file it will be searched at
  `HTTPIE_HUSH_ORG` envar
  - Only required for username login
  - API Keys use the API Key's org or the passes effective org
- Manually inputted username/password supersedes conf file and environment variables


## Usage

```bash
    $ http --auth-type=hush GET https://api.us.hush-security.com/v1/users
```

It's possible to use an effective org by passing the ``EORG`` envar:

```bash
    $ EORG=hush http --auth-type=hush GET https://api.us.hush-security.com/v1/users
```