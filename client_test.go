package googleplay

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func TestGeneratedClientRequestAndAllowlist(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			t.Errorf("method = %s, want GET", r.Method)
		}
		if r.Header.Get("x-api-key") != "test-key" {
			t.Errorf("x-api-key = %q", r.Header.Get("x-api-key"))
		}
		if r.URL.EscapedPath() != "/api/v1/googleplay/developer/folder%2Fitem" {
			t.Errorf("escaped path = %q", r.URL.EscapedPath())
		}
		if "num" != "" {
			if got := r.URL.Query().Get("num"); got != "1" {
				t.Errorf("query value = %q", got)
			}
			if false && len(r.URL.Query()["num"]) != 2 {
				t.Errorf("array query values = %#v", r.URL.Query()["num"])
			}
		}
		if "country" != "" && !strings.Contains(r.URL.RawQuery, "country=space+%26+value") {
			t.Errorf("raw query = %q, missing encoded parameter %s", r.URL.RawQuery, "country=space+%26+value")
		}
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(map[string]any{"ok": true})
	}))
	defer server.Close()
	client := NewClient("test-key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	got, err := client.Call(context.Background(), "googleplay-developer", Params{"dev_id": "folder/item", "num": 1, "country": "space & value", "lang": "space & value", "full_detail": true})
	if err != nil {
		t.Fatal(err)
	}
	if got.(map[string]any)["ok"] != true {
		t.Fatalf("JSON result = %#v", got)
	}
	if OperationCount != 11 || len(OperationIDs()) != OperationCount {
		t.Fatalf("operation count = %d IDs=%d", OperationCount, len(OperationIDs()))
	}
	if _, err := client.Call(context.Background(), "unselected-operation", nil); err == nil || !strings.Contains(err.Error(), "unknown") {
		t.Fatalf("unselected operation error = %v", err)
	}
	if "" != "" {
		if _, err := client.Call(context.Background(), "googleplay-developer", Params{"dev_id": "folder/item", "num": 1, "country": "space & value", "lang": "space & value", "full_detail": true}); err == nil || !strings.Contains(err.Error(), "invalid value") {
			t.Fatalf("invalid enum error = %v", err)
		}
	}
	if err := client.Close(); err != nil {
		t.Fatal(err)
	}
}

func TestGeneratedClientTextResponse(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/plain; charset=utf-8")
		_, _ = w.Write([]byte("feed text"))
	}))
	defer server.Close()
	client := NewClient("key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	got, err := client.Call(context.Background(), "googleplay-developer", Params{"dev_id": "folder/item", "num": 1, "country": "space & value", "lang": "space & value", "full_detail": true, "responseType": "text"})
	if err != nil {
		t.Fatal(err)
	}
	if got != "feed text" {
		t.Fatalf("text result = %#v", got)
	}
}

func TestGeneratedClientErrorsAndTimeout(t *testing.T) {
	t.Run("HTTP error", func(t *testing.T) {
		server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
			http.Error(w, "upstream unavailable", http.StatusBadGateway)
		}))
		defer server.Close()
		client := NewClient("key")
		client.BaseURL = server.URL + "/api/v1"
		client.HTTPClient = server.Client()
		_, err := client.Call(context.Background(), "googleplay-developer", Params{"dev_id": "folder/item", "num": 1, "country": "space & value", "lang": "space & value", "full_detail": true})
		if err == nil || !strings.Contains(err.Error(), "502") {
			t.Fatalf("HTTP error = %v", err)
		}
	})

	t.Run("timeout", func(t *testing.T) {
		server := httptest.NewServer(http.HandlerFunc(func(_ http.ResponseWriter, r *http.Request) {
			<-r.Context().Done()
		}))
		defer server.Close()
		client := NewClient("key")
		client.BaseURL = server.URL + "/api/v1"
		client.HTTPClient = server.Client()
		client.Timeout = 10 * time.Millisecond
		_, err := client.Call(context.Background(), "googleplay-developer", Params{"dev_id": "folder/item", "num": 1, "country": "space & value", "lang": "space & value", "full_detail": true})
		if err == nil {
			t.Fatal("expected request timeout")
		}
	})
}

func ExampleClient_Call() {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{"ok":true}`))
	}))
	defer server.Close()

	client := NewClient("your-crawlora-api-key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	result, err := client.Call(context.Background(), "googleplay-app", Params{"app_id": "sample"})
	if err != nil {
		panic(err)
	}
	fmt.Println(result.(map[string]any)["ok"])
	// Output: true
}
