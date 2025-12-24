// backend/main.go
package main

import (
	"math/rand"
	"net/http"
	"os"
	"time"

	"github.com/gin-gonic/gin"
)

type Quote struct {
	Text   string `json:"text"`
	Author string `json:"author"`
}

func main() {
	// Seed the random number generator for varied output on each request
	rand.Seed(time.Now().UnixNano())

	r := gin.Default()

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	quotes := []Quote{
		{"Code is like humor. When you have to explain it, it’s bad.", "Cory House"},
		{"Fix the cause, not the symptom.", "Steve McConnell"},
		{"Optimism is an occupational hazard of programming: feedback is the treatment.", "Kent Beck"},
		{"Simplicity is the soul of efficiency.", "Austin Freeman"},
		{"It’s not a bug – it’s an undocumented feature.", "Anonymous"},
	}

	r.GET("/health", func(c *gin.Context) {
		c.JSON(200, gin.H{"status": "healthy"})
	})

	r.GET("/quote", func(c *gin.Context) {
		randomIndex := rand.Intn(len(quotes))
		c.JSON(http.StatusOK, quotes[randomIndex])
	})

	r.Run(":" + port)
}