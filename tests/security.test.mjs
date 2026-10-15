import test from 'node:test';import assert from 'node:assert/strict';
import {passwordHash,verifyPassword,sessionToken,validSession} from '../lib/security.mjs';
test('password hashes reject incorrect passwords',()=>{const h=passwordHash('a long private password');assert.ok(verifyPassword('a long private password',h));assert.equal(verifyPassword('incorrect',h),false);assert.equal(verifyPassword('x','malformed'),false)});
test('session authentication rejects tampering and wrong secrets',()=>{const token=sessionToken('a'.repeat(32));assert.ok(validSession(token,'a'.repeat(32)));assert.equal(validSession(token+'x','a'.repeat(32)),false);assert.equal(validSession(token,'b'.repeat(32)),false);assert.equal(validSession('',undefined),false)});
