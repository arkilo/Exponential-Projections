# Exponential Library

Your very own offline-first open-source data-center! Includes over 50 services!

## Beta Software Warning

## Summary


## Goals


## Features
t and Virtual Box setup you can demo things locally by running `make develop`. This will spin up a temporary developer copy on your local computer without needing an actual server to point things at. Note no data will actually be saved from inside the VM, so this is for testing only.

## Requirements

A server with:

- Ubuntu 18.04 and [passwordless SSH via SSH keys](https://linuxconfig.org/passwordless-ssh) working.

Another computer with:

- Docker

Note: Two separate computers are not required, but are highly recommended. The idea is you have a server and then your personal computer, say a laptop or desktop. You deploy from your personal computer to the server. This way your settings are saved on your personal computer, and can be used to re-build the server and restore from backups if anything goes wrong.

