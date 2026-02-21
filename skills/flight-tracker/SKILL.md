# Flight Tracker Skill

**Description:** Track commercial flights using web search and flight tracking sites (FlightAware, FlightStats, etc.). Supports status checks, departure/arrival times, and recurring updates.

## Usage

Ask the agent to "track flight [Airline] [FlightNumber]" or "check status of [FlightNumber]".

## Instructions for Agent

1.  **Search:** Use `web_search` with queries like `"[Airline] [FlightNumber] status [Date]"` or `"[FlightNumber] arrival time"`.
2.  **Verify:** Check multiple results if possible (FlightAware, FlightStats, Airline official site).
3.  **Extract:**
    *   **Status:** Scheduled, En Route, Landed, Delayed, Cancelled.
    *   **Times:** Actual Departure, Estimated/Actual Arrival.
    *   **Gate/Terminal:** If available.
4.  **Updates:** If the user asks for updates, use the `cron` tool to schedule `agentTurn` jobs.
    *   *Strategy:* Schedule checks 1 hour before, 30 mins before, and at arrival time.

## Examples

*   "Where is flight KE469?"
*   "Is UA858 on time?"
*   "Update me on flight SQ24 when it lands."

## Limitations

*   Relies on public web data (scraped/searched).
*   No direct API access to flight data providers (unless configured separately).
*   Real-time position might be delayed by a few minutes.
